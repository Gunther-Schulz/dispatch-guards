#!/usr/bin/env python3
"""PostToolUse(Agent|Task) logger: one JSONL line per subagent dispatch.

Purpose: the model-routing table (CLAUDE.md) and the dispatch skill
call for accumulated dispatch evidence; this hook is the mechanical
collector. It records ONLY mechanical facts (never judgments — outcome/
class/verification live with whoever dispatched, e.g. the PBS journal):
ts, session, cwd, tool, agent name, model, subagent type, truncated title,
and the DISPATCHING context (`von_agent`: the spawning subagent's agent_id,
null in the main session).

Why von_agent (2026-07-28): the log recorded session_id only, so "did this
dispatch come from a subagent?" was not answerable from the record — the
question was unobservable, not unasked. The escalation lane in
agent-model-gate denies the expensive case; this field is how its
fire-rate (and any nesting at all) becomes visible at review time.

Why work_repo (2026-08-06): `cwd` is the DISPATCHING session's
directory, not the work's — a dispatch into a sibling repo records
the dispatcher's cwd, so "which repo was this work in?" was not
answerable from the log. The field carries the working-copy path the
brief names (§1 skeleton's `Working copy:` line), or null when the
prompt does not name one — never a guess.

Data home is OUTSIDE any git repo (log data never gets committed):
$CLAUDE_DISPATCH_LOG > $XDG_DATA_HOME/claude/dispatch-log.jsonl >
~/.local/share/claude/dispatch-log.jsonl.

Consumers: (1) the model-table re-check ritual and the fire-rate
review read it as accumulated dispatch evidence (counts replace the
"still thin" anecdote); (2) project-side completeness edges compare
it against their booking discipline (e.g. pbs-projekt check vs
journal bookings: a dispatch without a booking surfaces loudly). Title is truncated to 80 chars — outside PBS
a description may carry arbitrary text; the log stays lean by design.

Fail-open on every error (a broken logger must never brick dispatches);
--test is the tripwire (bootstrap doctor).
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

_TITEL_MAX = 80
_WORK_REPO_MARKER = "Working copy:"
_WORK_REPO_CUT = " Base check:"


def arbeits_repo(prompt: object) -> str | None:
    """The working-copy path the dispatch prompt names, or None.

    Sliced, never matched against a character class: a class that stops
    at an unexpected byte (umlaut, space) yields a TRUNCATED path whose
    negative verdict is indistinguishable from a legitimate finding
    (_dispatch_common extraction standard). Failure to extract maps to
    None (JSON null) — never a guess, never a partial path."""
    if not isinstance(prompt, str):
        return None
    for zeile_text in prompt.splitlines():
        stripped = zeile_text.strip()
        if not stripped.startswith(_WORK_REPO_MARKER):
            continue
        rest = stripped[len(_WORK_REPO_MARKER):]
        schnitt = rest.find(_WORK_REPO_CUT)
        if schnitt != -1:
            rest = rest[:schnitt]
        rest = rest.strip()
        if rest.endswith("."):
            rest = rest[:-1]
        return rest or None
    return None


def log_pfad() -> Path:
    if env := os.environ.get("CLAUDE_DISPATCH_LOG"):
        return Path(env).expanduser()
    xdg = os.environ.get("XDG_DATA_HOME") or "~/.local/share"
    return Path(xdg).expanduser() / "claude" / "dispatch-log.jsonl"


def zeile(payload: dict) -> dict | None:
    """Build the log record, or None (= not a dispatch)."""
    if payload.get("tool_name") not in ("Agent", "Task"):
        return None
    ti = payload.get("tool_input") or {}
    titel = str(ti.get("description") or "")[:_TITEL_MAX]
    return {
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "session_id": payload.get("session_id"),
        "von_agent": payload.get("agent_id"),  # None = main session
        "cwd": payload.get("cwd"),
        "work_repo": arbeits_repo(ti.get("prompt")),
        "tool": payload.get("tool_name"),
        "name": ti.get("name"),
        "modell": ti.get("model"),
        "subagent_type": ti.get("subagent_type"),
        "titel": titel,
    }


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0  # never fail the workflow on a hook parse error
    try:
        rec = zeile(payload)
        if rec is None:
            return 0
        pfad = log_pfad()
        pfad.parent.mkdir(parents=True, exist_ok=True)
        with pfad.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    except OSError:
        return 0  # fail-open: logging must never block a dispatch
    return 0


if __name__ == "__main__":
    if "--test" in sys.argv:
        import tempfile
        assert zeile({"tool_name": "Bash"}) is None
        assert zeile({}) is None
        rec = zeile({
            "tool_name": "Agent", "session_id": "s1", "cwd": "/tmp",
            "tool_input": {"description": "opus: Testlauf " + "x" * 200,
                           "name": "opus-test", "model": "opus"},
        })
        assert rec is not None and rec["name"] == "opus-test"
        assert rec["modell"] == "opus" and len(rec["titel"]) == _TITEL_MAX
        assert rec["von_agent"] is None  # main session: field present, null
        # Dispatching context (2026-07-28): a nested dispatch is only
        # visible in the record if agent_id is carried over.
        rec_sub = zeile({
            "tool_name": "Agent", "session_id": "s1", "agent_id": "a1",
            "tool_input": {"description": "sonnet: x", "model": "sonnet"},
        })
        assert rec_sub is not None and rec_sub["von_agent"] == "a1"
        # Work repo (2026-08-06): cwd is the DISPATCHER's directory, so
        # the work's repo is only in the record if the brief's
        # `Working copy:` line is extracted. Expectations derived from
        # the dispatch skill §1 brief skeleton, not from this code.
        rec_wr = zeile({
            "tool_name": "Agent", "session_id": "s1", "cwd": "/elsewhere",
            "tool_input": {"description": "d", "prompt":
                           "Title: t\nWorking copy: /home/g/dev/"
                           "Gunther-Schulz/dispatch-guards. Base check: "
                           "git merge-base --is-ancestor 7ee9b35 HEAD\n"
                           "Scratch: own scratchpad."},
        })
        assert rec_wr is not None
        assert rec_wr["work_repo"] == ("/home/g/dev/Gunther-Schulz/"
                                       "dispatch-guards"), rec_wr
        # No such line → null, never a guess.
        rec_nowr = zeile({
            "tool_name": "Agent", "session_id": "s1", "cwd": "/elsewhere",
            "tool_input": {"description": "d", "prompt": "Just do X."},
        })
        assert rec_nowr is not None and rec_nowr["work_repo"] is None
        # Umlaut + space: the FULL path, asserted whole — a class-based
        # extractor truncating at the first non-ASCII byte fails HERE,
        # and its shorter value would resolve elsewhere silently.
        rec_uml = zeile({
            "tool_name": "Agent", "session_id": "s1", "cwd": "/elsewhere",
            "tool_input": {"description": "d", "prompt":
                           "Working copy: /home/g/dev/Öffentlich "
                           "Planungsbüro/repo. Base check: x"},
        })
        assert rec_uml is not None
        assert rec_uml["work_repo"] == ("/home/g/dev/Öffentlich "
                                        "Planungsbüro/repo"), rec_uml
        with tempfile.TemporaryDirectory() as td:
            os.environ["CLAUDE_DISPATCH_LOG"] = td + "/sub/log.jsonl"
            import io
            sys.stdin = io.StringIO(json.dumps({
                "tool_name": "Task", "session_id": "s2", "cwd": "/x",
                "tool_input": {"description": "t", "name": None},
            }))
            assert main() == 0
            zeilen = Path(td + "/sub/log.jsonl").read_text().splitlines()
            assert len(zeilen) == 1 and json.loads(zeilen[0])["tool"] == "Task"
            sys.stdin = io.StringIO("kein json")
            assert main() == 0  # fail-open
            del os.environ["CLAUDE_DISPATCH_LOG"]
        print("dispatch-log: all tests passed")
        sys.exit(0)
    sys.exit(main())
