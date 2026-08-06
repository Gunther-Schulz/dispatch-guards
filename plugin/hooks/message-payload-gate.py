#!/usr/bin/env python3
"""PreToolUse(SendMessage) gate: payload vs. pointer.

Primary rationale — context economy: a large result injected into the
dispatcher's running session occupies its context window for the rest
of the session; every later turn carries it, and the long-context
session is where tokens are scarcest. A file plus a short pointer
keeps the full data on disk, selectively readable on demand.

Secondary (hypothesis, n=2, UNPROVEN — the evidence has one home:
dev-notes/payload-cache-correlation.md, which also states what would
settle it): large injections have coincided with full prompt-cache
rewrites of the receiving session (Claude Code #27048 class).
Cache-key-stabilizing proxies may mitigate that class upstream; they
do not touch the context-economy point at all, and this lane rests on
the primary rationale alone.

The expensive direction is subagent → dispatcher (long main context);
the reverse (dispatcher briefing a subagent) may be long — the
receiver's context is small. So: in a SUBAGENT context, a string
message beyond `max_message_chars` is denied with the file+pointer
instruction. Structured (object) messages — protocol responses — pass.

Fail-open on parse errors; `--test` bite-test included.
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from _dispatch_common import fire, is_subagent, policy  # noqa: E402

DEFAULT_MAX = 3000


def max_chars() -> int:
    v = policy().get("max_message_chars", DEFAULT_MAX)
    return v if isinstance(v, int) and v > 0 else DEFAULT_MAX


def check(payload: dict) -> str | None:
    """Return a deny reason, or None (= allow)."""
    if payload.get("tool_name") != "SendMessage":
        return None
    if not is_subagent(payload):
        return None  # dispatcher → subagent: long briefs are legitimate
    msg = (payload.get("tool_input") or {}).get("message")
    if not isinstance(msg, str):
        return None  # structured protocol responses are small and pass
    if len(msg) <= max_chars():
        return None
    return (
        f"Payload gate: message is {len(msg)} chars (limit "
        f"{max_chars()}). A large result injected into the dispatcher's "
        "session occupies its context for the rest of the session (and "
        "can force a full prompt-cache rewrite). Write the full result "
        "to a FILE, then send a SHORT message: the key findings plus "
        "the file path."
    )


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0  # never fail the workflow on a hook parse error
    reason = check(payload)
    if reason:
        # mode-aware deny: logged, warn-stageable via guard_modes
        fire(reason, source="dispatch-guards/message-payload-gate",
             payload=payload)
    return 0


if __name__ == "__main__":
    if "--test" in sys.argv:
        os.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = "/nonexistent"
        from _dispatch_common import _reset_policy_cache
        _reset_policy_cache()
        gross = "x" * 4000
        klein = "kurzer Bericht, Datei: /tmp/x.md"
        # Subagent + groß → deny
        assert check({"tool_name": "SendMessage", "agent_id": "a1",
                      "tool_input": {"message": gross}}) is not None
        # Subagent + klein → pass
        assert check({"tool_name": "SendMessage", "agent_id": "a1",
                      "tool_input": {"message": klein}}) is None
        # Hauptsession + groß → pass (Zusatzauftrag-Richtung)
        assert check({"tool_name": "SendMessage",
                      "tool_input": {"message": gross}}) is None
        # Objekt-Nachricht (Protokoll) → pass
        assert check({"tool_name": "SendMessage", "agent_id": "a1",
                      "tool_input": {"message": {"type": "shutdown_response",
                                                 "request_id": "r", "approve": True}}}) is None
        # anderes Tool → pass
        assert check({"tool_name": "Bash", "agent_id": "a1",
                      "tool_input": {"message": gross}}) is None
        # Config-Schwelle greift
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as tf:
            tf.write('{"max_message_chars": 100}')
            os.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = tf.name
        _reset_policy_cache()
        assert check({"tool_name": "SendMessage", "agent_id": "a1",
                      "tool_input": {"message": klein * 10}}) is not None
        print("message-payload-gate: all tests passed")
        sys.exit(0)
    sys.exit(main())
