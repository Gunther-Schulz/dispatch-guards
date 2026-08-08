#!/usr/bin/env python3
"""Worktree doctor: a REPORTING verdict over registered git worktrees.

REPORTING ONLY. This tool has no removal path whatsoever — no
`--remove`, no `--force`, no code path that calls `git worktree
remove`, `git worktree prune`, `git branch -d`, or any other mutating
git command. It reads registered worktrees and their working-tree
status, prints a classification and an overall verdict, and — for
worktrees it can safely recommend — prints the exact (unforced)
`git worktree remove <path>` command as TEXT for the operator to run.
Nothing here executes a removal.

Why: dev-notes/worktree-OBSERVATIONS.md, "2026-08-08 — LIFECYCLE".
A dispatcher's `for w in $(git worktree list ...); do git worktree
remove --force "$w"; done` destroyed 16 registered worktrees in one
repo, including one belonging to a different, still-live session,
because (a) nothing marks ownership at worktree-create time and (b)
`--force` overrides the refusal that would otherwise protect a dirty
worktree. This tool answers "what's here and is it safe to remove"
without ever removing anything itself, so a human (or a later,
separately-decided mechanism) makes the destructive call.

OWNERSHIP IS DECLARED, NEVER INFERRED. `--owned PATH` (repeatable)
is the *only* way a worktree is treated as belonging to the caller.
A worktree not declared via `--owned` is UNKNOWN — never treated as
foreign or as removable — because this tool cannot know whose it is.
Ownership is never derived from a path shape, name prefix, directory
component, branch name, or commit trailer: a predicate keyed on a
naming convention re-creates the exact pattern-blind-spot class the
founding incident exposed (a naming-based sweep cannot tell "this
session's worktree" from "a week of other people's").

Usage:
    worktree_doctor.py [--owned PATH]... [--repo PATH] [--json]
    worktree_doctor.py --test

Classification (every registered worktree except the main one):
    DIRTY       modified tracked files or untracked files present.
                Outranks everything — a declared-owned dirty
                worktree is still DIRTY and is never removable.
    REMOVABLE   clean AND declared owned via --owned.
    UNKNOWN     clean, ownership not declared. Not removable.
    UNREADABLE  the worktree path is missing, or a git command
                against it failed. Never inferred to be anything
                else; feeds the could-not-verify verdict.

Overall verdict (worst status present; drives the exit code):
    clean            no worktrees besides main, or every one is
                      REMOVABLE.                          exit 0
    stale-found       at least one DIRTY, UNKNOWN, or REMOVABLE
                      worktree exists and everything was readable.
                                                            exit 1
    could-not-verify  at least one UNREADABLE worktree, or the repo
                      itself could not be read.            exit 2

Parsing uses `git worktree list --porcelain` (never the human
format). Per git's own documented behavior, the first entry in that
listing is always the main worktree, followed by linked worktrees in
registration order — this script relies on that ordering to identify
the main worktree it never classifies.
"""
from __future__ import annotations

import argparse
import json
import os
import shlex
import subprocess
import sys

STATUS_RANK = {"UNREADABLE": 3, "DIRTY": 2, "UNKNOWN": 2, "REMOVABLE": 1}


def _run(cmd: list[str], cwd: str | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)


def parse_porcelain(text: str) -> list[dict]:
    """Parse `git worktree list --porcelain` output into per-worktree dicts."""
    entries: list[dict] = []
    current: dict = {}
    for line in text.splitlines():
        if not line.strip():
            if current:
                entries.append(current)
                current = {}
            continue
        if line.startswith("worktree "):
            current["path"] = line[len("worktree "):]
        elif line.startswith("HEAD "):
            current["head"] = line[len("HEAD "):]
        elif line.startswith("branch "):
            ref = line[len("branch "):]
            prefix = "refs/heads/"
            current["branch"] = ref[len(prefix):] if ref.startswith(prefix) else ref
            current["detached"] = False
        elif line == "detached":
            current["detached"] = True
        elif line == "bare":
            current["bare"] = True
        elif line.startswith("locked"):
            current["locked"] = True
        elif line.startswith("prunable"):
            current["prunable"] = True
    if current:
        entries.append(current)
    return entries


def get_worktrees(repo: str | None) -> tuple[list[dict] | None, str | None]:
    """Return (entries, None) or (None, error). entries[0] is always main."""
    cmd = ["git"]
    if repo:
        cmd += ["-C", repo]
    cmd += ["worktree", "list", "--porcelain"]
    r = _run(cmd)
    if r.returncode != 0:
        return None, (r.stderr.strip() or "git worktree list failed")
    entries = parse_porcelain(r.stdout)
    if not entries:
        return None, "git worktree list returned no entries"
    return entries, None


def classify_worktree(entry: dict, owned_set: set[str]) -> tuple[str, str]:
    """Return (status, why) for one non-main worktree entry."""
    path = entry["path"]
    if not os.path.isdir(path):
        return "UNREADABLE", "worktree path missing"
    r = _run(["git", "-C", path, "status", "--porcelain", "--untracked-files=normal"])
    if r.returncode != 0:
        return "UNREADABLE", f"git status failed: {r.stderr.strip()}"
    lines = [ln for ln in r.stdout.splitlines() if ln.strip()]
    if lines:
        untracked = sum(1 for ln in lines if ln.startswith("??"))
        modified = len(lines) - untracked
        parts = []
        if modified:
            parts.append(f"{modified} modified")
        if untracked:
            parts.append(f"{untracked} untracked")
        return "DIRTY", ", ".join(parts) if parts else f"{len(lines)} changed"
    if os.path.realpath(path) in owned_set:
        return "REMOVABLE", "clean; declared owned via --owned"
    return "UNKNOWN", "clean; not declared owned"


def classify_all(entries: list[dict], owned_paths: list[str]) -> list[dict]:
    """Classify every (non-main) entry. Never mutates anything."""
    owned_set = {os.path.realpath(p) for p in owned_paths}
    out = []
    for e in entries:
        status, why = classify_worktree(e, owned_set)
        branch = e.get("branch")
        if not branch:
            branch = "(detached HEAD)" if e.get("detached") else None
        out.append({
            "path": e["path"],
            "branch": branch,
            "status": status,
            "why": why,
        })
    return out


def overall_verdict(results: list[dict]) -> str:
    """Worst status present drives the verdict; no results = clean."""
    if not results:
        return "clean"
    worst = max(STATUS_RANK[r["status"]] for r in results)
    if worst == 3:
        return "could-not-verify"
    if worst == 2:
        return "stale-found"
    return "clean"


EXIT_CODE = {"clean": 0, "stale-found": 1, "could-not-verify": 2}


def print_human(main_entry: dict, results: list[dict], verdict: str) -> None:
    print(f"main worktree: {main_entry['path']}")
    if not results:
        print("  (no other registered worktrees)")
    for r in results:
        branch = r["branch"] or "(unknown)"
        print(f"  {r['status']:10} {r['path']}  [{branch}]  — {r['why']}")
    removable = [r for r in results if r["status"] == "REMOVABLE"]
    if removable:
        print()
        print("Recommended removals (review before running — not executed here):")
        for r in removable:
            print(f"  git worktree remove {shlex.quote(r['path'])}")
    print()
    print(f"verdict: {verdict}")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        prog="worktree_doctor.py",
        description="REPORTING verdict over registered git worktrees. "
                     "Never removes anything.")
    parser.add_argument("--owned", action="append", default=[], metavar="PATH",
                         help="declare PATH as caller-owned (repeatable)")
    parser.add_argument("--repo", default=None, metavar="PATH",
                         help="repo to inspect (default: cwd)")
    parser.add_argument("--json", action="store_true",
                         help="emit machine-readable JSON instead of text")
    args = parser.parse_args(argv)

    entries, err = get_worktrees(args.repo)
    if err is not None:
        if args.json:
            print(json.dumps({"verdict": "could-not-verify", "worktrees": [],
                               "error": err}, indent=2))
        else:
            print(f"error: {err}")
            print("verdict: could-not-verify")
        return 2

    main_entry, non_main = entries[0], entries[1:]
    results = classify_all(non_main, args.owned)
    verdict = overall_verdict(results)

    if args.json:
        out = {
            "verdict": verdict,
            "main_worktree": main_entry["path"],
            "worktrees": results,
        }
        print(json.dumps(out, indent=2))
    else:
        print_human(main_entry, results, verdict)

    return EXIT_CODE[verdict]


def self_test() -> int:
    import shutil
    import tempfile

    # --- pure overall_verdict() aggregation, no git involved ---
    assert overall_verdict([]) == "clean"
    assert overall_verdict([{"status": "REMOVABLE"}]) == "clean"
    assert overall_verdict([{"status": "REMOVABLE"}, {"status": "REMOVABLE"}]) == "clean"
    assert overall_verdict([{"status": "UNKNOWN"}]) == "stale-found"
    assert overall_verdict([{"status": "DIRTY"}]) == "stale-found"
    assert overall_verdict([{"status": "REMOVABLE"}, {"status": "UNKNOWN"}]) == "stale-found"
    assert overall_verdict([{"status": "UNREADABLE"}]) == "could-not-verify"
    assert overall_verdict(
        [{"status": "REMOVABLE"}, {"status": "UNREADABLE"}]) == "could-not-verify"

    # --- UNREADABLE via a genuinely missing path, no repo needed ---
    ghost = [{"path": "/nonexistent/path/for/worktree/doctor/test",
              "branch": "ghost", "detached": False}]
    ghost_results = classify_all(ghost, owned_paths=[])
    assert ghost_results[0]["status"] == "UNREADABLE", ghost_results
    assert overall_verdict(ghost_results) == "could-not-verify"

    # --- real-git fixture: the brief's three-arm scenario ---
    tmp = tempfile.mkdtemp(prefix="worktree_doctor_test_")
    try:
        repo = os.path.join(tmp, "repo")
        os.makedirs(repo)
        assert _run(["git", "init", "-q"], repo).returncode == 0
        _run(["git", "config", "user.email", "t@t"], repo)
        _run(["git", "config", "user.name", "t"], repo)
        readme = os.path.join(repo, "README.md")
        with open(readme, "w") as f:
            f.write("hello\n")
        _run(["git", "add", "README.md"], repo)
        assert _run(["git", "commit", "-q", "-m", "init"], repo).returncode == 0

        wt_a = os.path.join(tmp, "wt-a")  # will be declared owned, clean
        wt_b = os.path.join(tmp, "wt-b")  # clean, NOT declared
        wt_c = os.path.join(tmp, "wt-c")  # declared owned, but DIRTY
        for wt, branch in ((wt_a, "a"), (wt_b, "b"), (wt_c, "c")):
            r = _run(["git", "worktree", "add", "-b", branch, wt], repo)
            assert r.returncode == 0, r.stderr

        with open(os.path.join(wt_c, "README.md"), "a") as f:
            f.write("edit\n")
        with open(os.path.join(wt_c, "new.txt"), "w") as f:
            f.write("x\n")

        entries, err = get_worktrees(repo)
        assert err is None, err
        assert len(entries) == 4, entries  # main + a + b + c
        assert os.path.realpath(entries[0]["path"]) == os.path.realpath(repo), entries[0]

        results = classify_all(entries[1:], owned_paths=[wt_a, wt_c])
        by_path = {os.path.realpath(r["path"]): r for r in results}
        assert by_path[os.path.realpath(wt_a)]["status"] == "REMOVABLE", by_path
        assert by_path[os.path.realpath(wt_b)]["status"] == "UNKNOWN", by_path
        # Arm C: declared owned AND dirty. The incident's own loop would
        # have force-removed this one; the doctor must refuse it loudly.
        assert by_path[os.path.realpath(wt_c)]["status"] == "DIRTY", by_path
        assert "owned" not in by_path[os.path.realpath(wt_c)]["why"], (
            "arm C's why-string must not read as an ownership clearance")

        assert overall_verdict(results) == "stale-found", results

        # Clean arm C to prove the all-REMOVABLE -> clean path too,
        # still through real git status, not a synthetic status list.
        _run(["git", "checkout", "--", "README.md"], wt_c)
        os.remove(os.path.join(wt_c, "new.txt"))
        entries2, err2 = get_worktrees(repo)
        assert err2 is None, err2
        only_a_c = [e for e in entries2[1:]
                    if os.path.realpath(e["path"]) in
                    (os.path.realpath(wt_a), os.path.realpath(wt_c))]
        results2 = classify_all(only_a_c, owned_paths=[wt_a, wt_c])
        assert all(r["status"] == "REMOVABLE" for r in results2), results2
        assert overall_verdict(results2) == "clean", results2
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print("worktree_doctor: all tests passed")
    return 0


if __name__ == "__main__":
    if "--test" in sys.argv:
        sys.exit(self_test())
    sys.exit(main(sys.argv[1:]))
