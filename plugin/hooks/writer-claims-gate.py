#!/usr/bin/env python3
"""PreToolUse+PostToolUse(Write|Edit) gate: per-file writer claims —
the mechanical slice of "one writer per working copy; parallel writers
need disjoint, brief-named ownership" (corpus Insurance / dispatch
skill §1; harvest 2026-08-06 item 5, source idea:
kitepon-rgb/dotagents' writer-reservation lock, re-shaped from an
explicit-release lock to TTL'd claims because stale locks are the
known failure of release-based schemes).

One file, two events (payload `hook_event_name` discriminates):

- PostToolUse, SUBAGENT context: record/refresh a claim
  {file, agent_id, session_id, ts} in the claims store. Only subagent
  writes are recorded — the dispatcher legitimately pre-writes files
  it then assigns, and main-session claims would turn that into noise.
- PreToolUse, SUBAGENT context: a fresh claim (within
  `write_claim_ttl_hours`, default 6) on the same file by ANOTHER
  agent → fire. DEFAULT-WARN (staged lane): brief-sanctioned
  serialization ("second agent touches the shared file after the
  first's commit lands", skill §1 ladder) is legitimate same-file
  writing this hook cannot see, and a stale claim outliving its agent
  false-fires by construction — the lane earns "deny" only through
  the fire-rate review (guard_modes).
- PreToolUse, MAIN session: a fresh subagent claim on the file →
  one-line additionalContext reminder, never a deny — the §4 mirror
  duty ("before writing in the same working copy, treat a reported
  named/mailbox agent as a live writer"); main-session denies train the
  override reflex.

Both PreToolUse lanes RELIEVE a claim whose file has no uncommitted
work left (`no_uncommitted_work`) — the TTL-residue class this gate
was measured false-firing on (three fires across two dotfiles waves,
2026-08-09/10, every one on a file whose claimer had already
committed and had its report booked: the claim outlived its lane by
TTL alone).

Store: JSONL, latest-record-per-file wins, at
$CLAUDE_DISPATCH_GUARDS_CLAIMS > $XDG_DATA_HOME/claude/
write-claims.jsonl (outside any repo, mirroring dispatch-log.py);
compacted in place when it outgrows _COMPACT_BYTES (keep latest
fresh claim per file).

Accepted residue (documented, same shape as push/amend gates):
Bash-mediated writes (sed -i, tee, heredocs) never pass this matcher
— the session-cut checks and review remain the outer net; and claims
are keyed on the realpath STRING, so two paths reaching one file via
an unresolvable symlink chain can miss.

Fail-open everywhere (a broken claims store must never brick edits);
--test bite-test registered via the doctor's content scan.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from _dispatch_common import (fire, fire_log, git_status_lines,  # noqa: E402
                              is_subagent, policy)

_SOURCE = "dispatch-guards/writer-claims-gate"
_WRITE_TOOLS = ("Write", "Edit")
_COMPACT_BYTES = 512 * 1024
_GIT_TIMEOUT = 10.0


def claims_path() -> Path:
    if env := os.environ.get("CLAUDE_DISPATCH_GUARDS_CLAIMS"):
        return Path(env).expanduser()
    xdg = os.environ.get("XDG_DATA_HOME") or "~/.local/share"
    return Path(xdg).expanduser() / "claude" / "write-claims.jsonl"


def ttl_seconds() -> float:
    v = policy().get("write_claim_ttl_hours", 6)
    hours = v if isinstance(v, (int, float)) and v > 0 else 6
    return hours * 3600.0


def target_file(payload: dict) -> str | None:
    """The realpath of the file a Write/Edit call touches, or None."""
    if payload.get("tool_name") not in _WRITE_TOOLS:
        return None
    fp = (payload.get("tool_input") or {}).get("file_path")
    if not isinstance(fp, str) or not fp:
        return None
    try:
        return os.path.realpath(fp)
    except (OSError, ValueError):
        return fp


def load_claims() -> dict:
    """{file: latest record} — malformed lines skipped, missing file =
    no claims. Freshness is the CALLER's question (fresh_claim)."""
    out: dict = {}
    try:
        with claims_path().open(encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if isinstance(rec, dict) and isinstance(rec.get("file"), str):
                    out[rec["file"]] = rec
    except OSError:
        pass
    return out


def fresh_claim(path: str, now: float | None = None) -> dict | None:
    """The latest claim on `path` if it is within TTL, else None."""
    rec = load_claims().get(path)
    if not rec:
        return None
    ts = rec.get("ts")
    if not isinstance(ts, (int, float)):
        return None
    now = time.time() if now is None else now
    return rec if (now - ts) <= ttl_seconds() else None


def no_uncommitted_work(path: str) -> bool:
    """True iff git reports a CLEAN tree at `path` — nothing staged,
    unstaged or untracked there. The relief predicate: a live claim on
    such a file is dropped.

    Why it relieves: this gate protects IN-FLIGHT uncommitted co-writer
    work. A clean tree at the claimed file means no such work exists —
    landed or reverted, there is nothing left to protect — whatever the
    TTL still says. GIT EVIDENCE ONLY: a dirty file (modified, staged,
    or untracked `??`) keeps every claim live regardless of the claim's
    age or of any text in a claim, a brief, or a message.

    Could-not-verify maps to NOT relieved, because relief takes positive
    evidence: a path outside any git repo, a missing directory, git
    unrunnable, slow, or exiting non-zero → False, and the gate keeps
    firing.

    The git-status call itself lives in `_dispatch_common.git_status_lines`
    — one home, because two guards now ask this question and the flags
    each cost a fix to get right. The flag rationale (including why THIS
    caller passes include_ignored=True while the reservation lane passes
    False) is documented there and must not be copied back here."""
    lines = git_status_lines(os.path.dirname(path) or ".", pathspec=path,
                             include_ignored=True, timeout=_GIT_TIMEOUT)
    return lines is not None and not lines


def record_claim(payload: dict) -> None:
    """PostToolUse, subagent: append/refresh this agent's claim."""
    path = target_file(payload)
    if not path or not is_subagent(payload):
        return
    try:
        p = claims_path()
        p.parent.mkdir(parents=True, exist_ok=True)
        rec = {"file": path, "agent_id": payload.get("agent_id"),
               "session_id": payload.get("session_id"), "ts": time.time()}
        with p.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        if p.stat().st_size > _COMPACT_BYTES:
            _compact(p)
    except OSError:
        pass  # fail-open: claims must never brick a write


def _compact(p: Path) -> None:
    """Rewrite the store keeping only the latest FRESH claim per file."""
    now = time.time()
    keep = [rec for rec in load_claims().values()
            if isinstance(rec.get("ts"), (int, float))
            and (now - rec["ts"]) <= ttl_seconds()]
    tmp = p.with_suffix(".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        for rec in keep:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    tmp.replace(p)


def check(payload: dict, now: float | None = None):
    """PreToolUse: (kind, text) — ("fire", reason) for a subagent
    cross-agent collision, ("remind", text) for the main session's
    live-writer reminder, else None. Both lanes stay silent on a
    RELIEVED claim (no_uncommitted_work)."""
    path = target_file(payload)
    if not path:
        return None
    rec = fresh_claim(path, now=now)
    if not rec:
        return None
    if no_uncommitted_work(path):
        return None  # relieved: no in-flight work left at `path`
    owner = rec.get("agent_id")
    if is_subagent(payload):
        if owner == payload.get("agent_id"):
            return None  # own claim: refresh follows on PostToolUse
        return ("fire", (
            f"Writer-claims gate: {path} was written by another agent "
            f"({owner}) within the claim TTL — write sets must be "
            "DISJOINT per file (dispatch skill §1); overlap means the "
            "brief serializes the edits. If your brief names this file "
            "as yours after the co-writer's commit landed, this is the "
            "sanctioned serialization — proceed; otherwise surface the "
            "overlap to your dispatcher as a gap, don't write over it."))
    return ("remind", (
        f"Writer-claims note (§4 mirror duty): a subagent ({owner}) "
        f"wrote {path} within the claim TTL and may still be a live "
        "writer. Book its closing report / close its lane before "
        "writing here, or check `git status` for its uncommitted work "
        "first."))


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0  # never fail the workflow on a hook parse error
    event = payload.get("hook_event_name")
    if event == "PostToolUse":
        record_claim(payload)
        return 0
    result = check(payload)
    if not result:
        return 0
    kind, text = result
    if kind == "fire":
        # staged lane: ships warn, promotable to deny via guard_modes
        fire(text, source=_SOURCE, payload=payload, default_mode="warn")
    else:
        fire_log(_SOURCE, "remind", text, payload)
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "additionalContext": text,
            }
        }))
    return 0


if __name__ == "__main__":
    if "--test" in sys.argv:
        import contextlib
        import io
        import tempfile
        from _dispatch_common import _reset_policy_cache

        os.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = "/nonexistent"
        _reset_policy_cache()

        with tempfile.TemporaryDirectory() as td:
            os.environ["CLAUDE_DISPATCH_GUARDS_CLAIMS"] = td + "/c/claims.jsonl"
            os.environ["CLAUDE_DISPATCH_GUARDS_FIRELOG"] = td + "/f.jsonl"
            fp = td + "/proj/x.py"

            def pl(event, tool, agent=None, path=fp):
                p = {"hook_event_name": event, "tool_name": tool,
                     "session_id": "s1", "tool_input": {"file_path": path}}
                if agent:
                    p["agent_id"] = agent
                return p

            # no claims yet → everything silent
            assert check(pl("PreToolUse", "Write", "a1")) is None
            assert check(pl("PreToolUse", "Edit")) is None

            # subagent A writes → claim recorded (PostToolUse)
            record_claim(pl("PostToolUse", "Write", "a1"))
            rp = os.path.realpath(fp)
            assert load_claims()[rp]["agent_id"] == "a1"

            # A again pre-write → own claim, silent
            assert check(pl("PreToolUse", "Edit", "a1")) is None
            # B pre-write same file → fire, names owner + serialization
            kind, text = check(pl("PreToolUse", "Edit", "b2"))
            assert kind == "fire" and "a1" in text and "DISJOINT" in text
            # main session pre-write → reminder, not fire
            kind, text = check(pl("PreToolUse", "Write"))
            assert kind == "remind" and "a1" in text and "git status" in text
            # different file → silent
            assert check(pl("PreToolUse", "Write", "b2",
                            path=td + "/proj/other.py")) is None
            # non-write tools / missing path → silent, never recorded
            assert target_file({"tool_name": "Bash",
                                "tool_input": {"file_path": fp}}) is None
            assert check({"hook_event_name": "PreToolUse",
                          "tool_name": "Write", "agent_id": "b2",
                          "tool_input": {}}) is None
            record_claim(pl("PostToolUse", "Bash", "a9"))  # not recorded
            assert "Bash" not in json.dumps(load_claims())
            # main-session writes are NOT recorded as claims
            record_claim(pl("PostToolUse", "Write"))
            assert load_claims()[rp]["agent_id"] == "a1"

            # TTL: a stale claim (beyond write_claim_ttl_hours) is silent
            future = time.time() + ttl_seconds() + 60
            assert fresh_claim(rp, now=future) is None
            assert check(pl("PreToolUse", "Edit", "b2"), now=future) is None
            # latest-wins: B records later → B owns, A now collides
            record_claim(pl("PostToolUse", "Write", "b2"))
            kind, text = check(pl("PreToolUse", "Edit", "a1"))
            assert kind == "fire" and "b2" in text

            # compaction: stale + duplicate records collapse to fresh set
            p = claims_path()
            with p.open("a", encoding="utf-8") as f:
                f.write(json.dumps({"file": td + "/old.py", "agent_id": "z",
                                    "ts": time.time() - ttl_seconds() - 99})
                        + "\n")
                f.write("not json\n")
            _compact(p)
            after = load_claims()
            assert rp in after and (td + "/old.py") not in after

            # ── relief: a claim whose file has NO uncommitted work ──
            # The TTL-residue false-fire class (BACKLOG READY 2026-08-10):
            # every measured fire sat on a file whose claimer had already
            # committed. Relief is GIT EVIDENCE ONLY, so each control
            # below keeps the claim live for a reason git can see.
            def git_fx(*args, cwd):
                return subprocess.run(
                    ["git", "-c", "user.email=t@t", "-c", "user.name=t",
                     "-c", "core.hooksPath=/nonexistent", *args],
                    cwd=cwd, capture_output=True, text=True)

            repo = os.path.realpath(td) + "/repo"
            os.makedirs(repo)
            git_fx("init", "-q", ".", cwd=repo)
            landed = repo + "/landed.py"
            Path(landed).write_text("x = 1\n")
            git_fx("add", "--", landed, cwd=repo)
            assert git_fx("commit", "-q", "--no-verify", "-m", "l",
                          cwd=repo).returncode == 0
            record_claim(pl("PostToolUse", "Write", "a1", path=landed))
            assert fresh_claim(landed) is not None      # the claim IS live
            # committed-clean → relieved, both lanes silent
            assert no_uncommitted_work(landed)
            assert check(pl("PreToolUse", "Edit", "b2", path=landed)) is None
            assert check(pl("PreToolUse", "Write", path=landed)) is None
            # …the same claim over a DIRTY file → both lanes fire again
            Path(landed).write_text("x = 2\n")
            assert not no_uncommitted_work(landed)
            assert check(pl("PreToolUse", "Edit", "b2",
                            path=landed))[0] == "fire"
            assert check(pl("PreToolUse", "Write", path=landed))[0] == "remind"
            Path(landed).write_text("x = 1\n")          # == HEAD: clean again
            # …UNTRACKED file → fires; git sees `??`, nothing landed
            untracked = repo + "/untracked.py"
            Path(untracked).write_text("y = 1\n")
            record_claim(pl("PostToolUse", "Write", "a1", path=untracked))
            assert not no_uncommitted_work(untracked)
            assert check(pl("PreToolUse", "Edit", "b2",
                            path=untracked))[0] == "fire"
            # …GITIGNORED file with live content → fires. Plain status
            # reports nothing for an ignored path, so without
            # --ignored=matching this was the one hole where relief fired
            # WITHOUT evidence (measured 2026-08-10); ignored-path claims
            # stay TTL-governed forever, the conservative direction.
            Path(repo + "/.gitignore").write_text("ignored.py\n")
            git_fx("add", "--", repo + "/.gitignore", cwd=repo)
            assert git_fx("commit", "-q", "--no-verify", "-m", "i",
                          cwd=repo).returncode == 0
            ignored = repo + "/ignored.py"
            Path(ignored).write_text("in_flight = True\n")
            record_claim(pl("PostToolUse", "Write", "a1", path=ignored))
            assert not no_uncommitted_work(ignored)
            assert check(pl("PreToolUse", "Edit", "b2",
                            path=ignored))[0] == "fire"
            # …and the flag does not over-fire: committed-clean relief
            # above must still hold with .gitignore present
            assert no_uncommitted_work(landed)
            # …outside any repo, or under a missing dir → could-not-verify,
            # which is not relief: relief takes positive evidence
            outside = os.path.realpath(td) + "/outside.py"
            Path(outside).write_text("z = 1\n")
            record_claim(pl("PostToolUse", "Write", "a1", path=outside))
            os.environ["GIT_CEILING_DIRECTORIES"] = os.path.realpath(td)
            assert not no_uncommitted_work(outside)
            assert check(pl("PreToolUse", "Edit", "b2",
                            path=outside))[0] == "fire"
            del os.environ["GIT_CEILING_DIRECTORIES"]
            assert not no_uncommitted_work(td + "/nodir/ghost.py")
            # …and relief never outranks the TTL: stale stays silent
            assert check(pl("PreToolUse", "Edit", "b2", path=untracked),
                         now=time.time() + ttl_seconds() + 60) is None

            # ── e2e through main(): warn JSON, reminder JSON, recording ──
            def run_main(raw):
                old = sys.stdin
                out = io.StringIO()
                exited = False
                ret = None
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

            # subagent collision → warn additionalContext (default mode)
            ret, out, exited = run_main(json.dumps(pl("PreToolUse", "Edit", "a1")))
            assert exited and ret == 0
            j = json.loads(out)
            assert "would DENY" in j["hookSpecificOutput"]["additionalContext"]
            # main-session reminder → plain additionalContext, no exit
            ret, out, exited = run_main(json.dumps(pl("PreToolUse", "Write")))
            assert not exited and ret == 0
            assert "mirror duty" in json.loads(out)["hookSpecificOutput"][
                "additionalContext"]
            # PostToolUse e2e records
            run_main(json.dumps(pl("PostToolUse", "Write", "c3")))
            assert load_claims()[rp]["agent_id"] == "c3"
            # promotion to deny via guard_modes
            with tempfile.NamedTemporaryFile("w", suffix=".json",
                                             delete=False, dir=td) as tf:
                tf.write('{"guard_modes": {"writer-claims-gate": "deny"}}')
                os.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = tf.name
            _reset_policy_cache()
            ret, out, exited = run_main(json.dumps(pl("PreToolUse", "Edit", "a1")))
            assert json.loads(out)["hookSpecificOutput"][
                "permissionDecision"] == "deny"
            # fail-open: garbage stdin, unwritable store
            ret, out, exited = run_main("}{")
            assert ret == 0 and not exited
            os.environ["CLAUDE_DISPATCH_GUARDS_CLAIMS"] = "/proc/nope/c.jsonl"
            record_claim(pl("PostToolUse", "Write", "a1"))  # must not raise
            assert check(pl("PreToolUse", "Edit", "b2")) is None

            os.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = "/nonexistent"
            del os.environ["CLAUDE_DISPATCH_GUARDS_CLAIMS"]
            del os.environ["CLAUDE_DISPATCH_GUARDS_FIRELOG"]
            _reset_policy_cache()

        print("writer-claims-gate: all tests passed")
        sys.exit(0)
    sys.exit(main())
