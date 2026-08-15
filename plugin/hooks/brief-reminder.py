#!/usr/bin/env python3
"""PreToolUse(Agent|Task) reminder: brief-side counterpart to report-reminder.

Closes the §1 consumer gap (skill-craft review finding, 2026-07-19):
the brief form had no mechanical consumer at dispatch time — a
below-session-tier dispatch with an underspecified brief passed
silently (only fable dispatches force the permission dialog). One
line lands before the dispatch starts, reminding the dispatcher of
the §1 brief checks and the §2 report channel (dispatch skill,
this plugin: skills/dispatch/SKILL.md + references/forms.md).
The hook never judges the brief — judgment stays with the
dispatcher: it reminds on the judgment half and DENIES on the
computable slice of §§1-2. The enforced subset is THIS hook's,
version-stamped with the plugin — the skill deliberately does not
enumerate it. Deny-repair and relief-valve rules: SKILL.md §5
(general form for every guard; source label, not restated here).

Environment binding (as-of 2026-08-05): PreToolUse
`additionalContext` injection into the dispatching conversation —
CONFIRMED live, reminder line visible before each spawn (unverified
only at mint time 2026-07-19). Fail-open and
inert if the harness ignores it; --test covers the logic only
(bootstrap doctor tripwire).
"""
from __future__ import annotations

import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from _dispatch_common import deny, fire, policy  # noqa: E402

_SOURCE = "dispatch-guards/brief-reminder"


def _forms_path() -> str:
    """The dispatch skill's forms reference (§2 tails + §3 roadmap),
    resolved relative to this hook — valid in the source repo and in
    the installed plugin cache alike. Denies point HERE so a bounce
    carries the exact file the fix is pasted from."""
    return os.path.normpath(os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "..", "skills", "dispatch", "references", "forms.md"))


def _norm(text: str) -> str:
    """Lowercase and collapse all whitespace runs to single spaces.

    Every marker/anchor below is matched against THIS form. Basis
    (live false-fire 2026-07-30): the §2 tails carry hard line wraps
    in their source file (now references/forms.md), so a tail pasted
    verbatim — exactly what the deny text instructs — arrived as
    "never bridged\\nwith a guess" and failed the single-line
    anchor."""
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


def mailbox_lane(tool_input: dict) -> bool:
    """True iff this dispatch lands in the MAILBOX lane, where the
    agent's final text reaches no one and only SendMessage delivers.

    `name` alone decides the lane (forms.md §2, binding as of
    2026-08-15, harness 2.1.232, controlled probe matrix): a NAMED
    dispatch — generic or pinned type alike — spawns as a mailbox
    teammate ("Spawned successfully … via mailbox"), promises no
    completion notification, and does not appear in the subagent
    listing. An UNNAMED dispatch launches as a background task
    ("Async agent launched") whose completion task-notification
    carries the agent's final text to the dispatcher VERBATIM —
    observed from an agent that called no tool at all, so that
    delivery does not depend on the agent cooperating.

    Supersedes the run_in_background predicate: the Agent tool takes
    no such parameter (schema `additionalProperties: false`, key
    absent), so the old `.get("run_in_background") is not False` was
    CONSTANT TRUE. That classified every dispatch as background,
    which made the unnamed lane's correct channel line unreachable
    and had tail_mode_mismatch deny it — the guard manufacturing the
    defect it exists to prevent, the same shape the 2026-08-07 lane
    repair closed for named sync-flagged dispatches.

    One predicate for both call sites below, so the two lanes cannot
    disagree about which channel line a dispatch owes."""
    return bool(tool_input.get("name"))


def missing_channel(payload: dict) -> bool:
    """True iff this is a MAILBOX-lane Agent dispatch whose prompt
    names no report channel — the deliver-into-the-void class (JOURNAL
    2026-07-27, epsilon-probe: agent finished, reported as final text,
    reached no one). The lane is decided by mailbox_lane() above:
    a `name` is present. Fail-open on any doubt."""
    if payload.get("tool_name") != "Agent":
        return False  # Task tool has its own return path
    tool_input = payload.get("tool_input") or {}
    if not mailbox_lane(tool_input):
        return False  # background task: final text IS delivered
    prompt = _norm(tool_input.get("prompt") or "")
    if not prompt:
        return False
    return not any(m in prompt for m in _CHANNEL_MARKERS)


def deny_text(payload: dict) -> str:
    """Deny text for missing_channel — it must name a repair that
    clears on retry. missing_channel fires on the MAILBOX lane only,
    which is exactly the named case, so there is one repair: paste
    the mailbox channel line. The other exit — dropping the name —
    changes the lane, so it is named too, with the gate that limits
    it. The superseded text offered `run_in_background: false`, a
    parameter the Agent tool does not accept: a repair that could
    never clear on retry."""
    return (
        "Blocked: mailbox-lane dispatch without a report channel. "
        "This dispatch is NAMED, and a name puts it in the mailbox "
        "lane — no completion notification fires for it, so its "
        "final text reaches no one. The brief must instruct "
        "delivery: paste the tail block's mailbox channel line from "
        f"{_forms_path()} §2 (SendMessage to the dispatcher — your "
        "final text reaches no one). Dropping the `name` instead "
        "moves the dispatch to the background-task lane, whose "
        "completion notification does deliver the final text — but "
        "the model gate mandates a name on every generic dispatch, "
        "so that exit is open to pinned types only. Fix the brief "
        "and retry."
    )


_TAIL_ANCHOR = "never bridged with a guess"
# Lane markers, named for the DELIVERY each asserts rather than for a
# launch mode: the unnamed lane's notification delivers the final
# text, the mailbox lane's does not exist.
_DELIVERED_TAIL_MARKER = "final text is the report"
_MAILBOX_TAIL_MARKER = "final text reaches no one"

# The BRIEF is prompt + any brief files the prompt names (forms.md
# §2: the tail reaches the executing agent inline OR in a referenced
# brief file; inline is required only when no file brief exists). The
# channel lanes above stay prompt-only by design — the channel line
# is bound to `name`, decided at the call site, which a static file
# cannot know.
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
    return (
        "Blocked: dispatch brief without the §2 tail block. Paste the "
        f"EXECUTION or READ-ONLY tail verbatim from {_forms_path()} "
        "into the prompt — "
        "pick the channel line matching the dispatch mode (background "
        "vs synchronous) — or point the prompt at a brief FILE that "
        "carries the tail, and retry."
    )


def tail_mode_mismatch(payload: dict) -> bool:
    """True iff the pasted tail's channel line contradicts the
    dispatch's LANE — the wrong tail variant for the lane `name`
    selects (§2: named/mailbox → SendMessage/'reaches no one';
    unnamed/background task → 'final text IS the report'). Fail-open
    on any parse doubt."""
    if payload.get("tool_name") != "Agent":
        return False
    tool_input = payload.get("tool_input") or {}
    prompt = _norm(tool_input.get("prompt") or "")
    if not prompt:
        return False
    if mailbox_lane(tool_input):
        return _DELIVERED_TAIL_MARKER in prompt
    return _MAILBOX_TAIL_MARKER in prompt


def tail_mode_mismatch_deny_text(payload: dict) -> str:
    doc = policy().get("discipline_doc") or "the dispatch skill"
    tool_input = payload.get("tool_input") or {}
    if mailbox_lane(tool_input):
        wrong = ('the background-task channel line ("your final text '
                 'IS the report") was pasted into a NAMED dispatch, '
                 'which runs in the mailbox lane — no completion '
                 'notification fires, so that final text reaches no '
                 'one')
    else:
        wrong = ('the mailbox channel line ("your final text reaches '
                 'no one") was pasted into an UNNAMED dispatch, whose '
                 'completion notification does deliver the final text')
    return (
        "Blocked: tail channel line contradicts the dispatch lane — "
        f"{wrong}. The lane is set by `name` alone. Pick the channel "
        f"line matching it ({doc} §2) and retry."
    )


_SECTIONS_ANCHOR = "closing report (mandatory"
# The READ-ONLY tail's own signature. Needed because forms.md carries
# BOTH tails verbatim, and the brief text this guard reads includes
# every .md file the prompt names: a verifier brief whose only offence
# is CITING forms.md — which §1 tells verifier briefs to cite — picked
# up the execution anchor from the citation and was denied for lacking
# §1 execution sections it is explicitly exempt from. Observed live on
# a legitimate verifier dispatch.
_READONLY_ANCHOR = "no repo writes, no report files"
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
    execution brief per the dispatch skill §1 always carries a
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
    if _tail_kind(payload) != "execution":
        return False  # verifier/discovery or no tail; exempt
    brief = _brief_text(payload)
    return not (any(m in brief for m in _GROUNDING_MARKERS)
                and any(m in brief for m in _WRITE_BOUNDARY_MARKERS))


def _tail_kind(payload: dict) -> str:
    """Which §2 tail governs this dispatch: 'execution' | 'readonly' |
    'none'.

    Decided from the PROMPT wherever the prompt itself carries a tail,
    and only otherwise from the referenced brief files. Prompt-first is
    the whole point: forms.md contains both tails verbatim, so reading
    the referenced files first makes every brief that cites the forms
    file look like an execution brief — the false fire this exemption
    closes. A brief file may still carry the tail (§2 allows it), which
    is why the referenced-file fallback stays."""
    tool_input = payload.get("tool_input") or {}
    prompt = _norm(tool_input.get("prompt") or "")
    for text in (prompt, _brief_text(payload)):
        if _READONLY_ANCHOR in text:
            return "readonly"
        if _SECTIONS_ANCHOR in text:
            return "execution"
    return "none"


def _brief_text(payload: dict) -> str:
    """The whole normalized brief: prompt + referenced brief files."""
    tool_input = payload.get("tool_input") or {}
    parts = [tool_input.get("prompt") or ""]
    parts += _referenced_md_texts(payload)
    return _norm(" ".join(parts))


def missing_sections_deny_text(payload: dict) -> str:
    doc = policy().get("discipline_doc") or "the dispatch skill"
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


# The §1 skeleton's `## Commit plan` heading. Two spellings, both
# normalized: `_norm` collapses the hard wrap in a pasted skeleton
# ("Commit\nplan") to the spaced form.
_COMMIT_PLAN_MARKERS = ("commit plan", "commit-plan")


def missing_commit_plan(payload: dict) -> bool:
    """True iff an execution-tail Agent brief carries no commit-plan
    section — the §1 skeleton slot where the dispatcher states the
    target repo's commit-blocking guards, read at compose time, and
    where the bump or ordering commit sits.

    Scope is exactly missing_sections' above: Agent tool, execution
    tail present, brief = prompt plus referenced brief files. What
    this establishes is PRESENCE OF THE LABEL and nothing more — a
    plan naming the wrong guard reads identical to a correct one
    here, so this lane grades composition, never the plan. Staged: it
    ships WARN and earns deny only through the fire-rate review
    (repo CLAUDE.md), never by assertion. Fail-open on parse doubt."""
    if payload.get("tool_name") != "Agent":
        return False
    tool_input = payload.get("tool_input") or {}
    if not (tool_input.get("prompt") or ""):
        return False
    brief = _brief_text(payload)
    if _SECTIONS_ANCHOR not in brief:
        return False  # not an execution-tail brief; exempt
    return not any(m in brief for m in _COMMIT_PLAN_MARKERS)


def missing_commit_plan_warn_text() -> str:
    doc = policy().get("discipline_doc") or "the dispatch skill"
    return (
        f"Execution brief without a commit-plan section ({doc} §1 "
        "skeleton, '## Commit plan'). State the target repo's "
        "commit-blocking guards READ at compose time and where the "
        "bump or ordering commit sits: a payload-version guard "
        "comparing against the RELEASE state clears every later "
        "same-batch commit once the bump is in, so bump-first turns "
        "one shared gate into zero bounces for every writer behind "
        "it — where its basis is the origin manifest, push at "
        "integration only, and a plugin-payload brief names who "
        "bumps the manifest. 'none' (no such guard) is a valid "
        "filling; silence is not."
    )


def check(payload: dict) -> str | None:
    """Return the reminder, or None (= stay silent)."""
    if payload.get("tool_name") not in ("Agent", "Task"):
        return None
    return reminder_text()


def worktree_advisory_text() -> str:
    return (
        "Worktree isolation — base advisory: harness-cut worktrees have "
        "come from a snapshot OLDER than local HEAD (observed twice "
        "2026-08-05, both cuts == origin/main while local main was "
        "ahead; mechanism unverified). Three classes: (1) SESSION-repo "
        "worktree cut stale — the brief must STATE the base commit and "
        "carry the §1 sanctioned recovery (ff-only to that base over a "
        "clean tree), else the executor halts on a guard doing its job; "
        "(2) a brief naming a SIBLING repo — isolation cuts the session "
        "repo regardless, so provision the working copy yourself and "
        "name its path in the brief; (3) a sibling-repo brief run UNDER "
        "isolation — the unused session worktree can be auto-reclaimed "
        "mid-run, killing Bash outright: run sibling-repo dispatches "
        "WITHOUT isolation."
    )


def worktree_advisory(payload: dict) -> str | None:
    """Non-blocking advisory for `isolation: "worktree"` Agent calls.

    Fires only on that call shape; every other dispatch is untouched.
    Rides this ALREADY-WIRED hook entry deliberately: a hooks.json
    entry new in an update stays dormant until a full restart, while
    changed code behind a wired entry reloads (dotfiles CLAUDE.md,
    probe 2026-08-05)."""
    if payload.get("tool_name") != "Agent":
        return None
    tool_input = payload.get("tool_input") or {}
    if tool_input.get("isolation") != "worktree":
        return None
    return worktree_advisory_text()


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
        deny(deny_text(payload), source=_SOURCE, payload=payload)
    if missing_tail(payload):
        deny(missing_tail_deny_text(), source=_SOURCE, payload=payload)
    if tail_mode_mismatch(payload):
        deny(tail_mode_mismatch_deny_text(payload), source=_SOURCE,
             payload=payload)
    if missing_sections(payload):
        deny(missing_sections_deny_text(payload), source=_SOURCE,
             payload=payload)
    # Staged lane: ships warn, promotable to deny via guard_modes
    # (key "brief-reminder" — the four deny lanes above call deny()
    # directly, so that key reaches this lane alone). fire() exits in
    # EVERY mode, so a warn here replaces the reminder line below for
    # this one brief: the warn names the same §1 check more
    # specifically, and every deny lane above already exits the same
    # way.
    if missing_commit_plan(payload):
        fire(missing_commit_plan_warn_text(), source=_SOURCE,
             payload=payload, default_mode="warn")
    # One additionalContext field per hook call: the advisory rides
    # the reminder line rather than replacing it.
    lines = [t for t in (check(payload), worktree_advisory(payload)) if t]
    if lines:
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "additionalContext": "\n".join(lines),
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
            tf.write('{"discipline_doc": "dispatch skill"}')
            os.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = tf.name
        _reset_policy_cache()
        assert "dispatch skill §1" in check({"tool_name": "Agent"})
        assert check({"tool_name": "Bash"}) is None
        assert check({}) is None
        # Channel gate: mailbox lane (NAMED) + no channel → deny
        assert missing_channel({"tool_name": "Agent", "tool_input": {
            "name": "sonnet-x",
            "prompt": "Go read files and report your findings."}})
        # Channel named (any marker) → allow
        assert not missing_channel({"tool_name": "Agent", "tool_input": {
            "name": "sonnet-x",
            "prompt": "Do X. Deliver via SendMessage to main."}})
        # Task tool, empty prompt, non-dispatch tools → never deny
        assert not missing_channel({"tool_name": "Task", "tool_input": {
            "name": "sonnet-x", "prompt": "no channel here"}})
        assert not missing_channel({"tool_name": "Agent", "tool_input": {}})
        assert not missing_channel({"tool_name": "Bash", "tool_input": {
            "command": "ls"}})
        _named = {"tool_name": "Agent", "tool_input": {
            "name": "sonnet-x", "prompt": "do the thing"}}
        assert "Blocked" in deny_text(_named)
        assert "mailbox" in deny_text(_named)
        # The superseded text advised `run_in_background: false`, a
        # parameter the Agent tool does not accept — a repair that
        # could never clear on retry. It must not come back.
        assert "run_in_background" not in deny_text(_named)

        # ── The LANE is set by `name` alone ────────────────────────
        # Expectations derived from forms.md §2's binding (as of
        # 2026-08-15, harness 2.1.232) and the probe matrix behind
        # it — never from this hook's behavior. Measured: a NAMED
        # dispatch (generic or pinned type) spawns as a mailbox
        # teammate and fires no completion notification; an UNNAMED
        # one launches as a background task whose notification
        # carried the agent's final text verbatim, from an agent
        # that called no tool at all.
        # (i) UNNAMED + no channel line → NO deny. The background
        # task's notification delivers the final text, so nothing is
        # owed. The superseded flag predicate was constant-true and
        # denied here.
        assert not missing_channel({"tool_name": "Agent", "tool_input": {
            "prompt": "Do the thing and report back."}})
        # (ii) UNNAMED carrying the background-task line → silent.
        # This is the shape the superseded predicate bounced: it read
        # every dispatch as background and denied the line that is
        # true for this lane.
        _unnamed_delivered = {"tool_name": "Agent", "tool_input": {
            "subagent_type": "claude-code-guide",
            "prompt": "Do the thing.\nReport channel: your final text "
                      "IS the report."}}
        assert not missing_channel(_unnamed_delivered)
        assert not tail_mode_mismatch(_unnamed_delivered)
        # (iii) UNNAMED carrying the MAILBOX line → mismatch: that
        # line tells an agent its final text reaches no one when the
        # notification does deliver it.
        assert tail_mode_mismatch({"tool_name": "Agent", "tool_input": {
            "subagent_type": "claude-code-guide",
            "prompt": "Do the thing.\nReport channel: SendMessage to "
                      "the dispatcher — your final text reaches no "
                      "one."}})
        # (iv) NAMED carrying the correct mailbox line → silent;
        # NAMED carrying the background-task line → mismatch.
        assert not tail_mode_mismatch({"tool_name": "Agent", "tool_input": {
            "name": "x-agent",
            "prompt": "Do the thing.\nReport channel: SendMessage to "
                      "the dispatcher — your final text reaches no "
                      "one."}})
        assert tail_mode_mismatch({"tool_name": "Agent", "tool_input": {
            "name": "x-agent",
            "prompt": "Do the thing.\nReport channel: your final text "
                      "IS the report."}})
        # (v) a pinned type is not itself a lane: NAMED pinned sits in
        # the mailbox lane with every other named dispatch. This is
        # the cell that separated `name` from agent type in the probe.
        assert mailbox_lane({"name": "x-agent",
                             "subagent_type": "claude-code-guide"})
        assert not mailbox_lane({"subagent_type": "claude-code-guide"})
        # the predicate itself, both directions
        assert mailbox_lane({"name": "x-agent"})
        assert not mailbox_lane({})
        # a dead `run_in_background` key changes nothing either way
        assert mailbox_lane({"name": "x-agent",
                             "run_in_background": False})
        assert not mailbox_lane({"run_in_background": False})

        # ── Tail-presence lane (missing_tail) ──────────────────────
        # Tails copied verbatim from the §2 forms (cite: dispatch
        # skill, references/forms.md §2) — literals here, never
        # referenced from the detection constants, so the test
        # doesn't share parentage with what it's meant to catch.
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
            "Message ≤3000 chars each: a report longer than one "
            "message is SPLIT into labeled parts (1/N) — do NOT write "
            "a report FILE (harness-blocked for subagents); supporting "
            "data goes to the brief's assigned DATA files, the message "
            "carries key findings + any such paths. A missing "
            "decision, file, or value is surfaced as a gap, never "
            "bridged with a guess.\n"
            "A check that got backgrounded is AWAITED before the "
            "closing report (TaskOutput block=true on its task id) — "
            "ending your turn orphans it; a report sent with a check "
            "still running is an INTERIM report, says so, and names "
            "what remains.\n"
            "Commits unpushed, by pathspec — `git commit -- <paths>`, "
            "never `git add` then `git commit` and never `-A`: the "
            "index is shared, so a co-writer staging between your `git "
            "status` and your commit rides out under your message "
            "whatever you added. A NEW file is invisible to a pathspec "
            "commit until `git add -N <path>` registers it "
            "(intent-to-add: zero content staged, full body still "
            "committed). Trailer: `Co-Authored-By: Claude <model> "
            "<noreply@anthropic.com>`.\n"
            "Never amend — always a new commit: the amend-gate denies "
            "subagent amends regardless of ownership (source: \xa71 amend "
            "rule).\n"
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
            "name": "sonnet-x",
            "prompt": "Do X and report back."}})

        # (ii) each §2 tail verbatim, correct channel line for the
        # mode used → missing_tail False, tail_mode_mismatch False
        bg_brief = {"tool_name": "Agent", "tool_input": {
            "name": "sonnet-x",
            "prompt": "Do X.\n" + EXECUTION_TAIL_BG}}
        assert not missing_tail(bg_brief)
        assert not tail_mode_mismatch(bg_brief)
        sync_brief = {"tool_name": "Agent", "tool_input": {
            "prompt": "Do X.\n" + READONLY_TAIL_SYNC}}
        assert not missing_tail(sync_brief)
        assert not tail_mode_mismatch(sync_brief)

        # (iii) wrong channel line for the mode → tail_mode_mismatch
        # True, both directions
        bg_with_sync_line = {"tool_name": "Agent", "tool_input": {
            "name": "sonnet-x",
            "prompt": "Do X.\n" + EXECUTION_TAIL_SYNC_LINE}}
        assert not missing_tail(bg_with_sync_line)  # tail present
        assert tail_mode_mismatch(bg_with_sync_line)
        sync_with_bg_line = {"tool_name": "Agent", "tool_input": {
            "prompt": "Do X.\n" + READONLY_TAIL_BG_LINE}}
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
        # Section markers named in the dispatch skill §1 ("Grounding
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

        # ── verifier brief citing forms.md → EXEMPT (false fire) ───
        # forms.md carries BOTH tails verbatim and this guard reads
        # every .md the prompt names, so a verifier brief that merely
        # CITES the forms file inherited the execution anchor and was
        # denied for lacking §1 sections it is exempt from. Observed
        # live on a legitimate verifier dispatch. Expectation from §1
        # ("verifier dispatches stay exempt from the rich §1 brief
        # form ... artifact + question + that block"), not from code.
        _READONLY_TAIL_REAL = (
            "Report channel: SendMessage to the dispatcher — your "
            "final text reaches no one.\n"
            "Return your findings in ONE message where they fit "
            "(verifier: verdict + basis; discovery: the N named "
            "facts, sources actually read); past the message-size "
            "gate, labeled parts (1/N) — never a report file. A "
            "missing decision, file, or value is surfaced as a gap, "
            "never bridged with a guess. No repo writes, no report "
            "files, no interim messages; transient probe scratch in "
            "your OWN scratchpad is permitted and is not a report "
            "file.")
        # The citation is the REAL forms.md by ABSOLUTE path: the
        # fixture must actually read a file carrying the execution
        # anchor, or it tests nothing. A relative path here silently
        # resolved to no file (no cwd in the payload) and the case
        # passed against the unfixed code — caught by running it
        # red-first.
        _vet = {"tool_name": "Agent", "tool_input": {
            "name": "opus-vet",
            "prompt": ("Verifier dispatch. ARTIFACT: the diff. "
                       "QUESTION: is " + _forms_path() + " §2 "
                       "consistent with the hook?\n"
                       + _READONLY_TAIL_REAL)}}
        assert _SECTIONS_ANCHOR in _brief_text(_vet), (
            "fixture reads no execution-anchor file — it would pass "
            "regardless of the exemption")
        assert _tail_kind(_vet) == "readonly", _tail_kind(_vet)
        assert not missing_sections(_vet)
        assert not tail_mode_mismatch(_vet)
        assert not missing_channel(_vet)
        assert not missing_tail(_vet)
        # the lane still bites a real execution brief citing forms.md
        _exec_bad = {"tool_name": "Agent", "tool_input": {
            "name": "sonnet-x",
            "prompt": ("Do X per " + _forms_path() + ".\n"
                       + EXECUTION_TAIL_BG)}}
        assert _tail_kind(_exec_bad) == "execution"
        assert missing_sections(_exec_bad)

        # ── Commit-plan lane (missing_commit_plan), STAGED WARN ────
        # Slot named in the dispatch skill §1 skeleton ("## Commit
        # plan") — literal here, never the detection constant, so the
        # test doesn't share parentage with what it's meant to catch.
        COMMIT_PLAN_SECTION = (
            "Commit plan: the repo's payload-version gate compares "
            "against the release state, so the bump commit lands "
            "first; then the two payload commits by pathspec.")

        # (i) the PAIR that grades this lane: one brief carrying the
        # slot, one not. They must DIFFER — a pair both readings
        # satisfy grades nothing. Red-proven against the pre-change
        # module (a copy of the whole hooks dir at the parent commit),
        # where the predicate did not exist at all.
        commit_plan_absent_brief = {"tool_name": "Agent", "tool_input": {
            "prompt": "Do X.\n" + GROUNDING_SECTION + "\n"
                      + WRITE_BOUNDARIES_SECTION + "\n"
                      + EXECUTION_TAIL_BG}}
        commit_plan_present_brief = {"tool_name": "Agent", "tool_input": {
            "prompt": "Do X.\n" + GROUNDING_SECTION + "\n"
                      + WRITE_BOUNDARIES_SECTION + "\n"
                      + COMMIT_PLAN_SECTION + "\n"
                      + EXECUTION_TAIL_BG}}
        assert missing_commit_plan(commit_plan_absent_brief)
        assert not missing_commit_plan(commit_plan_present_brief)
        assert (missing_commit_plan(commit_plan_absent_brief)
                != missing_commit_plan(commit_plan_present_brief))

        # (ii) the pasted skeleton's own hard wrap ("Commit\nplan")
        # still counts — the normalization lane, applied here.
        assert not missing_commit_plan({"tool_name": "Agent", "tool_input": {
            "prompt": "Do X.\nGrounding basis: read spec.md first.\n"
                      "Write boundaries: src/foo.py only.\n"
                      "## Commit\nplan: bump first, then the payloads.\n"
                      + EXECUTION_TAIL_BG}})

        # (iii) a real dispatcher brief states the plan as numbered
        # prose, not as a `##` heading — the marker family is
        # label-shaped, not heading-anchored, so that form counts too.
        assert not missing_commit_plan({"tool_name": "Agent", "tool_input": {
            "prompt": "Do X.\n" + GROUNDING_SECTION + "\n"
                      + WRITE_BOUNDARIES_SECTION + "\n"
                      "1. COMMIT PLAN, ordered against this repo's "
                      "payload-version gate — THREE commits.\n"
                      + EXECUTION_TAIL_BG}})

        # (iv) scope negatives: READ-ONLY tail (no execution anchor),
        # Task tool, parse-garbage → never fires
        assert not missing_commit_plan(readonly_neither_brief)
        assert not missing_commit_plan({"tool_name": "Task", "tool_input": {
            "prompt": "Do X.\n" + EXECUTION_TAIL_BG}})
        assert not missing_commit_plan({"tool_name": "Agent",
                                        "tool_input": {}})
        assert not missing_commit_plan({"tool_name": "Bash", "tool_input": {
            "command": "ls"}})
        assert not missing_commit_plan({})

        # (v) the lane's own docstring, wrapped in a real execution
        # brief: in-domain adversarial text by the same author. This
        # predicate fires on ABSENCE, so a self-matching docstring can
        # only prove the silent direction — it bounds the true
        # negative, it is NOT a false-fire proof for this lane.
        assert not missing_commit_plan({"tool_name": "Agent", "tool_input": {
            "prompt": "Do X.\n" + (missing_commit_plan.__doc__ or "")
                      + "\n" + EXECUTION_TAIL_BG}})

        assert "commit-plan section" in missing_commit_plan_warn_text()

        # ── Whitespace-normalization lane (false-fire 2026-07-30) ──
        # The §2 tails carry hard line wraps in references/forms.md
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

        # ── File-carried briefs (forms.md §2: inline tail required ──
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
        # behavior — the §2 forms (references/forms.md): "The tail reaches the
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

        # ── Worktree-base advisory lane ────────────────────────────
        # Expectation derived from the observed incidents, not from
        # this hook: a harness worktree cut from an older snapshot
        # makes the executor's base check fail correctly, and the
        # brief is where the stated base + ff-recovery must live.
        # (i) fires on the isolation=worktree Agent call shape
        wt_call = {"tool_name": "Agent", "tool_input": {
            "prompt": "Do X.", "isolation": "worktree"}}
        assert worktree_advisory(wt_call) is not None
        assert "base commit" in worktree_advisory(wt_call)
        assert "ff-only" in worktree_advisory(wt_call)
        # all three classes named (the dispatcher's ruling: stale
        # session-repo cut, sibling-repo provisioning, sibling-repo
        # under isolation)
        assert "SESSION-repo" in worktree_advisory_text()
        assert "SIBLING repo" in worktree_advisory_text()
        assert "WITHOUT isolation" in worktree_advisory_text()
        # (ii) silent on every other call shape
        assert worktree_advisory({"tool_name": "Agent", "tool_input": {
            "prompt": "Do X."}}) is None
        assert worktree_advisory({"tool_name": "Agent", "tool_input": {
            "prompt": "Do X.", "isolation": "remote"}}) is None
        assert worktree_advisory({"tool_name": "Task", "tool_input": {
            "isolation": "worktree"}}) is None
        assert worktree_advisory({"tool_name": "Bash", "tool_input": {
            "command": "git worktree add /tmp/wt"}}) is None
        assert worktree_advisory({"tool_name": "Agent",
                                  "tool_input": {}}) is None
        assert worktree_advisory({}) is None
        # (iii) the advisory never blocks and never displaces the
        # existing reminder — both lanes answer on the same call
        assert check(wt_call) is not None

        print("brief-reminder: all tests passed")
        sys.exit(0)
    sys.exit(main())
