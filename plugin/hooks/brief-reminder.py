#!/usr/bin/env python3
"""PreToolUse(Agent|Task) reminder: brief-side counterpart to report-reminder.

Closes the §1 consumer gap (skill-craft review finding, 2026-07-19):
the brief form had no mechanical consumer at dispatch time — a
below-session-tier dispatch with an underspecified brief passed
silently (only fable dispatches force the permission dialog). One
line lands before the dispatch starts, reminding the dispatcher of
the §1 brief checks and the §2 report channel (dispatch-discipline.md).
The hook never judges the brief — judgment stays with the dispatcher.

Environment binding (as-of 2026-07-19): PreToolUse `additionalContext`
injection into the dispatching conversation — UNVERIFIED against a
live fire at mint time; first real dispatch confirms. Fail-open and
inert if the harness ignores it; --test covers the logic only
(bootstrap doctor tripwire).
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from _dispatch_common import policy  # noqa: E402


def reminder_text() -> str:
    doc = policy().get("discipline_doc")
    if doc:
        return (
            f"Dispatch starting — brief check ({doc} §1): "
            "decision-complete (assignments made, files listed not "
            "paraphrased, grounding section, write boundaries, commit "
            "convention verbatim, gaps-surface instruction)? Report "
            "channel per §2 named in the brief? Verifier dispatch → "
            "artifact + question ONLY."
        )
    return (
        "Dispatch starting — brief check: decision-complete (assignments "
        "made, files listed not paraphrased, grounding stated, write "
        "boundaries, gaps surfaced not filled)? Report channel named in "
        "the brief? Verifier dispatch → artifact + question ONLY."
    )


_CHANNEL_MARKERS = ("sendmessage", "send_message", "report channel",
                    "final text is the report")


def missing_channel(payload: dict) -> bool:
    """True iff this is a BACKGROUND Agent dispatch whose prompt names
    no report channel — the deliver-into-the-void class (JOURNAL
    2026-07-27, epsilon-probe: agent finished, reported as final text,
    reached no one). Background is the Agent tool's default, so only an
    explicit run_in_background=False exempts. Fail-open on any doubt."""
    if payload.get("tool_name") != "Agent":
        return False  # Task tool has its own return path
    tool_input = payload.get("tool_input") or {}
    if tool_input.get("run_in_background") is False:
        return False  # synchronous: final text IS the report
    prompt = (tool_input.get("prompt") or "").lower()
    if not prompt:
        return False
    return not any(m in prompt for m in _CHANNEL_MARKERS)


def deny_text() -> str:
    doc = policy().get("discipline_doc") or "dispatch-discipline.md"
    return (
        "Blocked: background dispatch without a report channel. A "
        "background agent's final text reaches no one — the brief "
        "must instruct delivery (paste the tail block's channel "
        f"line, {doc} §2: SendMessage to the dispatcher), or pass "
        "run_in_background: false for a synchronous dispatch. "
        "Fix the brief and retry."
    )


def check(payload: dict) -> str | None:
    """Return the reminder, or None (= stay silent)."""
    if payload.get("tool_name") not in ("Agent", "Task"):
        return None
    return reminder_text()


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0  # never fail the workflow on a hook parse error
    if missing_channel(payload):
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
            },
            "systemMessage": deny_text(),
        }))
        return 0
    reminder = check(payload)
    if reminder:
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "additionalContext": reminder,
            }
        }))
    return 0


if __name__ == "__main__":
    if "--test" in sys.argv:
        import tempfile
        from _dispatch_common import _reset_policy_cache
        os.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = "/nonexistent"
        _reset_policy_cache()
        assert check({"tool_name": "Agent"}) is not None
        assert check({"tool_name": "Task"}) is not None
        assert "brief check" in check({"tool_name": "Agent"})
        with tempfile.NamedTemporaryFile("w", suffix=".json",
                                         delete=False) as tf:
            tf.write('{"discipline_doc": "dispatch-discipline.md"}')
            os.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = tf.name
        _reset_policy_cache()
        assert "dispatch-discipline.md §1" in check({"tool_name": "Agent"})
        assert check({"tool_name": "Bash"}) is None
        assert check({}) is None
        # Channel gate: background + no channel → deny
        assert missing_channel({"tool_name": "Agent", "tool_input": {
            "prompt": "Go read files and report your findings."}})
        # Channel named (any marker) → allow
        assert not missing_channel({"tool_name": "Agent", "tool_input": {
            "prompt": "Do X. Deliver via SendMessage to main."}})
        assert not missing_channel({"tool_name": "Agent", "tool_input": {
            "prompt": "Do X.\nReport channel: your final text IS the "
                      "report."}})
        # Explicit synchronous → allow
        assert not missing_channel({"tool_name": "Agent", "tool_input": {
            "prompt": "Do X, answer inline.",
            "run_in_background": False}})
        # Task tool, empty prompt, non-dispatch tools → never deny
        assert not missing_channel({"tool_name": "Task", "tool_input": {
            "prompt": "no channel here"}})
        assert not missing_channel({"tool_name": "Agent", "tool_input": {}})
        assert not missing_channel({"tool_name": "Bash", "tool_input": {
            "command": "ls"}})
        assert "Blocked" in deny_text()
        print("brief-reminder: all tests passed")
        sys.exit(0)
    sys.exit(main())
