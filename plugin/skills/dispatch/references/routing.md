# Tier routing evidence — which tier a dispatch takes

_The `## Site overlay` section at the end carries the operating
site's bindings and standing decisions; it wins on conflict with
the portable evidence here._

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
  fresh-context verdict on a bounded artifact.** Width prices
  differently by KIND, and one sentence for both steers dispatchers
  off the splits that save tokens. REPLICATED fan-outs — the same
  work k times, parallel reviewers on one artifact, eval arms —
  multiply cost by width; a harness's prescribed width (skill,
  effort level, workflow) is a default someone else chose, not a
  judgment about this task. PARTITIONED fan-outs, where the work is
  divided across lanes, do not: each lane's context grows only with
  its OWN calls, so the per-call re-read of the accumulated prefix —
  quadratic in a lane's call count, and the dominant term on any
  long lane — shrinks with splitting, while width adds one marginal
  arrival context per lane. Above a crossover in calls-per-lane,
  splitting is cheaper on tokens ALONE, wall-clock arguing the same
  way. Crossover n* = sqrt(4·C_lane / (w_r·g)) — C_lane the marginal
  lane's weighted startup, g the per-call context growth, w_r the
  cache-read weight. Measure them per workload rather than carrying
  a number (`tools/lane-cost.py`, source repo); g in particular is
  growth over calls 2..n, and folding the one-time per-lane startup
  into it inflated a real measurement by half again. Grade: measured
  once, on one read-only workload, with the single-lane arm MODELED
  and never run — the direction is structural, the constants are not.
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

Site-overlay slots — the ranked model table with its staleness
stamp, which model each role names, pool/cost bindings, standing
exceptions — are filled by the `## Site overlay` section below
(relocated from the site corpus 2026-09-10 on the corpus-relocation
ablation's verdict; record: dotfiles
claude/records/corpus-relocation-2026-09-10/). Still corpus-side by
necessity: the always-loaded SEAM conventions that fire before this
skill loads — the route line naming "dispatching to <model> — <tier
basis>" or "inline: <why>", the intake gauge, the brief-family
dispatch default, and the standing tier defaults — an inline route
never loads this skill at all (the ablation's intake arms held on
those retained lines alone).

## Site overlay — this installation's bindings (win on conflict)

Consumed at dispatch-compose and tier-choice moments, which this
skill's gate-forced load precedes. The site corpus keeps the
intake-seam conventions and the standing defaults (sonnet for
brief-covered execution and discovery; site roles: cheapest daily
tier = sonnet, review tier = opus, top tier = fable) and points
here for everything below.

### Cost model, rankings, lineup

Glossary: **intelligence** = how hard a problem the model handles
unsupervised. **taste** = code quality, API design, UI/UX, copy.
**cost** = what the operator actually pays (Claude sub; no
Codex/OpenAI currently): per-token price rises sonnet → opus →
fable, but fable draws a separately capped pool (as of 2026-07-27:
50% of the weekly sub limit); other tiers draw the slack remainder
— so cross-tier token comparisons are the wrong currency: a
dispatch spending a multiple of the inline token volume still
relieves the capped pool, and on a fable session fable-tokens-spent
is the routing cost.
Rankings 1–10, higher = better on every column.
Lineup as of 2026-09-10: the set now names Fable 5.1
(`claude-fable-5-1`) while live sessions still run
`claude-fable-5` — the row below prices the fable TIER and both
ids resolve to it, so this is a set that GAINED a member, never a
rename. Rankings as of 2026-07-18; opus row's
bar-clearance corroborated in operation (as of 2026-08-06);
re-check when
the model set or the payment model (sub → API) changes. The
sonnet–opus gap carries a measured domain split (2026-08-08;
paired probes, pre-registered criteria, arms not blind, n=1 per
shape): brief-covered execution tied across the gap while the
fresh-context verdict opened it (≥2, the blocking finding
opus-side only) — the intelligence number prices unsupervised
judgment, not briefed execution; the site corpus's sonnet
execution default and the opus verdict default below are its
operational rendering.

| model     | intelligence | taste |
|-----------|--------------|-------|
| fable-5   | 9            | 9     |
| opus-5    | 7            | 8     |
| sonnet-5  | 5            | 7     |

### Fable dispatches — the reviewer default

OPUS is the default fresh-context reviewer even on fable-authored
bounded artifacts (operator decision) — opus-tier fresh review has
caught a blocking defect in a fable-authored artifact, and the one
paired fable-vs-opus measurement to date had the opus arm
out-bitting the fable arm (single domain, arms not blind). A fable
dispatch is an operator-named exception, not a tier default; the
top-tier context/cost facts and the fan-out width rule are in the
portable half above.

### Haiku — the register's certification basis

No gate denies haiku and none asks — the register, not a veto, is
what places it. Certified as of 2026-08-10: fixed-schema
enumeration, on a paired haiku-vs-sonnet probe over identical §3b
briefs with criteria committed before any arm output, tied at full
marks for a third of the sonnet price. Outside a certified class
haiku is not the default — a misroute there is prose-governed, not
blocked.

### Veto-gates — conduct at the dialog

The plugin's veto-gates pause fable dispatches, Workflow launches,
and config writes for a one-click operator veto; subagent pushes
are denied outright — the dispatcher pushes after verification. A
gate receives a decision already made and stated; deferring the
decision to the dialog is the failure. The decision-complete bar,
the gaps-surfaced-beat-gaps-filled rule, and the conventions that
keep the veto cheap (the model rides the NAME, fan-outs state
count × tier, the chosen model named in the turn's final message)
are canonical in SKILL.md §1.
