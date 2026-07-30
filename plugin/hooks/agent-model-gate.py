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

Extension (2026-07-18, dispatch-discipline.md §5): the dispatch title
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
prose (dispatch-discipline.md §4). Subagents dispatching sideways or
down are untouched; nesting itself stays legal (3 layers by default).
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
    """Return an error message, or None (= allow through)."""
    subagent = tool_input.get("subagent_type")
    if subagent not in ENFORCED_TYPES:
        return None  # specialized/plugin agent: its definition pins the model
    model = tool_input.get("model")
    if model in _allowed_models():
        if model in policy()["deny_models"]:
            return (
                f"Model gate: `{model}` is denied by site policy "
                "(deny_models in the dispatch-guards config). Choose "
                "another tier."
            )
        desc = (tool_input.get("description") or "").strip()
        match = _title_re().match(desc)
        if not match:
            return (
                "Model gate: dispatch title must start with the strict "
                'prefix `<model>: ` (e.g. "opus: Migrate YAML keys") '
                "so every dispatch shows its model live in the UI "
                f"({doc_ref('§5')}). Title seen: {desc!r}."
            )
        if match.group(1).lower() != model:
            return (
                f"Model gate: title prefix {match.group(1).lower()!r} "
                f"diverges from model field {model!r} — the prefix is a "
                "verified mirror of the field; make them match."
            )
        name = (tool_input.get("name") or "").strip()
        if name and not name.lower().startswith(model + "-"):
            return (
                f"Model gate: agent name {name!r} must start with "
                f"`{model}-` — the teammate panel shows the NAME, not the "
                "title, so the name carries the model too "
                f'({doc_ref("§5")}). Example: "{model}-{name}".'
            )
        return None
    return (
        "Model gate: agent dispatch without an explicit `model` — the agent "
        "would silently inherit the session model. Choose deliberately per "
        "the model table (~/.claude/CLAUDE.md 'Model routing for "
        "dispatches') or project routing (e.g. PROZESS.md §1a). Even an "
        "intentional inherit must be made "
        "explicit as model:\"fable\". Name the choice in your reply."
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
            "im Script prüfen."
        )
    if payload.get("tool_name") not in ("Agent", "Task"):
        return 0
    tool_input = payload.get("tool_input") or {}
    error = check(tool_input)
    if error:
        print(error, file=sys.stderr)
        return 2  # blocking; stderr goes back as feedback to the main agent
    if grund := escalation_deny(payload):
        deny(grund, source="dispatch-guards/agent-model-gate")  # before the ask: a subagent gets the deny, not the dialog
    if needs_model_ask(tool_input):
        desc = (tool_input.get("description") or "").strip()
        ask(  # exits 0 with permissionDecision "ask"
            f"⚠️ FABLE-DISPATCH: {desc!r}. Teuerste Stufe; ihr "
            "komparativer Vorteil laut CLAUDE.md: Fresh-Context-Verdikt "
            "auf begrenztem Artefakt. Die Entscheidung ist getroffen — "
            "abbrechen, wenn der Einsatz sie nicht rechtfertigt."
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
                      "description": "haiku: Scan"}) is None  # default: kein deny
        assert not needs_model_ask({"model": "fable",
                                    "description": "fable: X"})  # default: kein ask
        assert check({"subagent_type": "statusline-setup"}) is None
        assert check({"subagent_type": "plugin-dev:agent-creator"}) is None
        assert check({"subagent_type": "claude", "model": "nonsense"}) is not None
        # Title-prefix extension (2026-07-18, format `<model>: <title>`):
        assert check({"model": "opus"}) is not None           # model ok, title missing
        assert check({"model": "opus", "description": "Fix tests"}) is not None
        assert check({"model": "opus", "description": "opus-fix-tests"}) is not None  # old format
        assert check({"model": "opus", "description": "opus: Fix tests"}) is None
        assert check({"model": "opus", "description": "Opus: Fix tests"}) is None
        assert check({"model": "opus", "description": "sonnet: Fix tests"}) is not None
        assert check({"subagent_type": "Explore", "model": "sonnet",
                      "description": "sonnet: Scan repo"}) is None
        assert check({"subagent_type": "Explore", "model": "fable",
                      "description": "fable: Review architecture"}) is None
        assert check({"model": "opus", "description": "opus:"}) is not None   # no title
        assert check({"model": "opus", "description": "opus: "}) is not None  # blank title
        # Name lane (2026-07-19): a given name must start `<model>-`.
        assert check({"model": "opus", "description": "opus: Fix tests",
                      "name": "fixer"}) is not None
        assert check({"model": "fable", "description": "fable: Vet draft",
                      "name": "draft-vet"}) is not None       # the observed gap
        assert check({"model": "opus", "description": "opus: Fix tests",
                      "name": "opus-fixer"}) is None
        assert check({"model": "opus", "description": "opus: Fix tests",
                      "name": "Opus-Fixer"}) is None          # case-insensitive
        assert check({"model": "sonnet", "description": "sonnet: Scan",
                      "name": "opus-scanner"}) is not None    # wrong model in name
        assert check({"model": "opus", "description": "opus: Fix tests"}) is None  # no name: unchanged
        # ── Site-Policy (Config): deny + ask greifen ──
        with tempfile.NamedTemporaryFile("w", suffix=".json",
                                         delete=False) as tf:
            tf.write('{"deny_models": ["haiku"], "ask_models": ["fable"],'
                     ' "discipline_doc": "dispatch-discipline.md"}')
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
        assert "dispatch-discipline.md §5" in check(
            {"model": "opus", "description": "Fix tests"})  # doc_ref greift
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
        print("agent-model-gate: all tests passed")
        sys.exit(0)
    sys.exit(main())
