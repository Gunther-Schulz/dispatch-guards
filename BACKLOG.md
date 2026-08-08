# dispatch-guards — backlog

Two grades. **Parked** items carry their named missing evidence or
trigger. **Ready** items are decision-complete: design decided,
verifier named, done-criterion stated. Items leave by commit ref, or
are dropped with a one-line reason.

## Open

- **READY 2026-08-08 — the 0.6.x release shipped with the repo's own
  verify block RED: replay-bench 2 mismatches, both agent-model-gate;
  fix the corpus case, then settle the escalation-ordering half.**
  Found by a fresh opus review post-release (the releasing session ran
  the hook batteries but never bench command #1 — the lesson is booked
  in the dotfiles record rank-probe-2026-08-08.md). Two halves:
  (a) LANDED d2fdfdb (2026-08-08, sonnet dispatch, verified by the
  dispatcher's own bench run): guards.jsonl:31 flipped to `block` +
  lane-change note. Bench now 39/40, false fires 0 — the item's
  "40/40 green" presumed (b) settled; the sole remaining mismatch is
  (b)'s line 33, red until the ordering decision below lands.
  (b) CARRIES A DESIGN DECISION: guards.jsonl:33 (subagent + fable +
  UNNAMED, expect escalation deny) now hits the mandatory-name block
  first — main() consults check() before escalation_deny(), so an
  escalating subagent's first bounce teaches "add a name" instead of
  "return the question to your dispatcher"; the named retry does
  reach the escalation deny (no leak, one wasted round). Decide:
  reorder so escalation_deny precedes the name block for subagent
  ask-tier payloads, or accept the two-bounce path and update the
  corpus case to expect the name block. Either way, add battery
  coverage for the check-vs-escalation ordering (the existing
  ordering assert pins escalation-vs-ask only).

- **READY 2026-08-08 — brief-reminder's missing_channel deny_text
  names a repair that cannot clear the newly-caught named shape.**
  Converging evidence from two independent arms of the rank probe:
  the deny text ends "…or pass run_in_background: false for a
  synchronous dispatch", but for a NAMED dispatch the flag is already
  overridden by the name (is_background reads the name alone), so the
  advised retry denies identically — repair-loop / override-reflex
  class. Design: deny_text() gains the payload parameter its sibling
  tail_mode_mismatch_deny_text already takes and, when a name is
  present, states the real repair ("a named dispatch is background —
  paste the background channel line"). Verifier, red-first: probe
  {name, run_in_background:false, no channel} and assert the deny
  text names a repair that actually clears on retry; current text
  fails that assert.

- **READY 2026-08-08 — briefs to cheaper tiers lack the two surfacing
  mechanisms that make the cheap-tier default safe, so the tier gets
  bought as insurance against brief defects instead.** Grounding: an
  operator-relayed opus-desk retrospective graded 4 of its 7 opus
  dispatches as needed-only-because-the-brief-was-defective, and named
  the two mechanisms that would have made the sweep-shaped lanes
  sonnet-safe; the operator corpus's residual-judgment rule now rests
  on briefs carrying them. Design: §1 (or §3b where sweep-specific)
  gains two clauses — (a) post-sweep accounting: after any sweep or
  multi-site change, the report dispositions EVERY hit as fixed /
  correct / excluded / still-wrong (first real run returned 65
  instances after three sweeps each believed the class closed); (b)
  instrument-positive: a brief commissioning a pattern-scoped sweep
  names one member the pattern provably catches, so a zero-hit result
  is distinguishable from a dead pattern. Verifier: skill-craft
  authoring checks on the final render + replay of the motivating
  case against the clause text (the 65-instance accounting run and
  the four-of-five site miss must both fail a clause-less brief and
  pass a compliant one, on paper). Done: clauses landed in the skill,
  JOURNAL line in the corpus repo.

- **READY 2026-08-08 — graduate the outcomes-vs-sites candidate from
  dev-notes into §1's settled-design part.** It has now fired twice
  from opposite directions (2026-08-07: an outcome-criterion found a
  call site the brief's site list missed; 2026-08-08: a site-shaped
  brief left a defect the outcome would have caught), and the second
  firing was briefed by a session that had READ the candidate in
  dev-notes hours earlier — evidence the clause is consulted where it
  lives, not where briefs are written, so the fix is relocation into
  §1, not sharper wording. Design: one clause in §1's settled-design
  part — criteria stated as OUTCOMES out-reach criteria stated as
  edit sites; name the observable the change must produce, then the
  known sites, never the sites alone. Verifier: skill-craft render
  checks; the two firing cases both satisfied by the clause as
  written. Done: clause in §1, dev-notes candidate marked graduated,
  JOURNAL line in the corpus repo.

- **READY 2026-08-08 — §1 gains the two commit-plan clauses the
  name-lane build halted on.** Both from executor escalations in one
  dispatch, both spec defects a brief-form clause prevents: (a) in a
  repo with a payload-version guard, a brief-prescribed commit
  sequence orders the version-bump commit FIRST (the dotfiles
  pre-commit `unbumped_plugins` guard reads the staged manifest and
  tolerates later same-batch commits by comparing against origin);
  (b) an item that must record a commit's ref cannot share that
  commit — the brief either orders it into a LATER commit or splits
  the pathspec. Verifier: replay the halted dispatch's two gaps
  against the clause text — both must be prevented as written.
  Done: clauses in §1's write-boundaries part, JOURNAL line in the
  corpus repo.

- **READY 2026-08-08 — §1 gains a declared-exemption repair lane so a
  halt-worthy gap with an executor-derived fix does not cost a full
  round trip.** Grounding: the name-lane build's executor derived the
  exact commit-reorder fix with evidence, halted per the box, and the
  dispatcher approved it unchanged — a round trip spent ratifying a
  repair already reasoned out. Design: the brief skeleton's
  write-boundaries part gains an optional pre-authorized repair
  class — "if the commit plan collides with a repo guard, reorder to
  satisfy the guard and report the permutation as a deviation" — the
  same declared-exemption shape the corpus prescribes for guards,
  applied to briefs; novel deviations still halt. Verifier: replay
  the name-lane halt against the clause — GAP 1 resolves without a
  round trip, GAP 2 (self-referential ref, not a pre-named class)
  still halts. Done: clause in §1, JOURNAL line in the corpus repo.

- **READY 2026-08-08 — §1's Background part gains per-line provenance
  grades, closing the citation pass-through.** Grounding: the
  2026-08-08 observation "a Background section claimed dispatcher
  verification over a citation the dispatcher never opened" — its two
  rule candidates are the design, decision-complete as written there
  (per-line OPENED-or-carried-with-provenance; audit findings
  verified at the brief boundary where testimony becomes
  instruction). Verifier: replay the phantom-citation case — the
  unopened line must be un-writable as "established" under the
  clause. Done: clauses in §1's Background part, JOURNAL line in the
  corpus repo.

- **READY 2026-08-07 — a data-file report names the file's PROSE field
  names, and the dispatcher then queries the wrong keys.** The §3b
  enumeration brief assigns a data file and the tail returns a pointer
  to it. Nothing requires the report to carry the file's ACTUAL key
  set, so the agent describes its schema in prose — and prose drifts
  from the bytes it describes.
  Measured 2026-08-07, twice in one round: an agent reported a JSONL
  field as `command_truncated_400` where the file writes
  `command_verbatim_truncated_to_400_chars`, and a second reported
  `question_or_null` for `the_question_it_appears_to_answer_quoted_
  from_surrounding_text_or_null`. The dispatcher queried the reported
  names, got null on every row, and read the nulls as a DEFECT IN THE
  DATA — a wrong finding about the agent's work, caused by the report
  form. Caught only because 100% null looked implausible.
  This is the corpus paraphrase-drift rule (a label over its own body)
  landing on a schema instead of a status header, and the fix is the
  same one the corpus prescribes: carry the body, not the label.
  Design: the §3b data-file provision gains one clause — the returning
  message quotes the file's real key set, taken from the file
  (`jq -r 'keys_unsorted|@csv' <file> | head -1` for JSONL), never
  retyped from memory. One line in the brief, one line in the report.
  Verifier, red-first: replay tonight's two reports against the clause
  — both fail it as written (neither carries a key set); a report
  carrying the jq output passes. And a negative: a dispatch assigned
  NO data file must not be asked for a key set, so the clause fires
  only where a data file was assigned.

- LEFT 2026-08-08 by 5b31814: brief-reminder background predicate (READY 2026-08-07).

- **PARKED 2026-08-05 — worktree skill: name the failure SHAPE of a
  missing dependency tree (hang, not error).** The skill already has
  the section this belongs to — `plugin/skills/worktree/SKILL.md:87`,
  "A fresh worktree has no untracked state" — so this is a WIDENING of
  an existing rule, one clause, not a new section.

  *The gap.* The existing text covers **correctness**: it names
  dependency trees, virtualenvs, and gitignored files as absent, and
  tells the reader to prove the worktree resolves the project's own
  code before trusting a check run inside it. What it does not cover is
  **failure shape**. When the dependencies are simply missing —
  concretely, `node_modules` absent — the suite does not fail with a
  clear error. It wedges until the documented **900-second timeout**:
  the "hang" trap. A reader who has fully internalised "a fresh
  worktree has no untracked state" still loses the debugging time,
  because nothing tells them the symptom of the missing dep is a
  15-minute wedge rather than a stack trace.

  *Evidence.* Four recurrences across Node worktrees, all `node_modules`.
  On 2026-08-02, two of fifteen minutes of debugging went to exactly
  this; the cache-fix runbook records both "hangs" that day as this
  artifact. The 900s figure is what makes the clause actionable — it
  tells the reader the wedge is bounded and diagnosable, not a genuine
  deadlock to be chased.

  *Candidate text (one clause, in the existing section).* The absent
  dependency tree surfaces as a 900-second wedge, not an error —
  provision before running anything that imports. The fix is a symlink to the main
  checkout's tree, which the section's existing isolation note already
  blesses for third-party deps (relative-path imports resolve
  worktree-local and pass the probe even with deps shared by symlink).

  *NAMED MISSING EVIDENCE — this is why it is parked, not ready.* The
  clause asserts a failure SHAPE, and the evidence is one ecosystem:
  four Node worktrees is a real recurrence, but the Python and Go
  equivalents have not been observed failing this way. Two exits:
  (a) observe or reproduce the hang-not-error shape in a second
  ecosystem, which promotes the clause as written; or (b) scope the
  clause explicitly to Node, which closes the evidence gap by
  narrowing the claim and makes the item ready as-is. Choosing (b) is
  a design decision, not a fallback — decide it deliberately.

  *Execution requirements (both were reasons NOT to do it inline).*
  (1) This is a plugin skill: the edit must go through
  `skill-craft:release-plugin` — version bump, marketplace pin,
  operator `/reload-plugins` handoff. Editing the source and leaving
  it unreleased puts source and served version out of step, which is
  the exact staleness the plugin-stale-gate exists to catch.
  (2) Corpus edits here follow `anneal-dev`, and widening an existing
  rule rather than adding one is precisely the judgment that protocol
  exists to make carefully.

  *Done-criterion.* The clause lands inside the existing section (no
  new heading), the ecosystem question is resolved by (a) or (b) with
  the choice stated, and the plugin is released and reload-verified.

- **PARKED 2026-08-06 — harvest deferred list: two §2/§4 corpus
  candidates** (status enum `DONE | DONE_WITH_CONCERNS | BLOCKED |
  NEEDS_CONTEXT` for the closing report; bounded fix-loop with
  breaker for dispatcher conduct). Full rationale + sources:
  `dev-notes/harvest-2026-08-06.md`, "Deferred". Named trigger:
  these are operational-corpus edits (forms.md §2 / SKILL.md §4)
  and go through the anneal-dev protocol with an operator GO —
  parked until that pass is convened, never folded in casually.

- **PARKED 2026-08-08 — forms.md §2's channel/binding paragraphs rest
  on two bindings contradicted by same-day probes (n=1 each): an
  unnamed `run_in_background: false` dispatch launched async, and an
  async agent's final text WAS delivered via the completion
  task-notification.** Missing evidence: a controlled probe pair
  (named/unnamed × run_in_background true/false) recording launch
  mode and whether the final text reaches the dispatcher. On
  confirmation, rewrite forms.md §2's 2026-07-30 binding paragraph,
  the channel-line rationale, and brief-reminder's mode logic.
  Entry: dev-notes/dispatch-OBSERVATIONS.md 2026-08-08.

## Done

- **DONE 2026-08-06 — fire-log blindness: the `shape` field.**
  Parked on the secrets-vs-usefulness decision; operator chose (b),
  the shape digest. `_dispatch_common.command_shape` now records a
  secret-free discriminator on every fire — verbs and flags only,
  operands dropped. The absence claim is pinned two ways: a case
  list per secret-carrier shape, and a property that constrains the
  OUTPUT ALPHABET (every emitted token is a separator, a degraded
  marker, a safe word, or a normalized flag), so a secret can only
  survive by being one of those. Both went red first — the case
  list caught `mysql -phunter2`, where the attached short-flag
  value passes any looks-like-a-flag pattern.

