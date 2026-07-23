#!/usr/bin/env python3
"""SubagentStop enforcer: re-demand the closing report from the stopping agent.

Root cause this closes (dispatch-discipline.md §2, "Channel rule"): a
BACKGROUND/teammate dispatch's final text answer reaches NO ONE — the
closing report only arrives if the agent SENDs it (SendMessage) to its
dispatcher. The observed failure is a channel mismatch: the agent writes
its report as final text, goes idle, and the dispatcher never sees it.
`report-reminder.py` nudges the DISPATCHER to demand the report; this hook
closes the other side — it nudges the stopping SUBAGENT to SEND it before
going idle, replacing the manual re-demand loop.

Mechanism (verified against the Claude Code hooks reference, as-of
2026-07-18): on SubagentStop, `hookSpecificOutput.additionalContext` is
wrapped in a system reminder and inserted into the STOPPING subagent's own
conversation, which "continues so Claude can act on the feedback" (docs,
"Add context for Claude" + Stop/SubagentStop decision-control row). So the
injected instruction reaches the agent that just finished, in time to act.
This is the same additionalContext channel report-reminder.py documents as
subagent-local (report-reminder.py:10-15).

Loop-breaker (docs, SubagentStop/Stop input, as-of 2026-07-18):
additionalContext on SubagentStop "keeps the subagent running", so an
UNGUARDED hook re-fires on every subsequent stop — an indefinite loop
(observed live during this hook's own build). The `stop_hook_active` field
is "true when Claude Code is already continuing as a result of a stop hook";
this hook returns None in that case, injecting exactly ONCE and letting the
next stop through. The instruction's "already sent → do not send twice"
clause is the secondary guard against a double-send within that one nudge.

Fail-open on parse errors (dispatch guard family standard); the --test
bite-test is the compensation and is auto-discovered by the machine-bootstrap
doctor (doctor.py globs hooks/*.py carrying "--test").
"""
from __future__ import annotations

import json
import sys

INSTRUCTION = (
    "Closing-report check: If you are a background/teammate agent (your "
    "final text does NOT reach your dispatcher), send your closing report "
    "NOW via SendMessage to your dispatcher — going idle without having "
    "SENT it counts as no report. Keep it SHORT: key findings plus the "
    "file path; write any large result to a FILE first (a big payload "
    "pushed into the dispatcher's running session can force a full "
    "prompt-cache rewrite there). If you are a synchronous subagent, your "
    "final text IS the report — ensure it contains the full closing-report "
    "form; do NOT call SendMessage. If you already sent/delivered the "
    "report, stop — do not send it twice."
)


def check(payload: dict) -> str | None:
    """Return the instruction to inject, or None (= stay silent).

    Injects once per subagent completion. `stop_hook_active` is true when
    the subagent is only still running because THIS hook already fired
    (docs, SubagentStop/Stop input); returning None then lets it stop,
    breaking the re-fire loop additionalContext otherwise causes ("keeps
    the subagent running"). Otherwise the event itself is the gate —
    SubagentStop carries no tool_name/matcher to filter on.
    """
    if payload.get("stop_hook_active"):
        return None
    return INSTRUCTION


def output_json(context: str) -> str:
    """The exact SubagentStop additionalContext emission (docs schema)."""
    return json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "SubagentStop",
            "additionalContext": context,
        }
    })


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0  # never fail the workflow on a hook parse error
    context = check(payload)
    if context:
        print(output_json(context))
    return 0


if __name__ == "__main__":
    if "--test" in sys.argv:
        import contextlib
        import io

        # injects on a fresh SubagentStop payload (event is the gate)
        assert check({"agent_id": "a1", "hook_event_name": "SubagentStop"}) is not None
        assert check({}) is not None
        assert check({"agent_id": "a1", "stop_hook_active": False}) is not None
        # loop-breaker: silent once Claude is already continuing from this hook
        assert check({"agent_id": "a1", "stop_hook_active": True}) is None
        text = check({})
        # channel + idempotency phrasing must survive edits
        assert "sendmessage" in text.lower()          # names the real channel
        assert "final text is the report" in text.lower().replace("  ", " ")
        assert "do not send it twice" in text.lower() # idempotency clause
        # correct JSON emission format (SubagentStop additionalContext schema)
        out = json.loads(output_json("X"))
        assert out["hookSpecificOutput"]["hookEventName"] == "SubagentStop", out
        assert out["hookSpecificOutput"]["additionalContext"] == "X", out
        # fail-open path: unparseable stdin → exit 0, no output
        sys.stdin = io.StringIO("}{ not json")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = main()
        assert rc == 0, rc
        assert buf.getvalue() == "", repr(buf.getvalue())
        # happy path: valid payload → emits the instruction JSON, exit 0
        sys.stdin = io.StringIO(json.dumps({"agent_id": "a1",
                                            "hook_event_name": "SubagentStop"}))
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = main()
        assert rc == 0, rc
        emitted = json.loads(buf.getvalue())
        assert emitted["hookSpecificOutput"]["hookEventName"] == "SubagentStop"
        assert "do not send it twice" in \
            emitted["hookSpecificOutput"]["additionalContext"].lower()
        # loop-breaker path: stop_hook_active=True → empty output, exit 0
        sys.stdin = io.StringIO(json.dumps({"agent_id": "a1",
                                            "stop_hook_active": True}))
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = main()
        assert rc == 0, rc
        assert buf.getvalue() == "", repr(buf.getvalue())
        print("report-enforcer: all tests passed")
        sys.exit(0)
    sys.exit(main())
