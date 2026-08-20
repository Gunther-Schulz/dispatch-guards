# dispatch-guards — backlog

Two grades. **Parked** items carry their named missing evidence or
trigger. **Ready** items are decision-complete: design decided,
verifier named, done-criterion stated. Items leave by commit ref, or
are dropped with a one-line reason.

## Open

- **READY 2026-08-20 — two unlabeled restatements in the forms.md
  EXECUTION tail (corpus-harmony F7 + F13).** F7: the tail restates
  the full pathspec / shared-index mechanism with no source label,
  while its two block-neighbours in the same tail carry them ("§1
  amend rule", "§4 ownership rule") — a reader cannot tell the
  borrowed copy from the home statement, which is the label-over-body
  class the corpus names. F13 is the same edit's neighbour: the
  skip-count rule lives in four homes and the EXECUTION-tail copy is
  the unlabeled one. Both dispositions are decided: add the matching
  source label to each tail copy, no wording change to the mechanism
  itself. Explicitly NOT in scope: the dispatcher-side
  skip-vs-baseline rule in SKILL.md §4 — the reviewer and the Fable
  desk both graded it a genuinely different act, and it keeps its own
  statement.
  Design (decided): append to each of the two tail restatements the
  same source-label form its block-neighbours already use — a
  parenthetical naming the section the clause borrows from, placed at
  the end of the restated clause. The mechanism's own wording is not
  touched, no clause moves, and nothing is deleted: this is a
  provenance label over an existing body, which is exactly what makes
  it safe to do without a fresh-context vet.
  Write-set: `plugin/skills/dispatch/references/forms.md` (the
  EXECUTION tail block only).
  Verifier: `python3 tools/check-doc-drift.py` green (the EXECUTION
  tail is fixture-checked, so a tail edit that breaks the fixture goes
  red), the 69-column wrap block from CLAUDE.md's verify section, and
  a reader test — each labeled clause names the section it borrows
  from. Done when both labels are in the tail and the plugin is
  released.
  Execution note: `plugin/skills/` is operational corpus — the edit
  runs `skill-craft` and its review checklist (repo CLAUDE.md), is
  governed by `~/.claude/CLAUDE-maintenance.md`, and lands with a
  ledger line. Not a structural restructure, so no fresh-context vet
  is owed.
  Basis: fresh-opus corpus-harmony review 2026-08-20, relayed by the
  Fable desk; full body with both-side quotes in dotfiles
  `claude/records/corpus-harmony-review-2026-08-20.jsonl` — read it
  before editing (it was unpushed at relay time; confirm it landed).
  Findings graded at the Fable desk, realizing writes are ours.

- **PARKED 2026-08-20 — "site corpus" vs "operator corpus": one
  referent, two terms, and a grep-audit on either misses the other
  (corpus-harmony F12).** The dispatch SKILL.md declares the two
  equivalent and then uses both, so any later sweep keyed on one term
  silently under-reaches — the chosen-mark failure the grounding
  module names, sitting inside our own corpus.
  **Named missing evidence, and why parked rather than ready:** WHICH
  term survives is undecided, and it is not ours alone to decide. The
  vocabulary spans this repo's two skill files AND the operator's
  dotfiles corpus, which cites the same referent from the other side;
  picking a term here and sweeping only our half re-creates the split
  one level up. Two things would settle it: the operator's or the
  Fable desk's call on the surviving term, and a cross-repo hit count
  for both terms so the sweep's size is known before it starts.
  Until then the equivalence declaration stands and nothing is
  half-renamed. Basis: same review record as the entry above.

- **PARKED 2026-08-20 — a PDF-extraction recipe sits among the
  executor's format-agnostic conduct rules (corpus-harmony F14).**
  `plugin/skills/executor/SKILL.md` carries a qpdf / `grep -a` recipe
  in a section otherwise stating conduct that holds whatever the
  artifact's format. By the corpus's own ethic-versus-lens test the
  recipe is lens-shaped: situational ("when doing X, watch for Y"),
  which the calibration module routes to a lens or reference home
  rather than to always-loaded text.
  **Named missing evidence, and why parked rather than ready:** the
  destination is undecided and the choice is not mechanical — a
  `references/` file under the executor skill, a lens file outside
  this repo, or deletion in favour of the fixing-module rule it
  instantiates. Each has a different consumer and a different read
  path, and a recipe moved to a home nobody loads is worse than one
  sitting in the wrong section. What would decide it: whether any
  session has actually reached for this recipe since it was minted
  (the fire log and the journals can answer), plus the label back to
  the fixing-module rule it instantiates, which the review names but
  does not quote. Basis: same review record as the entries above.

- **READY 2026-08-17 — a marker-gated Stop lane for handed-off desks:
  report-enforcer's sibling one level up.** A session that received
  whole work over the peer channel composes its report as FINAL TEXT,
  which on that lane reaches no one — measured twice within one hour
  on one desk, with the operator seeing only an idle session. §4 now
  mandates a machine-readable `REPORT-CHANNEL: SendMessage <name>`
  line in the handoff; this entry is the mechanical half.
  Design (decided): a Stop hook fires only when ALL of — the
  transcript carries a `REPORT-CHANNEL: SendMessage <name>` marker,
  the ending turn composes substantial final text, and no SendMessage
  to `<name>` occurred in that turn. Marker-gated, so a session that
  never received such a handoff is silent by construction and the
  false-fire profile is near zero. Ships default-warn like every new
  lane.
  Write boundary: a new `plugin/hooks/` script + its `hooks.json`
  roster entry, README guard roster, `tools/corpus/guards.jsonl`
  cases, doc-drift roster labels. No skill text — §4 already carries
  the prose half.
  Verifier: `--test` bite-test plus corpus cases, red-first against
  the shipped predicate — the arms that must differ are (i) marker
  present + final text + no send → fires, (ii) marker present + final
  text + send in the same turn → silent, (iii) no marker → silent
  whatever the turn did. Arm (iii) is the false-fire control.
  Done when the bench and the bite-test cover all three arms and the
  lane is registered in the README roster at mode warn.
  Basis: dev-notes/dispatch-OBSERVATIONS.md, 2026-08-17 sender-half
  entry (slot 3b) — its own pre-formulated exit was this booking.

- **PARKED 2026-08-18 — a report-form lane for UNDISPOSITIONED skips:
  the count is computable, the disposition is not.** Slot (b) now
  demands the full counts with every skip dispositioned
  (`forms.md:18`, both tails, `executor/SKILL.md:60`); the prose half
  is minted and applied. The mechanical half would extend
  report-form-gate, which today checks slot PRESENCE only: a
  report-shaped subagent message carrying `K skipped` with `K > 0` is
  exactly computable, and that is the whole of what is computable.
  **Named missing evidence, and why parked rather than ready:**
  whether a DISPOSITION can be detected without false fires. The
  candidate predicate — a skip count mentioned once and never again —
  fires on the legitimate one-line form ("4 skipped, all
  pre-existing and unrelated to this item"), which disposes correctly
  inside the same sentence. A guard that fires on legitimate work
  trains the override reflex that kills it (this repo's own rule: a
  new lane ships default-warn and earns deny by fire rate, never by
  assertion). What would decide it: real report bodies from the fire
  log — how many carry skip counts at all, and in which of the two
  shapes. Until that is measured, the report carries the disposition
  and no lint claims to. Basis: this pass's mint decision, recorded
  in `dev-notes/dispatch-OBSERVATIONS.md` under the drained entry.

- **PARKED 2026-08-15 — the channel lanes read the PROMPT as a flat
  substring haystack, and three shapes slip through.** All found by a
  second fresh-context vet, each with a run control; none is a false
  fire, all are silent misses. (i) A NAMED brief whose only channel
  token is incidental prose — "the previous agent's SendMessage was
  truncated" — satisfies missing_channel; rename the token and it
  denies. A prefix/substring test in an equality's costume, the
  corpus's own named class. (ii) An UNNAMED brief that pastes the
  tail BODY but omits the channel line entirely is seen by no lane:
  missing_channel exempts the unnamed lane wholesale, and
  missing_tail's anchor sits in the body, not the line — yet §2 says
  paste exactly one. (iii) An UNNAMED dispatch whose referenced brief
  FILE carries the wrong-lane line is silent, though §2 calls it
  wrong twice over (wrong lane, and the channel line must be
  prompt-side).
  **Named missing evidence, and why this is parked rather than
  ready:** the obvious repair — require a channel-line SHAPE
  ("report channel:" + a lane marker) rather than any of four loose
  tokens — would deny briefs that name the channel in prose, and one
  such brief is already asserted as legitimate in this hook's own
  bite-tests ("Deliver via SendMessage to main."). So the design
  question is whether that prose form is still sanctioned by §2; it
  is an operator/§2 call, not a predicate tweak, and tightening
  first would trade three silent misses for an unknown false-fire
  rate on the lane that gates every dispatch. Decide the §2 question,
  then the predicate follows. Related: no fixture anywhere
  discriminates the "report channel" marker — deleting it from
  _CHANNEL_MARKERS leaves both nets green, because every fixture
  using it also carries "sendmessage".
  Basis: fresh-context vet 2026-08-15, controls pasted in its report.

- **PARKED 2026-08-15 — `isolation: "remote"` is a lane cell the
  probe matrix never covered.** The Agent tool documents remote
  dispatches as "always runs in background". Whether `name` still
  selects the mailbox lane there — and whether a remote agent's
  final text reaches the dispatcher — is unverified, so the §2
  binding is stated over a matrix with a hole in it. Named missing
  evidence: the same controlled probe this batch ran (launch text,
  and whether the final text arrives in a completion notification),
  for named × unnamed at `isolation: "remote"`. Cheap; it needs a
  session willing to spend two remote dispatches.
  Basis: fresh-context vet 2026-08-15; Agent tool schema
  `isolation` enum.

- **PARKED 2026-08-15 — report-enforcer asks the stopping agent a
  question it may not be able to answer: which LANE it is in.** Its
  instruction branches on "if you are a background/teammate agent"
  vs "if you are a synchronous subagent", and its own docstring
  already names this a known soft spot ("the background-vs-sync
  judgment is delegated to the stopping agent and has been misjudged
  once"). The 2026-08-15 lane rework sharpens the stakes: the branch
  is now decided by whether the dispatch carries a `name`, and the
  two branches give OPPOSITE instructions — a named agent must
  SendMessage or its report reaches no one, an unnamed one must
  re-emit its final text in full and must NOT send. Both wordings
  remain true, so nothing is broken today; what is unverified is
  whether the agent can observe the deciding fact.
  **Named missing evidence:** whether a subagent can read its own
  `name`/lane from its own context or hook input at SubagentStop —
  if it can, the branch becomes computable and the hook should
  state the lane instead of asking the agent to classify itself; if
  it cannot, the honest repair is to state both duties
  unconditionally rather than behind a self-classification the
  agent may get wrong. Probe: dispatch one named and one unnamed
  agent, each instructed to report what it can see about its own
  name and launch mode.
  CORRECTION (fresh-context vet, same day): an earlier version of
  this entry claimed report-enforcer's two branches "remain true, so
  nothing is broken today". That was FALSE and is withdrawn. The
  branch read "if you are a background/teammate agent (your final
  text does NOT reach your dispatcher)" — and under the 2026-08-15
  binding "background" names the UNNAMED lane, the one whose
  completion notification DOES deliver the final text. The wording
  attached the void property to the delivering lane, inverting the
  instruction for whichever agent read it literally. The vocabulary
  is repaired (the hook now branches on NAMED/mailbox vs UNNAMED and
  its docstring says so), so what remains parked is only the
  question below, not the wording.
  Basis: this session's probe matrix (OBSERVATIONS resolution
  2026-08-15) plus report-enforcer.py's own docstring soft-spot note.

- **READY 2026-08-11 — the §6 register consult has no mechanism at the
  moment it is owed, and the skill already records that this fails.**
  §1's brief parts say the consult-moment is at brief-writing, and the
  section itself notes the observed failure: "dispatch runs with the
  register never opened". It happened again on 2026-08-11 (PBS office
  session, enumeration dispatch): the dispatcher chose sonnet from the
  standing discovery default, wrote the brief, spawned — and opened
  `~/.claude/readiness.json` only when the OPERATOR asked why not
  haiku. The register confirmed the choice (the sweep needed live tool
  runs and per-item judgment about what its "body" even is, so it sits
  outside the certified `enumeration-fixed-schema` class, whose own
  text excludes "work whose noticing needs judgment"). Confirmation
  after the fact is not a consult: had the work BEEN a fixed-schema
  enumeration, the default would have cost triple, and nothing in the
  dispatch path would have said so.
  The prose has now failed at least twice with the rule in force, which
  is the §6-of-the-corpus condition for precipitating the computable
  slice.
  **Design.** `brief-reminder.py` already emits an allow-path
  `additionalContext` on every `PreToolUse:Agent` ("Dispatch starting —
  brief check (dispatch skill §1) …"). Append to it the register's own
  rows, read from `~/.claude/readiness.json` at hook time: one line per
  process — `id · tier · status · klasse` (the klasse one-liner
  truncated to keep the block short). Informational only, never a deny,
  no predicate over the brief text: the hook cannot know the work's
  class, and a guess would be the false-fire class the corpus forbids.
  It puts the certified classes in front of the dispatcher's eyes at
  the one moment the choice is made, which is exactly what the prose
  cannot do.
  Absent or unreadable register → one line saying so, never silence:
  a missing register that renders as nothing reads as "no certified
  classes", the could-not-verify-as-verified failure.
  **Verifier / red-first.** A bite with a fixture register carrying two
  processes must show both rows in the emitted context, and the same
  bite against the current hook must show none (that is the red). A
  second bite with the register path pointing at a nonexistent file
  must emit the explicit absence line, not an empty block. Add both to
  the hook's `--test` bites so the doctor sweep carries them.
  **Done-criterion.** A real dispatch in a live session shows the
  register rows in its PreToolUse context.
  **Write boundary.** `plugin/hooks/brief-reminder.py` + its bite
  registration; no skill-text change — §1 already carries the rule, and
  a second prose copy is the dependent that rots.

- **READY 2026-08-11 — a Bash deny does not say that NOTHING in the
  command ran, and the compound-command case bites.**
  The corpus already carries the class ("a step that was BLOCKED left
  the state its successor assumes was created, and the successor is
  where the damage lands"), with a recorded incident where a denied
  probe commit was followed by a reset that destroyed real work. Live
  again on 2026-08-11, same shape, cheaper outcome: a command chained
  `printf >> msg.txt && git commit && git push` was denied WHOLE by
  push-claim-reminder's fused-push lane. The deny text explained the
  push rule correctly and said nothing about the two earlier links —
  so the session re-ran the commit believing the trailer had been
  appended, and only the repo's own commit-msg hook caught it. One
  bounce here; the same reasoning in front of a destructive link is the
  recorded expensive case.
  **Design.** In `_dispatch_common.py`, where a deny decision is
  rendered, append one fixed sentence whenever the denied command
  contains a chaining operator (`&&`, `||`, `;`, or a newline outside
  quotes — a conservative scan; on any doubt, emit it): "Nothing in
  this command ran — including any earlier links that chained into the
  denied one. Re-check their effects before assuming them." Fixed text,
  no per-hook wording, so every Bash gate inherits it at once. Where no
  chaining operator is present the sentence is omitted, which keeps the
  single-command case clean.
  Rationale for putting it in the deny renderer rather than in each
  hook: the failing reader is the same in every lane, and a per-hook
  copy is five dependents that drift.
  **Verifier / red-first.** A bite feeding a chained command to any
  denying lane must show the sentence; the same lane with an unchained
  command must NOT show it (the pair — a sentence that always appears
  proves nothing about the scan). Against the current renderer both
  bites show nothing: that is the red.
  **Done-criterion.** Both bites in the doctor sweep, and the
  2026-08-11 command shape reproduced against the fused-push lane emits
  the sentence.
  **Write boundary.** `plugin/hooks/_dispatch_common.py` + bite
  registration. No lane's own predicate is touched.

- **PARKED 2026-08-10 — writer-claims-gate cannot see shell-redirect
  writes, so its claims store has a hole of unknown size.** The gate
  hooks Write/Edit; a `> file` redirect through Bash reaches the same
  paths and fires nothing. Reported by the dg-corpus-bundle executor,
  which created `lint.txt` and `SKILL.old.md` in the shared scratchpad
  by redirect and could NOT determine whether either overwrote a peer's
  file — the gate had no record either way. Same shape as the corpus
  wrap guard's own PostToolUse blind spot, which the commit-time lane
  was built to close (dotfiles 5e6fdde).
  **Named missing evidence.** Whether the hole is reachable in a way
  that matters: the gate's purpose is peer-overlap warning, so the
  question is how often a redirect write lands on a path another lane
  claimed. The fire log records Write/Edit fires only, so it cannot
  answer this about itself — the measurement needs a second source
  (a PreToolUse Bash lane recording redirect targets, itself a design
  question). Until measured, the gate's coverage claim is scoped to
  tool-mediated writes, and that scope belongs in its docstring.

- **RE-GRADED 2026-08-17 — the built half is gone; only the trigger
  is still parked.** `worktree_doctor.py` ships proposals 1–3
  (ownership DECLARED via `--owned` and never inferred, no removal
  path at all, the three reporting verdicts), and the observation
  carrier drained accordingly. What remains parked is proposal 4
  alone — the retirement TRIGGER — with its named missing evidence
  unchanged: a candidate predicate's measured false-fire rate. Read
  the entry below for the incident, not for the open work.

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
  **WIDENED 2026-08-10 — it is now TWO lanes, not one.**
  `writer-reservation-gate` hits the same wall and harder: it needs a
  real git fixture repo AND a reservation object inside that repo's
  git dir, where writer-claims-gate needed a fixture plus a rebound
  claims store. The bench's own docstring is the authority — "Boundary:
  STATELESS guards only … The bench never seeds state" — so this is a
  declared limit being reached twice, not a bug.
  What the second lane adds to the DECISION: a stdin-only case for it
  would be `silent` with no reservation anywhere, i.e. a test that
  passes against a lane which ignores reservations entirely. So the
  option "record a declared per-guard exclusion the bench verifies" is
  not merely cheaper here — writing a case instead would manufacture a
  vacuous green, which is worse than the gap it papers over. Weigh
  that when the decision is taken.
  Coverage for both meanwhile is their own `--test` batteries.

- **PARKED 2026-08-10 — two probe-craft clauses for the class devbook,
  batched to spare the register fingerprint.** From the TTL-relief
  build, measured: (1) a dead-predicate bite proves the assertion, not
  the controls — forcing the predicate TRUE is what shows over-firing
  controls can go red (the inverted injection); (2) a test condition
  that "obviously holds" gets pinned, not assumed (GIT_CEILING_DIRECTORIES
  for outside-any-repo). Both are devbook step-4/5 candidates; each
  devbook text change resets guard-checker-bau to eval-open, so they
  land TOGETHER with the next devbook amendment, not as two solo
  fingerprint churns.
  **THIRD CLAUSE, added 2026-08-10 (dotfiles global-lane dispatch,
  measured):** where a mechanism's correctness depends on a DEPLOY
  PATH, the red-first probe runs against that path's SHAPE, not a
  convenient stand-in. Measured: a roster battery green against a
  fixture whose directory was a real directory, red against the
  deployment's directory SYMLINK — and the failing lane was SILENT, so
  the mechanism would have deployed, injected nothing and reported no
  error. The cheap seam is rebinding HOME in a subprocess: production
  code exercised, zero writes to the real config dir. This is step 4's
  bite-proof clause seen from the other side — the injection proves
  the check can go red, the deploy shape proves it goes red on the
  thing that actually ships.
  **FOURTH CLAUSE, added 2026-08-10 (writer-lock dispatch, measured):**
  where a guard's predicate reads SHELL SYNTAX, the docstring
  false-fire probe strips `'`, `"` and backticks before matching — or
  it proves nothing while looking clean. Measured: the probe returned
  SILENT, but only because an odd number of apostrophes made `shlex`
  bail into the fail-open exit before any matching happened; the text
  never reached the predicate. Stripped, the same probe found a real
  match — a documentation paragraph containing `cd <elsewhere> && git
  commit`, a CORRECT shell reading of prose — pinned by identity so a
  second match goes red.
  Its sibling observation is the clause's second half: the author then
  wrote "this probe is vacuous" INTO the docstring, which balanced the
  apostrophe count and made the docstring start parsing, so the
  sentence was false the moment it was written. A claim about an
  artifact, stated inside that artifact, can be falsified by the act of
  stating it. Caught only because the bite-test asserted the vacuity
  being documented. Trigger: the next devbook edit, whatever
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

- 2026-08-20 — **0.11.3 release-train grab-bag** (booked READY
  2026-08-17): both halves shipped in `78ea1e5`, which the 0.11.3
  pass's own ledger line says it carried ("Done-Kriterium lautet
  wörtlich 'landet mit dem nächsten Version-Bump' und dieser Pass
  ist der Bump"). Verified against the world, not the ledger:
  `agent-model-gate.py:114` names
  `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` as the governing knob, and
  README:161-168 carries the "A spawn-depth cap" bullet. The entry
  outlived its own build by three days — the stale-stored-brief
  class, caught by re-reading premises against the source before
  dispatching it.

- 2026-08-17 — **three READY items built in the retirement pass**,
  each with its own checks (doc-drift green, skill_lint exit 0
  blocking=0, every added line ≤69 cols):
  (a) the untracked-outputs clause now covers ANY file written under
  a shared scratch root, not only tool-DEFAULTED names — the
  agent-CHOSEN name is the one that slipped, because a rule about
  defaults reads as not applying to it;
  (b) §1 gained the compose-time twin of the executor-side
  outward-facing prohibition: a verifier that cannot pass inside the
  write set grants what it needs in words, or the criterion is
  replaced. STALE PREMISE in that entry, recorded because it is the
  class this pass amended §1 about: it located the prohibition in §1,
  while a governed-set scan puts it in the executor skill — the
  design was unaffected, the citation was not;
  (c) the section map now states that §§2, 3, 3b are headings of
  references/forms.md, so every "§2" citation resolves without
  guessing. That entry also showed the census defect below.

- 2026-08-17 — **first maintenance pass over
  `dev-notes/dispatch-OBSERVATIONS.md`**: closes the READY
  2026-08-14 entry below. Every live entry got an exit — applied,
  already-applied with its basis, discarded with a reason, or (three
  entries) marked RESIDUUM because their target file is the
  guard-checker-bau devbook in dotfiles, which this working copy does
  not own. DEVIATION from the stored design, in the cheap direction:
  the planned CUTOFF rule for the 15 pre-form entries was not needed —
  each was graded individually against the current corpus, and five of
  them turned out already applied, one discarded on a hypothesis
  refuted at the source. Stale premise in the entry itself, worth
  recording: it said "27 entries, none ever drained", while four had
  drained on 2026-08-15. The pass also found what the entry's verifier
  predicted it would test — the `## Abgeflossen` branch — plus one
  live contradiction between two shipped skills (the reader-worktree
  removal clause) and one broken mechanism dependent (brief-reminder's
  read-only anchor). Realized: this commit series.

  - **READY 2026-08-14 — first maintenance pass over
  `dev-notes/dispatch-OBSERVATIONS.md`: 27 entries, none ever
  drained.** The quota banner shipped this day (dotfiles `b485ec7`,
  FB 112) and its first real run named this carrier:
  `maintenance pass owed: dev-notes/dispatch-OBSERVATIONS.md — booked
  ~8 vs drained ~0 over the last +30% stretch (8 commits)`. The
  sibling `worktree-OBSERVATIONS.md` stays silent (~1 vs ~0), so the
  banner discriminates rather than flagging every carrier.
  Design: an enumeration over the carrier ran the same day and its
  result decides the CUT, so the pass is a mechanical join, not a
  judgement sweep. The form's four slots reach back only to
  2026-08-12, the day the form was minted — all 12 entries from that
  date on carry a named target file, all 15 before it carry none.
  Two halves, and only the first is mechanical: (1) the 12
  form-conforming entries apply or get discarded with a one-line
  reason, clustered by target — class devbook (`CLAUDE.md
  §Registered procedure`) ×3, dispatch SKILL.md §1/§2/§4 ×8,
  executor SKILL.md ×1; (2) the 15 pre-form entries need a CUTOFF
  rule rather than 15 judgements, the shape `ENVELOPE_CUTOFF`
  already uses in `dotfiles/git/hooks/pre-commit` — a pass that
  reds the whole file gets worked around instead of followed.
  One entry sits outside both halves: the one at line 410 carries no
  date in its heading, so no date-based rule reaches it at all. It
  has a sibling at line 683 on the same mechanism and probably
  merges there; decide at the body, not the title.
  ⚠ Do NOT open this together with a class-devbook change: 3 of the
  12 target the very section a withdrawn attempt touched on 2026-08-14
  (pbs-office FB 133, parked with named missing evidence). Same
  paragraph twice in one round is what made that the day's most
  expensive lane.
  Verifier: after the pass, the banner goes silent for this carrier —
  and that silence is only evidence once a `## Abgeflossen` section
  actually exists, since none does anywhere yet and the drain branch
  is fixture-covered only (FB 112's own honest residue). So the pass
  is also the first real test of that branch.
  Done when every one of the 27 has an exit — applied with its commit
  ref, discarded with a one-line reason, or covered by the stated
  cutoff rule — and the count of open entries is stated, not implied.


- 2026-08-15 — **the §2 channel rules, settled by the controlled
  re-probe**: closes the PARKED 2026-08-08 item, whose named missing
  evidence was that probe. Outcome INVERTED the entry's own proposal:
  the `run_in_background` axis it was built on does not exist (Agent
  tool schema lists no such parameter), the live axis is `name`, and
  for an UNNAMED dispatch the completion notification delivers the
  final text verbatim — so the sync line is TRUE there and the
  proposed background-line default would have been wrong in the other
  direction. Root defect was the predicate: `is_background()` read a
  key the harness stopped supplying and was constant-true. Realized:
  forms.md §2 channel block + binding, SKILL.md ×2, `mailbox_lane()`
  in brief-reminder, agent-model-gate docstring, README roster,
  doc-drift labels, six replay-corpus cases (the guard had zero).
  Probe matrix and evidence in the OBSERVATIONS resolution of the
  same date.

- 2026-08-11 — **commit-plan origin-basis + who-bumps, and the
  state-token convention**: realized cfdbc6e (dispatch §1 bullet +
  skeleton slot + brief-reminder warn text; forms.md §2 paragraph;
  executor §1.7 — both sides audited per the corpus rule). Booked
  and realized same day (504b2fc the booking); incident lineage in
  the entry bodies at that ref.


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
