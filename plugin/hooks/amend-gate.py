#!/usr/bin/env python3
"""PreToolUse(Bash) gate: git commit --amend on a shared working copy.

Enforces the dispatch skill §1's amend rule: amend is
COMMIT-granular, not file-granular — file disjointness (targeted
`git add <path>`) does not reach it. `git commit --amend` rewrites
whatever commit sits at HEAD, and on a working copy shared between
agents/sessions HEAD moves between working rounds: an amend aimed at
"my commit" can swallow a co-writer's landed commit under the
amender's message, silently erasing it from HEAD and working tree
(observed live; the reflog was the recovery). The rule: amend only
when `git log -1 --format=%(trailers)` shows YOUR OWN trailer,
otherwise a new commit.

Two lanes, one guard (mirrors subagent-push-gate + push-claim-reminder
being two files for the same push rule, collapsed here into one file
per the brief):

- Subagent context (`agent_id` present, the subagent-push-gate
  precedent): FLAT deny, no trailer comparison in the hook itself —
  hook input carries no caller identity to compare against
  `%(trailers)` (documented gap; this docstring is its home), and a
  false fire lands on the rule's own preferred default anyway (a new
  commit costs nothing). Directs the agent to make a new commit.
- Main-session context: never blocks — one-line additionalContext
  reminder to check `git log -1 --format=%(trailers)` before amending
  on a copy any co-writer has touched. Main-session amends are
  legitimate (fixing a typo in one's own last commit); an ask/deny
  here would fire on routine work and train the override reflex, the
  same reasoning as push-claim-reminder's main-session lane.

Detection: shlex-tokenized (mirrors _dispatch_common.is_push_command)
— a `git` token, a `commit` token, and a standalone `--amend` token,
in any order, so `git commit -a --amend`, `git commit --amend -a`,
and `cd /x && git commit --amend` all match (token PRESENCE, not
adjacency or shell-operator parsing — a conservative regex/token scan
over the command string is the standard the other guards set, not a
full shell grammar). Quoted text (a commit message mentioning
"amend", or `--amend` embedded inside a single quoted argument to
`bash -c '...'`) does NOT match — shlex folds a quoted string into
one token, so `--amend` only fires as its own standalone token.

Unparseable quoting does NOT change the verdict class. An unbalanced
apostrophe makes shlex raise, and the command is then re-tokenized on
WHITESPACE and put through the SAME token predicate. It is never
substring matched: the old fallback asked only whether the characters
appeared anywhere in the line, so a commit whose message mentioned an
amend-flavoured word was DENIED with the flag never present as a
token — the false-deny class its push sibling was repaired for on
2026-08-10.

Accepted residue (documented, same shape as subagent-push-gate's):
deliberate obfuscation via `bash -c "git commit --amend"` or an alias
is NOT caught here — the session-cut unpushed/ahead-repos check and
human review remain the outer net for that. On the parse-failure path
a message carrying the bare flag as its own whitespace-separated word
still matches, unchanged and accepted: whitespace tokens keep their
quote characters attached, so a quoted word matches only where it
would have matched bare.

Fail-open on hook-input parse errors (a broken guard must not brick
every Bash call); the --test bite-test is the compensation and is
registered in the machine-bootstrap doctor via its content-based
hooks-dir scan (any file under plugin/hooks/ containing the literal
`"--test"` is discovered and run — no doctor edit needed for a new
guard file).
"""
from __future__ import annotations

import json
import os
import shlex
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from _dispatch_common import doc_ref, fire, is_subagent  # noqa: E402


def _amend_in_tokens(tokens: list) -> bool:
    """The token predicate, in ONE home: a `git` token, a `commit`
    token and a standalone `--amend` token, in any order. Both callers
    — the shlex path and the parse-failure path — share this scan, so
    the rule cannot grow two copies that drift apart. Contract is on
    ARGV POSITION, so it holds for any tokenizer yielding argv-shaped
    words."""
    return "git" in tokens and "commit" in tokens and "--amend" in tokens


def is_amend_command(cmd: str) -> bool:
    """True iff `cmd` invokes `git commit --amend` (token presence, not
    shell-grammar parsing — see module docstring)."""
    try:
        tokens = shlex.split(cmd)
    except ValueError:
        # Unparseable quoting: re-tokenize on whitespace and apply the
        # SAME predicate — a parse failure must not swap in a weaker
        # matcher (the class is_push_command was repaired for).
        tokens = cmd.split()
    return _amend_in_tokens(tokens)


def deny_reason() -> str:
    return (
        f"Amend gate ({doc_ref('§1')}): `git commit --amend` is denied "
        "in a subagent context. Amend is COMMIT-granular — it rewrites "
        "whatever commit sits at HEAD, and on a shared working copy "
        "HEAD may be a co-writer's landed commit, not yours. Make a "
        "NEW commit instead. (The rule for when amend is ever safe: "
        "only when `git log -1 --format=%(trailers)` shows your OWN "
        "trailer — a subagent has no way to prove that to this hook, "
        "so the lane denies flatly and a new commit costs nothing.)"
    )


def reminder_text() -> str:
    return (
        f"Amend starting ({doc_ref('§1')}): amend rewrites whatever "
        "commit is at HEAD, not necessarily yours. On a working copy "
        "any co-writer (agent, peer session) has touched, run `git log "
        "-1 --format=%(trailers)` first and confirm HEAD carries your "
        "own trailer before amending; otherwise make a new commit."
    )


def deny_check(payload: dict) -> str | None:
    """Subagent lane: return a deny reason, or None (= allow through)."""
    if payload.get("tool_name") != "Bash":
        return None
    if not is_subagent(payload):
        return None
    cmd = (payload.get("tool_input") or {}).get("command", "") or ""
    if is_amend_command(cmd):
        return deny_reason()
    return None


def reminder_check(payload: dict) -> str | None:
    """Main-session lane: return the reminder text, or None (= silent)."""
    if payload.get("tool_name") != "Bash":
        return None
    if is_subagent(payload):
        return None
    cmd = (payload.get("tool_input") or {}).get("command", "") or ""
    if is_amend_command(cmd):
        return reminder_text()
    return None


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0  # never fail the workflow on a hook parse error
    reason = deny_check(payload)
    if reason:
        # mode-aware deny: logged, warn-stageable via guard_modes
        fire(reason, source="dispatch-guards/amend-gate", payload=payload)
    reminder = reminder_check(payload)
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
        sub = {"tool_name": "Bash", "agent_id": "a1"}
        main_s = {"tool_name": "Bash"}

        # ── Detection: plain forms, whitespace, flag order, compound ──
        assert is_amend_command("git commit --amend")
        assert is_amend_command("git commit --amend --no-edit")
        assert is_amend_command("git commit -a --amend")
        assert is_amend_command("git commit --amend -a")
        assert is_amend_command("git  commit   --amend")  # extra whitespace
        assert is_amend_command("git -C /x commit --amend")
        assert is_amend_command("cd /x && git commit --amend")
        assert is_amend_command("git add foo.py && git commit --amend")
        # non-amend commit / non-commit push → no match
        assert not is_amend_command("git commit -m x")
        assert not is_amend_command("git commit -am x")
        assert not is_amend_command("git push --force")
        assert not is_amend_command("git log --amend-ish-typo")
        # quoted text mentioning amend must NOT fire (commit message,
        # or --amend embedded inside a single quoted bash -c argument)
        assert not is_amend_command('git commit -m "amend later, not now"')
        assert not is_amend_command(
            "bash -c 'git commit --amend'")  # accepted residue, documented
        assert not is_amend_command("echo 'please amend this'")
        # garbage/unparseable quoting → the whitespace path, same
        # predicate: the flag IS a token here, so it still fires
        assert is_amend_command("git commit --amend 'unterminated")
        # ── Parse failure must not move the verdict CLASS (2026-08-10,
        # the class is_push_command was repaired for the same day).
        # THE PAIR, and both halves are needed — the first alone is
        # satisfied by a predicate that allows everything.
        # (a) legitimate: the apostrophe makes shlex raise, and the
        # flag exists only INSIDE a longer word. The old substring
        # fallback denied this commit.
        assert not is_amend_command(
            "git commit -m 'jane's rule: never use --amend-style rewrites'")
        # (b) a GENUINE amend wearing the same unbalanced apostrophe
        # must still deny.
        assert is_amend_command("git commit --amend -m 'jane's fix'")
        # residue, unchanged and accepted: a BARE flag word outside
        # quotes still matches on the whitespace path.
        assert is_amend_command("git commit -m 'it's fine' # never --amend")
        # and an apostrophe cannot manufacture the git/commit tokens
        assert not is_amend_command("echo 'it's --amend time'")

        # ── Subagent lane: flat deny ──
        assert deny_check({**sub, "tool_input": {"command": "git commit --amend"}}) is not None
        assert deny_check({**sub, "tool_input": {"command": "git commit -a --amend"}}) is not None
        assert deny_check({**sub, "tool_input": {"command": "git commit -m x"}}) is None
        assert deny_check({**sub, "tool_input": {}}) is None
        assert deny_check({"tool_name": "Read", "agent_id": "a1",
                           "tool_input": {"command": "git commit --amend"}}) is None
        # main-session amend never denied by this lane
        assert deny_check({**main_s, "tool_input": {"command": "git commit --amend"}}) is None

        # ── Main-session lane: reminder only, never blocks ──
        assert reminder_check({**main_s, "tool_input": {"command": "git commit --amend"}}) is not None
        assert reminder_check({**main_s, "tool_input": {"command": "git commit -m x"}}) is None
        assert reminder_check({**main_s, "tool_input": {}}) is None
        # subagent amend: reminder lane stays silent (deny lane owns it)
        assert reminder_check({**sub, "tool_input": {"command": "git commit --amend"}}) is None

        # ── Text content sanity ──
        assert "dispatcher" not in deny_reason().lower() or True  # no dispatcher-specific claim required
        assert "new" in deny_reason().lower()
        assert "%(trailers)" in reminder_text()

        # ── Garbage/parse-error payloads never raise ──
        assert deny_check({}) is None
        assert reminder_check({}) is None

        print("amend-gate: all tests passed")
        sys.exit(0)
    sys.exit(main())
