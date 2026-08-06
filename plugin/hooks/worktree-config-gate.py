#!/usr/bin/env python3
"""PreToolUse(Bash): a shared-config write issued from inside a worktree.

A linked worktree shares the repository's config, refs, remotes and
stash; only its checkout, index, HEAD and `.git/worktrees/<name>/` are
private. So a config write run "in the worktree" lands in the shared
`.git/config`, where every checkout — including the main clone — sees
it. Two recorded instances of the class, both self-inflicted while
isolating an agent:

- `git remote remove` in an isolation worktree stripped the remote
  from the operator's main repo; main-tree push then failed with "No
  configured push destination".
- `git remote set-url --push <remote> <dev-null>`, reached for as the
  obvious way to deny push inside the worktree, wrote
  `remote.<name>.pushurl` to the shared config and redirected the MAIN
  clone's pushes to nowhere.

The trap is that `git remote` reads as local while having no
`--worktree` form at all (`git remote set-url --worktree` → "unknown
option"): every subcommand of it writes shared config. `git config`
has the form but does not default to it.

Lanes (one deny lane, shipped default-warn per this repo's new-lane
discipline — promotion to deny is earned against the fire log, never
asserted):

- SHARED-CONFIG WRITE FROM A WORKTREE. Fires when the command is a
  config-WRITE shape AND the repository it targets is a linked
  worktree. Reads never fire (`git config --get`, `git remote show`);
  neither does the correct form, `git config --worktree`, nor a write
  explicitly aimed elsewhere (`--global`, `--system`, `--file`).

Targeting: an explicit `git -C <path>` wins, else the hook payload's
`cwd`, else the hook process's cwd. Both fallback branches are
verified to fire and stay silent identically, so whether the harness
supplies a `cwd` field is NOT a load-bearing binding here — a hook
process inherits the session's directory either way. Worktree
detection is git's own
answer, not a path heuristic — `rev-parse --path-format=absolute
--git-dir --git-common-dir` returns two different paths in a linked
worktree and the same path in a main checkout. Ordering is deliberate:
the cheap token shape is tested first, so the subprocess runs only on
the handful of commands that already look like config writes.

Accepted residue, all of it UNDER-firing (this lane's false-negative
is the skill's prose, its false-positive would be an override reflex
trained on the fix itself): a `cd <elsewhere> && git config …` chain
is judged against the payload cwd, not the `cd` target; a wrapped
invocation (`sudo git …`, `env X=1 git …`) and an unspaced separator
(`foo;git config …`) both miss the command-position anchor; a write
inside quoted text does not fire at all. Fail-open on parse errors, on
git being absent, and on the subprocess timing out — a broken guard
must not brick every Bash call; the --test bite-test is the
compensation.
"""
from __future__ import annotations

import json
import os
import shlex
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from _dispatch_common import fire  # noqa: E402

_SOURCE = "dispatch-guards/worktree-config-gate"

# `git remote` subcommands that WRITE the shared config. Reads
# (show, get-url, prune, update) are absent by design.
_REMOTE_WRITES = frozenset({
    "add", "remove", "rm", "rename", "set-url", "set-head", "set-branches",
})

# `git config` flags that make it a write regardless of arg count.
_CONFIG_WRITE_FLAGS = frozenset({
    "--add", "--unset", "--unset-all", "--replace-all", "--edit", "-e",
    "--rename-section", "--remove-section",
})

# Flags that aim a `git config` write somewhere OTHER than the shared
# repo config — none of them are the hazard.
_CONFIG_ELSEWHERE = frozenset({
    "--worktree", "--global", "--system", "--file", "-f", "--blob",
})

# `git` GLOBAL options, which sit between `git` and its subcommand.
# Those taking a separate argument consume the next token too, so the
# subcommand scan does not mistake an option's VALUE for the verb.
_GIT_GLOBAL_WITH_ARG = frozenset({
    "-C", "-c", "--git-dir", "--work-tree", "--namespace", "--exec-path",
    "--config-env",
})


# Tokens after which the next word starts a new command. shlex keeps
# SPACED shell operators as tokens, which is all the sequencing this
# guard needs.
_SHELL_SEPARATORS = frozenset({"&&", "||", ";", "|", "&", "(", "{", "!"})


def _git_subcommands(tokens: list) -> list:
    """Every `git` INVOCATION's (subcommand, following-tokens) pair.

    Anchored twice, because each anchor alone leaks. Requiring a real
    `git` token keeps quoted prose out (shlex makes a commit message
    one token). Requiring that token to sit in COMMAND POSITION keeps
    unquoted prose out: `echo git remote remove origin` contains the
    `git` token and writes nothing — an argument, not a command.
    """
    out = []
    for i, t in enumerate(tokens):
        if t != "git":
            continue
        if i and not (tokens[i - 1] in _SHELL_SEPARATORS
                      or tokens[i - 1].endswith(";")):
            continue
        j = i + 1
        while j < len(tokens) and tokens[j].startswith("-"):
            j += 1 if tokens[j] not in _GIT_GLOBAL_WITH_ARG else 2
        if j < len(tokens):
            out.append((tokens[j], tokens[j + 1:]))
    return out


def _target_dir(tokens: list, payload: dict) -> str:
    """Directory the command operates on: explicit `-C <path>` wins."""
    for i, t in enumerate(tokens):
        if t == "-C" and i + 1 < len(tokens):
            return tokens[i + 1]
    return payload.get("cwd") or os.getcwd()


def is_shared_config_write(cmd: str) -> bool:
    """True iff `cmd` writes the repository-shared git config.

    Shape only — says nothing about worktrees; the caller pairs this
    with _is_linked_worktree so the subprocess stays off the hot path.
    """
    try:
        tokens = shlex.split(cmd)
    except ValueError:
        return False          # unparseable quoting: stay silent (warn lane)

    for subcmd, after in _git_subcommands(tokens):
        if subcmd == "remote":
            if after and after[0] in _REMOTE_WRITES:
                return True
        elif subcmd == "config":
            if any(t in _CONFIG_ELSEWHERE for t in after):
                continue
            if any(t in _CONFIG_WRITE_FLAGS for t in after):
                return True
            # `config <key> <value>` writes; `config <key>` alone reads.
            if len([t for t in after if not t.startswith("-")]) >= 2:
                return True
    return False


def _is_linked_worktree(path: str) -> bool:
    """True iff `path` sits in a LINKED worktree — git's own answer.
    False on every error (not a repo, git absent, timeout): fail-open."""
    try:
        r = subprocess.run(
            ["git", "-C", path, "rev-parse", "--path-format=absolute",
             "--git-dir", "--git-common-dir"],
            capture_output=True, text=True, timeout=5,
        )
    except (OSError, subprocess.SubprocessError):
        return False
    if r.returncode != 0:
        return False
    lines = r.stdout.split()
    return len(lines) == 2 and lines[0] != lines[1]


def reason() -> str:
    return (
        "Shared-config write from a worktree: a linked worktree shares "
        "the repository's config, refs and remotes — this command "
        "rewrites `.git/config`, so every checkout sees it, the main "
        "clone included. `git remote` has NO `--worktree` form; every "
        "subcommand of it writes shared config. For a setting that "
        "should differ per worktree: `git config extensions."
        "worktreeConfig true` once per repository, then `git -C "
        "<worktree> config --worktree <key> <value>`. For push denial "
        "specifically, poison per-worktree instead of touching the "
        "remote: `git config --worktree remote.<name>.pushurl "
        "file:///dev/null/nowhere`, for every remote the repo declares. "
        "If a `git remote` write already escaped, repair from the main "
        "checkout with `git config --unset-all remote.<name>.pushurl`."
    )


def check(payload: dict) -> str | None:
    """Return the fire reason, or None (= stay silent)."""
    if payload.get("tool_name") != "Bash":
        return None
    cmd = (payload.get("tool_input") or {}).get("command", "") or ""
    if not is_shared_config_write(cmd):
        return None
    try:
        tokens = shlex.split(cmd)
    except ValueError:
        return None
    if not _is_linked_worktree(_target_dir(tokens, payload)):
        return None
    return reason()


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0  # never fail the workflow on a hook parse error
    if check(payload):
        # New lane: ships warn, earns deny against the fire log.
        fire(reason(), source=_SOURCE, payload=payload, default_mode="warn")
    return 0


if __name__ == "__main__":
    if "--test" in sys.argv:
        import tempfile

        # ── Shape lane: is_shared_config_write, worktree-independent ──
        # Expectations derived from git's DEFINITION of which commands
        # write the repo config (git-config(1), git-remote(1)), not from
        # this implementation's behavior.
        W = is_shared_config_write
        # (i) the two recorded instances of the class
        assert W("git remote set-url --push origin file:///dev/null/nowhere")
        assert W("git remote remove origin")
        # (ii) every other config-writing `git remote` subcommand
        assert W("git remote add upstream https://example.invalid/r.git")
        assert W("git remote rm upstream")
        assert W("git remote rename origin upstream")
        assert W("git remote set-head origin main")
        assert W("git remote set-branches origin main")
        assert W("git -C /some/wt remote set-url --push origin /dev/null")
        # (iii) `git remote` READS never fire
        assert not W("git remote show origin")
        assert not W("git remote get-url --push origin")
        assert not W("git remote prune origin")
        assert not W("git remote update")
        assert not W("git remote -v")
        assert not W("git remote")
        # (iv) `git config` writes fire
        assert W("git config user.email t@t")
        assert W("git config --unset remote.origin.pushurl")
        assert W("git config --unset-all remote.origin.pushurl")
        assert W("git config --add remote.origin.fetch +refs/x:refs/y")
        assert W("git config --remove-section remote.origin")
        # (v) `git config` reads never fire
        assert not W("git config user.email")
        assert not W("git config --get remote.origin.url")
        assert not W("git config --get-regexp '^remote\\.'")
        assert not W("git config -l")
        assert not W("git config --list")
        # (vi) THE CORRECT FORM never fires — the whole point of the
        # guard is to route here, so firing on it would train the
        # override reflex on the very fix being taught
        assert not W("git config --worktree remote.origin.pushurl /dev/null")
        assert not W("git -C /wt config --worktree remote.origin.pushurl x")
        # (vii) writes aimed elsewhere than the shared repo config
        assert not W("git config --global user.email t@t")
        assert not W("git config --system core.editor vim")
        assert not W("git config --file /tmp/other user.email t@t")
        # (viii) prose ABOUT git, quoted and unquoted, never fires —
        # both anchors, each red before it was added
        assert not W('git commit -m "git remote remove origin"')  # shlex
        assert not W("echo git remote remove origin")   # command position
        assert not W("grep -r git config --unset .")    # ditto, real shape
        assert W("cd /x && git remote remove origin")   # separator: fires
        assert W("git status ; git config user.email t@t")
        # (ix) non-git and degenerate input
        assert not W("ls")
        assert not W("")
        assert not W("git")
        assert not W("git config --get x 'unterminated")  # unparseable

        # ── Worktree lane: _is_linked_worktree, against REAL git ──────
        # Modelling git's layout would re-introduce the class this
        # guard exists for; these run the real binary.
        with tempfile.TemporaryDirectory() as td:
            env = {**os.environ, "GIT_CONFIG_GLOBAL": os.path.join(td, "gc"),
                   "GIT_CONFIG_SYSTEM": os.path.join(td, "gs")}
            main_repo, wt = os.path.join(td, "m"), os.path.join(td, "w")

            def g(*a, cwd=td):
                return subprocess.run(["git", *a], cwd=cwd, env=env,
                                      capture_output=True, text=True)

            g("init", "-q", "m")
            g("-C", main_repo, "config", "user.email", "t@t")
            g("-C", main_repo, "config", "user.name", "t")
            g("-C", main_repo, "commit", "-q", "--allow-empty", "-m", "i")
            r = g("-C", main_repo, "worktree", "add", "-q", wt, "-b", "probe")
            assert r.returncode == 0, f"worktree add failed: {r.stderr}"

            assert _is_linked_worktree(wt), "linked worktree not detected"
            assert not _is_linked_worktree(main_repo), "main checkout flagged"
            assert not _is_linked_worktree(td), "non-repo flagged"
            assert not _is_linked_worktree(os.path.join(td, "nonexistent"))

            # ── End-to-end through check(), the shape the hook runs ──
            base = {"tool_name": "Bash"}
            poison = "git remote set-url --push origin file:///dev/null/nowhere"
            # fires in the worktree …
            assert check({**base, "cwd": wt,
                          "tool_input": {"command": poison}}) is not None
            # … and not in the main checkout, where it is legitimate
            assert check({**base, "cwd": main_repo,
                          "tool_input": {"command": poison}}) is None
            # -C targeting beats cwd, in both directions
            assert check({**base, "cwd": main_repo, "tool_input": {
                "command": f"git -C {wt} remote remove origin"}}) is not None
            assert check({**base, "cwd": wt, "tool_input": {
                "command": f"git -C {main_repo} remote remove origin"}}) is None
            # the correct recipe stays silent inside the worktree
            assert check({**base, "cwd": wt, "tool_input": {
                "command": "git config --worktree remote.origin.pushurl x"
            }}) is None
            # non-Bash, empty and garbage payloads never raise
            assert check({"tool_name": "Read", "cwd": wt,
                          "tool_input": {"command": poison}}) is None
            assert check({**base, "cwd": wt, "tool_input": {}}) is None
            assert check({}) is None

        # ── Instrument sanity: the message carries the FIX, not just
        # the diagnosis — a guard that only says "no" trains overrides.
        assert "--worktree" in reason()
        assert "pushurl" in reason()
        assert "--unset-all" in reason()

        print("worktree-config-gate: all tests passed")
        sys.exit(0)
    sys.exit(main())
