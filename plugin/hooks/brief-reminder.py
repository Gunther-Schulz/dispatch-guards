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
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from _dispatch_common import deny, policy  # noqa: E402

_SOURCE = "dispatch-guards/brief-reminder"


def _norm(text: str) -> str:
    """Lowercase and collapse all whitespace runs to single spaces.

    Every marker/anchor below is matched against THIS form. Basis
    (live false-fire 2026-07-30): the §2 tails carry hard line wraps
    in dispatch-discipline.md itself, so a tail pasted verbatim —
    exactly what the deny text instructs — arrived as "never
    bridged\\nwith a guess" and failed the single-line anchor."""
    return re.sub(r"\s+", " ", text.lower())


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
    prompt = _norm(tool_input.get("prompt") or "")
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

# The BRIEF is prompt + any brief files the prompt names (DD §2: the
# tail reaches the executing agent inline OR in a referenced brief
# file; inline is required only when no file brief exists). The
# channel lanes above stay prompt-only by design — the channel line
# is bound to run_in_background, decided at the call site, which a
# static file cannot know.
#
# Two alternatives, because a brief names a path in two forms and both
# occur here: QUOTED (the only form that can carry spaces) and bare.
# Neither may be restricted to ASCII — project trees carry directories
# like "Planungsbüro …", and a character class that stops at the umlaut
# does not fail loudly: it yields a TRUNCATED path, which resolves to
# nothing and is indistinguishable from a brief file carrying no tail.
_MD_PATH_RE = re.compile(
    r"""["']([^"'`\n]*\.md)["']"""
    r"""|((?:~/|/|[^\s"'`()\[\]]*/)[^\s"'`()\[\]]*\.md)\b""")
_MAX_REFERENCED_FILES = 8
_MAX_FILE_BYTES = 262144


def _md_paths(text: str) -> list[str]:
    """Every .md path the text names, quoted span or bare token."""
    return [m.group(1) if m.group(1) is not None else m.group(2)
            for m in _MD_PATH_RE.finditer(text)]


def _referenced_md_texts(payload: dict) -> list[str]:
    """Contents of .md files the prompt references, best-effort.

    Relative paths resolve against the hook input's cwd. Unreadable,
    oversized, or missing files contribute nothing — only verified
    content counts toward the tail/section checks (naming a file is
    not evidence its tail exists)."""
    tool_input = payload.get("tool_input") or {}
    prompt = tool_input.get("prompt") or ""
    cwd = payload.get("cwd") or ""
    texts: list[str] = []
    for match in _md_paths(prompt)[:_MAX_REFERENCED_FILES]:
        path = os.path.expanduser(match)
        if not os.path.isabs(path):
            if not cwd:
                continue
            path = os.path.join(cwd, path)
        path = os.path.normpath(path)
        try:
            if os.path.getsize(path) > _MAX_FILE_BYTES:
                continue
            with open(path, encoding="utf-8", errors="replace") as f:
                texts.append(f.read())
        except OSError:
            continue
    return texts


def missing_tail(payload: dict) -> bool:
    """True iff an Agent dispatch's BRIEF — prompt plus any referenced
    brief files — lacks the §2 tail block's anchor sentence ("never
    bridged with a guess"): the free-composed-brief-drops-the-
    invariant-tail class named in §2. Inline tail required only when
    the prompt names no tail-bearing brief file. Fail-open on any
    parse doubt."""
    if payload.get("tool_name") != "Agent":
        return False
    tool_input = payload.get("tool_input") or {}
    prompt = _norm(tool_input.get("prompt") or "")
    if not prompt:
        return False
    if _TAIL_ANCHOR in prompt:
        return False
    return not any(_TAIL_ANCHOR in _norm(t)
                   for t in _referenced_md_texts(payload))


def missing_tail_deny_text() -> str:
    doc = policy().get("discipline_doc") or "dispatch-discipline.md"
    return (
        "Blocked: dispatch brief without the §2 tail block. Paste the "
        f"EXECUTION or READ-ONLY tail from {doc} §2 into the prompt — "
        "pick the channel line matching the dispatch mode (background "
        "vs synchronous) — or point the prompt at a brief FILE that "
        "carries the tail, and retry."
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
    prompt = _norm(tool_input.get("prompt") or "")
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


_SECTIONS_ANCHOR = "closing report (mandatory"
# Marker-Familien statt Einzel-Literale: Haus-Briefe folgen dem
# DEV-RUNBOOK-Formular mit deutschen Feld-Etiketten (GROUNDING-BASIS,
# SCHREIB-GRENZEN) — die Erkennung akzeptiert die Abschnitts-Etiketten
# beider Sprachen; ein Treffer je Familie genügt.
_GROUNDING_MARKERS = ("grounding", "grounding-basis")
_WRITE_BOUNDARY_MARKERS = ("write boundar", "schreib-grenzen",
                           "schreibgrenzen")


def missing_sections(payload: dict) -> bool:
    """True iff an Agent dispatch's prompt carries the EXECUTION tail
    (identified by its "closing report (mandatory" signature, present
    only in the execution tail and absent from the READ-ONLY tail) but
    lacks one or both §1 mandatory execution-brief sections: a
    grounding-basis section and a write-boundaries section. An
    execution brief per dispatch-discipline.md §1 always carries a
    grounding-basis section (what to read before building) and a
    write-boundaries section (paths owned); verifier/discovery briefs
    take the READ-ONLY tail and are exempt by that tail's absence of
    the anchor. Reads the BRIEF — prompt plus referenced brief files
    (see _referenced_md_texts). Fail-open on any parse doubt."""
    if payload.get("tool_name") != "Agent":
        return False
    tool_input = payload.get("tool_input") or {}
    if not (tool_input.get("prompt") or ""):
        return False
    brief = _brief_text(payload)
    if _SECTIONS_ANCHOR not in brief:
        return False  # not an execution-tail brief; exempt
    return not (any(m in brief for m in _GROUNDING_MARKERS)
                and any(m in brief for m in _WRITE_BOUNDARY_MARKERS))


def _brief_text(payload: dict) -> str:
    """The whole normalized brief: prompt + referenced brief files."""
    tool_input = payload.get("tool_input") or {}
    parts = [tool_input.get("prompt") or ""]
    parts += _referenced_md_texts(payload)
    return _norm(" ".join(parts))


def missing_sections_deny_text(payload: dict) -> str:
    doc = policy().get("discipline_doc") or "dispatch-discipline.md"
    prompt = _brief_text(payload)
    missing = []
    if not any(m in prompt for m in _GROUNDING_MARKERS):
        missing.append("a grounding-basis section (label "
                       "'Grounding' or 'GROUNDING-BASIS')")
    if not any(m in prompt for m in _WRITE_BOUNDARY_MARKERS):
        missing.append("a write-boundaries section (label "
                       "'Write boundaries' or 'SCHREIB-GRENZEN')")
    missing_text = " and ".join(missing)
    return (
        f"Blocked: execution brief missing mandatory {doc} §1 "
        f"section(s) — {missing_text}. An execution brief always "
        "carries a grounding-basis section (what to read before "
        "building) and a write-boundaries section (paths owned, "
        "targeted git add). Add the missing section(s) to the brief "
        "and retry."
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
    # deny() emits BOTH permissionDecisionReason (reaches the model)
    # and systemMessage (reaches the user), source-tagged. Basis
    # (2026-07-30): a deny carrying only systemMessage left the model
    # with the harness's bare "Hook PreToolUse:Agent denied this tool",
    # which two sessions misattributed to a Claude Code permission bug.
    if missing_channel(payload):
        deny(deny_text(), source=_SOURCE)
    if missing_tail(payload):
        deny(missing_tail_deny_text(), source=_SOURCE)
    if tail_mode_mismatch(payload):
        deny(tail_mode_mismatch_deny_text(payload), source=_SOURCE)
    if missing_sections(payload):
        deny(missing_sections_deny_text(payload), source=_SOURCE)
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

        # ── Section lane (missing_sections) ────────────────────────
        # Section markers named in dispatch-discipline.md §1 ("Grounding
        # basis as a mandatory section." / "Write boundaries.") —
        # literals here, never the detection constants, so the test
        # doesn't share parentage with what it's meant to catch.
        GROUNDING_SECTION = (
            "Grounding basis: read spec.md and the current module "
            "before building.")
        WRITE_BOUNDARIES_SECTION = (
            "Write boundaries: you own src/foo.py only; targeted git "
            "add, never -A.")

        # (i) execution-tail brief carrying both markers → False
        both_sections_brief = {"tool_name": "Agent", "tool_input": {
            "prompt": "Do X.\n" + GROUNDING_SECTION + "\n"
                      + WRITE_BOUNDARIES_SECTION + "\n"
                      + EXECUTION_TAIL_BG}}
        assert not missing_sections(both_sections_brief)

        # (ii) execution-tail brief missing "grounding" → True
        missing_grounding_brief = {"tool_name": "Agent", "tool_input": {
            "prompt": "Do X.\n" + WRITE_BOUNDARIES_SECTION + "\n"
                      + EXECUTION_TAIL_BG}}
        assert missing_sections(missing_grounding_brief)

        # (iii) execution-tail brief missing only "write boundar" → True
        missing_write_boundaries_brief = {
            "tool_name": "Agent", "tool_input": {
                "prompt": "Do X.\n" + GROUNDING_SECTION + "\n"
                          + EXECUTION_TAIL_BG}}
        assert missing_sections(missing_write_boundaries_brief)

        # (iii-b) deutsche Abschnitts-Etiketten (DEV-RUNBOOK-Formular:
        # GROUNDING-BASIS / SCHREIB-GRENZEN) → False — Literale, nie
        # die Erkennungs-Konstanten (keine geteilte Elternschaft)
        german_sections_brief = {"tool_name": "Agent", "tool_input": {
            "prompt": "Baue X.\n"
                      "GROUNDING-BASIS: lies spec.md vor dem Bau.\n"
                      "SCHREIB-GRENZEN: nur src/foo.py; gezieltes "
                      "git add, nie -A.\n" + EXECUTION_TAIL_BG}}
        assert not missing_sections(german_sections_brief)

        # (iv) READ-ONLY-tail brief with neither marker → False (exempt:
        # no execution-tail anchor present)
        readonly_neither_brief = {"tool_name": "Agent", "tool_input": {
            "prompt": "Do X.\n" + READONLY_TAIL_SYNC,
            "run_in_background": False}}
        assert not missing_sections(readonly_neither_brief)

        # (v) Task tool and parse-garbage payloads → never deny
        assert not missing_sections({"tool_name": "Task", "tool_input": {
            "prompt": "Do X.\n" + WRITE_BOUNDARIES_SECTION + "\n"
                      + EXECUTION_TAIL_BG}})
        assert not missing_sections({"tool_name": "Agent",
                                      "tool_input": {}})
        assert not missing_sections({"tool_name": "Bash", "tool_input": {
            "command": "ls"}})
        assert not missing_sections({})

        assert "Blocked" in missing_sections_deny_text(
            missing_grounding_brief)

        # ── Whitespace-normalization lane (false-fire 2026-07-30) ──
        # The §2 tails carry hard line wraps in dispatch-discipline.md
        # itself; a verbatim paste therefore wraps mid-anchor ("never
        # bridged\nwith a guess"). Replayed live deny: hookinput-probe3,
        # session 78b3e7fe (guard 0.1.7 went red on a conforming brief).
        WRAPPED_READONLY_TAIL = (
            "Report channel: your final text IS the report.\n"
            "Return your findings in ONE message (verifier: verdict + "
            "basis;\ndiscovery: the N named facts, sources actually "
            "read). A missing\ndecision, file, or value is surfaced as "
            "a gap, never bridged\nwith a guess. No file writes, no "
            "interim messages."
        )
        wrapped_sync_brief = {"tool_name": "Agent", "tool_input": {
            "prompt": "Do X.\n" + WRAPPED_READONLY_TAIL,
            "run_in_background": False}}
        assert not missing_tail(wrapped_sync_brief)
        assert not tail_mode_mismatch(wrapped_sync_brief)
        # Channel line wrapped mid-marker ("Report\nchannel") still counts
        assert not missing_channel({"tool_name": "Agent", "tool_input": {
            "prompt": "Do X. Report\nchannel: SendMessage to the "
                      "dispatcher — your final text reaches no one.\n"
                      "A missing decision, file, or value is surfaced "
                      "as a gap, never\nbridged with a guess."}})
        # Section markers wrapped ("write\nboundaries") still count
        wrapped_sections_brief = {"tool_name": "Agent", "tool_input": {
            "prompt": "Do X.\nGrounding basis: read spec.md first.\n"
                      "Write\nboundaries: you own src/foo.py only.\n"
                      + EXECUTION_TAIL_BG}}
        assert not missing_sections(wrapped_sections_brief)

        # ── File-carried briefs (DD §2: inline tail required only ──
        # when no file brief) — the wave-2 false-positive class:
        # four dispatches pointing at a tail-bearing brief file were
        # denied as tail-less (2026-07-30, sessions 633915a8/78b3e7fe).
        import tempfile as _tf
        _tmpdir = _tf.mkdtemp()
        _brief_with_tail = os.path.join(_tmpdir, "brief-with-tail.md")
        with open(_brief_with_tail, "w") as f:
            f.write("# Brief\nGrounding basis: read spec.md first.\n"
                    "Write boundaries: you own src/foo.py only.\n"
                    + EXECUTION_TAIL_BG)
        _brief_no_tail = os.path.join(_tmpdir, "brief-no-tail.md")
        with open(_brief_no_tail, "w") as f:
            f.write("# Brief\nDo the thing, no tail here.\n")

        _file_prompt = ("Execute the brief at " + _brief_with_tail
                        + " — read it top to bottom first.\n"
                        "Report channel: SendMessage to the dispatcher "
                        "— your final text reaches no one.")
        file_brief = {"tool_name": "Agent",
                      "tool_input": {"prompt": _file_prompt}}
        # (i) tail + sections live in the referenced file → allow
        assert not missing_tail(file_brief)
        assert not missing_sections(file_brief)
        # (ii) referenced file lacks the tail → still deny
        assert missing_tail({"tool_name": "Agent", "tool_input": {
            "prompt": "Execute the brief at " + _brief_no_tail
                      + "\nReport channel: SendMessage to the "
                      "dispatcher — your final text reaches no one."}})
        # (iii) nonexistent file contributes nothing → deny
        assert missing_tail({"tool_name": "Agent", "tool_input": {
            "prompt": "Execute " + os.path.join(_tmpdir, "gone.md")
                      + "\nReport channel: SendMessage to the "
                      "dispatcher — your final text reaches no one."}})
        # (iv) relative path resolves against hook-input cwd
        assert not missing_tail({"tool_name": "Agent",
                                 "cwd": _tmpdir,
                                 "tool_input": {"prompt":
            "Execute the brief at docs/../brief-with-tail.md\n"
            "Report channel: SendMessage to the dispatcher — your "
            "final text reaches no one."}})
        # (v) execution tail in file but sections missing → sections
        # lane still fires on the combined brief
        _brief_tail_only = os.path.join(_tmpdir, "brief-tail-only.md")
        with open(_brief_tail_only, "w") as f:
            f.write("# Brief\n" + EXECUTION_TAIL_BG)
        assert missing_sections({"tool_name": "Agent", "tool_input": {
            "prompt": "Execute the brief at " + _brief_tail_only
                      + "\nReport channel: SendMessage to the "
                      "dispatcher — your final text reaches no one."}})

        # ── Brief paths with spaces and non-ASCII letters ───────────
        # Expectation derived from the rule, never from this hook's
        # behavior — dispatch-discipline.md §2: "The tail reaches the
        # executing agent pasted in the DISPATCH PROMPT or inside a
        # brief FILE the prompt names — inline required only when no
        # file brief exists." A prompt naming a tail-bearing brief file
        # is therefore CONFORMING whatever characters its path carries,
        # so the tail and section lanes must stay silent on it.
        _umlaut_dir = os.path.join(_tmpdir, "Planungsbüro-Test")
        os.makedirs(_umlaut_dir, exist_ok=True)
        _umlaut_brief = os.path.join(_umlaut_dir, "brief.md")
        _spaced_dir = os.path.join(_tmpdir, "Planungsbüro Projekte")
        os.makedirs(_spaced_dir, exist_ok=True)
        _spaced_brief = os.path.join(_spaced_dir, "mein brief.md")
        for _p in (_umlaut_brief, _spaced_brief):
            with open(_p, "w") as f:
                f.write("# Brief\nGrounding basis: read spec.md first.\n"
                        "Write boundaries: you own src/foo.py only.\n"
                        + EXECUTION_TAIL_BG)
        _channel = ("\nReport channel: SendMessage to the dispatcher "
                    "— your final text reaches no one.")

        # (i) bare path through an umlaut directory
        umlaut_brief_call = {"tool_name": "Agent", "tool_input": {
            "prompt": "Execute the brief at " + _umlaut_brief + _channel}}
        assert not missing_tail(umlaut_brief_call)
        assert not missing_sections(umlaut_brief_call)

        # (ii) quoted path carrying both a space and an umlaut, either
        # quote style — a path with a space has no unquoted form
        for _q in ('"', "'"):
            spaced_brief_call = {"tool_name": "Agent", "tool_input": {
                "prompt": "Execute the brief at " + _q + _spaced_brief
                          + _q + _channel}}
            assert not missing_tail(spaced_brief_call)
            assert not missing_sections(spaced_brief_call)

        # (ii-b) the sections lane reads the same file: a tail-only
        # brief under an umlaut path must still be caught for its
        # missing sections. Asserted in this direction because the
        # conforming case above passes for either reason — an unread
        # file leaves the brief without the execution-tail anchor,
        # which exempts the lane instead of clearing it.
        _umlaut_tail_only = os.path.join(_umlaut_dir, "nur-tail.md")
        with open(_umlaut_tail_only, "w") as f:
            f.write("# Brief\n" + EXECUTION_TAIL_BG)
        assert missing_sections({"tool_name": "Agent", "tool_input": {
            "prompt": "Execute " + _umlaut_tail_only + _channel}})

        # (iii) the extracted path is the WHOLE path: a class that
        # breaks at the first non-ASCII letter does not miss the
        # reference, it returns a different, shorter one that resolves
        # elsewhere — the failure the lanes above cannot see.
        assert _md_paths("siehe " + _umlaut_brief) == [_umlaut_brief]
        assert _md_paths('siehe "' + _spaced_brief + '"') == [_spaced_brief]
        assert _md_paths("siehe '" + _spaced_brief + "'") == [_spaced_brief]
        # (iv) a bare filename is not a path reference (unchanged):
        # the token must carry a separator or start at ~/ or /
        assert _md_paths("do X, see brief.md") == []
        assert _md_paths("read ~/notes/brief.md") == ["~/notes/brief.md"]
        # (v) a named-but-absent umlaut file still contributes nothing
        assert missing_tail({"tool_name": "Agent", "tool_input": {
            "prompt": "Execute " + os.path.join(_umlaut_dir, "weg.md")
                      + _channel}})

        # ── Deny payload shape (misattribution class 2026-07-30) ────
        # Both audiences must get the reason: permissionDecisionReason
        # reaches the model, systemMessage the user; source tag makes a
        # guard fire self-identifying. Live defect: fresh-session deny
        # (session 3741ed60) carried systemMessage only — the model saw
        # the harness's bare denial line and misattributed it to CC.
        from _dispatch_common import _deny_payload
        dp = _deny_payload("Blocked: test reason", source=_SOURCE)
        hso = dp["hookSpecificOutput"]
        assert hso["permissionDecision"] == "deny"
        assert hso["permissionDecisionReason"].startswith(
            "[dispatch-guards/brief-reminder] ")
        assert "Blocked: test reason" in hso["permissionDecisionReason"]
        assert dp["systemMessage"] == hso["permissionDecisionReason"]

        print("brief-reminder: all tests passed")
        sys.exit(0)
    sys.exit(main())
