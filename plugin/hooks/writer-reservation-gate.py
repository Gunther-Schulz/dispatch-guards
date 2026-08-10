#!/usr/bin/env python3
"""PreToolUse(Bash) + PostToolUse(Write|Edit) + Stop/SubagentStop:
the writer-reservation lock — a WARN at `git commit` when ANOTHER writer
holds the target WORKING COPY's reservation.

Design authority: dotfiles `docs/directives/writer-reservation-lock-
spec.md` (settled 2026-08-06); granularity fixed by the dotfiles
BACKLOG's `READY 2026-08-06 — guard-lifecycle adoption` entry.

The failure it answers (observed 2026-08-06): a session held
uncommitted hunks in two files; a peer session committed its own edit
to the same two files with a clean targeted `git add`, and the peer's
commit ABSORBED the first session's hunks, which travelled to origin
under a message describing only the peer's change. Nothing was lost
and nothing warned. Two facts the incident settles:

- Edit discipline cannot prevent it. Both sessions used targeted `git
  add` on files they legitimately owned; staging is file-granular and
  takes the whole working-tree state of the named file.
- An open-time live-writer check cannot see it. Both repos were clean
  at open; the co-writer arrived mid-session. A check that runs once
  at the start is blind to every arrival after it.

GRANULARITY: the working copy, and only the working copy. Path
granularity over-fires — the general case is two sessions writing
DISJOINT files in one copy, where a path-granular lock fires on every
honest parallel pair and trains the override reflex that kills the
guard. The commit is what serializes, so the commit is what the lock
guards; a disjoint path set is no defence against absorption.

NOT a duplicate of writer-claims-gate, and deliberately not
harmonized with it. That gate is per-FILE at write time and records
claims for SUBAGENT writes only (`record_claim`, "main-session claims
would turn that into noise") — so on the motivating incident, two
MAIN sessions, no claim would ever have existed to fire on. This lane
is per-COPY at commit time and claims for the main session too. They
are complementary: same ancestor idea, disjoint firing conditions.

## The three events

- PostToolUse(Write|Edit): CLAIM the copy containing the written
  file. Claiming is automatic by design — an explicit claim step
  would be a prose instruction the consumer eventually skips,
  silently, on the success path. Recorded post-write, so a denied or
  failed call claims nothing.
- PreToolUse(Bash): a `git commit` against a copy whose reservation
  is held by a DIFFERENT writer and has not expired → WARN naming the
  holder, when it claimed, and what the commit will absorb.
- Stop / SubagentStop: RELEASE this writer's reservation on the
  session's cwd copy — but only on GIT EVIDENCE that the copy has
  nothing left to protect. See below.

## Release is gated on git evidence, not on the stop event

The release condition is not "stopped", it is "stopped AND has
nothing to protect" (operator decision 2026-08-10). Ask what the WARN
asserts: another writer holds this copy, and your commit may absorb
their uncommitted hunks. If a writer stops having LEFT uncommitted
work, that sentence is still true and the warning still earns its
place — releasing there would drop protection at exactly the moment
the work is most orphaned, with nobody actively minding it. If it
stops CLEAN, the sentence is false, and every later commit in that
copy eats a false fire for up to 90 minutes; on a fan-out that is
constant, and a guard that fires on legitimate work trains the
override reflex that kills it.

So: clean copy → release. Dirty copy → keep, and let the TTL end it.
Could not establish which → keep. Release takes POSITIVE evidence,
the same direction writer-claims-gate's relief takes.

This is load-bearing rather than a noise tweak, because `Stop` is not
a session-end event: it fires at the end of each main-agent response
(basis: the operator's own Stop wiring runs `claude-worktime log
--response` and a mid-turn answer check, dotfiles
`claude/settings.json`). An ungated release would therefore drop the
reservation after every turn, leaving the lock alive only within a
single response.

The predicate is `_dispatch_common.git_status_lines`, SHARED rather
than copied — writer-claims-gate's `no_uncommitted_work` answers the
per-PATH question and cannot answer this per-COPY one as written: it
runs `git -C dirname(path)`, so handed a copy's toplevel it shells
into the repo's PARENT and git exits 128 (measured 2026-08-10 — it
returns False there, the right answer for the wrong reason). The two
questions also differ on ignored files, deliberately; the flag split
and its measurement live in that helper's docstring.

## The record

`<git-dir>/writer-reservation.json`, one JSON object:
`{session_id, agent_id, claimed_at, ttl_seconds}` — `agent_id` null
in a main session, `claimed_at` epoch seconds. Inside the git dir
deliberately: never committed, never shared by a worktree's parent
(git's own `rev-parse --git-dir` answers per-worktree, so a linked
worktree reserves separately from the main checkout), and removed
with the repo. Written atomically (temp + `os.replace`), because two
sessions can claim the same copy concurrently.

TTL is a BINDING, stamped here: 90 minutes (spec 2026-08-06), so an
abandoned session cannot wedge a repo. Readers honour the TTL the
WRITER stamped into the record, not this constant — that is what the
field is for.

CONTENTION: the FIRST write-shaped call claims; a live foreign
reservation is never stolen, only refreshed by its own holder (which
keeps `claimed_at` honest for a session that is actively writing) and
never removed by anyone else. A record that cannot be read as a
holder at all (malformed, or unreadable) is overwritten rather than
respected: a single unparseable object would otherwise make the lock
permanently dead, and a malformed record names nobody to protect.

MODE: ships WARN and stays there until its fire rate is measured
(this repo's new-lane discipline). A deny would block the legitimate
case where the holder has nothing uncommitted — which this lane
cannot see from the reservation alone, by construction.

COULD-NOT-VERIFY, as ONE rule: any condition under which the lane
cannot establish BOTH the working copy and the current holder is
silent and fail-open — never a pass, never a fire. Its shapes: the
command's quoting does not parse; the invocation relocates the copy
(`--git-dir`/`--work-tree`); the target directory is not inside a git
working copy; the reservation is unreadable; the reservation is
malformed; the payload carries no `session_id`, so the committing
writer cannot be identified. `verdict()` returns the reason for each,
so they stay distinguishable to a reader and to the bite-test. The
extraction standard in `_dispatch_common`'s docstring binds here by
name: extraction failure maps to could-not-verify, never to a pass.

Accepted residue, all of it UNDER-firing:

- One holder per copy. A commit BY the holder stays silent even when
  a non-holder also has uncommitted work there — a single-object
  record cannot express two writers, and the spec fixes the record.
- `cd <elsewhere> && git commit` is judged against the payload cwd,
  not the `cd` target; a wrapped invocation (`sudo git …`, `bash -c
  '…'`) and an unspaced separator (`foo;git commit`) miss the
  command-position anchor. Same residue as worktree-config-gate.
- Only `git commit` is a lane. Other absorbing shapes (`git merge`,
  `git revert`, `git stash push`) are out of the spec's scope.
- Release covers the copy at the session's cwd; a reservation taken
  in some OTHER copy expires by TTL. A holder that stops dirty and
  never returns also runs to TTL — deliberate, per the gate above.
- Bash-mediated writes (`sed -i`, `tee`, heredocs) never reach the
  Write|Edit matcher, so they claim nothing.

FALSE-FIRE PROBE, with its measured reach (2026-08-10): this text run
through the lane as a Bash command does not fire. Taken alone that
result is worth little, because whether the text REACHES the
predicate at all depends on the parity of the apostrophes in it —
odd, and shlex bails into the fail-open exit before any matching
happens (measured both ways while editing this very paragraph). So
the probe with reach strips `'`, `"` and backticks first. Stripped,
exactly ONE paragraph matches: the residue list above, which
literally contains `cd <elsewhere> && git commit`. That match is a
CORRECT shell reading — a real command in command position — so it is
documentation read as a command, not a predicate defect, and the same
residue is shared with every guard here that reads shell syntax. The
bite-test pins that one match by identity, so a second one goes red.

Fail-open everywhere (a broken lock must never brick a call);
`--test` bite-test registered via the doctor's content scan.
"""
from __future__ import annotations

import json
import os
import shlex
import subprocess
import sys
import time
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from _dispatch_common import fire, git_status_lines  # noqa: E402

_SOURCE = "dispatch-guards/writer-reservation-gate"
_RESERVATION = "writer-reservation.json"
_WRITE_TOOLS = ("Write", "Edit")
_GIT_TIMEOUT = 5.0

# Binding, stamped: 90 minutes (spec 2026-08-06). Stamped into every
# record this lane writes; readers use the record's own value.
_TTL_SECONDS = 90 * 60

# `git` GLOBAL options sitting between `git` and its subcommand. Those
# taking a separate argument consume the next token too, so the
# subcommand scan never mistakes an option's VALUE for the verb.
_GIT_GLOBAL_WITH_ARG = frozenset({
    "-C", "-c", "--git-dir", "--work-tree", "--namespace", "--exec-path",
    "--config-env", "--super-prefix",
})

# Globals that RELOCATE the working copy: with either of them the copy
# a commit targets cannot be read off `-C`/cwd → could-not-verify.
_OPAQUE_GLOBALS = frozenset({"--git-dir", "--work-tree"})

# Tokens after which the next word starts a new command. shlex keeps
# SPACED shell operators as tokens, which is all the sequencing needed.
_SHELL_SEPARATORS = frozenset({"&&", "||", ";", "|", "&", "(", "{", "!"})


# ── Command reading ──────────────────────────────────────────────────

def _git_invocations(tokens: list) -> list:
    """(subcommand, -C value, relocates-the-copy) per `git` INVOCATION.

    Anchored twice, because each anchor alone leaks. A real `git` token
    keeps quoted prose out (shlex folds a commit message into one
    token). COMMAND POSITION keeps unquoted prose out: `echo git commit
    -m x` carries the token and commits nothing.
    """
    out = []
    for i, t in enumerate(tokens):
        if t != "git":
            continue
        if i and not (tokens[i - 1] in _SHELL_SEPARATORS
                      or tokens[i - 1].endswith(";")):
            continue
        cdir, opaque, j = None, False, i + 1
        while j < len(tokens) and tokens[j].startswith("-"):
            tok = tokens[j]
            if tok.split("=", 1)[0] in _OPAQUE_GLOBALS:
                opaque = True
            if tok in _GIT_GLOBAL_WITH_ARG:
                if tok == "-C" and j + 1 < len(tokens):
                    cdir = tokens[j + 1]
                j += 2
            else:
                j += 1
        out.append((tokens[j] if j < len(tokens) else None, cdir, opaque))
    return out


def _base_dir(payload: dict) -> str:
    """The directory the command runs in: the payload's cwd, else the
    hook process's — which inherits the session's directory anyway."""
    return payload.get("cwd") or os.getcwd()


def commit_targets(cmd: str, payload: dict) -> tuple:
    """(kind, why, dirs) — kind in {"targets", "none", "unverifiable"}.

    "none": the command commits nothing. "unverifiable": it does, but
    which copy cannot be established (the could-not-verify rule).
    """
    try:
        tokens = shlex.split(cmd)
    except ValueError:
        return ("unverifiable", "the command's quoting does not parse", [])
    base, dirs = _base_dir(payload), []
    for sub, cdir, opaque in _git_invocations(tokens):
        if sub != "commit":
            continue
        if opaque:
            return ("unverifiable",
                    "`--git-dir`/`--work-tree` relocates the working copy", [])
        if not cdir:
            dirs.append(base)
        elif os.path.isabs(cdir):
            dirs.append(cdir)
        else:
            dirs.append(os.path.join(base, cdir))
    return ("targets" if dirs else "none", "", dirs)


def git_dir(directory: str) -> str | None:
    """Git's own answer for the copy at `directory` — absolute, and
    PER-WORKTREE, which is what keeps a linked worktree's reservation
    out of its parent's. None on every error: fail-open.

    `--no-optional-locks` per the standing guard rule: this runs
    against a working copy whose index is shared with the very
    co-writers the lane exists for."""
    try:
        r = subprocess.run(
            ["git", "-C", directory, "--no-optional-locks", "rev-parse",
             "--path-format=absolute", "--git-dir"],
            capture_output=True, text=True, timeout=_GIT_TIMEOUT)
    except (OSError, ValueError, subprocess.SubprocessError):
        return None
    return r.stdout.strip() or None if r.returncode == 0 else None


# ── The record ───────────────────────────────────────────────────────

def reservation_path(gitdir: str) -> str:
    return os.path.join(gitdir, _RESERVATION)


def identity(payload: dict) -> tuple:
    """(session_id, agent_id) — the writer this payload comes from."""
    sid = payload.get("session_id")
    aid = payload.get("agent_id")
    return (sid if isinstance(sid, str) and sid else None,
            aid if isinstance(aid, str) and aid else None)


def read_reservation(gitdir: str, now: float | None = None) -> tuple:
    """(state, record, detail) — state in {"free", "held", "expired",
    "unverifiable"}.

    An ABSENT record is "free", not could-not-verify: it establishes
    the holder (there is none). Only an unreadable or malformed record
    is unverifiable — the lane cannot tell whose it is, so it neither
    passes nor fires.
    """
    path = reservation_path(gitdir)
    try:
        with open(path, encoding="utf-8") as f:
            raw = f.read()
    except FileNotFoundError:
        return ("free", None, "no reservation on this copy")
    except OSError as exc:
        return ("unverifiable", None, f"reservation unreadable: {exc}")
    try:
        rec = json.loads(raw)
    except (json.JSONDecodeError, ValueError) as exc:
        return ("unverifiable", None, f"reservation is not JSON: {exc}")
    if not isinstance(rec, dict):
        return ("unverifiable", None, "reservation is not a JSON object")
    sid, aid = rec.get("session_id"), rec.get("agent_id")
    at, ttl = rec.get("claimed_at"), rec.get("ttl_seconds")
    if not isinstance(sid, str) or not sid:
        return ("unverifiable", None, "reservation names no session_id")
    if aid is not None and not isinstance(aid, str):
        return ("unverifiable", None, "reservation's agent_id is not a string")
    if not isinstance(at, (int, float)) or isinstance(at, bool):
        return ("unverifiable", None, "reservation's claimed_at is not a number")
    if not isinstance(ttl, (int, float)) or isinstance(ttl, bool) or ttl <= 0:
        return ("unverifiable", None,
                "reservation's ttl_seconds is not a positive number")
    now = time.time() if now is None else now
    if now - at > ttl:
        return ("expired", rec, "the reservation expired")
    return ("held", rec, "")


def holder(rec: dict) -> tuple:
    aid = rec.get("agent_id")
    return (rec.get("session_id"), aid if isinstance(aid, str) and aid else None)


def write_reservation(gitdir: str, payload: dict,
                      now: float | None = None) -> str:
    """Claim or refresh. Returns the outcome, for the bite-test:
    "claimed" | "refreshed" | "foreign" (a live holder, left alone) |
    "unidentified" | "failed".

    Atomic: a temp file in the same directory plus `os.replace`, since
    two sessions can claim one copy concurrently.
    """
    sid, aid = identity(payload)
    if not sid:
        return "unidentified"
    state, rec, _ = read_reservation(gitdir, now=now)
    if state == "held":
        if holder(rec) != (sid, aid):
            return "foreign"          # never steal a live reservation
        outcome = "refreshed"
    else:
        outcome = "claimed"           # free, expired, or unreadable-as-holder
    path = reservation_path(gitdir)
    tmp = path + f".{os.getpid()}.tmp"
    try:
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump({"session_id": sid, "agent_id": aid,
                       "claimed_at": time.time() if now is None else now,
                       "ttl_seconds": _TTL_SECONDS}, f)
        os.replace(tmp, path)
    except OSError:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        return "failed"               # fail-open: a lock must not brick a write
    return outcome


def release_reservation(gitdir: str, payload: dict, worktree: str,
                        now: float | None = None) -> str:
    """Drop the reservation IFF this writer holds it AND the copy has
    nothing left to protect. Returns "released" | "kept-dirty" |
    "kept-unverified" | "not-held" | "foreign" | "failed".

    The gate is the point (see the module docstring): stopping is not
    the release condition, stopping with nothing uncommitted is.
    Release takes POSITIVE evidence of a clean copy, so a status
    question that could not be answered keeps the reservation.
    """
    sid, aid = identity(payload)
    if not sid:
        return "not-held"
    state, rec, _ = read_reservation(gitdir, now=now)
    if state in ("free", "unverifiable"):
        return "not-held"
    if holder(rec) != (sid, aid):
        return "foreign"              # never remove another writer's record
    # include_ignored=False: `git commit` never stages an ignored file,
    # so an ignored artifact is unabsorbable and must not block release.
    lines = git_status_lines(worktree, include_ignored=False)
    if lines is None:
        return "kept-unverified"      # could not answer → do not act
    if lines:
        return "kept-dirty"           # still work to protect → TTL ends it
    try:
        os.unlink(reservation_path(gitdir))
    except OSError:
        return "failed"
    return "released"


# ── The lane ─────────────────────────────────────────────────────────

def _stamp(ts: float) -> str:
    return datetime.fromtimestamp(ts, timezone.utc).isoformat(
        timespec="seconds")


def reason(rec: dict, directory: str, now: float | None = None) -> str:
    now = time.time() if now is None else now
    sid, aid = holder(rec)
    who = f"session {sid}" + (f", agent {aid}" if aid else " (main session)")
    age = max(0, int((now - rec["claimed_at"]) // 60))
    return (
        f"Writer-reservation lock: another writer holds this working copy "
        f"({directory}). Holder: {who}, claimed {_stamp(rec['claimed_at'])} "
        f"({age} min ago; TTL {int(rec['ttl_seconds'] // 60)} min). "
        "`git commit` takes the whole WORKING-TREE state of every path it "
        "names, so this commit can absorb that holder's uncommitted hunks "
        "and carry them to origin under YOUR message — observed 2026-08-06, "
        "both sessions using clean targeted `git add` on files they "
        "legitimately owned. A disjoint path set is no defence: the commit "
        "is what serializes, which is why this lock is per working copy and "
        "not per path. Before committing: read `git -C "
        f"{directory} --no-optional-locks status --porcelain` and check "
        "whether anything there is not yours; then either wait for the "
        "holder's commit or closing report, or commit by explicit pathspec "
        "once you have confirmed those paths carry only your hunks. WARN "
        "only — this lane cannot see whether the holder actually has "
        "uncommitted work, so it never blocks.")


def verdict(payload: dict, now: float | None = None) -> tuple:
    """(outcome, detail) — outcome in {"fire", "silent", "cannot-verify"}.

    The detail is the lane's REASON for its answer, so every
    could-not-verify shape stays distinguishable to a reader and to the
    bite-test rather than collapsing into one indistinguishable silence.
    """
    if payload.get("tool_name") != "Bash":
        return ("silent", "not a Bash call")
    cmd = (payload.get("tool_input") or {}).get("command", "") or ""
    kind, why, dirs = commit_targets(cmd, payload)
    if kind == "unverifiable":
        return ("cannot-verify", f"target copy not extractable: {why}")
    if kind == "none":
        return ("silent", "no `git commit` invocation in command position")
    me = identity(payload)
    if not me[0]:
        return ("cannot-verify", "the payload carries no session_id: the "
                                 "committing writer cannot be identified")
    last = ("silent", "no reservation on the target copy")
    for directory in dirs:
        gd = git_dir(directory)
        if gd is None:
            return ("cannot-verify",
                    f"`{directory}` is not inside a readable git working copy")
        state, rec, detail = read_reservation(gd, now=now)
        if state == "unverifiable":
            return ("cannot-verify", f"reservation unusable: {detail}")
        if state in ("free", "expired"):
            last = ("silent", detail)
            continue
        if holder(rec) == me:
            last = ("silent", "the reservation is this writer's own")
            continue
        return ("fire", reason(rec, directory, now=now))
    return last


def check(payload: dict, now: float | None = None) -> str | None:
    """The fire reason, or None (= stay silent)."""
    outcome, detail = verdict(payload, now=now)
    return detail if outcome == "fire" else None


def on_write(payload: dict) -> str:
    """PostToolUse(Write|Edit): claim the copy holding the written file."""
    if payload.get("tool_name") not in _WRITE_TOOLS:
        return "not-a-write"
    fp = (payload.get("tool_input") or {}).get("file_path")
    if not isinstance(fp, str) or not fp:
        return "no-path"
    gd = git_dir(os.path.dirname(fp) or ".")
    if gd is None:
        return "no-git-dir"
    return write_reservation(gd, payload)


def on_stop(payload: dict) -> str:
    """Stop/SubagentStop: release this writer's reservation on the
    session's copy, gated on the copy being clean."""
    worktree = _base_dir(payload)
    gd = git_dir(worktree)
    if gd is None:
        return "no-git-dir"
    return release_reservation(gd, payload, worktree)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0  # never fail the workflow on a hook parse error
    event = payload.get("hook_event_name")
    if event == "PostToolUse":
        on_write(payload)
        return 0
    if event in ("Stop", "SubagentStop"):
        # Both, and for the same reason: a stopping SUBAGENT is a
        # different writer from its parent session (the record carries
        # agent_id), so its reservation is its own to release.
        on_stop(payload)
        return 0
    if check(payload):
        # New lane: ships warn, earns deny against the fire log.
        fire(check(payload), source=_SOURCE, payload=payload,
             default_mode="warn")
    return 0


if __name__ == "__main__":
    if "--test" in sys.argv:
        import contextlib
        import io
        import tempfile
        from _dispatch_common import _reset_policy_cache

        os.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = "/nonexistent"
        _reset_policy_cache()

        # ── Command reading, working-copy independent ──────────────────
        # Expectations derived from what the SPEC guards (a `git commit`
        # against a copy), not from this implementation's behaviour.
        def T(cmd, cwd="/base"):
            return commit_targets(cmd, {"cwd": cwd})

        assert T("git commit -m x") == ("targets", "", ["/base"])
        assert T("git commit --amend") == ("targets", "", ["/base"])
        assert T("git -C /other commit -m x") == ("targets", "", ["/other"])
        assert T("git -C sub commit -m x") == ("targets", "", ["/base/sub"])
        assert T("git -c user.email=t@t commit -m x") == \
            ("targets", "", ["/base"])
        assert T("git add -- f && git commit -m x")[2] == ["/base"]
        assert T("git status ; git commit -m x")[2] == ["/base"]
        # not a commit / not a command-position git → nothing to check
        assert T("git status")[0] == "none"
        assert T("git log --grep commit")[0] == "none"
        assert T("echo git commit -m x")[0] == "none"
        assert T('git log -m "git commit -m x"')[0] == "none"
        assert T("ls")[0] == "none" and T("")[0] == "none"
        assert T("git")[0] == "none"
        # could-not-verify shapes of the extraction itself
        assert T("git commit -m 'unterminated")[0] == "unverifiable"
        assert T("git --git-dir=/g commit -m x")[0] == "unverifiable"
        assert T("git --work-tree /w --git-dir /g commit -m x")[0] == \
            "unverifiable"

        with tempfile.TemporaryDirectory() as td:
            os.environ["CLAUDE_DISPATCH_GUARDS_FIRELOG"] = td + "/f.jsonl"
            env = {**os.environ, "GIT_CONFIG_GLOBAL": td + "/gc",
                   "GIT_CONFIG_SYSTEM": td + "/gs"}
            copy = os.path.realpath(td) + "/copy"
            os.makedirs(copy)

            def g(*a, cwd=copy):
                # hooksPath pinned: a fixture repo otherwise inherits the
                # machine's GLOBAL core.hooksPath and runs the operator's
                # real hook battery inside the tempdir.
                return subprocess.run(
                    ["git", "-C", cwd, "-c", "user.email=t@t",
                     "-c", "user.name=t", "-c", "core.hooksPath=/nonexistent",
                     *a], env=env, capture_output=True, text=True)

            g("init", "-q", ".")
            # a fresh `git init` installs only `.sample` hooks, but the
            # chain-back path is real: assert nothing executable is there.
            assert not [f for f in os.listdir(copy + "/.git/hooks")
                        if not f.endswith(".sample")]
            tracked = copy + "/f.py"
            open(tracked, "w").write("x = 1\n")
            g("add", "--", tracked)
            assert g("commit", "-q", "--no-verify", "-m", "base").returncode == 0

            gd = git_dir(copy)
            assert gd == os.path.realpath(copy) + "/.git", gd
            assert git_dir(td) is None          # not a repo → fail-open
            assert git_dir(td + "/ghost") is None

            MINE = {"hook_event_name": "PreToolUse", "tool_name": "Bash",
                    "session_id": "s-mine", "cwd": copy,
                    "tool_input": {"command": 'git commit -m "my change"'}}

            # ── BASELINE FIRST: the unmutated case, real payload, real
            # repo, NOTHING reserved. A red-first proof over an
            # already-red baseline proves nothing.
            assert not os.path.exists(reservation_path(gd))
            base_outcome, base_detail = verdict(MINE)
            assert base_outcome == "silent", (base_outcome, base_detail)
            assert check(MINE) is None

            # DIRTY the copy — the holder's in-flight hunk. Every arm
            # below runs in THIS state, so a silence can never be the
            # trivial silence of a clean fixture.
            open(tracked, "w").write("x = 2\n")
            assert g("status", "--porcelain").stdout.strip() == "M f.py", \
                g("status", "--porcelain").stdout

            # ── RED: a foreign holder → fire, in the dirty state ───────
            now = time.time()
            json.dump({"session_id": "s-foreign", "agent_id": None,
                       "claimed_at": now - 300, "ttl_seconds": _TTL_SECONDS},
                      open(reservation_path(gd), "w"))
            outcome, text = verdict(MINE, now=now)
            assert outcome == "fire", (outcome, text)
            assert "s-foreign" in text and "absorb" in text
            # the message carries the FIX, not only the diagnosis — a
            # guard that only says "no" trains overrides
            assert "status --porcelain" in text and "pathspec" in text
            assert "per working copy" in text

            # ── The two silences, IN THE SAME DIRTY STATE ──────────────
            # (i) expired reservation
            assert verdict(MINE, now=now + _TTL_SECONDS + 60)[0] == "silent"
            assert check(MINE, now=now + _TTL_SECONDS + 60) is None
            # (ii) the reservation is MINE
            json.dump({"session_id": "s-mine", "agent_id": None,
                       "claimed_at": now - 300, "ttl_seconds": _TTL_SECONDS},
                      open(reservation_path(gd), "w"))
            assert verdict(MINE, now=now)[1] == "the reservation is this "\
                "writer's own"
            assert check(MINE, now=now) is None
            # …and the copy is still dirty, so neither silence was free
            assert g("status", "--porcelain").stdout.strip() == "M f.py"

            # a subagent of the same session is a DIFFERENT writer: its
            # uncommitted work is exactly what the §4 mirror duty names
            assert verdict({**MINE, "agent_id": "a1"}, now=now)[0] == "fire"
            # …and that subagent's own commit of its own claim is silent
            json.dump({"session_id": "s-mine", "agent_id": "a1",
                       "claimed_at": now - 60, "ttl_seconds": _TTL_SECONDS},
                      open(reservation_path(gd), "w"))
            assert verdict({**MINE, "agent_id": "a1"}, now=now)[0] == "silent"
            assert verdict(MINE, now=now)[0] == "fire"   # …parent's is not

            # ── COULD-NOT-VERIFY, each shape, each distinguishable ─────
            # All silent and fail-open, in the same dirty state with a
            # live FOREIGN reservation — so a silence here is the rule
            # firing, not an absent holder.
            json.dump({"session_id": "s-foreign", "agent_id": None,
                       "claimed_at": now - 300, "ttl_seconds": _TTL_SECONDS},
                      open(reservation_path(gd), "w"))
            assert verdict(MINE, now=now)[0] == "fire"   # control: fires here
            cnv = {}
            # (a) un-extractable target copy: unparseable quoting
            cnv["quoting"] = verdict(
                {**MINE, "tool_input": {"command": "git commit -m 'x"}}, now=now)
            # (b) un-extractable target copy: the copy is relocated
            cnv["relocated"] = verdict(
                {**MINE, "tool_input": {"command": "git --git-dir=/g commit -m x"}},
                now=now)
            # (c) no git dir at the target
            cnv["no-git-dir"] = verdict({**MINE, "cwd": td}, now=now)
            # (d) the committing writer cannot be identified
            cnv["no-session"] = verdict({**MINE, "session_id": None}, now=now)
            # (e) malformed reservation — not JSON …
            open(reservation_path(gd), "w").write("{not json")
            cnv["not-json"] = verdict(MINE, now=now)
            # … and JSON with an invalid field
            for bad, label in [({"session_id": "s", "claimed_at": "soon",
                                 "ttl_seconds": 60}, "bad-claimed-at"),
                               ({"session_id": "", "claimed_at": now,
                                 "ttl_seconds": 60}, "empty-session"),
                               ({"session_id": "s", "claimed_at": now,
                                 "ttl_seconds": 0}, "bad-ttl"),
                               ([1, 2, 3], "not-an-object")]:
                json.dump(bad, open(reservation_path(gd), "w"))
                cnv[label] = verdict(MINE, now=now)
            # (f) unreadable reservation
            os.chmod(reservation_path(gd), 0o000)
            cnv["unreadable"] = verdict(MINE, now=now)
            os.chmod(reservation_path(gd), 0o644)

            if os.geteuid() == 0:      # root reads through mode 000
                cnv.pop("unreadable")
            for label, (outcome, detail) in cnv.items():
                assert outcome == "cannot-verify", (label, outcome, detail)
                assert detail, label
            # distinguishable: every shape names a DIFFERENT reason
            assert len(set(d for _, d in cnv.values())) == len(cnv), cnv

            # ── FALSE-FIRE PROBE: the lane against its own docstring ───
            # Free, adversarial, in-domain text by the same author — and
            # it runs with the FOREIGN reservation live and the copy
            # dirty, so a silence here means the predicate declined, not
            # that there was nothing to fire on.
            json.dump({"session_id": "s-foreign", "agent_id": None,
                       "claimed_at": now - 300, "ttl_seconds": _TTL_SECONDS},
                      open(reservation_path(gd), "w"))
            assert verdict(MINE, now=now)[0] == "fire"   # control
            doc_outcome, doc_detail = verdict(
                {**MINE, "tool_input": {"command": __doc__}}, now=now)
            assert doc_outcome != "fire", ("docstring false fire", doc_detail)
            # …and no paragraph of it alone fires either, so one silent
            # whole cannot hide a firing part.
            for para in __doc__.split("\n\n"):
                o, d = verdict({**MINE, "tool_input": {"command": para}},
                               now=now)
                assert o != "fire", ("docstring paragraph false fire", para, d)
            # The probe with real reach: strip the quote characters so
            # the text DOES reach the predicate, then probe per
            # paragraph. Exactly one matches — the residue list, which
            # literally contains `cd <elsewhere> && git commit`, a
            # correct shell reading of prose. Pinned by identity, so a
            # SECOND matching paragraph goes red.
            flat = __doc__.replace("'", "").replace('"', "").replace("`", "")
            matched = [p for p in flat.split("\n\n")
                       if commit_targets(p, MINE)[0] == "targets"]
            assert len(matched) == 1, [p[:60] for p in matched]
            assert "cd <elsewhere> && git commit" in matched[0]
            # instrument sanity: the probe CAN match — the same reader,
            # in the same quote-stripped shape, on known positives
            for pos in ("git commit -m x", "cd /x && git commit -m x",
                        "git status ; git commit --amend"):
                assert commit_targets(pos, MINE)[0] == "targets", pos

            # ── Claiming (PostToolUse) ────────────────────────────────
            os.unlink(reservation_path(gd))
            W = {"hook_event_name": "PostToolUse", "tool_name": "Write",
                 "session_id": "s-a", "tool_input": {"file_path": tracked}}
            assert on_write(W) == "claimed"
            state, rec, _ = read_reservation(gd)
            assert state == "held" and holder(rec) == ("s-a", None)
            assert rec["ttl_seconds"] == _TTL_SECONDS   # the stamped binding
            assert on_write(W) == "refreshed"           # own claim refreshes
            # a live FOREIGN reservation is never stolen
            assert on_write({**W, "session_id": "s-b"}) == "foreign"
            assert holder(read_reservation(gd)[1]) == ("s-a", None)
            # …but an EXPIRED one is claimable
            json.dump({"session_id": "s-a", "agent_id": None,
                       "claimed_at": now - _TTL_SECONDS - 60,
                       "ttl_seconds": _TTL_SECONDS},
                      open(reservation_path(gd), "w"))
            assert on_write({**W, "session_id": "s-b"}) == "claimed"
            # …and a malformed one is overwritten, not respected: a dead
            # lock is worse than a lost record naming nobody
            open(reservation_path(gd), "w").write("{not json")
            assert on_write(W) == "claimed"
            assert holder(read_reservation(gd)[1]) == ("s-a", None)
            # non-write tools, missing path, non-repo path → no claim
            assert on_write({**W, "tool_name": "Bash"}) == "not-a-write"
            assert on_write({**W, "tool_input": {}}) == "no-path"
            assert on_write({**W, "tool_input": {
                "file_path": td + "/outside.py"}}) == "no-git-dir"
            assert on_write({**W, "session_id": None}) == "unidentified"
            # MAIN-SESSION writes DO claim — the incident was main-vs-main,
            # which is exactly what writer-claims-gate's subagent-only
            # recording cannot see
            assert "agent_id" not in W

            # ── Release (Stop/SubagentStop), GATED ON GIT EVIDENCE ────
            # Both directions in ONE fixture: a release test that only
            # checks the clean case passes against a lane that always
            # releases, which is exactly the injection below.
            S = {"hook_event_name": "Stop", "session_id": "s-a", "cwd": copy}
            FOREIGN_COMMIT = {**MINE, "session_id": "s-other"}

            # (i) holder stops with the copy DIRTY → reservation SURVIVES,
            #     and a later foreign commit still warns.
            open(tracked, "w").write("x = dirty\n")
            assert git_status_lines(copy) == [" M f.py"]
            os.unlink(reservation_path(gd))
            assert on_write(W) == "claimed"          # s-a holds it
            assert on_stop(S) == "kept-dirty"
            assert os.path.exists(reservation_path(gd))
            assert holder(read_reservation(gd)[1]) == ("s-a", None)
            assert verdict(FOREIGN_COMMIT)[0] == "fire"   # protection intact

            # (ii) …the SAME holder stops again once the copy is CLEAN →
            #     reservation GONE, and the same commit goes silent.
            open(tracked, "w").write("x = 1\n")      # == HEAD
            assert git_status_lines(copy) == []
            assert on_stop(S) == "released"
            assert not os.path.exists(reservation_path(gd))
            assert verdict(FOREIGN_COMMIT)[0] == "silent"

            # (iii) IGNORED-only dirt counts as clean: a commit cannot
            #     stage an ignored file, so it is unabsorbable. Without
            #     this, "clean" is unreachable in any repo with a build
            #     directory and the release path would be dead.
            open(copy + "/.gitignore", "w").write("build/\n")
            g("add", "--", copy + "/.gitignore")
            assert g("commit", "-q", "--no-verify", "-m", "i").returncode == 0
            os.makedirs(copy + "/build", exist_ok=True)
            open(copy + "/build/out.o", "w").write("artifact\n")
            assert on_write(W) == "claimed"
            assert git_status_lines(copy) == []
            assert git_status_lines(copy, include_ignored=True) == ["!! build/"]
            assert on_stop(S) == "released"

            # (iv) could-not-verify on release → KEEP, never drop
            assert on_write(W) == "claimed"
            assert on_stop({**S, "cwd": td}) == "no-git-dir"
            assert os.path.exists(reservation_path(gd))
            # a status question that cannot be answered keeps it too
            assert release_reservation(gd, S, td + "/ghost") == \
                "kept-unverified"
            assert os.path.exists(reservation_path(gd))

            # (v) another writer's reservation is never removed, and a
            #     clean copy does not license stealing one either
            assert git_status_lines(copy) == []
            assert on_write({**W, "session_id": "s-b"}) == "foreign"
            assert holder(read_reservation(gd)[1]) == ("s-a", None)
            os.unlink(reservation_path(gd))
            on_write({**W, "session_id": "s-b"})     # now s-b holds it
            assert on_stop(S) == "foreign"
            assert holder(read_reservation(gd)[1]) == ("s-b", None)
            os.unlink(reservation_path(gd))

            # (vi) a stopping SUBAGENT releases its OWN reservation, and
            #     only its own — the parent session's Stop does not.
            SUB_W = {**W, "session_id": "s-p", "agent_id": "a7"}
            assert on_write(SUB_W) == "claimed"
            assert holder(read_reservation(gd)[1]) == ("s-p", "a7")
            parent_stop = {"hook_event_name": "Stop", "session_id": "s-p",
                           "cwd": copy}
            assert on_stop(parent_stop) == "foreign"     # not the parent's
            sub_stop = {"hook_event_name": "SubagentStop", "session_id": "s-p",
                        "agent_id": "a7", "cwd": copy}
            assert on_stop(sub_stop) == "released"
            assert not os.path.exists(reservation_path(gd))

            # ── e2e through main(): stdin JSON in, stdout JSON out ─────
            def run_main(raw):
                old, out, exited, ret = sys.stdin, io.StringIO(), False, None
                try:
                    sys.stdin = io.StringIO(raw)
                    with contextlib.redirect_stdout(out):
                        try:
                            ret = main()
                        except SystemExit as e:
                            exited, ret = True, e.code
                finally:
                    sys.stdin = old
                return ret, out.getvalue(), exited

            json.dump({"session_id": "s-foreign", "agent_id": "a9",
                       "claimed_at": time.time() - 60,
                       "ttl_seconds": _TTL_SECONDS},
                      open(reservation_path(gd), "w"))
            ret, out, exited = run_main(json.dumps(MINE))
            assert exited and ret == 0
            j = json.loads(out)
            # WARN, never deny: the shipped mode, and the spec's binding
            assert "permissionDecision" not in j["hookSpecificOutput"]
            ctx = j["hookSpecificOutput"]["additionalContext"]
            assert "would DENY" in ctx and "s-foreign" in ctx and "a9" in ctx
            # PostToolUse e2e claims; Stop e2e releases. The foreign
            # record above would legitimately block the claim, so it
            # goes first — the no-steal rule is asserted on its own.
            os.unlink(reservation_path(gd))
            run_main(json.dumps({"hook_event_name": "PostToolUse",
                                 "tool_name": "Edit", "session_id": "s-e2e",
                                 "tool_input": {"file_path": tracked}}))
            assert holder(read_reservation(gd)[1]) == ("s-e2e", None)
            run_main(json.dumps({"hook_event_name": "Stop",
                                 "session_id": "s-e2e", "cwd": copy}))
            assert not os.path.exists(reservation_path(gd))
            # fail-open: garbage stdin never blocks a call
            ret, out, exited = run_main("}{")
            assert ret == 0 and not exited and out == ""
            # promotion to deny stays possible via guard_modes (the lane
            # ships warn; promotion is the fire-rate review's to make)
            json.dump({"session_id": "s-foreign", "agent_id": None,
                       "claimed_at": time.time() - 60,
                       "ttl_seconds": _TTL_SECONDS},
                      open(reservation_path(gd), "w"))
            with tempfile.NamedTemporaryFile("w", suffix=".json",
                                             delete=False, dir=td) as tf:
                tf.write('{"guard_modes":'
                         ' {"writer-reservation-gate": "deny"}}')
                os.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = tf.name
            _reset_policy_cache()
            ret, out, exited = run_main(json.dumps(MINE))
            assert json.loads(out)["hookSpecificOutput"][
                "permissionDecision"] == "deny"

            os.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = "/nonexistent"
            del os.environ["CLAUDE_DISPATCH_GUARDS_FIRELOG"]
            _reset_policy_cache()

        print("writer-reservation-gate: all tests passed")
        sys.exit(0)
    sys.exit(main())
