# Site overlay template

_A TEMPLATE, not shipped policy — nothing in this file is read by
any guard or skill. Fill it in and paste it as your own
`## Site overlay` section. Copy the section below into your own
site corpus (or straight into your fork's `references/routing.md`,
replacing its `## Site overlay` section) and replace every `UNSET`
with your own binding. Slot names are drawn from
`references/routing.md`'s own
`## Site overlay` section — read it first; it also carries the
portable tier-ROLE rules this overlay attaches to. `python3
plugin/hooks/_dispatch_common.py --doctor` reports whether your
INSTALLED `routing.md` currently carries a filled-in overlay at all —
it does not check whether the slots below are still `UNSET`; that
reading is yours to do once, by eye, after you paste._

## Site overlay — this installation's bindings (win on conflict)

### Cost model, rankings, lineup

- **Ranked model table, with an as-of stamp:** `UNSET` — the
  models you actually dispatch to, each ranked 1–10 on
  *intelligence* (how hard a problem the tier handles
  unsupervised) and *taste* (output quality where craft matters —
  code, API design, UI/UX, copy), stamped with the date the
  ranking was made and named against what would invalidate it (a
  lineup change, a pricing change). A table with no date is a
  table nobody can tell is stale.
- **Pool/cost bindings:** `UNSET` — what you actually pay:
  subscription vs. API, whether any tier draws from a separately
  capped pool (cross-tier token comparisons are the wrong
  currency when one does), and which budget runs out first for
  you.

### Standing decisions

- **Tier roles — cheapest daily / review / top:** `UNSET` — which
  of your models fills each of the three portable roles
  `references/routing.md` defines (cheapest daily tier,
  fresh-context review-tier default, top tier).
- **Fresh-context reviewer default and its exceptions:** `UNSET`
  — the tier verdict stages route to by default, and any named
  exception (e.g. reserving the top tier for open design tension
  rather than routine review).
- **Denied / ask tiers:** `UNSET` — tiers this site refuses
  outright or gates behind an operator yes/no before every
  dispatch. This is the ROUTING-TABLE-level statement of the
  decision; `deny_models` / `ask_models` in
  `dispatch-guards.json` are its mechanical enforcement — state
  both, they answer different questions (why vs. what the guard
  actually does).
- **Refusal-classifier domains:** `UNSET` — which of your tiers
  decline which content domains, if any
  (`references/routing.md`'s "a tier's refusal classifiers are a
  routing input" rule) — a site fact, not portable, since it
  depends on which models you actually run.

### Certified cheap-tier classes

- **Register basis:** `UNSET` — if `~/.claude/readiness.json`
  names any certified classes for a cheaper-than-default tier
  (dispatch skill §6), the evidence behind each certification
  (what was measured, against what criterion) belongs here or
  pointed to from here — the register itself carries only the
  verdict, not the basis.
