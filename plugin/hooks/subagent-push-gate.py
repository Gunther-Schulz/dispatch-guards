#!/usr/bin/env python3
"""PreToolUse(Bash) gate: subagents must not push.

Enforces the integration rule mechanically (global CLAUDE.md
"Dispatched work" / dispatch skill §1): subagents commit
unpushed; pushing is the dispatcher's act, after verification.

Detection: subagent context = presence of `agent_id` in the hook input
(_dispatch_common, as-of 2026-07-18). Matching: the shared token matcher
(_dispatch_common.is_push_command) — a `git`/`gh` token plus a
standalone `push`/`--push` token; quoted text mentioning push (a commit
message like "unpushed, dispatcher will push") does not deny — a deny on
a legitimate commit trains the override reflex (2026-08-01 class, found
via the reminder twin). `git stash push` (purely local) is exempt.
Accepted residue: deliberate obfuscation (bash -c strings, aliases) is
NOT caught here — the session-cut unpushed/ahead-repos check remains
the outer net.

Fail-open on parse errors (a broken guard must not brick every Bash
call); the --test bite-test is the compensation and is registered in
the machine-bootstrap doctor.
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from _dispatch_common import deny, is_push_command, is_subagent  # noqa: E402

REASON = (
    "Push gate: subagents commit UNPUSHED — pushing is the dispatcher's "
    "act after verification (dispatch skill §1). Commit your "
    "work and report the hash; the main agent pushes."
)


def check(payload: dict) -> str | None:
    """Return a deny reason, or None (= allow through)."""
    if payload.get("tool_name") != "Bash":
        return None
    if not is_subagent(payload):
        return None
    cmd = (payload.get("tool_input") or {}).get("command", "") or ""
    if is_push_command(cmd):
        return REASON
    return None


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0  # never fail the workflow on a hook parse error
    reason = check(payload)
    if reason:
        deny(reason, source="dispatch-guards/subagent-push-gate")  # prints exit-0 deny JSON and exits
    return 0


if __name__ == "__main__":
    if "--test" in sys.argv:
        sub = {"tool_name": "Bash", "agent_id": "a1"}
        main_s = {"tool_name": "Bash"}
        assert check({**sub, "tool_input": {"command": "git push"}}) is not None
        assert check({**sub, "tool_input": {"command": "git -C /x push origin main"}}) is not None
        assert check({**sub, "tool_input": {"command": "cd /x && git push --force"}}) is not None
        assert check({**sub, "tool_input": {"command": "gh pr create --push"}}) is not None
        assert check({**sub, "tool_input": {"command": "git commit -m x"}}) is None
        assert check({**sub, "tool_input": {"command": "echo push it"}}) is None  # no git token
        assert check({**main_s, "tool_input": {"command": "git push"}}) is None  # main session
        assert check({**sub, "tool_input": {}}) is None
        assert check({"tool_name": "Read", "agent_id": "a1",
                      "tool_input": {"command": "git push"}}) is None
        # documented accepted false positive: reading about pushes
        assert check({**sub, "tool_input": {"command": "git log --grep push"}}) is not None
        # git stash push is local (no remote) — normalized out, allowed
        assert check({**sub, "tool_input": {"command": "git stash push"}}) is None
        assert check({**sub, "tool_input": {"command": 'git stash push -m "wip"'}}) is None
        assert check({**sub, "tool_input": {"command": "git stash push && git push origin main"}}) is not None
        # regression (2026-08-01): a subagent COMMIT whose quoted message
        # mentions push must not be denied — a false deny on legitimate
        # work trains the override reflex.
        assert check({**sub, "tool_input": {"command": 'git commit -m "unpushed, dispatcher will push"'}}) is None
        print("subagent-push-gate: all tests passed")
        sys.exit(0)
    sys.exit(main())
