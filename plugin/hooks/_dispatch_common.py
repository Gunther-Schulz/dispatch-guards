"""Shared helpers for the dispatch-guards plugin (one file per lifecycle event).

Mirrors the _restrict_common.py pattern: small hooks per lifecycle
event, shared logic here.

Environment binding (as-of 2026-07-18, Claude Code hooks): a subagent
context is marked by the presence of a non-empty `agent_id` field in the
hook input JSON; the main session has none. If a harness change removes
the field, the guards silently treat everything as the main session
(fail-open) — the --test bite-tests registered in the machine-bootstrap
doctor are the tripwire for that.
"""
from __future__ import annotations

import json
import sys


def is_subagent(payload: dict) -> bool:
    """True when the hook input comes from a subagent context."""
    return bool(payload.get("agent_id"))


def deny(reason: str) -> None:
    """Emit a clean PreToolUse deny (exit-0 JSON) and exit."""
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }))
    sys.exit(0)


def ask(reason: str) -> None:
    """Emit an 'ask' payload (force the permission dialog) and exit 0.

    reason is duplicated as systemMessage: the dialog does not visibly
    render permissionDecisionReason (live finding 2026-07-18, see
    _restrict_common.ask)."""
    print(json.dumps({
        "systemMessage": reason,
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": reason,
        }
    }))
    sys.exit(0)


# ── Policy (mechanism/policy split) ──────────────────────────────────────
# The plugin ships generic defaults; site policy is merged from
# $CLAUDE_DISPATCH_GUARDS_CONFIG, else ~/.claude/dispatch-guards.json.
# Fail-open: an unreadable config yields the defaults.
import os

_DEFAULTS: dict = {
    "models": ["sonnet", "opus", "haiku", "fable"],
    "deny_models": [],
    "ask_models": [],
    "discipline_doc": None,
    "max_message_chars": 3000,
}
_POLICY_CACHE: dict | None = None


def policy() -> dict:
    global _POLICY_CACHE
    if _POLICY_CACHE is None:
        cfg = dict(_DEFAULTS)
        pfad = os.environ.get("CLAUDE_DISPATCH_GUARDS_CONFIG") or os.path.expanduser(
            "~/.claude/dispatch-guards.json")
        try:
            with open(pfad, encoding="utf-8") as f:
                loaded = json.load(f)
            if isinstance(loaded, dict):
                cfg.update({k: loaded[k] for k in _DEFAULTS if k in loaded})
        except (OSError, json.JSONDecodeError, ValueError):
            pass  # fail-open: defaults
        _POLICY_CACHE = cfg
    return _POLICY_CACHE


def _reset_policy_cache() -> None:
    """Test helper: forget the cached config (used by --test bite-tests)."""
    global _POLICY_CACHE
    _POLICY_CACHE = None


def doc_ref(section: str) -> str:
    """A citable pointer into the site's discipline doc, or generic wording."""
    doc = policy().get("discipline_doc")
    return f"{doc} {section}" if doc else "your dispatch discipline"

