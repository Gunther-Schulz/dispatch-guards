#!/usr/bin/env python3
"""SubagentStop enforcer: re-demand the closing report from the stopping agent.

Root cause this closes (dispatch skill references/forms.md §2, "Channel rule"): a
BACKGROUND/teammate dispatch's final text answer reaches NO ONE — the
closing report only arrives if the agent SENDs it (SendMessage) to its
dispatcher. The observed failure is a channel mismatch: the agent writes
its report as final text, goes idle, and the dispatcher never sees it.
`report-reminder.py` nudges the DISPATCHER to demand the report; this hook
closes the other side — it nudges the stopping SUBAGENT to SEND it before
going idle, replacing the manual re-demand loop.

Known soft spot: the background-vs-sync judgment is delegated to the
stopping agent and has been misjudged once (agent-side; the channel
line in the brief tail is the dispatcher-side cure — forms.md §2).

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
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from _dispatch_common import policy  # noqa: E402

DEFAULT_MAX = 3000  # mirror of message-payload-gate.py, same policy key


def max_chars() -> int:
    v = policy().get("max_message_chars", DEFAULT_MAX)
    return v if isinstance(v, int) and v > 0 else DEFAULT_MAX


def instruction() -> str:
    return (
        "Closing-report check: FIRST — if a backgrounded task of yours "
        "(a long check, a replay) is still RUNNING, do not close on a "
        "guess: AWAIT it via TaskOutput(block=true) and report its real "
        "result, or send an INTERIM report that says so and names what "
        "remains — ending your turn with it running orphans the work. "
        "If you are a background/teammate agent "
        "(your final text does NOT reach your dispatcher), send your "
        "closing report NOW via SendMessage to your dispatcher — going "
        "idle without having SENT it counts as no report. BEFORE "
        f"composing it: message max {max_chars()} chars — write any "
        "larger result to a FILE first, then send key findings plus the "
        "file path (an injected payload occupies the dispatcher's "
        "context for the rest of its session; oversized sends are "
        "denied by a gate, costing you a rewrite). Already SENT it via "
        "SendMessage? Do not send twice — that idempotency applies to "
        "SendMessage ONLY. If you are a synchronous subagent, your "
        "final text IS the report, and only your LAST text block is "
        "delivered: so if you already wrote the report above, RE-EMIT "
        "IT IN FULL now. A bare acknowledgement ('already reported "
        "above', 'nothing further needed') becomes your final text and "
        "DELETES the report — the dispatcher receives the "
        "acknowledgement instead. Re-emitting costs tokens; not "
        "re-emitting costs the whole report. Do NOT call SendMessage."
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
    return instruction()


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
        import tempfile
        from _dispatch_common import _reset_policy_cache

        os.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = "/nonexistent"
        _reset_policy_cache()
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
        assert "do not send twice" in text.lower()    # idempotency clause
        # The idempotency clause MUST stay scoped to SendMessage. Unscoped, a
        # resumed SYNCHRONOUS agent reads "already reported → stop", emits a
        # bare acknowledgement, and that acknowledgement — being the LAST text
        # block — replaces the report the dispatcher was meant to receive.
        # The hook then destroys the artifact it exists to guarantee.
        low = text.lower()
        assert "sendmessage only" in low, "idempotency must name its channel"
        idem = low.index("do not send twice")
        scope = low.index("sendmessage only")
        assert scope - idem < 90, "the scope must sit next to the clause"
        # sync branch must demand RE-EMISSION, never a bare acknowledgement
        assert "re-emit" in low, "sync branch must demand re-emission"
        assert "in full" in low
        assert "deletes the report" in low, "must name the consequence"
        assert "last text block" in low, "must name the delivery mechanism"
        # payload clause: names the limit BEFORE composition, file+pointer
        assert f"max {DEFAULT_MAX} chars" in text     # default threshold
        assert "before" in text.lower()               # pre-composition timing
        assert "file" in text.lower()                 # file+pointer remedy
        # threshold follows the same policy key as message-payload-gate
        with tempfile.NamedTemporaryFile("w", suffix=".json",
                                         delete=False) as tf:
            tf.write('{"max_message_chars": 1234}')
            os.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = tf.name
        _reset_policy_cache()
        assert "max 1234 chars" in check({})
        os.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = "/nonexistent"
        _reset_policy_cache()
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
        assert "re-emit it in full" in \
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
