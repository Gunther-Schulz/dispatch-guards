#!/usr/bin/env python3
"""PreToolUse gate: agent dispatches must choose the model EXPLICITLY.

Enforces the mechanical half of the model-routing discipline
(~/.claude/CLAUDE.md "Model routing for dispatches"; project-side e.g.
pbs-doc/PROZESS.md §1a): an agent spawn with no `model` field still
inherits the session model (most expensive case: Fable) — the gate blocks
the call and forces a deliberate choice. Whether the choice is CORRECT no
hook can check; that stays judgment + gate over the result.

Exceptions: agent types that pin their own model in their definition
(plugin agents "plugin:name" and other specialized types) — forcing an
override there would be backwards.

Occasion (evidence, 2026-07-11): an Explore dispatch "survey the B/C
landscape" without an override unintentionally ran on Fable instead of Opus.

Extension (2026-07-18): the dispatch title
(`description`) must start with the strict prefix `<model>: ` (colon +
space, free text after — operator-picked format) so every dispatch
shows its model live in the UI, and the prefix must equal the `model`
field — the doubling is a verified mirror (mini-checksum), not a
second truth source. Scope: only the generic ENFORCED_TYPES below;
agents whose definition pins their model need neither field nor prefix.

Fable brake (2026-07-19, fail-safe for the CLAUDE.md fable cost
facts): EVERY fable dispatch forces the permission
dialog — an explicit model choice proved insufficient cost control
when a review harness fanned out 8×fable (~100k tokens each) on one
GO-less turn. The gate cannot judge the brief's fit; the dialog
hands that call to the operator BEFORE anything
starts (operator decision 2026-07-19: control per yes/no, no budget
or counter semantics). Stateless by design. Dialogs speak veto
voice: the decision arrives made, the operator cancels or lets
pass — the dialog never prescribes what a fable dispatch must be.

Workflow lane (same day): Workflow launches ask unconditionally —
script-internal agent() calls never pass through PreToolUse Agent
hooks, and an agent() without a model override inherits the session
model, so a fable session's workflow is an ungated fable fan-out.
The dialog tells the operator to check the script's model overrides.

Name lane (2026-07-19, evening): a dispatch that sets `name` (for
SendMessage addressing) must prefix it `<model>-` — the teammate
panel renders the NAME plus prompt text, never the description, so
a title-only prefix is invisible exactly where the operator looks
(observed: "draft-vet" showed no model). Names can't contain ": "
(charset [A-Za-z0-9_-]), hence the hyphen form.

Title lane narrowed to the UNNAMED case (2026-08-02): since the panel
never renders the description for a named dispatch, requiring BOTH
prefixes there bought nothing and taxed the title — the model rides
the surface the panel actually renders. So: `name` set → the name
carries the model and the title prefix is optional; no `name` → the
title prefix stays required (it is then the only visible carrier).
When a title prefix IS present it must still mirror the model field;
the mini-checksum is unchanged. Observed live: a named dispatch
renders as "<name>  <prompt excerpt>" with the title absent entirely.
Corpus homes: the dispatch skill §1 + CLAUDE.md veto-gate
conventions, amended the same day — this hook is their enforcement,
and the amendment landing without it was the divergence that
surfaced the lane.

Name lane made mandatory (2026-08-08, operator decision): EVERY
generic dispatch is NAMED `<model>-<slug>`, panel style
`<model>-<slug>  <clean description>`. The name is the only model
carrier: the panel renders it, the title stays clean prose. So a
missing `name` now blocks, and the unnamed/title-prefix REQUIREMENT
is retired — the 2026-07-18 title extension and the 2026-08-02
narrowing are superseded (kept above as history). The mirror check
survives: a title that DOES start `<model>: ` must still match the
model field, and a matching prefix is tolerated rather than
rejected — style prefers none, tolerance keeps the false-fire
surface at zero.
Why the title lane could retire: it existed for the SYNCHRONOUS
dispatch, where no name is set and the title is the only carrier.
The controlled re-probe (forms.md §2) found no sync LAUNCH MODE to
carry a title: the Agent tool takes no `run_in_background`
parameter, an UNNAMED dispatch launches as a background task whose
completion notification delivers its final text, and `name` alone
selects that lane against the mailbox one. An unnamed dispatch is
then reachable only by pinned types, which this gate exempts
anyway — so the lane guards nothing.
CAVEAT, and it is why forms.md now decides the lane by a PER-SESSION
schema probe rather than a dated binding: the harness has withdrawn
`name` from the Agent schema mid-session, and in such a session the
synchronous shape is all there is. This gate's mandatory-name lane
then denies every GENERIC dispatch, since the mandate cannot be
satisfied at all. That is deliberate and stays: the guarded failure
— a dispatch whose model is invisible where the operator watches —
does not stop being a failure because the schema moved, and the
route in that state is the operator, never a silent workaround.

Verb conversion, name lane (2026-09-15, guard-rewrite arc item 1,
`docs/directives/2026-09-15-guard-rewrite-arc.md`): the missing-name
and wrong-prefix denies above are now a REWRITE, not a bounce. The
gate computes `<model>-<slug>` — slug from the existing `name` when
one is present (prefixed as-is, even if it carries a stale model
token) or from `description` otherwise (lowercased, anything outside
`[a-z0-9_-]` collapsed to one `-`, trimmed, capped ~24 chars,
fallback `task` on an empty result) — and emits it via
`hookSpecificOutput.updatedInput` with NO `permissionDecision` field,
the shape `docs/audits/wave0-probe-record-2026-09-15.md` found
correct (arms b2/b3: applies with no forced allow, permission flow
still runs unforced on a rewritten call). That record measured
`updatedInput` on the `prompt` and `command` fields, never on `name`
itself — the `name` rewrite generalizes from those two fields rather
than resting on a direct probe of this one. Any state where the
rewrite cannot be computed still denies (never a silent pass), though
`_slugify`'s `task` fallback means this should not occur in practice.
This is a verb CONVERSION under the three-verbs rule (CLAUDE.md):
the lane carries its 2026-08-08 day-one-blocking status forward
unconditionally — it was never a default-warn lane and is not being
re-staged, just repaired instead of bounced. Unaffected: missing or
denied model still denies (a routing forcing-function — the deny IS
the point, choosing is what it exists to force), the title-mirror
mismatch still denies and takes PRECEDENCE over a pending name
rewrite (a call failing both checks gets the mismatch deny, never a
silent partial repair), and the escalation/Workflow/fable lanes are
untouched. Fire log: a rewrite logs `mode="rewrite"`, reason naming
old name -> new name, so the fire-rate review can grade this lane
like any other.

Accepted residue: agent types that pin their model in their
definition bypass the gate entirely for the model/title checks
(ENFORCED_TYPES scope; the escalation lane below still applies);
and SendMessage RESUMES of an already-approved agent pass no Agent
hook — one GO covers the spawn and its continuations.

Escalation lane (2026-07-28): an ask-tier dispatch FROM a subagent is
DENIED, not asked — a subagent needing a tier above its own returns the
question to its dispatcher, which decides and dispatches. Basis: the
escalating agent would write the brief for its own reviewer, and it is
the context least able to state that question fairly — could it see the
flaw well enough to brief someone on it, it would mostly have caught it;
escalation-from-below inherits the blind spot it means to escape. Deny
rather than ask is deliberate: the operator's veto answers "is this
dispatch worth it", never "should this agent be the one deciding".
Scope, and why it cannot be general: hook input carries NO caller model
(hooks reference: only SessionStart may receive `model`; there is no
$CLAUDE_MODEL), so "above yourself" is NOT computable — only the
ask-tier case is mechanically decidable, and the general rule stays
prose (dispatch skill §4). Subagents dispatching sideways or
down are untouched; nesting itself stays legal — the governing knob
is the harness setting CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH (3 layers
by default), which a site may cap independently of this gate; read it
there rather than from this line, which states the gate's own
indifference to depth and not the depth a given site allows.
Binding as-of 2026-07-28: PreToolUse fires inside subagents and the
input carries `agent_id` — CONFIRMED live (this gate and the push gate
both observed biting from a subagent context, not merely bite-tested).
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from _dispatch_common import ask, deny, doc_ref, is_subagent, policy  # noqa: E402

# Generic types with no model pinning in their definition: here the choice
# MUST be in the call. A missing subagent_type defaults to general-purpose.
ENFORCED_TYPES = {"general-purpose", "Explore", "Plan", "claude", None, ""}

def _allowed_models() -> set:
    return set(policy()["models"])


def _title_re():
    # Strict title prefix: "<model>: " followed by free title text.
    alt = "|".join(re.escape(m) for m in policy()["models"])
    return re.compile(rf"^({alt}): \S", re.IGNORECASE)


def check(tool_input: dict) -> str | None:
    """Return an error message for a lane that STILL DENIES, or None.

    None covers three cases, not just "allow through": a
    specialized/pinned agent type (nothing here applies), an enforced
    type with a valid non-denied model and a clean title (nothing to
    fix), and — since 2026-09-15 — an enforced type with a valid
    non-denied model whose `name` is missing or wrongly prefixed.
    That last case used to deny here; it is now a REWRITE, computed
    by compute_name_rewrite() and applied in main() — check() itself
    never emits it (see the docstring's "Verb conversion" note)."""
    subagent = tool_input.get("subagent_type")
    if subagent not in ENFORCED_TYPES:
        return None  # specialized/plugin agent: its definition pins the model
    model = tool_input.get("model")
    if model not in _allowed_models():
        return (
            "Model gate: agent dispatch without an explicit `model` — the agent "
            "would silently inherit the session model. Choose deliberately per "
            "the model table (~/.claude/CLAUDE.md 'Model routing for "
            "dispatches') or project routing (e.g. PROZESS.md §1a). Even an "
            "intentional inherit must be made "
            "explicit as model:\"fable\". Name the choice in your reply."
        )
    if model in policy()["deny_models"]:
        return (
            f"Model gate: `{model}` is denied by site policy "
            "(deny_models in the dispatch-guards config). Choose "
            "another tier."
        )
    desc = (tool_input.get("description") or "").strip()
    match = _title_re().match(desc)
    if match and match.group(1).lower() != model:
        return (
            f"Model gate: title prefix {match.group(1).lower()!r} "
            f"diverges from model field {model!r} — the prefix is a "
            "verified mirror of the field; make them match."
        )
    return None


_SLUG_CAP = 24
_SLUG_BAD = re.compile(r"[^a-z0-9_-]+")
_SLUG_RUNS = re.compile(r"-{2,}")


def _slugify(text: str) -> str:
    """Lowercase; anything outside [a-z0-9_-] collapses to one '-';
    dash runs collapse to one; leading/trailing '-' trimmed; capped
    at _SLUG_CAP chars with a possible new trailing '-' trimmed again
    (the cut can land exactly on a separator). Empty input, or input
    that is nothing BUT disallowed characters, falls back to 'task'
    rather than returning ''. Output charset is [a-z0-9_-] by
    construction — nothing else can survive the substitution."""
    s = (text or "").lower()
    s = _SLUG_BAD.sub("-", s)
    s = _SLUG_RUNS.sub("-", s)
    s = s.strip("-")
    s = s[:_SLUG_CAP].strip("-")
    return s or "task"


def compute_name_rewrite(tool_input: dict, model: str) -> str | None:
    """The corrected `name` for a generic dispatch with a valid,
    non-denied `model`, or None when the existing name already
    carries the right prefix (case-insensitively) — no rewrite
    needed. Slug source: the existing name when one is present
    (prefixed as-is, per the settled design — a name already
    carrying a DIFFERENT model's prefix is not stripped, only
    re-prefixed), else `description`. Never raises: _slugify always
    returns a non-empty [a-z0-9_-]+ string."""
    name = (tool_input.get("name") or "").strip()
    if name and name.lower().startswith(model.lower() + "-"):
        return None
    source = name or (tool_input.get("description") or "")
    return f"{model}-{_slugify(source)}"


def _rewrite_or_none(tool_input: dict, model: str) -> tuple[str | None, bool]:
    """(new_name_or_None, ok). ok=False means the rewrite could not
    be computed and the caller must deny rather than pass silently —
    the directive's named fallback. compute_name_rewrite() does not
    raise in practice (its slugifier always falls back to 'task'), so
    this is a belt exercised only by a deliberately broken
    compute_name_rewrite in --test, not by any known real input."""
    try:
        return compute_name_rewrite(tool_input, model), True
    except Exception:
        return None, False


# Undelivered-text note (2026-08-05): text written in the SAME turn
# before a gated call is not rendered — the ask dialog is all the
# operator sees, so an explanation composed before the call is hidden
# exactly at the approval moment (corpus: "text preceding a
# permission-GATED call fails hardest", CLAUDE.md Recommending &
# reporting). Probe-verified binding (as-of 2026-08-05): the current
# turn's assistant text blocks are already flushed to the transcript
# when PreToolUse fires, so the hook can measure them. The note rides
# INSIDE an already-firing ask dialog — no new fire event, no
# false-fire surface; below the threshold (route-line one-liners) it
# stays silent.
_UNDELIVERED_NOTE_MIN_CHARS = 300


def _undelivered_text_chars(transcript_path: str) -> int:
    """Chars of assistant text written since the last real operator
    prompt (isMeta/tool-result/non-human-origin user events are not
    prompts). Fail-soft: unreadable transcript or no boundary → 0."""
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
        return 0
    last = -1
    for i, ev in enumerate(events):
        msg = ev.get("message")
        if not isinstance(msg, dict) or msg.get("role") != "user":
            continue
        if ev.get("isMeta") is True:
            continue
        origin = ev.get("origin")
        if origin and not (isinstance(origin, dict)
                           and origin.get("kind") == "human"):
            continue
        content = msg.get("content")
        if isinstance(content, str) or (
                isinstance(content, list)
                and any(isinstance(b, dict) and b.get("type") == "text"
                        for b in content)):
            last = i
    if last == -1:
        return 0
    total = 0
    for ev in events[last + 1:]:
        msg = ev.get("message")
        if not isinstance(msg, dict) or msg.get("role") != "assistant":
            continue
        content = msg.get("content", [])
        if not isinstance(content, list):
            continue
        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                total += len(block.get("text") or "")
    return total


def undelivered_note(payload: dict) -> str:
    """Appendix for an ask reason, or "" when this turn carries no
    substantial pre-call text."""
    n = _undelivered_text_chars(payload.get("transcript_path") or "")
    if n < _UNDELIVERED_NOTE_MIN_CHARS:
        return ""
    return (
        f" NB: ~{n} Zeichen Assistententext stehen in diesem Zug VOR "
        "diesem Aufruf und sind noch NICHT gerendert — sie erscheinen "
        "erst nach dem Dialog. Sollte erst eine Erklärung gelesen "
        "werden: abbrechen (No), Text liefern lassen, dann erneut "
        "dispatchen."
    )


def needs_workflow_ask(payload: dict) -> bool:
    """Workflow launches ask unconditionally (see docstring: their
    internal agent() spawns bypass this gate and inherit the session
    model when unspecified)."""
    return payload.get("tool_name") == "Workflow"


def needs_model_ask(tool_input: dict) -> bool:
    """True when the dispatch uses an ask_models tier on a generic type:
    every such dispatch gets the permission dialog (tier brake). Pinned
    agent types bypass the gate entirely — documented residue."""
    return (tool_input.get("subagent_type") in ENFORCED_TYPES
            and tool_input.get("model") in policy()["ask_models"])


def escalation_deny(payload: dict) -> str | None:
    """Deny reason when a SUBAGENT dispatches an ask-tier agent, else None.

    Escalation is the dispatcher's call (see docstring): the subagent
    returns the question, it does not spawn the answer. Unlike
    needs_model_ask this ignores ENFORCED_TYPES — a pinned agent type
    that pins an ask-tier model is the same spend from the same context,
    and here no title/name convention is needed to recognize it."""
    if not is_subagent(payload):
        return None
    tool_input = payload.get("tool_input") or {}
    model = tool_input.get("model")
    if model not in policy()["ask_models"]:
        return None
    return (
        f"Escalation gate: a subagent may not dispatch `{model}` — "
        "escalation is the DISPATCHER's decision, not the escalating "
        "agent's. Return the question to your dispatcher (report the "
        "evidence and what you could not settle at your tier); it "
        "decides and dispatches. Basis: briefing your own reviewer "
        f"inherits the blind spot it is meant to escape ({doc_ref('§4')}). "
        "Dispatching sideways or down is unaffected."
    )


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0  # never fail the workflow on a hook parse error
    if needs_workflow_ask(payload):
        ti = payload.get("tool_input") or {}
        label = ti.get("name") or ti.get("scriptPath") or "inline script"
        ask(  # exits 0 with permissionDecision "ask"
            f"⚠️ WORKFLOW-START ({label}): agent()-Aufrufe im Script "
            "passieren dieses Gate NICHT einzeln und erben ohne "
            "model-Override das Session-Modell — in einer Fable-Session "
            "ein ungegateter Fable-Fan-out. Vor dem GO: model-Overrides "
            "im Script prüfen." + undelivered_note(payload),
            source="dispatch-guards/agent-model-gate", payload=payload,
        )
    if payload.get("tool_name") not in ("Agent", "Task"):
        return 0
    if grund := escalation_deny(payload):
        deny(grund, source="dispatch-guards/agent-model-gate",
             payload=payload)  # before the name check and the ask: an escalating subagent gets the return-the-question rule, not a name lesson or the dialog
    tool_input = payload.get("tool_input") or {}
    error = check(tool_input)
    if error:
        from _dispatch_common import fire_log
        fire_log("dispatch-guards/agent-model-gate", "block", error, payload)
        print(error, file=sys.stderr)
        return 2  # blocking; stderr goes back as feedback to the main agent
    # check() returned None: either a pinned type (nothing applies), or
    # an enforced type with a valid non-denied model and a clean title.
    # In the latter case a name issue may still need the REWRITE repair
    # (2026-09-15 verb conversion — see module docstring).
    subagent = tool_input.get("subagent_type")
    model = tool_input.get("model")
    if subagent in ENFORCED_TYPES and model in _allowed_models():
        from _dispatch_common import fire_log
        new_name, ok = _rewrite_or_none(tool_input, model)
        if not ok:
            reason = (
                "Model gate: could not compute a `<model>-<slug>` name "
                f"for this dispatch ({doc_ref('§5')}) — falling back to "
                f'the explicit-name requirement. Add name: "{model}-'
                '<slug>" yourself.'
            )
            fire_log("dispatch-guards/agent-model-gate", "block", reason, payload)
            print(reason, file=sys.stderr)
            return 2
        if new_name is not None:
            old_name = tool_input.get("name") or "(none)"
            reason = (
                f"Model gate: rewrote name {old_name!r} -> {new_name!r} "
                f"({model}-<slug> convention; {doc_ref('§5')})."
            )
            new_input = dict(tool_input)
            new_input["name"] = new_name
            fire_log("dispatch-guards/agent-model-gate", "rewrite", reason, payload)
            print(json.dumps({
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "updatedInput": new_input,
                }
            }))
            return 0
    if needs_model_ask(tool_input):
        desc = (tool_input.get("description") or "").strip()
        ask(  # exits 0 with permissionDecision "ask"
            f"⚠️ FABLE-DISPATCH: {desc!r}. Teuerste Stufe; ihr "
            "komparativer Vorteil laut CLAUDE.md: Fresh-Context-Verdikt "
            "auf begrenztem Artefakt. Die Entscheidung ist getroffen — "
            "abbrechen, wenn der Einsatz sie nicht rechtfertigt."
            + undelivered_note(payload),
            source="dispatch-guards/agent-model-gate", payload=payload,
        )
    return 0


if __name__ == "__main__":
    if "--test" in sys.argv:
        import tempfile
        from _dispatch_common import _reset_policy_cache
        # ── Defaults (kein Config): keine Sperren, keine Asks ──
        os_mod = __import__("os")
        os_mod.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = "/nonexistent"
        _reset_policy_cache()
        assert check({"subagent_type": "general-purpose"}) is not None
        assert check({}) is not None                          # default type, no model
        assert check({"subagent_type": "Explore", "model": "haiku",
                      "name": "haiku-scan"}) is None      # default: kein deny
        assert not needs_model_ask({"model": "fable",
                                    "description": "fable: X"})  # default: kein ask
        assert check({"subagent_type": "statusline-setup"}) is None
        assert check({"subagent_type": "plugin-dev:agent-creator"}) is None
        assert check({"subagent_type": "claude", "model": "nonsense"}) is not None
        # Name lane made MANDATORY (2026-08-08), then converted DENY -> REWRITE
        # (2026-09-15): check() no longer denies on a missing/wrongly-prefixed
        # name at all — that state is now a REWRITE, computed by
        # compute_name_rewrite() and never reached through check(). A case
        # below whose ONLY old defect was the name is check()-None now; the
        # rewrite itself is asserted via compute_name_rewrite().
        assert check({"model": "opus", "description": "opus: Fix tests"}) is None
        assert compute_name_rewrite(
            {"model": "opus", "description": "opus: Fix tests"},
            "opus") == "opus-opus-fix-tests"   # slug built from the whole
            # description, including its own legacy "opus: " prefix — the
            # design derives the slug from description verbatim, it does not
            # strip a leading model token first.
        assert check({"model": "opus", "description": "Fix tests"}) is None
        assert compute_name_rewrite(
            {"model": "opus", "description": "Fix tests"},
            "opus") == "opus-fix-tests"
        assert check({"model": "opus"}) is None                # no name, no title
        assert compute_name_rewrite({"model": "opus"}, "opus") == "opus-task"
        assert check({"model": "opus", "description": "opus-fix-tests"}) is None
        assert check({"subagent_type": "Explore", "model": "sonnet",
                      "description": "Scan repo"}) is None
        assert compute_name_rewrite(
            {"description": "Scan repo"}, "sonnet") == "sonnet-scan-repo"
        # A NAMED dispatch with the right prefix needs no rewrite at all —
        # compute_name_rewrite returns None, whatever the title.
        assert check({"model": "opus", "description": "Fix tests",
                      "name": "opus-fixer"}) is None
        assert compute_name_rewrite(
            {"model": "opus", "description": "Fix tests", "name": "opus-fixer"},
            "opus") is None
        assert check({"model": "opus", "description": "",
                      "name": "opus-fixer"}) is None          # no title at all
        assert check({"model": "opus", "description": "opus:",
                      "name": "opus-fixer"}) is None          # not a prefix match
        assert check({"model": "opus", "name": "opus-mech-rerun",
                      "description": "F-2 mechanical re-run"}) is None
        assert check({"subagent_type": "Explore", "model": "fable",
                      "name": "fable-arch-review",
                      "description": "Review architecture"}) is None
        # A wrong-prefixed name (2026-07-19 lane) is now a REWRITE, not a
        # deny: check() is None and compute_name_rewrite prefixes the
        # existing name as the slug source.
        assert check({"model": "opus", "description": "Fix tests",
                      "name": "fixer"}) is None
        assert compute_name_rewrite(
            {"model": "opus", "description": "Fix tests", "name": "fixer"},
            "opus") == "opus-fixer"
        assert check({"model": "fable", "description": "Vet draft",
                      "name": "draft-vet"}) is None            # the observed gap
        assert compute_name_rewrite(                            # ...now self-heals
            {"model": "fable", "description": "Vet draft", "name": "draft-vet"},
            "fable") == "fable-draft-vet"
        assert check({"model": "opus", "description": "Fix tests",
                      "name": "Opus-Fixer"}) is None          # case-insensitive
        assert compute_name_rewrite(
            {"model": "opus", "description": "Fix tests", "name": "Opus-Fixer"},
            "opus") is None                                    # already fine
        assert check({"model": "sonnet", "description": "Scan",
                      "name": "opus-scanner"}) is None          # wrong model in name
        assert compute_name_rewrite(
            {"model": "sonnet", "description": "Scan", "name": "opus-scanner"},
            "sonnet") == "sonnet-opus-scanner"  # re-prefixed, not stripped —
            # the settled design takes the existing name as-is as the slug
        # Mirror check KEPT: a title that DOES carry `<model>: ` must match
        # the model field — a matching prefix is tolerated, not required.
        assert check({"model": "opus", "description": "opus: Fix tests",
                      "name": "opus-fixer"}) is None          # tolerated
        assert check({"model": "opus", "description": "sonnet: Fix tests",
                      "name": "opus-fixer"}) is not None      # mismatch denies
        assert check({"model": "opus", "name": "opus-mech-rerun",
                      "description": "sonnet: F-2 re-run"}) is not None
        # A wrong name is REWRITTEN when the title is clean or matches —
        # nothing here needs an operator (2026-09-15: was a deny before the
        # verb conversion).
        assert check({"model": "opus", "name": "mech-rerun",
                      "description": "opus: F-2 re-run"}) is None
        assert compute_name_rewrite(
            {"model": "opus", "name": "mech-rerun",
             "description": "opus: F-2 re-run"}, "opus") == "opus-mech-rerun"
        # PRECEDENCE: a title MISMATCH still denies even when the name also
        # needs a rewrite — main() only attempts the rewrite when check()
        # returns None, so a mismatch pre-empts it. Locks in the module
        # docstring's "takes PRECEDENCE" claim.
        assert check({"model": "opus", "name": "mech-rerun",
                      "description": "sonnet: F-2 re-run"}) is not None

        # ── Rewrite mechanics: _slugify, compute_name_rewrite, the
        # never-silent fallback, and the process-boundary shape replay-bench
        # cannot score today (it has no "rewrite" outcome kind; see the
        # critique-pass message to the judgment desk, 2026-09-15). ──
        assert _slugify("") == "task"
        assert _slugify("   ") == "task"
        assert _slugify("!!!") == "task"       # nothing but disallowed chars
        assert _slugify("A B_C-D!!e") == "a-b_c-d-e"
        assert _slugify("x" * 30) == "x" * 24  # capped
        # cap lands exactly on a separator -> the post-cap strip fires
        assert _slugify("x" * 23 + "-" + "y" * 5) == "x" * 23
        import re as _re_test
        for _t in ["", "   ", "!!!", "A B_C-D!!e", "x" * 30,
                  "x" * 23 + "-" + "y" * 5, "üñïçødé çhaos"]:
            _s = _slugify(_t)
            assert _s and _re_test.fullmatch(r"[a-z0-9_-]+", _s), (_t, _s)
        # Never-silent fallback: force compute_name_rewrite to raise and
        # confirm _rewrite_or_none reports NOT ok, rather than passing
        # silently. compute_name_rewrite does not raise on any known input
        # (the 'task' fallback covers empty slugs), so this is the only way
        # to exercise the directive's named fallback at all.
        _real_compute = compute_name_rewrite
        globals()["compute_name_rewrite"] = lambda *a, **k: (_ for _ in ()).throw(
            ValueError("forced"))
        assert _rewrite_or_none({"model": "opus"}, "opus") == (None, False)
        globals()["compute_name_rewrite"] = _real_compute
        assert _rewrite_or_none({"model": "opus"}, "opus")[1] is True  # restored

        # Process boundary: run the real script as a subprocess (stdin JSON
        # -> stdout JSON), the same boundary replay-bench exercises for
        # every OTHER hook — done here because replay-bench's KINDS has no
        # "rewrite" entry yet and extending it is outside this lane's write
        # boundary (dg-45 critique pass).
        import subprocess as _sp_test
        def _run_hook(payload, firelog):
            env = dict(os_mod.environ)
            env["CLAUDE_DISPATCH_GUARDS_CONFIG"] = "/nonexistent"
            env["CLAUDE_DISPATCH_GUARDS_FIRELOG"] = firelog
            return _sp_test.run(
                [sys.executable, os_mod.path.realpath(__file__)],
                input=json.dumps(payload), capture_output=True, text=True,
                env=env)
        _fl = os_mod.path.join(tempfile.mkdtemp(), "fires.jsonl")
        _proc = _run_hook({"tool_name": "Agent", "tool_input": {
            "subagent_type": "general-purpose", "model": "opus",
            "description": "Fix the tests"}}, _fl)
        assert _proc.returncode == 0, (_proc.returncode, _proc.stdout, _proc.stderr)
        _out = json.loads(_proc.stdout)
        _hso = _out["hookSpecificOutput"]
        assert _hso["updatedInput"]["name"] == "opus-fix-the-tests", _hso
        assert "permissionDecision" not in _hso, _hso  # wave0 b2/b3 shape
        assert _hso["hookEventName"] == "PreToolUse"
        # everything else in tool_input rides along unchanged
        assert _hso["updatedInput"]["description"] == "Fix the tests"
        _fires = [json.loads(_l) for _l in open(_fl, encoding="utf-8")]
        assert any(_f["mode"] == "rewrite" for _f in _fires), _fires
        assert any("opus-fix-the-tests" in _f["reason"] for _f in _fires), _fires
        # a still-denied case (missing model) stays exit 2, nothing rewritten
        _fl2 = os_mod.path.join(tempfile.mkdtemp(), "fires.jsonl")
        _proc2 = _run_hook({"tool_name": "Agent", "tool_input": {
            "subagent_type": "general-purpose",
            "description": "Fix the tests"}}, _fl2)
        assert _proc2.returncode == 2, (_proc2.returncode, _proc2.stdout)
        assert _proc2.stdout.strip() == ""
        # ── Site-Policy (Config): deny + ask greifen ──
        with tempfile.NamedTemporaryFile("w", suffix=".json",
                                         delete=False) as tf:
            tf.write('{"deny_models": ["haiku"], "ask_models": ["fable"],'
                     ' "discipline_doc": "dispatch skill"}')
            cfgp = tf.name
        os_mod.environ["CLAUDE_DISPATCH_GUARDS_CONFIG"] = cfgp
        _reset_policy_cache()
        assert check({"subagent_type": "Explore", "model": "haiku"}) is not None
        assert "site policy" in check({"model": "haiku"})
        assert needs_model_ask({"model": "fable",
                                "description": "fable: Vet edit"})
        assert needs_model_ask({"subagent_type": "Explore", "model": "fable"})
        assert not needs_model_ask({"model": "opus",
                                    "description": "opus: Grind logs"})
        assert not needs_model_ask({"subagent_type": "plugin-dev:agent-creator",
                                    "model": "fable"})  # pinned type: bypass
        # doc_ref now renders into the REWRITE reason, not a check() deny —
        # the name-missing case moved off check() entirely (2026-09-15).
        _fl3 = os_mod.path.join(tempfile.mkdtemp(), "fires.jsonl")
        env3 = dict(os_mod.environ)
        env3["CLAUDE_DISPATCH_GUARDS_CONFIG"] = cfgp
        env3["CLAUDE_DISPATCH_GUARDS_FIRELOG"] = _fl3
        _proc3 = _sp_test.run(
            [sys.executable, os_mod.path.realpath(__file__)],
            input=json.dumps({"tool_name": "Agent", "tool_input": {
                "model": "opus", "description": "Fix tests"}}),
            capture_output=True, text=True, env=env3)
        assert _proc3.returncode == 0, (_proc3.returncode, _proc3.stdout)
        _fires3 = [json.loads(_l) for _l in open(_fl3, encoding="utf-8")]
        assert any("dispatch skill §5" in _f["reason"] for _f in _fires3), _fires3
        os_mod.unlink = None  # noqa: keep tempfile (test artifact)
        # Workflow lane (2026-07-19): every Workflow launch asks.
        assert needs_workflow_ask({"tool_name": "Workflow"})
        assert not needs_workflow_ask({"tool_name": "Agent"})
        assert not needs_workflow_ask({})
        # ── Escalation lane (2026-07-28): subagent may not spawn ask-tier ──
        sub = {"agent_id": "a1", "tool_name": "Agent"}
        esk = escalation_deny({**sub, "tool_input": {
            "model": "fable", "description": "fable: Vet edit"}})
        assert esk is not None and "dispatcher" in esk
        # main session unaffected: it still ASKS, it is not denied
        assert escalation_deny({"tool_name": "Agent", "tool_input": {
            "model": "fable", "description": "fable: Vet edit"}}) is None
        # sideways/down from a subagent: untouched
        assert escalation_deny({**sub, "tool_input": {
            "model": "sonnet", "description": "sonnet: Scan"}}) is None
        assert escalation_deny({**sub, "tool_input": {
            "model": "opus", "description": "opus: Grind"}}) is None
        # pinned agent types bypass ENFORCED_TYPES but NOT this lane:
        # same spend from the same context (docstring rationale)
        assert escalation_deny({**sub, "tool_input": {
            "subagent_type": "plugin-dev:agent-creator",
            "model": "fable"}}) is not None
        assert escalation_deny({**sub, "tool_input": {}}) is None
        assert escalation_deny({**sub}) is None  # no tool_input at all
        # ORDER (the load-bearing wiring): a subagent's ask-tier dispatch
        # must hit deny, never the dialog — main() calls escalation_deny
        # BEFORE needs_model_ask. Pinned by source inspection, because
        # both paths exit the process.
        import inspect
        _src = inspect.getsource(main)
        assert _src.index("escalation_deny") < _src.index("needs_model_ask"), \
            "escalation deny must precede the fable ask in main()"
        assert _src.index("escalation_deny") < _src.index("error = check"), \
            "escalation deny must precede the name/model check in main()"

        # ── Undelivered-text note (2026-08-05 lane) ────────────────
        def _write_transcript(path, events):
            with open(path, "w", encoding="utf-8") as f:
                for ev in events:
                    f.write(json.dumps(ev) + "\n")

        def _prompt(text):
            return {"message": {"role": "user", "content": text}}

        def _atext(text):
            return {"message": {"role": "assistant", "content": [
                {"type": "text", "text": text}]}}

        # mkdtemp, not TemporaryDirectory: the deny-lane test above
        # sabotages os.unlink on purpose, which breaks cleanup — the
        # dir dies with /tmp, same as that lane's own tempfile.
        _d = tempfile.mkdtemp()
        if True:
            _t = os_mod.path.join(_d, "t.jsonl")
            # (a) substantial pre-call text this turn → note fires,
            # carries the char count.
            _write_transcript(_t, [_prompt("go"), _atext("e" * 900)])
            _note = undelivered_note({"transcript_path": _t})
            assert "NICHT gerendert" in _note and "900" in _note
            # (b) a bare route line stays under the threshold → silent.
            _write_transcript(_t, [_prompt("go"),
                                   _atext("dispatching to fable")])
            assert undelivered_note({"transcript_path": _t}) == ""
            # (c) text BEFORE the last prompt is delivered history, not
            # this turn's undelivered text → silent (stale window).
            _write_transcript(_t, [_atext("e" * 900), _prompt("go")])
            assert undelivered_note({"transcript_path": _t}) == ""
            # (d) fail-soft: missing transcript / no path → silent.
            assert undelivered_note({"transcript_path":
                                     _t + ".gone"}) == ""
            assert undelivered_note({}) == ""

        print("agent-model-gate: all tests passed")
        sys.exit(0)
    sys.exit(main())
