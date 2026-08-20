#!/usr/bin/env python3
"""Stop hook: nudge a handed-off desk to actually SEND its report.

Root cause this closes (BACKLOG.md, "a marker-gated Stop lane for
handed-off desks"; dispatch skill §4, "A handed-off run names its
report CHANNEL, machine-readably"): passing WHOLE WORK to a peer
session over SendMessage is neither a dispatch nor fact traffic —
nothing returns by construction, unlike a subagent dispatch whose
completion notification delivers the final text. A session that
received such a handoff composes its closing report as ordinary
final text, which on that lane reaches no one: measured twice within
one hour on one desk, the operator seeing only an idle session. §4
now mandates the handoff carry a machine-readable
`REPORT-CHANNEL: SendMessage <name>` line; this hook is the
mechanical half — `report-enforcer.py`'s sibling one level up
(that one nudges a SUBAGENT before SubagentStop, whose channel is
always known from the dispatch itself; this one nudges a session
that received a HANDOFF, whose channel is knowable only from a
marker in its own transcript, since a handoff is not a dispatch and
carries no `name` field the harness records).

Fires only when ALL of:
  - the transcript carries a `REPORT-CHANNEL: SendMessage <name>`
    marker, ANYWHERE (user- or assistant-role event: a handoff
    arrives as an incoming message, so the marker can sit in
    either) — case-sensitive on the `REPORT-CHANNEL:` token;
  - the ENDING TURN (transcript events after the last user-role
    message) composes substantial final text — the last
    assistant-role event's `text`-type content blocks total at
    least `_SUBSTANTIAL_CHARS`;
  - no `SendMessage` tool_use to the captured `<name>` occurred
    within that same ending-turn window (a send to a DIFFERENT name
    does not satisfy the duty).

Marker-gated by design: a session that never received such a
handoff carries no marker and this lane is silent by construction —
the false-fire profile is near zero (arm (iii) below is the
control). `stop_hook_active` true → silent (standard anti-loop
guard; a Stop hook that re-fires on its own continuation is a
defect, the same loop-breaker `report-enforcer.py` documents for
SubagentStop).

Emission shape, NOT routed through `_dispatch_common.fire()`: that
helper hardcodes `hookSpecificOutput.hookEventName` to `"PreToolUse"`
(correct for every existing caller, which are all PreToolUse
guards) — using it here would ship a Stop-event additionalContext
injection under the WRONG event name, which `report-enforcer.py`'s
own docstring and bite-test treat as load-bearing
(`hookEventName == "SubagentStop"`, verified against the harness
docs). This hook builds its own Stop-shaped payload (mirroring
`report-enforcer.output_json`) while still routing through
`_dispatch_common`'s `guard_mode()` (site-policy warn/deny/off
staging, key `handoff-report-gate`) and `fire_log()` (the fire-rate
review's ledger) — the shared STAGING vocabulary, not the
shared JSON shape, since the latter would be wrong for this event.
Ships default-warn (repo rule, CLAUDE.md): `off` stays silent,
`warn`/`deny` both emit the same additionalContext nudge — Stop
carries no `permissionDecision`, so there is no blocking verb for
`deny` to reach for yet; a future promotion is free to give it one.

Fail-open (standing guard rule, `_dispatch_common`): unparseable
stdin, missing `transcript_path`, or an unreadable/malformed
transcript → silent, nothing logged (the read never produced a
verdict to log).
"""
from __future__ import annotations

import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from _dispatch_common import fire_log, guard_mode  # noqa: E402

_SOURCE = "dispatch-guards/handoff-report-gate"

# One named knob (dispatcher's decision 4): the "substantial final
# text" threshold, in characters, of the ending turn's final
# assistant text.
_SUBSTANTIAL_CHARS = 400

# `REPORT-CHANNEL:` case-sensitive; `SendMessage` is the tool name
# proper, so matched literally too. The captured name run is
# whitespace/comma/semicolon-terminated; trailing markdown/prose
# punctuation is stripped separately (a marker line pasted inside
# backticks or ending a sentence must not poison the captured name).
_MARKER_RE = re.compile(r"REPORT-CHANNEL:\s*SendMessage\s+(\S+)")
_TRAIL_PUNCT = ".,;:)]}`'\">"


def _read_events(transcript_path: str) -> list | None:
    """Every parseable JSONL line of the transcript, or None on an
    unreadable file (fail-open: no verdict, nothing to log)."""
    try:
        events = []
        with open(transcript_path, "r", encoding="utf-8",
                  errors="replace") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    events.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    except OSError:
        return None
    return events


def _message_text(msg: dict) -> str:
    """Concatenated text content of one transcript message, user or
    assistant role: a plain string body, `text`-type blocks, and the
    text inside `tool_result` blocks (an incoming SendMessage payload
    is delivered to its recipient as a user-role tool_result)."""
    content = msg.get("content")
    if isinstance(content, str):
        return content
    if not isinstance(content, list):
        return ""
    parts = []
    for block in content:
        if not isinstance(block, dict):
            continue
        btype = block.get("type")
        if btype == "text":
            parts.append(str(block.get("text") or ""))
        elif btype == "tool_result":
            c = block.get("content")
            if isinstance(c, str):
                parts.append(c)
            elif isinstance(c, list):
                for b in c:
                    if isinstance(b, dict) and b.get("type") == "text":
                        parts.append(str(b.get("text") or ""))
    return "\n".join(parts)


def captured_channel(events: list) -> str | None:
    """The `<name>` from the first `REPORT-CHANNEL: SendMessage
    <name>` marker found anywhere in the transcript (user or
    assistant role), or None if no marker is present."""
    for ev in events:
        msg = ev.get("message")
        if not isinstance(msg, dict) or msg.get("role") not in (
                "user", "assistant"):
            continue
        text = _message_text(msg)
        if not text:
            continue
        m = _MARKER_RE.search(text)
        if m:
            name = m.group(1).rstrip(_TRAIL_PUNCT)
            if name:
                return name
    return None


def _last_user_index(events: list) -> int:
    """Index of the LAST user-role event, or -1 if none — the ending
    turn is everything after it."""
    last = -1
    for i, ev in enumerate(events):
        msg = ev.get("message")
        if isinstance(msg, dict) and msg.get("role") == "user":
            last = i
    return last


def _final_assistant_text_chars(window: list) -> int:
    """Chars of every `text`-type block across every assistant-role
    event in the window — "the ending turn's final assistant text".

    Summed over the WHOLE window, not just the window's last event:
    a turn that calls a tool (SendMessage included) before its
    closing remarks splits the text and the tool_use across separate
    assistant events (the harness only fires Stop once an assistant
    event carries no pending tool_use, so a pure-tool_use event can
    never be the window's last one — but it CAN sit anywhere before
    it), and restricting the count to one event would silently
    undercount exactly the turns this lane exists to catch."""
    total = 0
    for ev in window:
        msg = ev.get("message")
        if not isinstance(msg, dict) or msg.get("role") != "assistant":
            continue
        content = msg.get("content", [])
        if not isinstance(content, list):
            continue
        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                total += len(str(block.get("text") or ""))
    return total


def _sent_to(window: list, name: str) -> bool:
    """True iff a `SendMessage` tool_use with `input.to == name`
    occurred within the window — a send to a DIFFERENT name does not
    satisfy the duty and must not relieve the fire."""
    for ev in window:
        msg = ev.get("message")
        if not isinstance(msg, dict) or msg.get("role") != "assistant":
            continue
        content = msg.get("content", [])
        if not isinstance(content, list):
            continue
        for block in content:
            if not isinstance(block, dict) or block.get("type") != "tool_use":
                continue
            if block.get("name") != "SendMessage":
                continue
            inp = block.get("input")
            if isinstance(inp, dict) and inp.get("to") == name:
                return True
    return False


def reason_text(name: str) -> str:
    return (
        f"This session received a peer handoff naming "
        f"REPORT-CHANNEL: SendMessage {name}. The turn just ending "
        f"composed substantial final text, but on the peer-handoff "
        f"lane final text reaches no one — it is not delivered to "
        f"{name}. Send the report NOW via SendMessage to {name} "
        f"before going idle; going idle without having sent it "
        f"counts as no report."
    )


def check(payload: dict) -> str | None:
    """The fire reason, or None (= stay silent)."""
    if payload.get("stop_hook_active"):
        return None
    transcript_path = payload.get("transcript_path")
    if not isinstance(transcript_path, str) or not transcript_path:
        return None
    events = _read_events(transcript_path)
    if events is None:
        return None
    name = captured_channel(events)
    if not name:
        return None
    window = events[_last_user_index(events) + 1:]
    if _final_assistant_text_chars(window) < _SUBSTANTIAL_CHARS:
        return None
    if _sent_to(window, name):
        return None
    return reason_text(name)


def output_json(context: str) -> str:
    """The Stop additionalContext emission (mirrors
    report-enforcer.output_json's SubagentStop shape, event name
    corrected to Stop — see module docstring on why this does not
    route through `_dispatch_common.fire()`)."""
    return json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "Stop",
            "additionalContext": context,
        }
    })


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0  # never fail the workflow on a hook parse error
    reason = check(payload)
    if reason is None:
        return 0
    mode = guard_mode(_SOURCE, default="warn")
    fire_log(_SOURCE, mode, reason, payload)
    if mode == "off":
        return 0
    context = (f"[{_SOURCE}] WARN (staging): {reason}" if mode == "warn"
               else f"[{_SOURCE}] {reason}")
    print(output_json(context))
    return 0


if __name__ == "__main__":
    if "--test" in sys.argv:
        import contextlib
        import io
        import tempfile
        from _dispatch_common import _reset_policy_cache

        os.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = "/nonexistent"
        _reset_policy_cache()

        def user(text):
            return {"message": {"role": "user", "content": text}}

        def asst_text(text):
            return {"message": {"role": "assistant",
                                "content": [{"type": "text", "text": text}]}}

        def asst_send(to, msg="hi"):
            return {"message": {"role": "assistant", "content": [
                {"type": "tool_use", "name": "SendMessage",
                 "input": {"to": to, "message": msg}}]}}

        long_text = "x" * _SUBSTANTIAL_CHARS
        short_text = "x" * (_SUBSTANTIAL_CHARS - 1)

        # ── captured_channel: marker extraction ─────────────────────
        marker_user = user("REPORT-CHANNEL: SendMessage team-lead\nrest")
        assert captured_channel([marker_user]) == "team-lead"
        marker_asst = asst_text("brief tail\nREPORT-CHANNEL: SendMessage "
                                "team-lead.\nmore")
        assert captured_channel([marker_asst]) == "team-lead"  # trailing "."
        assert captured_channel([user("no marker here")]) is None
        # case-sensitivity on the REPORT-CHANNEL: token
        assert captured_channel(
            [user("report-channel: SendMessage team-lead")]) is None
        # backtick-wrapped, as it appears in prose/markdown
        assert captured_channel(
            [user("`REPORT-CHANNEL: SendMessage team-lead`")]) == "team-lead"

        # ── the three arms (dispatcher's verifier §2) ────────────────
        # (i) marker + substantial final text + no send → fires
        arm1 = [marker_user, asst_text(long_text)]

        def run(events, payload_extra=None):
            with tempfile.NamedTemporaryFile(
                    "w", suffix=".jsonl", delete=False) as tf:
                for ev in events:
                    tf.write(json.dumps(ev) + "\n")
                path = tf.name
            try:
                p = {"transcript_path": path}
                if payload_extra:
                    p.update(payload_extra)
                return check(p)
            finally:
                os.unlink(path)

        assert run(arm1) is not None, "arm (i) must fire"
        assert "team-lead" in run(arm1)

        # (ii) marker + final text + send to captured name in the SAME
        # window → silent
        arm2 = [marker_user, asst_text(long_text), asst_send("team-lead")]
        assert run(arm2) is None, "arm (ii) must be silent"

        # a send to a DIFFERENT name does not satisfy the duty
        arm2b = [marker_user, asst_text(long_text), asst_send("someone-else")]
        assert run(arm2b) is not None, \
            "a send to a different name must not relieve the fire"

        # (iii) no marker at all, whatever the turn did → silent
        # (the false-fire control)
        arm3 = [user("ordinary work, no handoff"), asst_text(long_text)]
        assert run(arm3) is None, "arm (iii), the false-fire control"
        arm3b = [user("ordinary work"), asst_text(long_text),
                 asst_send("team-lead")]
        assert run(arm3b) is None, "no marker: still silent even with a send"

        # ── threshold pin: 399/401-style pair ────────────────────────
        assert run([marker_user, asst_text(short_text)]) is None, \
            f"{_SUBSTANTIAL_CHARS - 1} chars must not fire"
        assert run([marker_user, asst_text(long_text)]) is not None, \
            f"{_SUBSTANTIAL_CHARS} chars must fire"

        # ── window scoping: marker anywhere, but final-text and send
        # predicates are evaluated ONLY after the LAST user message ──
        # a send BEFORE the last user message does not count for the
        # NEW ending turn.
        arm_stale_send = [marker_user, asst_send("team-lead"),
                          user("a second round"), asst_text(long_text)]
        assert run(arm_stale_send) is not None, \
            "a send from a PRIOR turn must not relieve a new ending turn"
        # ...but a fresh send after the new last-user message does
        arm_fresh_send = [marker_user, asst_send("team-lead"),
                          user("a second round"), asst_text(long_text),
                          asst_send("team-lead")]
        assert run(arm_fresh_send) is None

        # ── stop_hook_active: loop-breaker, silent unconditionally ──
        assert run(arm1, {"stop_hook_active": True}) is None

        # ── fail-open: missing/empty/unreadable transcript_path ─────
        assert check({}) is None
        assert check({"transcript_path": ""}) is None
        assert check({"transcript_path": "/nonexistent/path.jsonl"}) is None

        # ── main(): unparseable stdin never blocks ───────────────────
        old_stdin = sys.stdin
        sys.stdin = io.StringIO("}{ not json")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = main()
        sys.stdin = old_stdin
        assert rc == 0 and buf.getvalue() == ""

        # ── main(): happy path emits Stop-shaped additionalContext,
        # default mode warn, staging-prefixed ──────────────────────
        with tempfile.NamedTemporaryFile(
                "w", suffix=".jsonl", delete=False) as tf:
            for ev in arm1:
                tf.write(json.dumps(ev) + "\n")
            path = tf.name
        try:
            sys.stdin = io.StringIO(json.dumps({"transcript_path": path}))
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                rc = main()
            sys.stdin = old_stdin
            assert rc == 0
            out = json.loads(buf.getvalue())
            assert out["hookSpecificOutput"]["hookEventName"] == "Stop"
            ctx = out["hookSpecificOutput"]["additionalContext"]
            assert "team-lead" in ctx
            assert "WARN (staging)" in ctx  # default mode is warn
        finally:
            os.unlink(path)

        # ── guard_mode staging: off → silent even though check() fires
        with tempfile.NamedTemporaryFile(
                "w", suffix=".json", delete=False) as cf:
            cf.write(json.dumps(
                {"guard_modes": {"handoff-report-gate": "off"}}))
            cfg = cf.name
        os.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = cfg
        _reset_policy_cache()
        with tempfile.NamedTemporaryFile(
                "w", suffix=".jsonl", delete=False) as tf:
            for ev in arm1:
                tf.write(json.dumps(ev) + "\n")
            path = tf.name
        try:
            sys.stdin = io.StringIO(json.dumps({"transcript_path": path}))
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                rc = main()
            sys.stdin = old_stdin
            assert rc == 0 and buf.getvalue() == "", \
                "off mode must stay silent"
        finally:
            os.unlink(path)
        os.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = "/nonexistent"
        _reset_policy_cache()

        print("handoff-report-gate: all tests passed")
        sys.exit(0)
    sys.exit(main())
