#!/usr/bin/env python3
"""PostToolUse(Agent|Task) logger: one JSONL line per subagent dispatch.

Purpose: the model-routing table (CLAUDE.md) and dispatch-discipline.md
call for accumulated dispatch evidence; this hook is the mechanical
collector. It records ONLY mechanical facts (never judgments — outcome/
class/verification live with whoever dispatched, e.g. the PBS journal):
ts, session, cwd, tool, agent name, model, subagent type, truncated title.

Data home is OUTSIDE any git repo (log data never gets committed):
$CLAUDE_DISPATCH_LOG > $XDG_DATA_HOME/claude/dispatch-log.jsonl >
~/.local/share/claude/dispatch-log.jsonl.

Consumers: (1) the model-table re-check ritual reads it as evidence
(dispatch-discipline.md §5); (2) pbs-projekt check compares it against
journal dispatch bookings (completeness edge: a dispatch without a
booking surfaces loudly). Title is truncated to 80 chars — outside PBS
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
        "cwd": payload.get("cwd"),
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
