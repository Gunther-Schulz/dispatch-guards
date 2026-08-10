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
environment bindings, stamped with an as-of date where used. A
guard that EXTRACTS a value from its input (a path, an identifier)
distinguishes "could not extract" from "extracted, and clean": a
character class that silently truncates at an unexpected byte
(umlauts, spaces) yields a value whose negative verdict is
indistinguishable from a legitimate clean finding — extraction
failure maps to could-not-verify (fail-open or WARN per the
guard's error direction), never to a pass.
A guard that shells out to git against a working copy uses
`--no-optional-locks`: a plain `git status` REWRITES the index
(measured 2026-08-10), so an unflagged read-shaped call takes
index.lock and mutates shared state on every evaluation — the same
shared-index hazard that forbids `git add` for dispatched writers,
arriving through a command that reads as read-only. And a guard
`--test` fixture that runs `git commit` pins
`-c core.hooksPath=/nonexistent` (plus `--no-verify`): fixture repos
inherit the machine's GLOBAL core.hooksPath, so an unpinned fixture
silently runs the operator's real hook battery inside the tempdir.

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
            "shape": command_shape(payload),
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


# ── Command shape + push detection ───────────────────────────────────────
import re     # noqa: E402
import shlex  # noqa: E402

_SHAPE_MAX = 120
# A safe word: lowercase verb-ish, no separators, no case mixing. Values
# and secrets (URLs, tokens, paths, messages) fail it by construction.
_SHAPE_WORD = re.compile(r"^[a-z][a-z0-9-]*$")
_SHAPE_LONG_FLAG = re.compile(r"^--[a-z][a-z0-9-]*$")
_SHAPE_SEPS = frozenset({"&&", "||", ";", "|", "&", "(", ")", "{", "}"})


def command_shape(payload: dict) -> str | None:
    """A secret-free discriminator for WHAT a guard fired on.

    The fire log's `reason` is CONSTANT per lane, so a reviewer
    counting fires cannot separate a false fire from a true one. The
    `--push` false fire (a `git remote set-url --push` config write
    denied as a push) logged identically to a real push from the day
    its arm was minted, and was found by accident rather than from the
    log — the instrument for the warn→deny promotion criterion could
    not answer the question the criterion asks. This field is the
    missing half.

    Operands carry the secrets — tokens in URLs, `-p<password>`,
    commit messages, paths — so the shape keeps only VERBS and FLAGS.
    Per command-position invocation: the command's basename, up to two
    following subcommand words, and its flags — long flags with any
    `=value` stripped, short flags reduced to their letter, because a
    short flag can carry its value attached (`-p<password>`) in a form
    that passes any looks-like-a-flag pattern. Words stop at the first
    flag, since what follows a flag is its value. Anything failing the
    safe-word pattern degrades to `?` rather than being emitted. So
    `git remote set-url --push origin https://tok@host/r.git` reduces
    to `git remote set-url --push`, `git commit -m "<message>"` to
    `git commit -m`, and `SECRET=x curl -H "<auth>" <url>` to
    `? curl -H`.

    Dispatch tools report their routing fields instead (both
    non-secret and the discriminator that matters for a model gate).
    Every other tool returns None: adding a shape for Write/Edit or
    SendMessage means deciding what of a path or a message body is
    safe, which no evidence yet demands.
    """
    tool = payload.get("tool_name")
    tool_input = payload.get("tool_input") or {}
    if tool in ("Agent", "Task", "Workflow"):
        bits = [str(tool_input.get(k)) for k in ("subagent_type", "model")
                if tool_input.get(k)]
        return " ".join(bits)[:_SHAPE_MAX] or None
    if tool != "Bash":
        return None
    try:
        tokens = shlex.split(tool_input.get("command", "") or "")
    except ValueError:
        return None

    shape: list = []
    at_cmd, words = True, 0
    for t in tokens:
        if t in _SHAPE_SEPS or t.endswith(";"):
            shape.append(";")
            at_cmd, words = True, 0
            continue
        if at_cmd:
            name = os.path.basename(t)
            shape.append(name if _SHAPE_WORD.match(name) else "?")
            at_cmd, words = False, 0
            continue
        if t.startswith("--"):
            flag = t.split("=", 1)[0]
            shape.append(flag if _SHAPE_LONG_FLAG.match(flag) else "--?")
            words = 99          # what follows a flag is its VALUE
        elif t.startswith("-"):
            # A SHORT flag can carry its value attached and unseparated
            # (`-p<password>`, `-uroot`), and that form passes any
            # "looks like a flag" pattern — the leak this keeps out.
            # Only the letter survives; one character cannot be a secret.
            shape.append(f"-{t[1]}" if t[1:2].isalnum() else "-?")
            words = 99
        elif words < 2 and _SHAPE_WORD.match(t):
            shape.append(t)
            words += 1
        else:
            words = 99          # first operand ends the subcommand run
    return " ".join(shape)[:_SHAPE_MAX] or None


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
    a deny on legitimate work trains the override reflex.

    Two exemptions, each a token that reads as a push and is not one:

    - a `push` directly after `stash` — the purely-local `git stash push`.
    - a `--push` anywhere after a `remote` token — `git remote set-url
      --push` is a CONFIG WRITE, not a push. The `--push` arm exists for
      `gh pr create --push`; its only other real git referent is that
      set-url form, so before the exemption the arm denied a subagent's
      config write with a push-discipline message, and reminded the main
      session of a claim check for a command that publishes nothing.
      (What that command DOES warrant — it rewrites the shared config
      from a worktree — is worktree-config-gate's lane.) Scoped to the
      token, not the command: `git remote set-url --push … && git push`
      still matches on the later bare `push`.

    Unparseable quoting falls back to the substring match (fires; a
    guard unsure of what it reads stays loud, both consumers are
    deny/remind). Accepted residue unchanged: unquoted standalone
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
    seen_remote = False
    for t in tokens:
        if t == "remote":
            seen_remote = True
        if t == "push" and prev != "stash":
            return True
        if t == "--push" and not seen_remote:
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

    # ── command_shape: the discriminator, and the secrets it must not
    # carry. Expectations derived from what the fire-rate review needs
    # to ANSWER (which arm fired) and from what the log must never
    # become (a plaintext secret store) — not from the implementation.
    def S(cmd, tool="Bash"):
        return command_shape({"tool_name": tool,
                              "tool_input": {"command": cmd}})

    # (i) THE motivating case: the two records that were identical
    poison = "git remote set-url --push origin https://tok@host/r.git"
    assert S(poison) == "git remote set-url --push", S(poison)
    assert S("git push origin main") != S(poison)
    assert S("gh pr create --push") == "gh pr create --push"
    # (ii) operands dropped, flags kept, `=value` stripped
    assert S("git commit -m 'a long secret message'") == "git commit -m"
    assert S("git config --unset-all remote.origin.pushurl") == \
        "git config --unset-all"
    assert S("curl --header=Authorization:Bearer-xyz https://h/p") == \
        "curl --header"
    # (iii) SECRETS NEVER SURVIVE — the load-bearing claim, one case
    # per carrier shape. Each string below must be absent from the
    # shape entirely.
    for cmd, secret in [
        (poison, "tok"),
        ("git commit -m 'password is hunter2'", "hunter2"),
        ("mysql -phunter2 -u root", "hunter2"),
        ("curl -H 'Authorization: Bearer sk-abc123' https://h", "sk-abc123"),
        ("curl https://user:pw@host/path", "pw"),
        ("SECRET=abc123 git push", "abc123"),
        ("aws s3 cp /home/g/private/keys.txt s3://b", "keys"),
        ("git clone https://x-token:ghp_AAA@github.com/o/r", "ghp_AAA"),
        ("echo 'ssh-rsa AAAAB3Nza' >> ~/.ssh/authorized_keys", "AAAAB3Nza"),
    ]:
        got = S(cmd) or ""
        assert secret not in got, f"LEAK: {secret!r} survived in {got!r}"
    # (iii-b) PROPERTY, stronger than any case list: every emitted
    # token is a separator, a degraded marker, a safe word, or a
    # normalized flag. A secret can therefore only survive by BEING
    # one of those — which the case list above pins separately.
    _ok = {";", "?", "-?", "--?"}
    for cmd in [
        poison, "mysql -phunter2 -u root", "SECRET=abc123 git push",
        "curl -H 'Bearer sk-AAA' https://u:pw@h/p?t=SEKRET#frag",
        "psql 'postgres://u:p@h:5432/db' -c 'SELECT 1'",
        "docker run -e API_KEY=sk-XYZ img:tag /bin/sh -c 'echo $X'",
        "ssh -i ~/.ssh/id_ed25519 deploy@10.0.0.1 'sudo rm -rf /srv'",
        "openssl enc -aes-256-cbc -k Passw0rd! -in a -out b",
        "git -c http.extraHeader='Authorization: Basic QUJD' push",
        "find / -name '*.pem' -exec cat {} \\;",
        "printf '%s' \"$TOKEN\" | gh auth login --with-token",
    ]:
        for tok in (S(cmd) or "").split():
            assert (tok in _ok or _SHAPE_WORD.match(tok)
                    or _SHAPE_LONG_FLAG.match(tok)
                    or (len(tok) == 2 and tok[0] == "-"
                        and tok[1].isalnum())), \
                f"unconstrained token {tok!r} from {cmd!r}"
    # (iv) command position hardened: env prefixes and paths
    assert S("SECRET=abc123 git push").startswith("?")
    assert S("/usr/local/bin/git push") == "git push"      # basename
    # (v) sequencing preserved, so a fused command stays readable
    assert S("git commit -m x && git push") == "git commit -m ; git push"
    # (vi) non-Bash: dispatch tools report routing, others nothing
    assert command_shape({"tool_name": "Agent", "tool_input": {
        "subagent_type": "general-purpose", "model": "fable"}}) == \
        "general-purpose fable"
    assert command_shape({"tool_name": "Write",
                          "tool_input": {"file_path": "/secret/x"}}) is None
    assert command_shape({"tool_name": "SendMessage"}) is None
    # (vii) degenerate input never raises
    assert S("") is None
    assert S("git config --get x 'unterminated") is None   # unparseable
    assert command_shape({}) is None
    assert len(S("git " + " ".join(f"--flag{i}" for i in range(60))) or "") \
        <= _SHAPE_MAX

    print("_dispatch_common: all tests passed")
    sys.exit(0)

