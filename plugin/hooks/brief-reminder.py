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
        print("brief-reminder: all tests passed")
        sys.exit(0)
    sys.exit(main())
