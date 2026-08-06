#!/usr/bin/env python3
"""Guard replay bench: run the real hook scripts over curated stdin
payloads and check each one's emitted outcome against an expectation.

Why this exists (dev-notes/harvest-2026-08-06.md item 3): the per-hook
`--test` bite-tests pin the FUNCTION arms (`check()`, `deny_check()`,
detection helpers) — they do not exercise the process boundary a hook
actually lives at: stdin JSON in, stdout JSON (or exit 2 + stderr) out.
The bench pins that boundary, and it pins the historical false-fire
regressions as data rather than as assertions buried in a hook file
(`"note"` on those cases records which incident they descend from).
Survey items 2+4 converge here: this IS the end-to-end deny-arm test.

Boundary: STATELESS guards only. `writer-claims-gate` is EXCLUDED —
it is stateful (a claims store seeded across a PostToolUse/PreToolUse
pair), and its end-to-end coverage lives inside its own `--test`,
which can seed that state. The bench never seeds state.

Isolation: every run pins CLAUDE_DISPATCH_GUARDS_CONFIG,
CLAUDE_DISPATCH_GUARDS_FIRELOG and CLAUDE_DISPATCH_GUARDS_CLAIMS into
a per-run temp dir, so a bench run never reads the site config and
never appends to the real fire log or claims store.

Corpus format (JSONL, one case per line):

    {"hook": "<basename>.py",
     "expect": "deny"|"ask"|"context"|"block"|"silent",
     "payload": {...}}                # the hook-input JSON

  optional keys:
    "raw": "<literal stdin>"          # instead of payload (fail-open cases)
    "config": {...}                   # written to a temp file, pinned as
                                      # CLAUDE_DISPATCH_GUARDS_CONFIG
    "transcript_events": [...]        # written to a temp .jsonl whose path
                                      # is injected as payload.transcript_path
    "note": "<why this case exists>"  # carried by every regression case

Outcome classification of one run:
    exit 2                                          -> block
    exit 0, empty stdout                            -> silent
    exit 0, JSON stdout, permissionDecision deny    -> deny
    exit 0, JSON stdout, permissionDecision ask     -> ask
    exit 0, JSON stdout, additionalContext only     -> context
    anything else (unparseable stdout, other exit)  -> error (always a miss)

Usage:
    tools/replay-bench.py [--corpus PATH] [--hook <basename>]
Exit 0 iff every case matched its expectation, else 1.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
HOOKS = REPO / "plugin" / "hooks"
DEFAULT_CORPUS = Path(__file__).resolve().parent / "corpus" / "guards.jsonl"

KINDS = ("deny", "ask", "context", "block", "silent")
FIRE_KINDS = ("deny", "ask", "context", "block")


def classify(returncode: int, stdout: str) -> str:
    """Map one hook process result onto the outcome vocabulary."""
    if returncode == 2:
        return "block"
    if returncode != 0:
        return "error"
    out = stdout.strip()
    if not out:
        return "silent"
    try:
        j = json.loads(out)
    except (json.JSONDecodeError, ValueError):
        return "error"
    if not isinstance(j, dict):
        return "error"
    hso = j.get("hookSpecificOutput")
    if not isinstance(hso, dict):
        return "error"
    decision = hso.get("permissionDecision")
    if decision in ("deny", "ask"):
        return decision
    if "additionalContext" in hso:
        return "context"
    return "error"


def run_case(case: dict, tmp: Path, index: int) -> tuple[str, str]:
    """Run one corpus case; return (observed_kind, detail)."""
    hook = HOOKS / case["hook"]
    if not hook.exists():
        return "error", f"no such hook: {hook}"

    env = dict(os.environ)
    env["CLAUDE_DISPATCH_GUARDS_FIRELOG"] = str(tmp / f"fires-{index}.jsonl")
    env["CLAUDE_DISPATCH_GUARDS_CLAIMS"] = str(tmp / f"claims-{index}.jsonl")
    if "config" in case:
        cfg = tmp / f"config-{index}.json"
        cfg.write_text(json.dumps(case["config"]), encoding="utf-8")
        env["CLAUDE_DISPATCH_GUARDS_CONFIG"] = str(cfg)
    else:
        env["CLAUDE_DISPATCH_GUARDS_CONFIG"] = "/nonexistent"

    if "raw" in case:
        stdin = case["raw"]
    else:
        payload = dict(case["payload"])
        if "transcript_events" in case:
            tp = tmp / f"transcript-{index}.jsonl"
            tp.write_text(
                "".join(json.dumps(e) + "\n" for e in case["transcript_events"]),
                encoding="utf-8")
            payload["transcript_path"] = str(tp)
        stdin = json.dumps(payload)

    proc = subprocess.run(
        [sys.executable, str(hook)], input=stdin, env=env,
        capture_output=True, text=True)
    observed = classify(proc.returncode, proc.stdout)
    detail = (f"exit={proc.returncode} stdout={proc.stdout.strip()[:160]!r} "
              f"stderr={proc.stderr.strip()[:160]!r}")
    return observed, detail


def load_corpus(path: Path, hook_filter: str | None) -> list[dict]:
    cases = []
    with path.open(encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            case = json.loads(line)
            case["_line"] = lineno
            if case.get("expect") not in KINDS:
                raise SystemExit(
                    f"{path}:{lineno}: bad expect {case.get('expect')!r}")
            if ("payload" in case) == ("raw" in case):
                raise SystemExit(
                    f"{path}:{lineno}: exactly one of payload/raw required")
            if hook_filter and case["hook"] not in (
                    hook_filter, hook_filter + ".py"):
                continue
            cases.append(case)
    return cases


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--corpus", default=str(DEFAULT_CORPUS),
                    help="corpus JSONL (default: tools/corpus/guards.jsonl)")
    ap.add_argument("--hook", default=None,
                    help="run only cases for this hook basename")
    args = ap.parse_args()

    corpus = Path(args.corpus)
    if not corpus.exists():
        print(f"replay-bench: no corpus at {corpus}", file=sys.stderr)
        return 1
    cases = load_corpus(corpus, args.hook)
    if not cases:
        print("replay-bench: no cases selected", file=sys.stderr)
        return 1

    results = []
    with tempfile.TemporaryDirectory(prefix="replay-bench-") as td:
        tmp = Path(td)
        for i, case in enumerate(cases):
            observed, detail = run_case(case, tmp, i)
            results.append((case, observed, detail))

    by_hook: dict[str, list] = {}
    for case, observed, detail in results:
        by_hook.setdefault(case["hook"], []).append((case, observed, detail))

    mismatches = 0
    print(f"replay-bench: {len(results)} cases from {corpus}")
    for hook in sorted(by_hook):
        rows = by_hook[hook]
        bad = [r for r in rows if r[1] != r[0]["expect"]]
        mismatches += len(bad)
        status = "OK" if not bad else f"{len(bad)} MISMATCH"
        print(f"  {hook:<26} {len(rows):>3} cases  "
              f"{len(rows) - len(bad):>3} match  [{status}]")
        for case, observed, detail in bad:
            print(f"      line {case['_line']}: expected {case['expect']!r}, "
                  f"observed {observed!r}")
            if case.get("note"):
                print(f"        note: {case['note']}")
            print(f"        {detail}")

    expected_fires = [r for r in results if r[0]["expect"] != "silent"]
    caught = [r for r in expected_fires if r[1] == r[0]["expect"]]
    false_fires = [r for r in results
                   if r[0]["expect"] == "silent" and r[1] in FIRE_KINDS]
    rate = (100.0 * len(caught) / len(expected_fires)) if expected_fires else 0.0
    print(f"  totals: {len(results)} cases, "
          f"{len(results) - mismatches} match, {mismatches} mismatch")
    print(f"  catch rate:  {len(caught)}/{len(expected_fires)} "
          f"({rate:.1f}%) of expected fires")
    print(f"  false fires: {len(false_fires)} "
          f"(fired where the corpus expects silence)")
    for case, observed, _ in false_fires:
        print(f"      line {case['_line']} {case['hook']}: fired {observed!r}")
    return 1 if mismatches else 0


if __name__ == "__main__":
    sys.exit(main())
