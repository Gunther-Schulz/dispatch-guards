# dispatch-guards — backlog

Two grades. **Parked** items carry their named missing evidence or
trigger. **Ready** items are decision-complete: design decided,
verifier named, done-criterion stated. Items leave by commit ref, or
are dropped with a one-line reason.

## Open

- **PARKED 2026-08-08 — worktree LIFECYCLE: nobody removes worktrees, and the
  sweep that does has no ownership predicate. Named missing evidence: whether
  this generalises beyond one repo, and a false-fire rate for any retirement
  trigger before it removes anything.** Full incident, both halves, with the
  evidence limits: `dev-notes/worktree-OBSERVATIONS.md`, section
  "2026-08-08 — LIFECYCLE".
  Measured: 16 extra registered worktrees in one repo over ~a week, every
  creating session having committed and left, against a removal rule stated in
  BOTH the dispatch recipe and that repo's dev-loop. Then a dispatcher session
  intending to clear its own four force-removed all 16, including another
  session's. Committed work survived (branches untouched); uncommitted work is
  unrecoverable and its existence is now unknowable.
  **Why PARKED and not READY, with the missing evidence named so this is a spec
  rather than drift:** the two design questions are genuinely open — what marks
  ownership durably (a naming convention is rejected up front: it re-creates the
  pattern-blind-spot class), and what the retirement trigger is (age is wrong;
  long-lived PR-slice worktrees are legitimate and their branches are
  deliberately unmerged, so "merged into main" fails too). Shipping a remover
  before either is answered is the incident again with a different regex.
  **The doctor slice SHIPPED by ff7f9b5** —
  `plugin/skills/worktree/scripts/worktree_doctor.py`, reporting only, no
  removal code path at any flag; three verdicts (clean / stale-found /
  could-not-verify) with matching exit codes; per-worktree DIRTY / REMOVABLE /
  UNKNOWN / UNREADABLE each carrying its evidence string; recommendations
  printed as unforced `git worktree remove` TEXT, never executed; no branch
  command at any path. Red-first proof ran the incident's own loop against an
  independently built three-arm fixture (it destroys all three including the
  dirty arm) and the doctor against the same shape (refuses the dirty arm,
  recommends only the declared-clean one, mutates no registration); the
  falsifiability probe — cleaning the dirty arm and watching DIRTY flip to
  REMOVABLE and back — is what distinguishes the refusal from an always-red
  constant. Registered in CLAUDE.md's verify block as step 3a.
  **Design decision taken at dispatch time, filling a gap this entry left
  open:** ownership is DECLARED (`--owned <path>`, repeatable), never inferred
  — undeclared reads UNKNOWN, never FOREIGN, because the tool cannot know. Any
  predicate over path shape, name prefix, directory component, branch name, or
  commit trailer is rejected: that is this entry's own naming-convention
  rejection, and left unstated it would have been re-created inside the tool
  built to prevent it. A future durable mark simply auto-populates the flag.
  **What stays PARKED, with the missing evidence unchanged:** the remover
  itself, the durable ownership mark, and the retirement trigger. The doctor is
  now the mechanism that produces the missing evidence — run it across repos
  over time; whether accumulation generalises past one repo remains UNMEASURED,
  and the post-incident zero-scan still proves nothing.
  Do not delete branches as part of any worktree cleanup.

- **READY 2026-08-08 — skill-lint's dead-cite check fires on tool names in
  parentheses, blocking every dispatch-guards release.** `skill_lint.py`
  reports `forms.md:29: dead-cite: (SendMessage) matches no heading here`;
  the text is a tool name in prose, not a section citation, and the finding is
  pre-existing (proven by linting the unmodified HEAD copy). Exit 1 makes it
  blocking, so every release must hand-disposition a false fire — the override
  habit the corpus warns about. Fix belongs in skill-craft's `tools/
  skill_lint.py` (sibling repo), not in rewording correct prose: exclude
  known tool/function names, or require a cite to look like a section
  reference (`§`, "see", a heading-shaped token) before flagging. Verifier:
  the linter goes red on a genuinely dead section cite and silent on
  `(SendMessage)`, both in one run. Done when dispatch-guards releases at
  lint exit 0 with no hand-disposition.

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

- READY 2026-08-09 — RESTORE §2/§3 HEADINGS OR RENUMBER (corpus-vet
  nit n6, pre-existing): dispatch SKILL.md has headings for §§1, 4,
  5, 6 only, while §2 (report form) and §3 (roadmap) live in
  references/forms.md — yet SKILL.md:271, the operator corpus
  (insurance module), and briefs cite "§2"/"§3". Design: keep the
  numbering, add one line at the section map stating that §§2-3
  are the forms file's headings (they exist there as "## 2." and
  "## 3."), and verify every "§2"/"§3" citation resolves. Verifier:
  grep of citations + doc-drift check green. Done: a reader can
  resolve every § citation without guessing.

- **PARKED 2026-08-10 — replay-bench corpus does not cover
  writer-claims-gate (0 cases), and relief may not be expressible
  there at all.** Surfaced by the TTL-relief executor (its GAP 2):
  the repo rule says a guard change extends tools/corpus/guards.jsonl,
  but the bench feeds stdin payloads only, while relief needs a real
  git fixture repo plus a rebound claims store. Named missing
  decision: extend the bench's fixture model, or record a declared
  per-guard exclusion the bench itself verifies. Until decided, the
  gate's own --test battery (8 relief/control cases, red-proven both
  directions) is the coverage.

- **PARKED 2026-08-10 — two probe-craft clauses for the class devbook,
  batched to spare the register fingerprint.** From the TTL-relief
  build, measured: (1) a dead-predicate bite proves the assertion, not
  the controls — forcing the predicate TRUE is what shows over-firing
  controls can go red (the inverted injection); (2) a test condition
  that "obviously holds" gets pinned, not assumed (GIT_CEILING_DIRECTORIES
  for outside-any-repo). Both are devbook step-4/5 candidates; each
  devbook text change resets guard-checker-bau to eval-open, so they
  land TOGETHER with the next devbook amendment, not as two solo
  fingerprint churns. Trigger: the next devbook edit, whatever
  motivates it.

- **PARKED 2026-08-10 — neutralize the remaining `CLAUDE.md`
  mentions in HOOK docstrings and one runtime string for outside
  sharing.** The SKILL-text half is DONE (operator GO "yes fix",
  this entry's commit: 11 citation sites across dispatch SKILL.md /
  executor SKILL.md / forms.md renamed to the "site corpus"
  vocabulary routing.md already uses; the two deployment-scoped
  governance footers deliberately keep naming the operator corpus).
  Remaining: 5 hook files cite CLAUDE.md in docstrings and
  discovery-volume-reminder.py:85 in a runtime message — changing
  deny/remind texts obligates battery re-verification, so this half
  waits. Trigger unchanged: an actual decision to publish/share the
  plugin outside this farm.


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
