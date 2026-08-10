# Tier routing evidence — which tier a dispatch takes

Reference of the `dispatch` skill (operational corpus — see
SKILL.md's governance header). Consumer: the dispatching session,
any tier, at the moment a dispatch's MODEL is chosen — and, for
the final bullet, when weighing whether a fresh-context review is
worth its spend. This file
carries the portable evidence; it deliberately names tier ROLES,
not models. A site's own corpus overlays it with the concrete
lineup — a ranked model table, pool and cost bindings, and standing
operator decisions (which model is the review default, which tiers
are exceptions or denied). On any conflict the site overlay wins:
it encodes decisions this file cannot know.

Three roles, defined by function:

- **Cheapest daily tier** — the least expensive model in daily use
  (a site may keep cheaper models gated behind purpose-built
  harnesses; those are not "in daily use").
- **Review tier** — the tier the site names as its fresh-context
  reviewer default.
- **Top tier** — the most capable model available; typically the
  scarcest.

Axes used below (the third is a site binding): **intelligence** =
how hard a problem the tier handles unsupervised; **taste** =
output quality where craft matters, in any medium; **cost** = what
the operator actually pays — pools, caps, and prices are site
facts, slotted at the tail.

The evidence:

- **The executor's tier buys the RESIDUAL judgment a brief leaves
  it.** In under-specified work that ships, intelligence dominates,
  then taste, and cost decides only ties — but a decision-complete
  brief with surfacing mechanisms (exhaustive-accounting clauses,
  STOP-and-escalate criteria) moves that judgment to the
  dispatcher, so brief-covered execution and discovery DEFAULT TO
  THE CHEAPEST DAILY TIER; the verdict-stage reviewer default and a
  site's readiness-register certifications override. Measured
  across a dispatch log's window: every recorded dispatch failure
  traced to a brief defect, none to tier capacity — a higher tier
  bought as insurance against one's own brief defects is the
  recorded waste shape; that spend belongs in brief quality.
- **Discovery shows no tier sensitivity.** Lookups, sweeps,
  enumeration, extraction — cheapest daily tier, always; the §3b
  enumeration form (references/forms.md) is what makes the cheap
  tier unable to silently under-report.
- **Same-tier review catches slips, not judgment errors.** Verdicts
  (grading, confirm/refute, synthesis) flip only under a smarter or
  a fresh reviewer. At the top tier no smarter reviewer exists; a
  fresh context removes self-blindness, not the judgment ceiling;
  mechanical checks turn judgment calls into pass/fail lookups.
  Verdict stages route to tier ≥ producer, capped at the site's
  review-tier default (SKILL.md §4 carries the full rule).
- **Under-bar output redone one tier up is the cheap correction;
  iterating at the failing tier is not.** Judge the output, never
  the price tag — and never pre-emptively up-tier on price fear:
  the redo path is what makes the cheap default low-risk.
- **A top-tier subagent has less context than the dispatching
  session and costs the most; its comparative advantage is the
  fresh-context verdict on a bounded artifact.** Fan-outs multiply
  cost by width — a harness's prescribed width (skill, effort
  level, workflow) is a default someone else chose, not a judgment
  about this task.
- **A tier's refusal classifiers are a routing input, not an
  accident.** Where a tier's safeguards decline the DOMAIN the work
  sits in, it is the wrong tier for that work whatever its rank —
  benign work adjacent to a restricted domain trips the same
  classifier, and the loss is a whole reply, mid-turn. Two
  consequences: the choice is made at SESSION START, not at the
  dispatch seam, because the session model is what meets the
  material; and since every turn re-sends the prefix, once flagged
  material is IN the context the cure is a restart on another tier —
  rephrasing the next message leaves the trigger in place. Which
  tiers decline which domains is a site fact (site overlay).
- **What a fresh reviewer buys is independence, not verification
  effort.** However well a builder verifies its own work, it cannot
  see a defect that lives outside its briefed scope or inside its
  own premises — the blind spot is in the context doing the
  checking. Scope fresh-context review to self-blindness risks
  (completeness claims, surfaces whose wrongness is silent,
  statistical findings — briefed to refute — and a session's own
  booked verdicts); run mechanical verifiers anywhere, and skip
  instructed "double-check yourself" prose everywhere (source: the
  operator corpus' fresh-context verification rule, Insurance).

Site-overlay slots this file expects but cannot fill: the ranked
model table with its staleness stamp; which model each role names;
pool/cost bindings (what the operator actually pays, which pools
are capped); standing exceptions ("model X only as operator-named
exception", denied models); and the always-loaded SEAM conventions
that fire before this skill loads — the route line naming
"dispatching to <model> — <tier basis>" or "inline: <why>", the
intake gauge, and the brief-family dispatch default. Those live in
the site corpus by necessity: an inline route never loads this
skill at all.
