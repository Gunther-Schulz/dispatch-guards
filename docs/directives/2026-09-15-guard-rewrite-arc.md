# Directive: guard-rewrite arc — 2026-09-15

Delegation: judgment desk = fable session `dispatch-guards-bc`;
executing desk = opus session `dispatch-guards-c2`. Operator GO
2026-09-15 ("1-3 is a GO drive this session (opus)
@dispatch-guards-c"). Declaration: BUILD run — closes at least as
many items as it opens.

REPORT-CHANNEL: SendMessage dispatch-guards-bc
Cadence: wave completions, decision rounds, close report;
batched digests for routine findings. Escalation returns the
question to the judgment desk — never an up-tier dispatch.

Base: main @ 0dbae0f (clean tree, single worktree, read at
compose time). Write boundary: the executing desk owns this
working copy for the arc; the judgment desk commits nothing here
after this directive's commit. Push of main to origin is
authorized standing (CLAUDE.md `## Carve-outs`), under the repo's
push rules (claim log first, its own invocation, never chained
with the push). The marketplace release stays the operator's act.

Wave 0 is authorized only once the operator's first-hand
confirmation of this delegation is on the executing desk's
record and acknowledged to the judgment desk.

## Origin and evidence (verified at the judgment desk, 2026-09-15)

Proposal from Lilly Guo (peer user of this plugin), each claim
checked:

- PreToolUse hooks can rewrite tool input via
  `hookSpecificOutput.updatedInput`; the modified input replaces
  the original before the tool runs (code.claude.com/docs/en/hooks,
  raw-fetched 2026-09-15; peer's live test: a Bash echo rewrite
  executed the rewritten command; an added `model: haiku` on an
  Agent call took effect and shows in the recorded call).
- All matching hooks see the ORIGINAL call, not each other's
  rewrites (docs: matching hooks run in parallel) — so a repair
  must live INSIDE the gate that would otherwise deny; a separate
  rewriting hook cannot satisfy another guard.
- UNVERIFIED, probe leg A: whether a PROMPT edit via updatedInput
  reaches the subagent's effective prompt (the peer's added
  prompt line was recorded but the subagent did not follow it).
- UNVERIFIED, probe leg B: whether updatedInput applies without
  `permissionDecision: "allow"` — a forced allow would suppress
  permission dialogs on rewritten calls (this site pins manual
  permission mode; silent dialog bypass is not shippable without
  an operator decision).
- Value basis, machine-wide fire log all-time counts:
  agent-model-gate 140 blocks, brief-reminder 171 denies,
  dispatch-skill-gate 71 denies. Every deny forces the full call
  (often a multi-kilotoken brief) to be recomposed and re-sent.

## Wave 0 — probes (gate both build items)

Arrangement: a THROWAWAY scratch project with a project-level
`.claude/settings.json` PreToolUse hook — never the operator's
global config (config writes are veto-gated; the scratch layout
must not mirror `.claude/`-shaped paths beyond the project's own
settings file). Probes are run from a session in that scratch
project (a cheap `claude -p`-class child or a dispatched lane —
the executing desk's call), and each records command + observed
output in the item body.

- Probe A (sentinel): hook rewrites an Agent call's prompt,
  appending "Open your report with the token PROBE-<rand>."
  Dispatch a trivial cheap-tier agent. Positive: the report opens
  with the token → prompt edits reach the subagent. Control: the
  same dispatch with the hook disabled must NOT carry the token.
  Both runs recorded.
- Probe B: same arrangement, hook returns updatedInput WITHOUT
  permissionDecision — observe (i) does the rewrite apply,
  (ii) does normal permission flow still run. Then the "allow"
  variant — observe dialog suppression.

Dispositions: A red → item 2's rewrite is impossible; the deny
lane stays; item 2 closes with the finding. B shows rewrite
requires forced "allow" → STOP and escalate to the judgment desk
before shipping any rewrite lane. A and B green → waves 1-2.

## Item 1 (wave 1) — model-gate name rewrite (agent-model-gate.py)

Settled design; implement exactly this:

- Condition: generic subagent_type AND valid non-denied `model`
  AND (`name` missing OR not prefixed `<model>-`).
- Action: REWRITE via updatedInput instead of deny.
  `name := "<model>-<slug>"` — slug from the existing name when
  one is present (prefix it), else derived from `description`
  (lowercase, `[^a-z0-9_-]` → `-`, collapse runs, trim `-`, cap
  ~24 chars), fallback slug `task`. Charset stays within
  `[A-Za-z0-9_-]`.
- Unchanged: missing/invalid model DENIES (the deny is a routing
  forcing-function — the operator's "name the choice" moment);
  title-mirror mismatch denies; escalation lane, Workflow ask,
  fable ask all unchanged.
- Fallback: any state where the rewrite cannot be computed →
  the existing deny. Never a silent pass.
- Fire log: rewrites are logged (action `rewrite`, reason naming
  old → new) so the fire-rate review can grade the lane. Staging
  note for the docstring: the staged-lane rule governs warn→deny
  promotion; this lane REPLACES a deny with a repair — its
  staging is the fire-log record plus first-runs-watched.
- Homes: docstring amended (canonical); README guard-roster row;
  `check-doc-drift` stays green.
- Tests: extend the `--test` bites (name-missing → rewrite JSON
  with expected name; wrong prefix → prefixed; missing model →
  still deny; slug charset valid) and `tools/corpus/guards.jsonl`
  + replay-bench expectations. Red-first: the new expectations
  run against the OLD implementation and fail (old denies where
  new expects rewrite); the report states the arrangement and the
  baseline result.

## Item 2 (wave 2) — brief-gate tail auto-append (brief-reminder.py)

Gated on Probe A green. Design settled where mechanical; one
stop-criterion where not:

- The `missing_tail` DENY lane becomes a rewrite that appends the
  correct tail block to the prompt.
- Tail KIND (execution vs read-only) is decidable only where a
  mechanical rule has near-zero false fires (mechanism bar).
  Implement the rewrite ONLY for the mechanically decidable
  class; the AMBIGUOUS class keeps the existing deny. If no
  decision rule meets the bar, that finding goes to the judgment
  desk as a decision round — do not ship a guessing heuristic.
- Channel line computed from `name` presence (named → SendMessage
  line; unnamed is reachable only by gate-exempt pinned types).
- Tail text source: the plugin's own shipped forms.md, read at
  fire time (path resolved relative to the hook) — never a second
  copy pasted into the hook (paraphrase-drift). A bite asserts
  the appended tail equals the forms.md tail after the same
  normalization the missing_tail detector uses.
- Unchanged this arc: the other three deny lanes (deny_text,
  tail_mode_mismatch, missing_sections) and both fire() lanes.
  `guard_modes` semantics for the rewrite lane defined in the
  docstring.
- Tests/homes: as item 1 — bites, corpus extension, replay-bench,
  README row, check-doc-drift, red-first stated.

## Item 3 — booking only (no build this arc)

Book into ITEMS.md (lifecycle vocabulary, slots per the carrier's
checker): dispatch SKILL.md slimming — a skill-craft Pareto pass
over the ~17k-token SKILL.md (68500 bytes measured 2026-09-15) to
cut per-session prefix cost; operational corpus, so governed by
CLAUDE-maintenance (structural restructure → fresh-context vet
before push). PARKED — named missing prerequisite: a
corpus-maintenance session with its own operator GO; out of this
arc's scope.

Also at arc start: book items 1 and 2 as READY entries (write-set
naming the hook files + corpus/bench files); close them by commit
ref at arc close per lifecycle rules. Wave 0's probe findings are
recorded in the item bodies (and LEDGER.md for the arc-level
facts).

## Verify (before any commit touching hooks)

The repo CLAUDE.md verify block, in full: replay-bench,
replay-bench --test, the per-hook `--test` loop under a fresh
XDG_DATA_HOME, check_devbook_form --test, worktree_doctor --test,
check-doc-drift, manifest parse. A guard change without a
guards.jsonl extension reports clean on the untested lane — the
corpus extension is part of each item, not optional.

Arc close: recommend the release (`skill-craft:release-plugin`)
to the operator — version bump prepared, the release act itself
is theirs.
