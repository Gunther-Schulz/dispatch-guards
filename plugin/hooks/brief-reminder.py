#!/usr/bin/env python3
"""PreToolUse(Agent|Task) reminder: brief-side counterpart to report-reminder.

Closes the §1 consumer gap (skill-craft review finding, 2026-07-19):
the brief form had no mechanical consumer at dispatch time — a
below-session-tier dispatch with an underspecified brief passed
silently (only fable dispatches force the permission dialog). One
line lands before the dispatch starts, reminding the dispatcher of
the §1 brief checks and the §2 report channel (dispatch-discipline.md).
The hook never judges the brief — judgment stays with the dispatcher.

Environment binding (as-of 2026-07-19): PreToolUse `additionalContext`
injection into the dispatching conversation — UNVERIFIED against a
live fire at mint time; first real dispatch confirms. Fail-open and
inert if the harness ignores it; --test covers the logic only
(bootstrap doctor tripwire).
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from _dispatch_common import policy  # noqa: E402


def reminder_text() -> str:
    doc = policy().get("discipline_doc")
    if doc:
        return (
            f"Dispatch starting — brief check ({doc} §1): "
            "decision-complete (assignments made, files listed not "
            "paraphrased, grounding section, write boundaries, commit "
            "convention verbatim, gaps-surface instruction)? Report "
            "channel per §2 named in the brief? Verifier dispatch → "
            "artifact + question ONLY."
        )
    return (
        "Dispatch starting — brief check: decision-complete (assignments "
        "made, files listed not paraphrased, grounding stated, write "
        "boundaries, gaps surfaced not filled)? Report channel named in "
        "the brief? Verifier dispatch → artifact + question ONLY."
    )


_CHANNEL_MARKERS = ("sendmessage", "send_message", "report channel",
                    "final text is the report")


def missing_channel(payload: dict) -> bool:
    """True iff this is a BACKGROUND Agent dispatch whose prompt names
    no report channel — the deliver-into-the-void class (JOURNAL
    2026-07-27, epsilon-probe: agent finished, reported as final text,
    reached no one). Background is the Agent tool's default, so only an
    explicit run_in_background=False exempts. Fail-open on any doubt."""
    if payload.get("tool_name") != "Agent":
        return False  # Task tool has its own return path
    tool_input = payload.get("tool_input") or {}
    if tool_input.get("run_in_background") is False:
        return False  # synchronous: final text IS the report
    prompt = (tool_input.get("prompt") or "").lower()
    if not prompt:
        return False
    return not any(m in prompt for m in _CHANNEL_MARKERS)


def deny_text() -> str:
    doc = policy().get("discipline_doc") or "dispatch-discipline.md"
    return (
        "Blocked: background dispatch without a report channel. A "
        "background agent's final text reaches no one — the brief "
        "must instruct delivery (paste the tail block's channel "
        f"line, {doc} §2: SendMessage to the dispatcher), or pass "
        "run_in_background: false for a synchronous dispatch. "
        "Fix the brief and retry."
    )


_TAIL_ANCHOR = "never bridged with a guess"
_SYNC_TAIL_MARKER = "final text is the report"
_BACKGROUND_TAIL_MARKER = "final text reaches no one"


def missing_tail(payload: dict) -> bool:
    """True iff an Agent dispatch's prompt lacks the pasted §2 tail
    block's anchor sentence ("never bridged with a guess") — the
    free-composed-brief-drops-the-invariant-tail class named in §2.
    Both dispatch modes (sync and background) require a pasted tail.
    Fail-open on any parse doubt."""
    if payload.get("tool_name") != "Agent":
        return False
    tool_input = payload.get("tool_input") or {}
    prompt = (tool_input.get("prompt") or "").lower()
    if not prompt:
        return False
    return _TAIL_ANCHOR not in prompt


def missing_tail_deny_text() -> str:
    doc = policy().get("discipline_doc") or "dispatch-discipline.md"
    return (
        "Blocked: dispatch brief without the pasted §2 tail block. "
        f"Paste the EXECUTION or READ-ONLY tail from {doc} §2 "
        "verbatim — pick the channel line matching the dispatch mode "
        "(background vs synchronous) — and retry."
    )


def tail_mode_mismatch(payload: dict) -> bool:
    """True iff the pasted tail's channel line contradicts
    run_in_background — the wrong tail variant pasted for the
    dispatch mode (§2: background → SendMessage/'reaches no one';
    synchronous → 'final text IS the report'). Fail-open on any parse
    doubt."""
    if payload.get("tool_name") != "Agent":
        return False
    tool_input = payload.get("tool_input") or {}
    prompt = (tool_input.get("prompt") or "").lower()
    if not prompt:
        return False
    is_background = tool_input.get("run_in_background") is not False
    if is_background:
        return _SYNC_TAIL_MARKER in prompt
    return _BACKGROUND_TAIL_MARKER in prompt


def tail_mode_mismatch_deny_text(payload: dict) -> str:
    doc = policy().get("discipline_doc") or "dispatch-discipline.md"
    tool_input = payload.get("tool_input") or {}
    is_background = tool_input.get("run_in_background") is not False
    if is_background:
        wrong = ('the synchronous channel line ("your final text IS '
                 'the report") was pasted into a background dispatch')
    else:
        wrong = ('the background channel line ("your final text '
                 'reaches no one") was pasted into a synchronous '
                 'dispatch (run_in_background: false)')
    return (
        "Blocked: tail channel line contradicts the dispatch mode — "
        f"{wrong}. Pick the channel line matching the actual mode "
        f"({doc} §2) and retry."
    )


def check(payload: dict) -> str | None:
    """Return the reminder, or None (= stay silent)."""
    if payload.get("tool_name") not in ("Agent", "Task"):
        return None
    return reminder_text()


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0  # never fail the workflow on a hook parse error
    if missing_channel(payload):
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
            },
            "systemMessage": deny_text(),
        }))
        return 0
    if missing_tail(payload):
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
            },
            "systemMessage": missing_tail_deny_text(),
        }))
        return 0
    if tail_mode_mismatch(payload):
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
            },
            "systemMessage": tail_mode_mismatch_deny_text(payload),
        }))
        return 0
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
        import tempfile
        from _dispatch_common import _reset_policy_cache
        os.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = "/nonexistent"
        _reset_policy_cache()
        assert check({"tool_name": "Agent"}) is not None
        assert check({"tool_name": "Task"}) is not None
        assert "brief check" in check({"tool_name": "Agent"})
        with tempfile.NamedTemporaryFile("w", suffix=".json",
                                         delete=False) as tf:
            tf.write('{"discipline_doc": "dispatch-discipline.md"}')
            os.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = tf.name
        _reset_policy_cache()
        assert "dispatch-discipline.md §1" in check({"tool_name": "Agent"})
        assert check({"tool_name": "Bash"}) is None
        assert check({}) is None
        # Channel gate: background + no channel → deny
        assert missing_channel({"tool_name": "Agent", "tool_input": {
            "prompt": "Go read files and report your findings."}})
        # Channel named (any marker) → allow
        assert not missing_channel({"tool_name": "Agent", "tool_input": {
            "prompt": "Do X. Deliver via SendMessage to main."}})
        assert not missing_channel({"tool_name": "Agent", "tool_input": {
            "prompt": "Do X.\nReport channel: your final text IS the "
                      "report."}})
        # Explicit synchronous → allow
        assert not missing_channel({"tool_name": "Agent", "tool_input": {
            "prompt": "Do X, answer inline.",
            "run_in_background": False}})
        # Task tool, empty prompt, non-dispatch tools → never deny
        assert not missing_channel({"tool_name": "Task", "tool_input": {
            "prompt": "no channel here"}})
        assert not missing_channel({"tool_name": "Agent", "tool_input": {}})
        assert not missing_channel({"tool_name": "Bash", "tool_input": {
            "command": "ls"}})
        assert "Blocked" in deny_text()

        # ── Tail-presence lane (missing_tail) ──────────────────────
        # Tails copied verbatim from dispatch-discipline.md §2 (cite:
        # dispatch-discipline.md §2) — literals here, never referenced
        # from the detection constants, so the test doesn't share
        # parentage with what it's meant to catch.
        EXECUTION_TAIL_BG = (
            "Closing report (mandatory; the project's own report form "
            "if it defines one, else the \xa72 form here — never "
            "both; \"none\" is a valid slot answer, silence is not): "
            "(a) items completed w/ evidence, (b) checks RUN w/ real "
            "output, (c) gaps surfaced — incl. anything needing a "
            "tier above yours, returned as a question with its "
            "evidence, never settled at your tier, (d) deviations w/ "
            "reason, (e) candidate lessons, (f) files touched + commit "
            "hashes (unpushed), (g) what was NOT verified, (h) sources "
            "actually read, of those the brief named.\n"
            "Report channel: SendMessage to the dispatcher — your "
            "final text reaches no one.\n"
            "Message ≤3000 chars: full detail goes to a FILE, the "
            "message carries key findings + the file path. A missing "
            "decision, file, or value is surfaced as a gap, never "
            "bridged with a guess.\n"
            "Commits unpushed, targeted `git add <paths>` never `-A`, "
            "trailer: `Co-Authored-By: Claude <model> "
            "<noreply@anthropic.com>`.\n"
            "After sending the report your write grant is over: a "
            "defect you find later is REPORTED, never edited or "
            "amended (source: \xa74 ownership rule)."
        )
        EXECUTION_TAIL_SYNC_LINE = EXECUTION_TAIL_BG.replace(
            "Report channel: SendMessage to the dispatcher — your "
            "final text reaches no one.",
            "Report channel: your final text IS the report.",
        )
        READONLY_TAIL_SYNC = (
            "Report channel: your final text IS the report.\n"
            "Return your findings in ONE message (verifier: verdict + "
            "basis; discovery: the N named facts, sources actually "
            "read). A missing decision, file, or value is surfaced as "
            "a gap, never bridged with a guess. No file writes, no "
            "interim messages."
        )
        READONLY_TAIL_BG_LINE = READONLY_TAIL_SYNC.replace(
            "Report channel: your final text IS the report.",
            "Report channel: SendMessage to the dispatcher — your "
            "final text reaches no one.",
        )

        # (i) tail-less Agent brief, both modes → missing_tail True
        assert missing_tail({"tool_name": "Agent", "tool_input": {
            "prompt": "Do X and report back."}})
        assert missing_tail({"tool_name": "Agent", "tool_input": {
            "prompt": "Do X and report back.",
            "run_in_background": False}})

        # (ii) each §2 tail verbatim, correct channel line for the
        # mode used → missing_tail False, tail_mode_mismatch False
        bg_brief = {"tool_name": "Agent", "tool_input": {
            "prompt": "Do X.\n" + EXECUTION_TAIL_BG}}
        assert not missing_tail(bg_brief)
        assert not tail_mode_mismatch(bg_brief)
        sync_brief = {"tool_name": "Agent", "tool_input": {
            "prompt": "Do X.\n" + READONLY_TAIL_SYNC,
            "run_in_background": False}}
        assert not missing_tail(sync_brief)
        assert not tail_mode_mismatch(sync_brief)

        # (iii) wrong channel line for the mode → tail_mode_mismatch
        # True, both directions
        bg_with_sync_line = {"tool_name": "Agent", "tool_input": {
            "prompt": "Do X.\n" + EXECUTION_TAIL_SYNC_LINE}}
        assert not missing_tail(bg_with_sync_line)  # tail present
        assert tail_mode_mismatch(bg_with_sync_line)
        sync_with_bg_line = {"tool_name": "Agent", "tool_input": {
            "prompt": "Do X.\n" + READONLY_TAIL_BG_LINE,
            "run_in_background": False}}
        assert not missing_tail(sync_with_bg_line)  # tail present
        assert tail_mode_mismatch(sync_with_bg_line)

        # (iv) matched mode+line → False (covered by (ii) above;
        # explicit restatement for the background-default case)
        assert not tail_mode_mismatch(bg_brief)

        # (v) Task tool and parse-garbage payloads → never deny
        assert not missing_tail({"tool_name": "Task", "tool_input": {
            "prompt": "no tail here"}})
        assert not missing_tail({"tool_name": "Agent", "tool_input": {}})
        assert not missing_tail({"tool_name": "Bash", "tool_input": {
            "command": "ls"}})
        assert not missing_tail({})
        assert not tail_mode_mismatch({"tool_name": "Task",
                                        "tool_input": {"prompt": "x"}})
        assert not tail_mode_mismatch({"tool_name": "Agent",
                                        "tool_input": {}})
        assert not tail_mode_mismatch({})

        assert "Blocked" in missing_tail_deny_text()
        assert "Blocked" in tail_mode_mismatch_deny_text(bg_with_sync_line)

        print("brief-reminder: all tests passed")
        sys.exit(0)
    sys.exit(main())
