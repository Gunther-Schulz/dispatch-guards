"""Shared helpers for the dispatch-guards plugin (one file per lifecycle event).

Mirrors the _restrict_common.py pattern: small hooks per lifecycle
event, shared logic here.

Standing rules for every guard in this plugin (canonical home —
formerly dispatch-discipline.md §5, merged here with the skill-ify
move): each guard ships a `--test` self-check (bite-test),
registered in the machine-bootstrap doctor (dotfiles
bootstrap/doctor.py), so a harness change that silently breaks a
guard fails loudly. Guards stay FAIL-OPEN on hook-input parse
errors (verified per guard 2026-07-23 over the then-six guards;
later guards join the invariant through their own --test
parse-error bites; a broken guard must not brick every call, and
the enforced rules keep their non-hook safety nets) — the bite-tests
are the load-bearing compensation. Harness-dependent fields are
environment bindings, stamped with an as-of date where used.

Environment binding (as-of 2026-07-18, Claude Code hooks): a subagent
context is marked by the presence of a non-empty `agent_id` field in the
hook input JSON; the main session has none — confirmed live in a
subagent context as of 2026-07-28 (observed, not merely bite-tested).
If a harness change removes
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


def ask(reason: str, source: str = "dispatch-guards",
        payload: dict | None = None) -> None:
    """Emit an 'ask' payload (force the permission dialog) and exit 0.

    reason is duplicated as systemMessage: the dialog does not visibly
    render permissionDecisionReason (live finding 2026-07-18, see
    _restrict_common.ask). Logged to the fire log (an ask is a fire —
    the fire-rate review counts dialogs too)."""
    fire_log(source, "ask", reason, payload)
    print(json.dumps({
        "systemMessage": reason,
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": reason,
        }
    }))
    sys.exit(0)


# ── Fire log + guard modes (harvest 2026-08-06, dev-notes) ───────────────
# Every guard fire — deny, ask, warn, block — appends one JSONL line.
# Consumers: the fire-rate review (corpus Calibration: a guard firing on
# legitimate work trains the override reflex — the log is the instrument
# that makes fire rates countable instead of remembered) and warn→deny
# promotion decisions for staged lanes. Data home OUTSIDE any repo,
# mirroring dispatch-log.py.
_REASON_MAX = 300


def fire_log_path():
    from pathlib import Path
    if env := os.environ.get("CLAUDE_DISPATCH_GUARDS_FIRELOG"):
        return Path(env).expanduser()
    xdg = os.environ.get("XDG_DATA_HOME") or "~/.local/share"
    return Path(xdg).expanduser() / "claude" / "dispatch-guards-fires.jsonl"


def fire_log(source: str, mode: str, reason: str,
             payload: dict | None = None) -> None:
    """Append one fire record. Fail-open on every error — logging must
    never brick a call, and a fire that goes unlogged still fires."""
    try:
        from datetime import datetime, timezone
        payload = payload or {}
        rec = {
            "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "guard": source.rsplit("/", 1)[-1],
            "mode": mode,
            "session_id": payload.get("session_id"),
            "agent_id": payload.get("agent_id"),
            "tool_name": payload.get("tool_name"),
            "reason": reason[:_REASON_MAX],
        }
        pfad = fire_log_path()
        pfad.parent.mkdir(parents=True, exist_ok=True)
        with pfad.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    except Exception:
        pass


def guard_mode(source: str, default: str = "deny") -> str:
    """Effective mode for a guard's deny lane: site policy `guard_modes`
    keyed by guard name (the source tag's last segment), else the
    guard's own shipped default. Modes: deny | warn | off. A malformed
    value falls back to the default (fail toward the shipped behavior,
    not toward silence)."""
    modes = policy().get("guard_modes")
    if not isinstance(modes, dict):
        return default
    v = modes.get(source.rsplit("/", 1)[-1], default)
    return v if v in ("deny", "warn", "off") else default


def fire(reason: str, source: str = "dispatch-guards",
         payload: dict | None = None, default_mode: str = "deny") -> None:
    """Mode-aware deny: the single exit for every deny lane.

    deny → the standard deny JSON (exit). warn → additionalContext
    "WARN (staging…)" (exit) — the lane is visible and logged but does
    not block; how staged lanes earn promotion: dev-notes harvest note.
    off → logged, silent (exit). Every mode logs to the fire log
    first, so a staged lane's false-fire rate is countable before it
    ever denies real work."""
    mode = guard_mode(source, default_mode)
    fire_log(source, mode, reason, payload)
    if mode == "deny":
        print(json.dumps(_deny_payload(reason, source)))
    elif mode == "warn":
        print(json.dumps({
            "systemMessage": f"[{source}] WARN (staging): {reason}",
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "additionalContext": (
                    f"[{source}] WARN — staging mode, this lane would "
                    f"DENY: {reason}"),
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
    "discovery_volume_bytes": 50000,
    "guard_modes": {},
    "write_claim_ttl_hours": 6,
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


if __name__ == "__main__" and "--test" in sys.argv:
    # Bite-test for the shared machinery itself (fire log, guard modes,
    # fire() routing). The per-guard files test their own lanes; this
    # block owns what they all share. Auto-discovered by the doctor's
    # content-based "--test" scan like every guard file.
    import contextlib
    import io
    import tempfile
    from pathlib import Path

    os.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = "/nonexistent"
    _reset_policy_cache()

    with tempfile.TemporaryDirectory() as td:
        os.environ["CLAUDE_DISPATCH_GUARDS_FIRELOG"] = td + "/f/fires.jsonl"

        # ── guard_mode: defaults, site override, malformed values ──
        assert guard_mode("dispatch-guards/x") == "deny"
        assert guard_mode("dispatch-guards/x", default="warn") == "warn"
        with tempfile.NamedTemporaryFile("w", suffix=".json",
                                         delete=False, dir=td) as tf:
            tf.write('{"guard_modes": {"amend-gate": "warn",'
                     ' "push-gate": "bogus", "x-gate": "off"}}')
            cfg = tf.name
        os.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = cfg
        _reset_policy_cache()
        assert guard_mode("dispatch-guards/amend-gate") == "warn"
        assert guard_mode("dispatch-guards/x-gate") == "off"
        # malformed value → shipped default, never silence
        assert guard_mode("dispatch-guards/push-gate") == "deny"
        assert guard_mode("dispatch-guards/unlisted") == "deny"

        # ── fire(): deny / warn / off routing, each logged ──
        def run_fire(default_mode="deny", source="dispatch-guards/amend-gate"):
            buf = io.StringIO()
            code = None
            with contextlib.redirect_stdout(buf):
                try:
                    fire("R" * 400, source=source,
                         payload={"session_id": "s1", "agent_id": "a1",
                                  "tool_name": "Bash"},
                         default_mode=default_mode)
                except SystemExit as e:
                    code = e.code
            return code, buf.getvalue()

        code, out = run_fire()  # amend-gate is warn per config above
        assert code == 0
        j = json.loads(out)
        assert "additionalContext" in j["hookSpecificOutput"], j
        assert "would DENY" in j["hookSpecificOutput"]["additionalContext"]
        assert "permissionDecision" not in j["hookSpecificOutput"]

        code, out = run_fire(source="dispatch-guards/unlisted")  # deny
        assert code == 0
        j = json.loads(out)
        assert j["hookSpecificOutput"]["permissionDecision"] == "deny"
        assert j["systemMessage"].startswith("[dispatch-guards/unlisted]")

        code, out = run_fire(source="dispatch-guards/x-gate")  # off
        assert code == 0 and out == "", (code, repr(out))

        # ── ask(): logged and emitting the dialog payload ──
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            try:
                ask("dialog?", source="dispatch-guards/model-gate",
                    payload={"session_id": "s2", "tool_name": "Agent"})
            except SystemExit as e:
                assert e.code == 0
        j = json.loads(buf.getvalue())
        assert j["hookSpecificOutput"]["permissionDecision"] == "ask"

        # ── the log: one line per fire, fields + truncation ──
        lines = [json.loads(ln) for ln in
                 Path(td + "/f/fires.jsonl").read_text().splitlines()]
        assert len(lines) == 4, len(lines)
        modes = [ln["mode"] for ln in lines]
        assert modes == ["warn", "deny", "off", "ask"], modes
        assert lines[0]["guard"] == "amend-gate"
        assert lines[0]["agent_id"] == "a1"
        assert len(lines[0]["reason"]) == _REASON_MAX  # truncated
        assert lines[3]["guard"] == "model-gate"
        assert lines[3]["session_id"] == "s2"

        # ── fail-open: unwritable log path never raises or blocks ──
        os.environ["CLAUDE_DISPATCH_GUARDS_FIRELOG"] = "/proc/nope/f.jsonl"
        fire_log("dispatch-guards/x", "deny", "r", {})  # must not raise
        code, out = run_fire(source="dispatch-guards/unlisted")
        assert code == 0 and "deny" in out  # fire still denies unlogged

        del os.environ["CLAUDE_DISPATCH_GUARDS_FIRELOG"]
        os.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = "/nonexistent"
        _reset_policy_cache()

    print("_dispatch_common: all tests passed")
    sys.exit(0)

