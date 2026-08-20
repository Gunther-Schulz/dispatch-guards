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
CLAUDE_DISPATCH_GUARDS_FIRELOG, CLAUDE_DISPATCH_GUARDS_CLAIMS and
CLAUDE_DISPATCH_GUARDS_REGISTER into a per-run temp dir, so a bench
run never reads the site config or the operator's real
~/.claude/readiness.json, and never appends to the real fire log or
claims store.

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


def run_case(case: dict, tmp: Path, index: int) -> tuple[str, str, str]:
    """Run one corpus case; return (observed_kind, detail, raw_stdout)."""
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
    # Same premise class as `cwd` below, found the hard way. The §6
    # readiness register is an ENVIRONMENT premise the bench must pin,
    # not inherit: brief-reminder renders the register's own rows into
    # its advisory, so an unpinned run reads the OPERATOR's real
    # ~/.claude/readiness.json and the bench's output moves with a file
    # no case declares. What kept this invisible is that it does NOT
    # disturb the match/mismatch counts — classification is type-only —
    # so the bench stayed 61/61 green while exercising something it
    # never declared. Measured 2026-08-20: one brief-reminder case's
    # additionalContext carried three real register rows under the real
    # HOME and the absence line under an empty one. Per-index path, so a
    # future case can write its own register fixture there.
    env["CLAUDE_DISPATCH_GUARDS_REGISTER"] = str(
        tmp / f"register-{index}-absent.json")

    if "raw" in case:
        stdin = case["raw"]
    else:
        payload = dict(case["payload"])
        # A case's `cwd` is a PREMISE the bench must pin, not inherit. Two
        # cases cite a repo-relative path (plugin/skills/.../forms.md) and
        # carry `"cwd": "."`; a guard resolving that against the CALLER's
        # directory reads the citation only when the caller happens to sit
        # in this checkout. Measured 2026-08-18: green from the repo, 1
        # mismatch (brief-reminder deny-instead-of-context) when the
        # machine doctor ran it from its own repo — a red that indicts the
        # corpus, not the guard, and reads as a guard regression.
        if not str(payload.get("cwd", "/")).startswith("/"):
            payload["cwd"] = str((REPO / payload["cwd"]).resolve())
        if "transcript_events" in case:
            tp = tmp / f"transcript-{index}.jsonl"
            tp.write_text(
                "".join(json.dumps(e) + "\n" for e in case["transcript_events"]),
                encoding="utf-8")
            payload["transcript_path"] = str(tp)
        stdin = json.dumps(payload)

    proc = subprocess.run(
        [sys.executable, str(hook)], input=stdin, env=env, cwd=str(REPO),
        capture_output=True, text=True)
    observed = classify(proc.returncode, proc.stdout)
    detail = (f"exit={proc.returncode} stdout={proc.stdout.strip()[:160]!r} "
              f"stderr={proc.stderr.strip()[:160]!r}")
    # The RAW stdout rides along as a third element, untruncated. `detail`
    # cuts at 160 chars for readable mismatch output, which makes it
    # useless as an identity basis — the isolation selftest below compared
    # `detail` first and stayed green under its own mutation, because the
    # register rows sit past the cut. A truncated view read as the whole
    # body is the same blindness this pin exists to remove.
    return observed, detail, proc.stdout


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


def _test() -> int:
    """Bite-test for the bench's OWN isolation — the premises it pins.

    Graduated from a throwaway probe, per this repo's rule that a manual
    investigation is unfinished while the check that produced its finding
    does not exist. The finding (2026-08-20): `run_case` pinned CONFIG,
    FIRELOG and CLAIMS but not the §6 readiness register, so every
    brief-reminder case read the OPERATOR's real ~/.claude/readiness.json
    and the bench's rendered output moved with a file no case declares.

    Why the existing bench could not catch it, which is the whole reason
    this arm exists: classification is TYPE-only (`deny`/`context`/
    `silent`), so a case's CONTENT can swing wildly while the counts stay
    61/61 green. A check that passes while exercising something it never
    declared is the quiet direction of the premise-drift class, and only
    a content-identity assertion sees it.

    The arm is a discriminating PAIR: the same case is run under two
    different HOMEs, one carrying a register with a distinctive class id
    and one with none. Identical output = the premise is pinned. Without
    the pin the two differ, which is the red this was built against.
    """
    import shutil
    case = None
    for c in load_corpus(DEFAULT_CORPUS, "brief-reminder.py"):
        if c["expect"] == "context":
            case = c
            break
    if case is None:                       # corpus shrank; say so, don't pass
        print("replay-bench selftest: no brief-reminder 'context' case — "
              "cannot verify isolation", file=sys.stderr)
        return 2
    outs = []
    real_home = os.environ.get("HOME")
    # ONE tmp dir across both arms, deliberately. The pinned register path
    # is derived from tmp, and the absence line NAMES the resolved path —
    # so a per-arm tmp dir makes the two outputs differ for a reason that
    # belongs to the harness, not the artifact, and the arm goes red on a
    # correctly pinned bench. Measured while building this: the setup was
    # the instrument, exactly as the probe it replaces.
    try:
        with tempfile.TemporaryDirectory(prefix="rb-selftest-") as td:
            for populated in (True, False):
                home = tempfile.mkdtemp(prefix="rb-home-")
                if populated:
                    os.makedirs(os.path.join(home, ".claude"), exist_ok=True)
                    with open(os.path.join(home, ".claude", "readiness.json"),
                              "w", encoding="utf-8") as fh:
                        json.dump({"prozesse": [{
                            "id": "SELFTEST-SENTINEL-CLASS", "tier": "haiku",
                            "status": "ready", "klasse": "isolation probe"}]},
                            fh)
                os.environ["HOME"] = home
                outs.append(run_case(case, Path(td), 0))
                shutil.rmtree(home, ignore_errors=True)
    finally:
        if real_home is not None:
            os.environ["HOME"] = real_home
    bad = 0
    # Compare the RAW stdout (index 2), never `detail` (index 1): detail
    # truncates at 160 chars and the register rows sit past the cut, so a
    # detail-based comparison is green under the very defect this arm
    # exists to catch — measured, not reasoned: the first version of this
    # selftest passed its own mutate-the-pin-out proof.
    if outs[0][2] != outs[1][2]:
        bad += 1
        print("FAIL [register isolation]: the same case rendered differently "
              "under two HOMEs — the bench is reading a register no case "
              "declares", file=sys.stderr)
    if "SELFTEST-SENTINEL-CLASS" in outs[0][2]:
        bad += 1
        print("FAIL [register isolation]: the planted sentinel class reached "
              "the rendered output", file=sys.stderr)
    print("replay-bench selftest: isolation pinned" if not bad
          else f"replay-bench selftest: {bad} FAILED")
    return 1 if bad else 0


def main() -> int:
    if "--test" in sys.argv:
        return _test()
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
            observed, detail, _raw = run_case(case, tmp, i)
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
