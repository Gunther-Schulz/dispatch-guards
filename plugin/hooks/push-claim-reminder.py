#!/usr/bin/env python3
"""PreToolUse(Bash) reminder: claim every outgoing commit before a push.

Push-side counterpart to brief-reminder, mechanizing the reminder half
of the §1 push-set rule (dispatch skill): the push set is the
branch, never "my commits" — on a working copy shared with any
co-writer, `git push` publishes every local commit, including an
agent's mid-verification work. The observed slip is a chained
`add && commit && push` that publishes co-writer commits without the
`git log origin/<branch>..<branch>` claim pass.

One line of additionalContext lands before any main-session git/gh
push; the hook reminds — it never judges and never blocks (an ask/deny
on every push would fire on legitimate work constantly and train the
override reflex; the judgment stays with the dispatcher). Subagent
context is excluded: subagent pushes are already DENIED outright by
subagent-push-gate, and a reminder beside a denial is noise.

Matching: the shared token matcher (_dispatch_common.is_push_command) —
mirrors subagent-push-gate by construction (same function). Quoted text
mentioning push (commit messages, paths) does not fire; `git stash
push` (purely local) is exempt.

Fail-open on parse errors (a broken guard must not brick every Bash
call); the --test bite-test is the compensation, auto-discovered by
the machine-bootstrap doctor's plugin-hooks sweep.
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from _dispatch_common import doc_ref, is_push_command, is_subagent  # noqa: E402


def reminder_text() -> str:
    return (
        f"Push starting — claim check ({doc_ref('§1')}): the push set is "
        "the branch, never \"my commits\". On a working copy any co-writer "
        "(agent, peer session) has touched, run "
        "`git log origin/<branch>..<branch>` and claim each outgoing "
        "commit first; an unexpected commit halts the push."
    )


def check(payload: dict) -> str | None:
    """Return the reminder text, or None (= stay silent)."""
    if payload.get("tool_name") != "Bash":
        return None
    if is_subagent(payload):
        return None
    cmd = (payload.get("tool_input") or {}).get("command", "") or ""
    if is_push_command(cmd):
        return reminder_text()
    return None


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
        main_s = {"tool_name": "Bash"}
        sub = {"tool_name": "Bash", "agent_id": "a1"}
        assert check({**main_s, "tool_input": {"command": "git push"}}) is not None
        assert check({**main_s, "tool_input": {"command": "git add -A && git commit -m x && git push"}}) is not None
        assert check({**main_s, "tool_input": {"command": "git -C /x push origin main"}}) is not None
        assert check({**main_s, "tool_input": {"command": "gh pr create --push"}}) is not None
        assert check({**main_s, "tool_input": {"command": "git commit -m x"}}) is None
        assert check({**main_s, "tool_input": {"command": "echo push it"}}) is None  # no git token
        assert check({**sub, "tool_input": {"command": "git push"}}) is None  # subagent: deny-gate's lane
        assert check({**main_s, "tool_input": {}}) is None
        assert check({"tool_name": "Read", "tool_input": {"command": "git push"}}) is None
        # git stash push is local (no remote) — normalized out, silent
        assert check({**main_s, "tool_input": {"command": "git stash push"}}) is None
        assert check({**main_s, "tool_input": {"command": "git stash push && git push"}}) is not None
        # documented accepted false positive: reading about pushes
        assert check({**main_s, "tool_input": {"command": "git log --grep push"}}) is not None
        # regression (2026-08-01, red on the old substring matcher —
        # confirmed live by probe): QUOTED text mentioning push must not
        # fire; this repo's standing hold-line fired on every commit.
        assert check({**main_s, "tool_input": {"command": 'git commit -m "held — rides the next code push"'}}) is None
        assert check({**main_s, "tool_input": {"command": "chmod +x hooks/push-claim-reminder.py && git add hooks/push-claim-reminder.py && git commit -m x"}}) is None
        print("push-claim-reminder: all tests passed")
        sys.exit(0)
    sys.exit(main())
