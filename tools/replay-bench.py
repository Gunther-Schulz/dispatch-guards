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

Boundary: STATELESS guards only. The bench never seeds state, so the
stateful gates are EXCLUDED by a declared dict (EXCLUDED_STATEFUL:
`writer-claims-gate` — a claims store seeded across a
PostToolUse/PreToolUse pair — and `writer-reservation-gate` — a
reservation object inside a real git dir): a stdin-only case for
either would be a vacuous `silent`, and each one's end-to-end
coverage lives inside its own `--test`, which can seed that state.
A hook with no corpus case that is NOT stateful is a named debt, the
second declared dict (UNCOVERED_DECLARED). Both dicts are VERIFIED on
every full run (no `--hook`): every plugin/hooks/*.py (the directory
read at run time, minus _dispatch_common.py) has a corpus case or
sits in exactly one dict, no member has a case, no member names a
missing file; a violation prints the hook and the rule and exits 1.

Isolation: every run pins CLAUDE_DISPATCH_GUARDS_CONFIG,
CLAUDE_DISPATCH_GUARDS_FIRELOG, CLAUDE_DISPATCH_GUARDS_CLAIMS and
CLAUDE_DISPATCH_GUARDS_REGISTER into a per-run temp dir, so a bench
run never reads the site config or the operator's real
~/.claude/readiness.json, and never appends to the real fire log or
claims store.

Corpus format (JSONL, one case per line):

    {"hook": "<basename>.py",
     "expect": "deny"|"ask"|"context"|"warn"|"block"|"silent"|"rewrite",
     "payload": {...}}                # the hook-input JSON

  optional keys:
    "raw": "<literal stdin>"          # instead of payload (fail-open cases)
    "config": {...}                   # written to a temp file, pinned as
                                      # CLAUDE_DISPATCH_GUARDS_CONFIG
    "transcript_events": [...]        # written to a temp .jsonl whose path
                                      # is injected as payload.transcript_path
    "register": {...}                 # written as JSON to tmp/register-<i>.json
                                      # and pinned as
                                      # CLAUDE_DISPATCH_GUARDS_REGISTER
                                      # (dg-43, 2026-10-07); absent, the pin
                                      # stays a path that never exists
                                      # (register-<i>-absent.json). Register
                                      # shape: {"prozesse": [{"id": ...}]}
    "note": "<why this case exists>"  # carried by every regression case
    "expect_updated_input": {...}     # "rewrite" cases only (2026-09-15):
                                      # key/value pairs the observed
                                      # hookSpecificOutput.updatedInput must
                                      # carry — a kind-only "rewrite" match
                                      # proves a repair happened, never that
                                      # it repaired to the RIGHT value; this
                                      # is the value-discriminating half
                                      # (dg-45 judgment-desk ruling). Its
                                      # own discrimination is proven by
                                      # replay-bench.py --test, never by a
                                      # corpus case, since a case cannot
                                      # assert against a deliberately wrong
                                      # expectation of itself.

Outcome classification of one run:
    exit 2                                          -> block
    exit 0, empty stdout                            -> silent
    exit 0, JSON stdout, permissionDecision deny    -> deny
    exit 0, JSON stdout, permissionDecision ask     -> ask
    exit 0, JSON stdout, updatedInput, no decision  -> rewrite
    exit 0, JSON stdout, systemMessage carrying fire()'s own
      " WARN (staging): " marker + additionalContext -> warn
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

KINDS = ("deny", "ask", "context", "warn", "block", "silent", "rewrite")
FIRE_KINDS = ("deny", "ask", "context", "warn", "block", "rewrite")

# fire()'s warn-mode emitter (_dispatch_common.fire) writes this marker into
# the TOP-LEVEL systemMessage; it is matched there only, never in prose of
# additionalContext, so an ordinary reminder that merely quotes it stays
# "context" (dg-44, 2026-10-07).
WARN_MARKER = " WARN (staging): "

# Declared coverage limits (dg-26, 2026-10-07): hook basename -> reason.
# coverage_violations() checks both against the hooks directory and the
# corpus on every full run, so neither can age silently.
EXCLUDED_STATEFUL = {
    "writer-claims-gate.py": "stateful: needs a claims store seeded "
        "across a PostToolUse/PreToolUse pair, which the bench never "
        "provides; a stdin-only case would be a vacuous silent",
    "writer-reservation-gate.py": "stateful: needs a real git fixture "
        "repo plus a reservation object in its git dir, which the "
        "bench never provides; a stdin-only case would be a vacuous "
        "silent",
}
_NO_CASE_YET = "no corpus case yet; covered by its own --test only"
UNCOVERED_DECLARED = {
    "discovery-volume-reminder.py": _NO_CASE_YET,
    "dispatch-log.py": _NO_CASE_YET,
    "report-enforcer.py": _NO_CASE_YET,
    "report-reminder.py": _NO_CASE_YET,
}
# the shared module is not a hook
NOT_A_HOOK = "_dispatch_common.py"


def coverage_violations(cases: list[dict], hooks_dir: Path | None = None,
                        excluded: dict | None = None,
                        uncovered: dict | None = None) -> list[str]:
    """One line per violated coverage rule, [] when clean. The hook list
    is read from the directory at call time, never from a restated list;
    the dicts default to the module's declared ones at call time too, so
    a test that mutates them in-process reaches this check."""
    hooks_dir = HOOKS if hooks_dir is None else hooks_dir
    excluded = EXCLUDED_STATEFUL if excluded is None else excluded
    uncovered = UNCOVERED_DECLARED if uncovered is None else uncovered
    on_disk = sorted(p.name for p in hooks_dir.glob("*.py")
                     if p.name != NOT_A_HOOK)
    with_cases = {c["hook"] for c in cases}
    out = []
    for name in on_disk:
        in_ex, in_un = name in excluded, name in uncovered
        if in_ex and in_un:
            out.append(f"{name}: declared in BOTH EXCLUDED_STATEFUL and "
                       "UNCOVERED_DECLARED (exactly one allowed)")
        if name not in with_cases and not in_ex and not in_un:
            out.append(f"{name}: no corpus case and in neither "
                       "EXCLUDED_STATEFUL nor UNCOVERED_DECLARED")
    for label, decl in (("EXCLUDED_STATEFUL", excluded),
                        ("UNCOVERED_DECLARED", uncovered)):
        for name in sorted(decl):
            if name not in on_disk:
                out.append(f"{name}: named in {label} but no such hook "
                           f"file under {hooks_dir}")
            elif name in with_cases:
                out.append(f"{name}: in {label} but has corpus cases "
                           "(remove it from the dict)")
    return out


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
    # REWRITE (2026-09-15, guard-rewrite arc, dg-45 judgment-desk ruling):
    # a repair via updatedInput with NO permissionDecision — the shape
    # docs/audits/wave0-probe-record-2026-09-15.md found correct (arms
    # b2/b3: applies with no forced allow, permission flow still runs
    # unforced on a rewritten call). Checked AFTER the decision branch so
    # a hypothetical lane pairing updatedInput with an explicit deny/ask
    # still classifies by its decision, never silently as a rewrite.
    if "updatedInput" in hso:
        return "rewrite"
    # WARN (2026-10-07, dg-44): a staged lane's fire() warn carries the
    # marker in the top-level systemMessage beside additionalContext.
    # Before this branch it classified as "context", identical to an
    # ordinary reminder, so a staged lane silenced or promoted to deny
    # moved a case between kinds the bench could not tell apart from a
    # plain reminder going quiet.
    sm = j.get("systemMessage")
    if (isinstance(sm, str) and WARN_MARKER in sm
            and "additionalContext" in hso):
        return "warn"
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
    # A case's own `register` fixture (dg-43, 2026-10-07) replaces the
    # absent-path pin with a real file, so a lane whose firing arm needs
    # a readable register is reachable end to end through the process
    # boundary, not only through the hook's --test.
    if "register" in case:
        reg = tmp / f"register-{index}.json"
        reg.write_text(json.dumps(case["register"]), encoding="utf-8")
        env["CLAUDE_DISPATCH_GUARDS_REGISTER"] = str(reg)
    else:
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
            if "expect_updated_input" in case and case["expect"] != "rewrite":
                raise SystemExit(
                    f"{path}:{lineno}: expect_updated_input only makes "
                    "sense with expect=\"rewrite\"")
            if hook_filter and case["hook"] not in (
                    hook_filter, hook_filter + ".py"):
                continue
            cases.append(case)
    return cases


def _rewrite_value_mismatch(case: dict, raw_stdout: str) -> str | None:
    """None if `case`'s `expect_updated_input` (if any) matches the
    observed rewrite's actual `updatedInput`, else a description of the
    first mismatching key. A case with no `expect_updated_input` makes no
    value claim and always returns None — kind-matching alone ("rewrite"
    observed) still requires this to return None before a case counts as
    caught; see main()'s `caught` computation."""
    expected = case.get("expect_updated_input")
    if not expected:
        return None
    try:
        updated = json.loads(raw_stdout)["hookSpecificOutput"]["updatedInput"]
    except (json.JSONDecodeError, KeyError, TypeError):
        return "no updatedInput to compare expect_updated_input against"
    for k, v in expected.items():
        got = updated.get(k)
        if got != v:
            return f"{k}: expected {v!r}, observed {got!r}"
    return None


def _test() -> int:
    """Bite-tests for the bench's OWN machinery: the isolation premises it
    pins, and (2026-09-15) whether expect_updated_input can actually catch
    a wrong rewrite value.

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

    # ── Rewrite-value assertion: a discriminating PAIR (2026-09-15, dg-45
    # judgment-desk ruling on the guard-rewrite arc's item-1 critique pass).
    # A kind-only "rewrite" match proves a repair happened, never that it
    # repaired to the RIGHT value — this proves expect_updated_input can
    # actually FAIL before any real corpus case is allowed to rest on it
    # passing (Fixing's instrument-pair rule: a probe proven only by
    # agreement never varied the axis that matters). The pair is built
    # here rather than in guards.jsonl because a corpus case cannot assert
    # against a deliberately WRONG expectation of itself.
    _rw_base = {"hook": "agent-model-gate.py", "expect": "rewrite",
                "payload": {"tool_name": "Agent", "tool_input": {
                    "subagent_type": "general-purpose", "model": "opus",
                    "description": "Fix the tests"}}, "_line": 0}
    _rw_ok = {**_rw_base,
             "expect_updated_input": {"name": "opus-fix-the-tests"}}
    _rw_wrong = {**_rw_base,
                "expect_updated_input": {"name": "opus-DELIBERATELY-WRONG"}}
    with tempfile.TemporaryDirectory(prefix="rb-selftest-rw-") as td2:
        tmp2 = Path(td2)
        o_ok, _, raw_ok = run_case(_rw_ok, tmp2, 0)
        o_wrong, _, raw_wrong = run_case(_rw_wrong, tmp2, 1)
    assert o_ok == "rewrite" and o_wrong == "rewrite", (o_ok, o_wrong)
    mism_ok = _rewrite_value_mismatch(_rw_ok, raw_ok)
    mism_wrong = _rewrite_value_mismatch(_rw_wrong, raw_wrong)
    if mism_ok is not None:
        bad += 1
        print(f"FAIL [rewrite-value]: the CORRECT-value case was flagged "
              f"as mismatched: {mism_ok}", file=sys.stderr)
    if mism_wrong is None:
        bad += 1
        print("FAIL [rewrite-value]: the WRONG-value case was not "
              "flagged — expect_updated_input does not discriminate",
              file=sys.stderr)

    # ── Warn-kind classification (2026-10-07, dg-44): a discriminating
    # PAIR over classify() itself. The first stdout has fire()'s own
    # warn shape; the second is the same body with the top-level
    # systemMessage marker removed, which must fall back to "context";
    # the third carries the marker only inside additionalContext prose,
    # which must also stay "context".
    _warn_out = json.dumps({
        "systemMessage": "[x/y] WARN (staging): r",
        "hookSpecificOutput": {"hookEventName": "PreToolUse",
                               "additionalContext": "[x/y] WARN — staging "
                                                    "mode, this lane would "
                                                    "DENY: r"}})
    _nomark_out = json.dumps({
        "systemMessage": "[x/y] r",
        "hookSpecificOutput": {"hookEventName": "PreToolUse",
                               "additionalContext": "[x/y] WARN — staging "
                                                    "mode, this lane would "
                                                    "DENY: r"}})
    _prose_out = json.dumps({
        "hookSpecificOutput": {"hookEventName": "PreToolUse",
                               "additionalContext": "quotes WARN (staging): "
                                                    "in prose"}})
    for _label, _out, _want in (("warn shape", _warn_out, "warn"),
                                ("marker removed", _nomark_out, "context"),
                                ("marker in prose only", _prose_out,
                                 "context")):
        _got = classify(0, _out)
        if _got != _want:
            bad += 1
            print(f"FAIL [warn classify, {_label}]: expected {_want!r}, "
                  f"got {_got!r}", file=sys.stderr)

    # ── Register fixture reaches the hook (2026-10-07, dg-43): the same
    # brief with and without a `register` key must observe DIFFERENT
    # kinds — warn with a register certifying the class it cites,
    # context (could-not-verify silence on the pin lane) without one.
    _reg_base = {"hook": "brief-reminder.py", "_line": 0,
                 "payload": {"tool_name": "Agent", "tool_input": {
                     "name": "sonnet-x", "prompt": (
                         "REGISTERED-CLASS dispatch: selftest-fixture-class."
                         "\nGrounding basis: read src/spec.md first.\n"
                         "Write boundaries: you own src/foo.py; commits by "
                         "pathspec, never -A.\nCommit plan: one commit by "
                         "pathspec.\nClosing report (mandatory; the "
                         "project's own report form if it defines one, else "
                         "the \u00a72 form here \u2014 never both; "
                         "\"none\" is a valid slot answer, silence is "
                         "not): (a) items completed w/ evidence, (b) checks "
                         "RUN w/ real output, (c) gaps surfaced, (d) "
                         "deviations w/ reason, (e) candidate lessons, (f) "
                         "files touched + commit hashes (unpushed), (g) "
                         "what was NOT verified, (h) sources actually "
                         "read.\nA missing decision, file, or value is "
                         "surfaced as a gap, never bridged with a guess.\n"
                         "Report channel: SendMessage to the dispatcher "
                         "\u2014 your final text reaches no one.")}}}
    _reg_with = {**_reg_base, "expect": "warn", "register": {"prozesse": [
        {"id": "selftest-fixture-class", "tier": "sonnet",
         "status": "ready", "klasse": "selftest"}]}}
    _reg_without = {**_reg_base, "expect": "context"}
    with tempfile.TemporaryDirectory(prefix="rb-selftest-reg-") as td3:
        _o_with = run_case(_reg_with, Path(td3), 0)[0]
        _o_without = run_case(_reg_without, Path(td3), 1)[0]
    if (_o_with, _o_without) != ("warn", "context"):
        bad += 1
        print(f"FAIL [register fixture]: with-register observed "
              f"{_o_with!r} (want 'warn'), without {_o_without!r} (want "
              "'context') - the fixture does not reach the hook",
              file=sys.stderr)

    # ── Coverage verification (dg-26): the declared dicts are checked
    # against the real directory and corpus. Baseline first (unmodified
    # dicts must be CLEAN, else every red below proves nothing), then
    # each rule mutated in-process, the mutation always restored:
    # a member removed, a phantom added, a member that has cases, a
    # hook in both dicts, an undeclared hook file, and the whole main()
    # path (exit code + the printed violation line).
    import contextlib
    import io
    full = load_corpus(DEFAULT_CORPUS, None)
    base = coverage_violations(full)
    if base:
        bad += 1
        print(f"FAIL [coverage baseline]: unmodified dicts not clean: "
              f"{base}", file=sys.stderr)

    def _arm(label, mutate, restore, hook, want_rule):
        nonlocal_bad = 0
        try:
            mutate()
            got = coverage_violations(full)
        finally:
            restore()
        named = [v for v in got if v.startswith(hook + ":")
                 and want_rule in v]
        if len(named) != 1 or len(got) != 1:
            nonlocal_bad = 1
            print(f"FAIL [coverage, {label}]: want exactly one violation "
                  f"naming {hook} ({want_rule!r}), got {got}",
                  file=sys.stderr)
        return nonlocal_bad

    _ex, _un = dict(EXCLUDED_STATEFUL), dict(UNCOVERED_DECLARED)

    def _restore():
        EXCLUDED_STATEFUL.clear()
        EXCLUDED_STATEFUL.update(_ex)
        UNCOVERED_DECLARED.clear()
        UNCOVERED_DECLARED.update(_un)

    bad += _arm("member removed",
                lambda: EXCLUDED_STATEFUL.pop("writer-claims-gate.py"),
                _restore, "writer-claims-gate.py", "neither")
    bad += _arm("phantom member",
                lambda: UNCOVERED_DECLARED.update({"no-such-hook.py": "x"}),
                _restore, "no-such-hook.py", "no such hook file")
    bad += _arm("member with cases",
                lambda: UNCOVERED_DECLARED.update(
                    {"brief-reminder.py": "x"}),
                _restore, "brief-reminder.py", "has corpus cases")
    bad += _arm("in both dicts",
                lambda: UNCOVERED_DECLARED.update(
                    {"writer-claims-gate.py": "x"}),
                _restore, "writer-claims-gate.py", "BOTH")
    with tempfile.TemporaryDirectory(prefix="rb-selftest-hooks-") as hd:
        hdp = Path(hd)
        for name in os.listdir(HOOKS):
            if name.endswith(".py"):
                (hdp / name).write_text("", encoding="utf-8")
        (hdp / "brand-new-gate.py").write_text("", encoding="utf-8")
        got = coverage_violations(full, hooks_dir=hdp)
        if (len(got) != 1 or not got[0].startswith("brand-new-gate.py:")):
            bad += 1
            print(f"FAIL [coverage, undeclared hook file]: got {got}",
                  file=sys.stderr)
    # the whole path: main() over the real corpus with one member
    # removed exits 1 and prints the violation; restored, it exits 0
    _argv = sys.argv
    try:
        sys.argv = ["replay-bench.py"]
        results = []
        for mutate in (lambda: EXCLUDED_STATEFUL.pop(
                "writer-claims-gate.py"), lambda: None):
            _restore()
            mutate()
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                rc = main()
            results.append((rc, buf.getvalue()))
    finally:
        sys.argv = _argv
        _restore()
    (rc_red, out_red), (rc_ok, out_ok) = results
    if (rc_red != 1 or "COVERAGE VIOLATION writer-claims-gate.py" not in
            out_red):
        bad += 1
        print(f"FAIL [coverage, main red]: rc={rc_red}", file=sys.stderr)
    if rc_ok != 0 or "COVERAGE VIOLATION" in out_ok:
        bad += 1
        print(f"FAIL [coverage, main baseline]: rc={rc_ok}",
              file=sys.stderr)

    print("replay-bench selftest: isolation pinned, rewrite-value "
          "discriminates, warn classified, register fixture reaches the "
          "hook, coverage dicts verified" if not bad
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
            observed, detail, raw = run_case(case, tmp, i)
            # Value mismatch is only meaningful once the KIND already
            # matches "rewrite" — a case whose kind is wrong has nothing
            # coherent to compare updatedInput against.
            value_mismatch = (_rewrite_value_mismatch(case, raw)
                              if observed == "rewrite" else None)
            results.append((case, observed, detail, value_mismatch))

    by_hook: dict[str, list] = {}
    for row in results:
        by_hook.setdefault(row[0]["hook"], []).append(row)

    mismatches = 0
    print(f"replay-bench: {len(results)} cases from {corpus}")
    for hook in sorted(by_hook):
        rows = by_hook[hook]
        bad = [r for r in rows
              if r[1] != r[0]["expect"] or r[3] is not None]
        mismatches += len(bad)
        status = "OK" if not bad else f"{len(bad)} MISMATCH"
        print(f"  {hook:<26} {len(rows):>3} cases  "
              f"{len(rows) - len(bad):>3} match  [{status}]")
        for case, observed, detail, value_mismatch in bad:
            if observed != case["expect"]:
                print(f"      line {case['_line']}: expected "
                      f"{case['expect']!r}, observed {observed!r}")
            else:
                print(f"      line {case['_line']}: kind {observed!r} "
                      f"matched but the VALUE did not: {value_mismatch}")
            if case.get("note"):
                print(f"        note: {case['note']}")
            print(f"        {detail}")

    expected_fires = [r for r in results if r[0]["expect"] != "silent"]
    caught = [r for r in expected_fires
             if r[1] == r[0]["expect"] and r[3] is None]
    false_fires = [r for r in results
                   if r[0]["expect"] == "silent" and r[1] in FIRE_KINDS]
    rate = (100.0 * len(caught) / len(expected_fires)) if expected_fires else 0.0
    print(f"  totals: {len(results)} cases, "
          f"{len(results) - mismatches} match, {mismatches} mismatch")
    print(f"  catch rate:  {len(caught)}/{len(expected_fires)} "
          f"({rate:.1f}%) of expected fires")
    print(f"  false fires: {len(false_fires)} "
          f"(fired where the corpus expects silence)")
    for case, observed, _, _ in false_fires:
        print(f"      line {case['_line']} {case['hook']}: fired {observed!r}")
    violations = []
    if not args.hook:
        # coverage verification (dg-26): only over the FULL corpus, since
        # a --hook run selects a subset and every other hook would read
        # as uncovered
        violations = coverage_violations(cases)
        on_disk = [p.name for p in HOOKS.glob("*.py")
                   if p.name != NOT_A_HOOK]
        covered = {c["hook"] for c in cases}
        print(f"  coverage:    {len(covered & set(on_disk))} hooks covered, "
              f"{len(set(EXCLUDED_STATEFUL) & set(on_disk))} "
              "stateful-excluded, "
              f"{len(set(UNCOVERED_DECLARED) & set(on_disk))} "
              "uncovered-declared")
        for v in violations:
            print(f"      COVERAGE VIOLATION {v}")
    return 1 if mismatches or violations else 0


if __name__ == "__main__":
    sys.exit(main())
