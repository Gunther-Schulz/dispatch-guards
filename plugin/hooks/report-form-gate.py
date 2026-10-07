#!/usr/bin/env python3
r"""PreToolUse(SendMessage) gate: a report-shaped message must carry all
required closing-report slots.

The computable slice of schema-validating the §2 closing report
(harvest 2026-08-06, dev-notes/harvest-2026-08-06.md item 4; source
idea: agentic-coding-reference's schema-validated handoff records,
adapted to prose because §2's binding is that reports travel IN the
SendMessage — report files are harness-blocked for subagents).

What is computable: the §2 form's slots are labeled `(a)`…`(g)`
(+ `(h)` in the execution tail). A subagent message carrying MANY of
those markers is report-shaped, and a report-shaped message missing
required slots is the observed under-report failure ("checks run" and
"not verified" are the slots that get dropped). What is NOT
computable stays with the dispatcher: whether slot contents are true,
whether a slot-less message is a legitimate read-only-tail return
(verifier/discovery reports carry no slots by design — forms.md
READ-ONLY tail), or a §2-exempt project form.

Predicate: ≥ REPORT_MIN_SLOTS distinct markers from (a)–(h) →
report-shaped; required set REQUIRED_SLOTS (a–g; h is
execution-tail-only) minus found → fire naming the missing slots.
A marker COUNTS only at line start or after sentence-ending
punctuation (dg-1, 2026-10-07): `_SLOT_RE` is
`(?:^|(?<=[.;:!?]\s))\s*(?:-\s*)?\(([a-h])\)` under `re.M`. The
measured false-fire class of the old unanchored form
(`\(([a-h])\)` anywhere): a message that merely ENUMERATES slot
letters mid-sentence — a state-token ping, which §2 tells a lane to
send INSTEAD of re-sending a report — reached REPORT_MIN_SLOTS and
was graded a report missing `(b)`; the backlog entry's own body text
fired the same way (measured: missing (d)–(g)). The obvious repair
is REFUTED: a line-start-only anchor finds ONE slot in a genuine
single-paragraph report ("(a) done. (b) 275 OK. …"), drops below the
threshold and goes silent on a real report (executed: an inline
report missing `(e)` was quiet under it). The punctuation arm keeps
the inline report. The lane's verb is unchanged: a staged warn
lane, its staging record carrying forward.
Split-part reports (labeled 1/N, forms.md §2) fire per part in warn
mode — a part legitimately carries a subset, which is why this lane
must never run "deny" without a split-aware exemption; recorded
residue.

DEFAULT-WARN (staged lane): parenthesized-letter enumerations are an
ordinary prose style, so a 4-marker prose list false-fires by
construction. The lane ships `default_mode="warn"` — an advisory
line plus a fire-log record, never a block — and earns "deny" only
through the fire-rate review against the log (guard_modes policy
key). This is the harvest's staging discipline applied to its own
newest lane.

Direction: subagent context only — the expensive, §2-bound direction
(mirrors message-payload-gate). Fail-open on parse errors; --test
bite-test registered via the doctor's content scan.
"""
from __future__ import annotations

import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from _dispatch_common import doc_ref, fire, is_subagent  # noqa: E402

_SOURCE = "dispatch-guards/report-form-gate"

REPORT_MIN_SLOTS = 4
REQUIRED_SLOTS = set("abcdefg")  # (h) rides the execution tail only
_SLOT_RE = re.compile(
    r"(?:^|(?<=[.;:!?]\s))\s*(?:-\s*)?\(([a-h])\)", re.M)


def found_slots(message: str) -> set:
    return set(_SLOT_RE.findall(message))


def check(payload: dict) -> str | None:
    """Return a fire reason, or None (= allow)."""
    if payload.get("tool_name") != "SendMessage":
        return None
    if not is_subagent(payload):
        return None  # dispatcher→subagent messages are not §2 reports
    msg = (payload.get("tool_input") or {}).get("message")
    if not isinstance(msg, str):
        return None
    slots = found_slots(msg)
    if len(slots) < REPORT_MIN_SLOTS:
        return None  # not report-shaped (or a read-only-tail return)
    missing = REQUIRED_SLOTS - slots
    if not missing:
        return None
    miss = ", ".join(f"({s})" for s in sorted(missing))
    have = ", ".join(f"({s})" for s in sorted(slots))
    return (
        f"Report-form gate ({doc_ref('§2, references/forms.md')}): this "
        f"message is report-shaped (slots {have}) but is missing required "
        f"slot(s) {miss}. Every §2 slot must appear — \"none\" is a valid "
        "answer, silence is not; the dropped slots are where "
        "under-reporting hides (checks actually RUN, what was NOT "
        "verified). If this is part i/N of a split report, say so in the "
        "part and continue; if it is a read-only (verifier/discovery) "
        "return, slot markers are not required at all."
    )


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0  # never fail the workflow on a hook parse error
    reason = check(payload)
    if reason:
        # staged lane: ships warn, promotable to deny via guard_modes
        fire(reason, source=_SOURCE, payload=payload, default_mode="warn")
    return 0


if __name__ == "__main__":
    if "--test" in sys.argv:
        import contextlib
        import io
        import tempfile
        from _dispatch_common import _reset_policy_cache

        os.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = "/nonexistent"
        _reset_policy_cache()

        def report(slots: str) -> str:
            # one slot per line, the §2 form's own layout: the anchored
            # marker (dg-1) no longer counts a bare space-joined "(b)"
            # mid-sentence, which is the false-fire class it removes
            return "\n".join(f"({s}) content of {s}" for s in slots)

        sub = {"tool_name": "SendMessage", "agent_id": "a1"}

        # complete report → silent
        assert check({**sub, "tool_input": {"message": report("abcdefg")}}) is None
        # execution-tail report with (h) → silent
        assert check({**sub, "tool_input": {"message": report("abcdefgh")}}) is None
        # report-shaped but missing slots → fires, names them
        r = check({**sub, "tool_input": {"message": report("abcd")}})
        assert r is not None and "(e), (f), (g)" in r
        assert "(a), (b), (c), (d)" in r  # names what it found
        r = check({**sub, "tool_input": {"message": report("abcefg")}})
        assert r is not None and "(d)" in r and "(e)" not in r.split("missing")[1][:30]
        # below the shape threshold → silent (read-only returns, short prose)
        assert check({**sub, "tool_input": {"message": report("abc")}}) is None
        assert check({**sub, "tool_input": {"message": "verdict: CONFIRMED, basis: x"}}) is None
        # repeated markers count once (distinct letters, not occurrences)
        assert check({**sub, "tool_input": {"message": report("aaab")}}) is None
        # letters outside a-h don't count toward the shape
        assert check({**sub, "tool_input": {"message": "(x) (y) (z) (q) list"}}) is None
        # main session → silent even for partial report shapes
        assert check({"tool_name": "SendMessage",
                      "tool_input": {"message": report("abcd")}}) is None
        # object message / other tool / no input → silent
        assert check({**sub, "tool_input": {"message": {"type": "x"}}}) is None
        assert check({"tool_name": "Bash", "agent_id": "a1",
                      "tool_input": {"message": report("abcd")}}) is None
        assert check({**sub, "tool_input": {}}) is None
        assert check({}) is None

        # ── e2e: default mode is WARN (additionalContext), logged ──
        with tempfile.TemporaryDirectory() as td:
            os.environ["CLAUDE_DISPATCH_GUARDS_FIRELOG"] = td + "/f.jsonl"

            def run_main(raw):
                old = sys.stdin
                out = io.StringIO()
                exited = False
                try:
                    sys.stdin = io.StringIO(raw)
                    with contextlib.redirect_stdout(out):
                        try:
                            ret = main()
                        except SystemExit as e:
                            exited, ret = True, e.code
                finally:
                    sys.stdin = old
                return ret, out.getvalue(), exited

            ret, out, exited = run_main(json.dumps(
                {**sub, "tool_input": {"message": report("abcd")}}))
            assert exited and ret == 0
            j = json.loads(out)
            assert "additionalContext" in j["hookSpecificOutput"], j
            assert "permissionDecision" not in j["hookSpecificOutput"]
            # promoted to deny via guard_modes → real deny JSON
            with tempfile.NamedTemporaryFile(
                    "w", suffix=".json", delete=False, dir=td) as tf:
                tf.write('{"guard_modes": {"report-form-gate": "deny"}}')
                os.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = tf.name
            _reset_policy_cache()
            ret, out, exited = run_main(json.dumps(
                {**sub, "tool_input": {"message": report("abcd")}}))
            j = json.loads(out)
            assert j["hookSpecificOutput"]["permissionDecision"] == "deny"
            # both fires logged
            with open(td + "/f.jsonl") as f:
                modes = [json.loads(x)["mode"] for x in f]
            assert modes == ["warn", "deny"], modes
            # fail-open on garbage stdin
            ret, out, exited = run_main("}{")
            assert ret == 0 and not exited and out == ""
            os.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = "/nonexistent"
            del os.environ["CLAUDE_DISPATCH_GUARDS_FIRELOG"]
            _reset_policy_cache()

        # ── dg-1: slot markers are anchored. Gate-level arms: the REAL
        # hook script over stdin, never the predicate alone. Expected
        # outcomes come from what a message IS (a report, or a message
        # about one), not from the regex. Each arm that must be quiet
        # also has a mirror that must fire, so "quiet" cannot be a
        # gate that went deaf.
        import subprocess

        with tempfile.TemporaryDirectory() as td2:
            genv = dict(os.environ,
                        CLAUDE_DISPATCH_GUARDS_CONFIG="/nonexistent",
                        CLAUDE_DISPATCH_GUARDS_FIRELOG=td2 + "/f.jsonl")

            def gate(msg: str):
                """(exit code, stdout) of the real hook on one message."""
                p = {**sub, "tool_input": {"message": msg}}
                r = subprocess.run(
                    [sys.executable, os.path.realpath(__file__)],
                    input=json.dumps(p), env=genv,
                    capture_output=True, text=True)
                return r.returncode, r.stdout.strip()

            def fires(msg: str, missing: str | None = None) -> bool:
                code, out = gate(msg)
                assert code == 0, (code, out)
                if not out:
                    return False
                if missing is not None:
                    assert f"missing required slot(s) {missing}." in out, out
                return True

            # (1) a ping that enumerates slot letters → quiet. The
            # six-letter form clears REPORT_MIN_SLOTS (the unanchored
            # regex fired on it, missing (b)); the item-text form is the
            # original wording.
            assert not fires("slots (a)-(h) are all landed; part 5/7 "
                             "carried gaps (c)")
            assert not fires("ack: slots (a), (c), (d), (e), (f), (g) "
                             "are all landed; part 5/7 carried gaps (c)")
            # (2) prose mentioning slot letters mid-sentence → quiet
            # (four letters, so the OLD regex fires; three is the
            # below-threshold control)
            assert not fires("Before the second pass the (a) items and "
                             "the (b) evidence and the (c) gaps and (d) "
                             "deviations are rechecked in order.")
            assert not fires("Before the second pass the (a) items and "
                             "the (b) evidence and the (c) gaps are "
                             "rechecked in order.")
            # (3) inline one-paragraph report: recognised, quiet when
            # complete; the mirror (missing (e)) must FIRE, which is what
            # proves it was recognised (a line-start-only anchor reads
            # it as a non-report and is quiet on both)
            inline = ("(a) done. (b) 275 OK. (c) none. (d) none. (e) "
                      "none. (f) x. (g) none.")
            assert not fires(inline)
            assert fires(inline.replace("(e) none. ", ""), "(e)")
            # (4) line-start report: recognised (complete → quiet)
            assert not fires(report("abcdefg"))
            # (5) a report missing (b) → fires, naming it
            assert fires(report("acdefg"), "(b)")
            # self-match probe: the gate on its OWN docstring is quiet
            assert not fires(__doc__)
            # (the second probe, over the backlog entry's body text, is
            # the corpus case noted dg-1 in tools/corpus/guards.jsonl)

        print("report-form-gate: all tests passed")
        sys.exit(0)
    sys.exit(main())
