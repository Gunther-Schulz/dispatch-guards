#!/usr/bin/env python3
"""PreToolUse(Bash) reminder: claim every outgoing commit before a push.

Push-side counterpart to brief-reminder, mechanizing the reminder half
of the §1 push-set rule (dispatch skill): the push set is the
branch, never "my commits" — on a working copy shared with any
co-writer, `git push` publishes every local commit, including an
agent's mid-verification work. The observed slip is a chained
`add && commit && push` that publishes co-writer commits without the
`git log origin/<branch>..<branch>` claim pass.

Two lanes, in order:

- FUSED-PUSH DENY. A push sharing its invocation with a `git commit`
  or a `git log` is refused outright: the claim check degrades to
  nothing whenever the push rides the same command as its read. Four
  recorded instances of the class — twice a push with no claim log,
  once `log && push` chained (the halt the log exists to trigger is
  structurally impossible once the push is already queued), and
  2026-08-05 the first harmful variant, a fused
  `git commit … && git push` that published two unclaimed peer
  commits. The read-then-decide seam only exists across separate
  invocations, so the guard restores it by denying the fusion, not by
  judging the push.
- REMINDER (unchanged). One line of additionalContext lands before any
  other main-session git/gh push; here the hook reminds — it never
  judges and never blocks (an ask/deny on every push would fire on
  legitimate work constantly and train the override reflex; the
  judgment stays with the dispatcher).

Subagent context is excluded from BOTH lanes: subagent pushes are
already DENIED outright by subagent-push-gate, and a reminder — or a
second, less apt denial — beside that denial is noise.

Matching, reminder lane: the shared token matcher
(_dispatch_common.is_push_command) — mirrors subagent-push-gate by
construction (same function). Quoted text mentioning push (commit
messages, paths) does not fire; `git stash push` (purely local) is
exempt.

Matching, deny lane: command-position regexes, deliberately NOT the
token matcher — the question here is composition (does a push share
this invocation with a read or a commit?), which needs the shell
operators the token view discards. `(?:^|[;&|]\\s*)git\\s+push\\b`
for the push, the same anchoring for the `git commit` / `git log`
companion, so a commit MESSAGE merely containing the word "push"
cannot fire it. HEREDOC BODIES ARE STRIPPED BEFORE MATCHING,
for an opener whose delimiter is ATTACHED to the operator: a
`<<WORD … WORD` span is text being WRITTEN, not command position.
The lane measurably false-fired on a commit message that quoted a
fused form while describing an earlier, correct fire — and a guard
firing on legitimate work fails as hard as one staying silent,
because it trains the override reflex. Residue that remains, and
is accepted: separator text inside a single-line quoted ARGUMENT
(`git commit -m "x; git push"`) still reads as command position; a
`<<` inside a quoted argument can be misread as an opener; and a
SPACED opener (`<< EOF`, POSIX-legal) is NOT recognised, so its body
is not stripped and the old false-firing behaviour stands there. The
space stays out of the opener pattern deliberately: admitting it lets
`$((a << b))` read as an opener and swallow the rest of the command,
weakening a deny gate to buy a narrower false-fire fix. Remedy cost
in every case is splitting the command, i.e. the very thing the deny
asks for.

Fail-open on parse errors (a broken guard must not brick every Bash
call); the --test bite-test is the compensation, auto-discovered by
the machine-bootstrap doctor's plugin-hooks sweep.
"""
from __future__ import annotations

import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from _dispatch_common import (deny, doc_ref, is_push_command,  # noqa: E402
                              is_subagent)

_SOURCE = "dispatch-guards/push-claim-reminder"

# Command position: string start, or right after a shell separator.
_CMD_POS = r"(?:^|[;&|]\s*)"
_FUSED_PUSH_RE = re.compile(_CMD_POS + r"git\s+push\b")
_FUSED_COMPANION_RE = re.compile(_CMD_POS + r"git\s+(?:commit|log)\b")

# Heredoc opener: `<<` (optionally `<<-`) then the delimiter word,
# bare or single/double quoted. No space is allowed between the
# operator and the word — `a << b` in an arithmetic expression must
# not read as an opener and swallow the rest of the command.
_HEREDOC_OPEN_RE = re.compile(
    r"<<-?(?:'([^']*)'|\"([^\"]*)\"|([A-Za-z_][A-Za-z0-9_]*))")


def strip_heredoc_bodies(cmd: str) -> str:
    """Return `cmd` with every heredoc BODY removed, opener lines kept.

    A `<<WORD … WORD` span is text being WRITTEN — a commit message,
    a file — not command position, and the deny lane measurably
    false-fired on one. The opener's own LINE stays: it is command
    position, and a real fusion (`git commit -F - <<'EOF' && git
    push`) lives there. The body runs from the end of the opener line
    to a line whose stripped content equals the delimiter (which
    subsumes `<<-`'s leading-tab stripping); an UNTERMINATED heredoc
    strips to the end of the string. Several heredocs are handled
    left to right. Accepted residue: a `<<` inside a quoted argument
    can be misread as an opener."""
    kept: list[str] = []
    rest = cmd
    while True:
        m = _HEREDOC_OPEN_RE.search(rest)
        if m is None:
            kept.append(rest)
            break
        delim = next(g for g in m.groups() if g is not None)
        nl = rest.find("\n", m.end())
        if nl == -1:
            kept.append(rest)  # opener with no body line after it
            break
        kept.append(rest[:nl + 1])
        lines = rest[nl + 1:].split("\n")
        rest = ""  # unterminated: the body runs to end of string
        for i, line in enumerate(lines):
            if line.strip() == delim:
                rest = "\n".join(lines[i + 1:])
                break
        if not rest:
            break
    return "".join(kept)


def is_fused_push(cmd: str) -> bool:
    """True iff `cmd` runs a `git push` in command position AND also a
    `git commit` or `git log` in command position — the claim check's
    read-then-decide seam collapsed into one invocation."""
    return bool(_FUSED_PUSH_RE.search(cmd)
                and _FUSED_COMPANION_RE.search(cmd))


def deny_reason() -> str:
    return (
        f"Fused push ({doc_ref('§1')}): the push is its own invocation. "
        "This command runs `git push` together with a `git commit` or "
        "`git log` — a fused command pre-commits the decision the log "
        "exists to inform, so the claim check degrades to nothing. Run "
        "the claim log (`git log origin/<branch>..<branch>`), READ it, "
        "then push in a separate command."
    )


def deny_check(payload: dict) -> str | None:
    """Deny lane: return a deny reason, or None (= fall through)."""
    if payload.get("tool_name") != "Bash":
        return None
    if is_subagent(payload):
        return None  # subagent-push-gate's lane
    cmd = (payload.get("tool_input") or {}).get("command", "") or ""
    if is_fused_push(strip_heredoc_bodies(cmd)):
        return deny_reason()
    return None


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
    reason = deny_check(payload)
    if reason:
        deny(reason, source=_SOURCE, payload=payload)  # prints exit-0 deny JSON and exits
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
        # regression: `git remote set-url --push` publishes nothing, so a
        # claim check is the wrong prompt for it (its real hazard —
        # rewriting shared config from a worktree — is
        # worktree-config-gate's). Red on the pre-exemption matcher.
        assert check({**main_s, "tool_input": {"command": "git remote set-url --push origin file:///dev/null/nowhere"}}) is None
        assert check({**main_s, "tool_input": {"command": "git remote set-url --push origin /dev/null && git push"}}) is not None

        # ── Fused-push deny lane (claim-check-degradation class) ────
        # Expectation derived from the rule, not from this hook: the
        # dispatch skill §1 claim check is a READ, then a decision to
        # push — a seam that exists only across separate invocations.
        # Each recorded instance of the class is a case below.
        # (i) the 2026-08-05 harmful variant: commit fused to push
        assert deny_check({**main_s, "tool_input": {"command": "git commit -m x && git push"}}) is not None
        # (ii) the chained-read variant: log fused to push (halt
        # structurally impossible — the push is already queued)
        assert deny_check({**main_s, "tool_input": {"command": "git log origin/main..main && git push"}}) is not None
        # (iii) other separators, and either order
        assert deny_check({**main_s, "tool_input": {"command": "git log origin/main..main ; git push"}}) is not None
        assert deny_check({**main_s, "tool_input": {"command": "git push && git commit -m x"}}) is not None
        assert deny_check({**main_s, "tool_input": {"command": "git add -A && git commit -m x && git push origin main"}}) is not None
        # (iv) solo push: no deny — the reminder lane keeps it
        assert deny_check({**main_s, "tool_input": {"command": "git push"}}) is None
        assert check({**main_s, "tool_input": {"command": "git push"}}) is not None
        assert deny_check({**main_s, "tool_input": {"command": "git push origin main"}}) is None
        assert check({**main_s, "tool_input": {"command": "git push origin main"}}) is not None
        # (v) a commit alone never denies, whatever its message says —
        # command-position anchoring is what buys this
        assert deny_check({**main_s, "tool_input": {"command": 'git commit -m "docs: push conventions"'}}) is None
        assert deny_check({**main_s, "tool_input": {"command": 'git commit -m "explain git push rules"'}}) is None
        assert deny_check({**main_s, "tool_input": {"command": "git log origin/main..main"}}) is None
        # (vi) non-git companions do not fuse: only commit/log do
        assert deny_check({**main_s, "tool_input": {"command": "make build && git push"}}) is None
        assert deny_check({**main_s, "tool_input": {"command": "git status && git push"}}) is None
        # (vii) subagent context: silent here (subagent-push-gate denies)
        assert deny_check({**sub, "tool_input": {"command": "git commit -m x && git push"}}) is None
        # (viii) documented accepted residue: command-position text
        # inside a quoted string still reads as a fusion
        assert deny_check({**main_s, "tool_input": {"command": 'git commit -m "x; git push"'}}) is not None
        # (ix) garbage/parse-error payloads never raise
        assert deny_check({**main_s, "tool_input": {}}) is None
        assert deny_check({"tool_name": "Read", "tool_input": {"command": "git commit -m x && git push"}}) is None
        assert deny_check({}) is None
        # (x) deny payload reaches BOTH audiences, source-tagged
        # (misattribution class 2026-07-30)
        from _dispatch_common import _deny_payload
        dp = _deny_payload(deny_reason(), source=_SOURCE)
        hso = dp["hookSpecificOutput"]
        assert hso["permissionDecision"] == "deny"
        assert hso["permissionDecisionReason"].startswith(
            "[dispatch-guards/push-claim-reminder] ")
        assert dp["systemMessage"] == hso["permissionDecisionReason"]
        assert "separate command" in deny_reason()
        # (xi) heredoc BODIES are text being written, not command
        # position. Measured false fire (2026-08-10): a commit message
        # quoting a fused form denied a command holding no push at all.
        _hd_false_fire = (
            "git commit -F - <<'EOF'\n"
            "guard note: the first fire was correct — I had run\n"
            "`git log origin/main..main && git push` in one command.\n"
            "EOF\n"
        )
        assert deny_check({**main_s, "tool_input": {"command": _hd_false_fire}}) is None
        # the in-scope case in the SAME dirty fixture: a real fusion on
        # the opener LINE still denies, heredoc body present
        _hd_real_fusion = (
            "git commit -F - <<'EOF' && git push origin main\n"
            "a commit message body\n"
            "EOF\n"
        )
        assert deny_check({**main_s, "tool_input": {"command": _hd_real_fusion}}) is not None
        # unterminated heredoc (no closing delimiter line): the body
        # runs to end of string, so the quoted fusion stays silent
        _hd_unterminated = (
            "git commit -F - <<'EOF'\n"
            "guard note: the first fire was correct — I had run\n"
            "`git log origin/main..main && git push` in one command.\n"
        )
        assert deny_check({**main_s, "tool_input": {"command": _hd_unterminated}}) is None

        # ── deny renderer: the chained-command note (BACKLOG
        # 2026-08-11 — a Bash deny does not say that NOTHING in the
        # command ran; the compound-command case bites). One render
        # site in _dispatch_common (_deny_payload) serves every Bash
        # gate, so the pair is exercised here — this file is swept by
        # the doctor sweep, where _dispatch_common.py's own --test is
        # not (excluded by basename). The pair is the point: a
        # sentence that always appears proves nothing about the scan.
        import contextlib
        import io
        from _dispatch_common import _CHAIN_NOTE, _deny_payload

        _chained_payload = {**main_s, "tool_input": {
            "command": "printf 'x' >> msg.txt && git commit -m x && git push"}}
        _dp_chained = _deny_payload("r", source=_SOURCE,
                                    payload=_chained_payload)
        assert _CHAIN_NOTE in _dp_chained["hookSpecificOutput"][
            "permissionDecisionReason"], _dp_chained
        assert _CHAIN_NOTE in _dp_chained["systemMessage"], _dp_chained

        _unchained_payload = {**main_s, "tool_input": {"command": "git push"}}
        _dp_unchained = _deny_payload("r", source=_SOURCE,
                                      payload=_unchained_payload)
        assert _CHAIN_NOTE not in _dp_unchained["hookSpecificOutput"][
            "permissionDecisionReason"], _dp_unchained
        assert _CHAIN_NOTE not in _dp_unchained["systemMessage"], _dp_unchained

        # done-criterion: the incident's own command shape, through the
        # real fused-push deny lane end to end (deny_check() -> deny()).
        _incident_cmd = ("printf '\\nTrailer\\n' >> msg.txt "
                         "&& git commit -F msg.txt && git push")
        _incident_payload = {**main_s, "tool_input": {"command": _incident_cmd}}
        _incident_reason = deny_check(_incident_payload)
        assert _incident_reason is not None, _incident_cmd
        _buf = io.StringIO()
        with contextlib.redirect_stdout(_buf):
            try:
                deny(_incident_reason, source=_SOURCE,
                     payload=_incident_payload)
            except SystemExit:
                pass
        _j = json.loads(_buf.getvalue())
        assert _CHAIN_NOTE in _j["hookSpecificOutput"][
            "permissionDecisionReason"], _j

        print("push-claim-reminder: all tests passed")
        sys.exit(0)
    sys.exit(main())
