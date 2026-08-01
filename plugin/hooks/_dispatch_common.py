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


def _deny_payload(reason: str, source: str = "dispatch-guards") -> dict:
    """Build the deny JSON. Source-tagged and dual-field by design:
    permissionDecisionReason reaches the MODEL, systemMessage the user's
    UI — a deny carrying only one of them leaves the other audience with
    the harness's bare "Hook PreToolUse:<tool> denied this tool", which
    two sessions misattributed to a Claude Code permission bug (live
    finding 2026-07-30).

    Why the tag is load-bearing: CC builds the denial with the hook's
    identity (decisionReason.hookName/hookSource) but does not persist it
    to the transcript, so a guard fire is not attributable after the fact
    unless the guard names itself. The transcript's toolDenialKind is NOT
    the missing discriminator — the client documents "permission-rule" as
    covering hooks (verified in the shipped binary, 2.1.220), so it is
    working as designed. This tag is the only self-identification a guard
    fire gets."""
    tagged = f"[{source}] {reason}"
    return {
        "systemMessage": tagged,
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": tagged,
        },
    }


def deny(reason: str, source: str = "dispatch-guards") -> None:
    """Emit a clean PreToolUse deny (exit-0 JSON) and exit."""
    print(json.dumps(_deny_payload(reason, source)))
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


# ── Push-command detection (shared: subagent-push-gate + push-claim-reminder) ──
import re     # noqa: E402
import shlex  # noqa: E402

_GIT_RE = re.compile(r"\b(git|gh)\b")
_PUSH_RE = re.compile(r"\bpush\b")
_STASH_PUSH_RE = re.compile(r"\bstash\s+push\b")


def is_push_command(cmd: str) -> bool:
    """True iff the command actually invokes a push: a `git`/`gh` token
    plus a standalone `push` (or `--push`) token, split with shlex so
    QUOTED text — commit messages, quoted paths — never matches. The
    2026-08-01 false-fire class: a standing commit-message line ("rides
    the next code push") fired the reminder on every commit of a repo,
    and the same substring match would false-DENY a subagent's commit —
    a deny on legitimate work trains the override reflex. A `push` token
    directly after `stash` is the purely-local `git stash push` —
    exempt. Unparseable quoting falls back to the substring match
    (fires; a guard unsure of what it reads stays loud, both consumers
    are deny/remind). Accepted residue unchanged: unquoted standalone
    `push` words (`git log --grep push`) still match; deliberate
    obfuscation stays the session-cut check's net."""
    try:
        tokens = shlex.split(cmd)
    except ValueError:
        stripped = _STASH_PUSH_RE.sub("stash", cmd)
        return bool(_GIT_RE.search(stripped) and _PUSH_RE.search(stripped))
    if not any(t in ("git", "gh") for t in tokens):
        return False
    prev = ""
    for t in tokens:
        if (t == "push" and prev != "stash") or t == "--push":
            return True
        prev = t
    return False

