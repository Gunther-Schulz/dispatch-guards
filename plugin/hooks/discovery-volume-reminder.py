#!/usr/bin/env python3
"""PostToolUse(Bash|Grep|Glob) reminder: a large search result just
landed in MAIN-session context.

Root cause this tripwires (third loaded-but-inert instance of the
routing rule, 2026-08-05): CLAUDE.md's model-routing rule names the
tell ("the second consecutive discovery call in the main session")
and the skip condition ("met carrying the running work's momentum"),
and still did not fire on a 72KB dependents sweep run inline — the
route-named-in-the-GO-reply convention surfaced the miss to the
operator, not at the moment. Per the precipitation rule the
computable slice precipitates: ONE search-shaped tool result above a
size threshold entering main-session context. The judgment half —
should this have been a dispatch? — stays prose (CLAUDE.md model
routing; dispatch skill §1 discovery exception); this hook only
reminds, never blocks. Seam split: dispatch-skill-gate covers the
DISPATCH moment; this covers the missed-dispatch symptom upstream
of it.

Size measurement (probe-verified 2026-08-05, live PostToolUse dump):
the harness TRUNCATES `tool_response.stdout` to ~30000 chars before
the hook sees it, and persists the full output to a file, reporting
`persistedOutputPath` + `persistedOutputSize` in the response. A
threshold compared against the truncated string alone would never
fire above ~37KB — the dead-mechanism non-event. So the measured
size is max(persistedOutputSize, serialized response length); the
bite-test pins the truncated-but-persisted case as a known positive.

Matcher scope: Bash, Grep, Glob — the search-shaped tools. Read is
deliberately excluded: reading a named large source file is grounded
work on an identified artifact, not a sweep (the 575-line source
read beside the 72KB sweep was legitimate; the sweep was the miss).
Subagent contexts are silent — discovery running inline is exactly
a subagent's job (is_subagent, _dispatch_common).

Threshold: site policy (`discovery_volume_bytes`,
~/.claude/dispatch-guards.json), default 50000 — above routine test
output and ordinary command chatter, below the observed instance.
Advisory additionalContext only; a block here would fire on
legitimate large outputs (builds, suites) and train the override
reflex.
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from _dispatch_common import is_subagent, policy  # noqa: E402

_TOOLS = ("Bash", "Grep", "Glob")


def response_size(tool_response) -> int:
    """Best-available byte size of the FULL tool response. The harness
    hands hooks a truncated body for large outputs, with the real size
    in persistedOutputSize (probe-verified; see module docstring) —
    take the max of that and the serialized payload so both persisted
    and inline-large responses measure honestly."""
    persisted = 0
    if isinstance(tool_response, dict):
        raw = tool_response.get("persistedOutputSize")
        if isinstance(raw, (int, float)):
            persisted = int(raw)
    try:
        serialized = len(json.dumps(tool_response, default=str))
    except (TypeError, ValueError):
        serialized = 0
    return max(persisted, serialized)


def check(payload: dict) -> str | None:
    """Reminder text, or None (= stay silent)."""
    if payload.get("tool_name") not in _TOOLS:
        return None
    if is_subagent(payload):
        return None
    threshold = policy().get("discovery_volume_bytes") or 50000
    size = response_size(payload.get("tool_response"))
    if size < threshold:
        return None
    return (
        f"A ~{size // 1000}KB search result just entered main-session "
        "context — the discovery-dispatch rule may apply (CLAUDE.md "
        "model routing; dispatch skill §1, discovery exception): a "
        "question statable complete before its answer is known is "
        "briefable, and sweeps belong in a reader dispatch that "
        "returns the aggregate, not the dump."
    )


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
        from _dispatch_common import _reset_policy_cache
        os.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = "/nonexistent"
        _reset_policy_cache()

        big = "x" * 60000
        small = "x" * 1000

        # RED (known positive): over-threshold inline body fires.
        assert check({"tool_name": "Bash",
                      "tool_response": {"stdout": big, "stderr": ""}})
        # RED (the truncation case the probe surfaced): body truncated
        # to 30000 chars but persistedOutputSize carries the real size
        # — must still fire; a stdout-only measure would sit at ~30KB
        # and stay silent forever.
        truncated = {"tool_name": "Bash", "tool_response": {
            "stdout": "x" * 30000, "stderr": "",
            "persistedOutputPath": "/tmp/x", "persistedOutputSize": 108894}}
        assert check(truncated)
        assert response_size(truncated["tool_response"]) >= 108894

        # Under threshold → silent.
        assert check({"tool_name": "Bash",
                      "tool_response": {"stdout": small, "stderr": ""}}) is None
        # Subagent context → silent even over threshold.
        assert check({"tool_name": "Bash", "agent_id": "a1",
                      "tool_response": {"stdout": big}}) is None
        # Non-search tools (Read excluded by design) → silent.
        assert check({"tool_name": "Read",
                      "tool_response": {"file": big}}) is None
        assert check({"tool_name": "Edit", "tool_response": big}) is None
        # Grep/Glob string- or list-shaped responses measure too.
        assert check({"tool_name": "Grep", "tool_response": big})
        assert check({"tool_name": "Glob",
                      "tool_response": [big, big]})
        # Garbage/absent responses → silent, never a crash.
        assert check({"tool_name": "Bash"}) is None
        assert check({}) is None

        # Site-policy threshold override respected.
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".json",
                                         delete=False) as tf:
            tf.write('{"discovery_volume_bytes": 500}')
            os.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = tf.name
        _reset_policy_cache()
        assert check({"tool_name": "Bash",
                      "tool_response": {"stdout": small}})
        os.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = "/nonexistent"
        _reset_policy_cache()

        print("discovery-volume-reminder: all tests passed")
        sys.exit(0)
    sys.exit(main())
