# dispatch-guards — backlog

Two grades. **Parked** items carry their named missing evidence or
trigger. **Ready** items are decision-complete: design decided,
verifier named, done-criterion stated. Items leave by commit ref, or
are dropped with a one-line reason.

## Open

- **PARKED 2026-08-06 — the fire log cannot answer the question the
  fire-rate review asks it.** `_dispatch_common.fire_log` records
  `ts, guard, mode, session_id, agent_id, tool_name, reason` — and
  `reason` is a CONSTANT string per guard lane (verified against a
  live fire: every push-claim-reminder record carries the same
  sentence). So the log proves a lane fired and never what it fired
  ON. A reviewer asking "is this lane firing on legitimate work?" —
  the promotion criterion for every staged lane, and the standing
  false-fire check for shipped ones — cannot compute it from the
  log; they can only count.

  *Grounding.* Today's `--push` false fire (`git remote set-url
  --push` denied as a push) had been live since the `--push` arm was
  minted. The fire log had been recording those fires the whole
  time, and could not have surfaced them: every record read
  identically to a legitimate push. It was found by accident, when
  probe commands in an unrelated session tripped the hook and the
  reason text did not match the command that caused it.

  *Candidate fix.* Add a truncated triggering command (or the
  tool_input digest) to the record — one field, `_REASON_MAX`-style
  cap, same fail-open write path.

  *NAMED MISSING DECISION — this is why it is parked, not ready.*
  Bash commands routinely carry secrets (tokens in URLs, `env`
  assignments, here-doc bodies) and the log is a plaintext file
  outside any repo. Recording commands changes what that file is.
  Three exits, operator's call: (a) log the command truncated and
  accept the exposure; (b) log only a shape digest — the matched
  arm plus the git subcommand — enough to separate false fires
  without carrying payload; (c) leave it and accept that false-fire
  rates are found by accident. (b) is the recommendation: it answers
  the review's actual question and carries no secret material.

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

## Done

_(none yet)_
