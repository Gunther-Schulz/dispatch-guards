#!/usr/bin/env python3
"""PostToolUse(Agent|Task) reminder: check the subagent's closing report.

Kills the forget-to-check failure (~10 idle-without-report cases/day
observed): when a dispatch returns, one line lands next to the tool
result reminding the dispatcher to verify the closing report before
booking the outcome (dispatch skill references/forms.md §2, SKILL.md §4). The hook never
judges the report — it can't; judgment stays with the dispatcher.

Design decision (2026-07-18, verified against the Claude Code hooks
reference): SubagentStop `additionalContext` surfaces only in the
SUBAGENT's own transcript, not the parent session — so this hooks
PostToolUse on Agent|Task instead, whose `additionalContext` surfaces
in the dispatching conversation next to the tool result. Environment
binding as-of 2026-07-18; --test is the tripwire (bootstrap doctor).
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from _dispatch_common import policy  # noqa: E402


def reminder_text() -> str:
    doc = policy().get("discipline_doc")
    form = (f"{doc} §2, or the project's own report form" if doc
            else "your closing-report form")
    return (
        "Dispatch closed — before booking this result: check the closing "
        f"report ({form}). Missing or incomplete → demand it; verify its "
        "claims in the artifact before any push/merge/publish."
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
                "hookEventName": "PostToolUse",
                "additionalContext": reminder,
            }
        }))
    return 0


if __name__ == "__main__":
    if "--test" in sys.argv:
        assert check({"tool_name": "Agent"}) is not None
        assert check({"tool_name": "Task"}) is not None
        assert check({"tool_name": "Bash"}) is None
        assert check({}) is None
        print("report-reminder: all tests passed")
        sys.exit(0)
    sys.exit(main())
