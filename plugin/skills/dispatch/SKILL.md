---
name: dispatch
description: Brief, report, and integration discipline for delegating work to subagents — decision-complete briefs, closing-report and roadmap forms, dispatcher duties, tier-readiness register, Codex routing. Use when dispatching or delegating work to another agent (Agent/Task/Workflow tools), writing a dispatch brief, running parallel agents or agent worktrees, demanding or booking a subagent's closing report, integrating or pushing agent commits, or certifying a recurring procedure for a cheaper tier. Not for deciding WHETHER to dispatch — the model-routing table in the operator corpus governs that.
---

# Dispatch discipline — briefs, reports, and guards for delegated agent work

_Consumer: the dispatching session, any tier. Register follows each
rule's action — evidence for judgment steering, directive for
brief-form content and the dispatcher's own integration acts, a hook
where the lane is computable (§5); must-hold prose still exists here,
which is what §5's "best-effort" concedes. Maintenance and evolution:
the closing section._

Load when delegating substantial work to another agent (builds,
migrations, multi-file edits, research with consequences) —
mandatory when the target tier is below the session model (§§1
and 3 target that case; §§2, 4 and 5 apply to every dispatch; §6
certifies RECURRING procedure classes for a cheaper tier once,
globally, via the class register; §7 routes Codex work when that
CLI is installed). The receiving side — how the executing session
conducts itself — is the sibling `executor` skill; briefs to
cheaper tiers name its load first (§1). The dispatch-skill-gate
hook in this plugin demands this load before any dispatch.

Citations reading "site corpus" name the operating site's
always-loaded rule layer — here the operator's global corpus
(`~/.claude/CLAUDE.md`); this skill is that corpus' dispatch
half. Companion to the model table
there ("Model routing for dispatches"). "Cheaper tier" means any
tier below the session model, whatever the current lineup calls
it.

Section map — §§1, 4, 5, 6 are below; the rest load on demand:

- §2 report form + brief tails: `references/forms.md` — load it
  BEFORE composing any brief (the tails are pasted, never
  recalled).
- §3 roadmap form: `references/forms.md` (same file).
- Tier-choice evidence (WHICH model a dispatch takes):
  `references/routing.md` — load it BEFORE choosing a dispatch's
  model. The portable rules over tier roles; a site corpus's
  routing section overlays it with the concrete lineup and
  standing decisions, and wins on conflict.
- §7 Codex / gpt-5.5 routing: `references/codex-routing.md` —
  only when `command -v codex` succeeds.

Core finding (measured in operation, restamped 2026-08-02:
dispatch-log counts 183 dispatches over six days, verified green
builds across tiers, every recorded failure traces to a brief
defect, none to tier capacity; the log keeps accumulating for
future restamps):
**template/roadmap-filling PASSES, free design FAILS** — the
dispatcher's job is to remove design freedom, not to write longer
prompts.

## 1. The brief (decision-complete, or don't dispatch)

A brief is decision-complete only when a fresh context could execute
it without making any design or placement decision — system
placement (which rules apply, where the work belongs) is itself a
decision, pre-filled so the dispatch verifies rather than derives
it. (Canonical here; the operator corpus routing module points to
this section.)

**Exception — verifier dispatches:** a fresh-context verifier gets the
artifact and the question ONLY, never your reasoning (source:
site corpus fresh-context rule); the rich brief form below is for
EXECUTION dispatches — applying it to a verifier contaminates the
independence that is its point.

**Exception — discovery dispatches** (lookups, sweeps, extraction —
no writes): the brief names the N facts to return and the pointers
to trust unverified; no report files, no interim messages — each
extra output medium re-writes the answer and the observed cost
driver is output volume, not finding quality. The return channel
follows the tail block (references/forms.md) verbatim (background →
SendMessage; "final message" alone has read as final text, which
reaches no one — the §2 re-demand loop, live).

Mandatory parts (execution briefs):

- **Assignments are made by the dispatcher.** IDs, slugs, file names,
  numbering, target paths — named in the brief. The executor invents
  no naming and no placement.
- **Scratch is assigned too — the agent's OWN scratchpad, never the
  dispatcher's.** A subagent writing under another session's scratch
  or project roots draws the harness's permission dialogs to the
  operator (harness binding, as of 2026-08-01). Scratch layouts never
  MIRROR sensitive path shapes — a `.claude/`-shaped directory
  anywhere trips the harness's sensitive-path protection, which keys
  on shape, not location; where a tool hardcodes home paths, the
  brief names the tool's env override (CLAUDE_CONFIG_DIR-class)
  instead of a fakehome mirror. Source: the shape-keyed protection
  fact is canonical in the operator corpus (CLAUDE.md, Shell and
  privilege, the config-directory binding); this clause is its
  subagent-scratch application — amending either home means auditing
  the other.
- **Files to read, listed — never paraphrased.** Bind the source files
  (specs, decision docs, the code to change); a paraphrase carried in
  the brief drifts and the agent can't detect it.
- **Grounding basis as a mandatory section.** Name what the agent must
  read before building and require the final report to cite what was
  actually read.
- **Every claim the brief asserts carries a per-line provenance
  grade, and the grade follows the CLAIM, never the section
  holding it.** "Established" is a per-line verification claim,
  never a section-level tone: each cited line is either OPENED at
  brief-write time or carried with its provenance and grade —
  "from <source>, unverified" — so the executor can tell which
  citations hold dispatcher weight and which are inherited (mixed
  provenance under one uniform header is the label-over-body
  drift, and an ABSENT citation is the lucky case: reading
  falsifies it; a merely STALE one reads as a near-miss the
  executor plausibly "corrects" toward). Opening a REFERENCE is
  not opening its CONTENT: proving a ref, path or ticket RESOLVES
  establishes nothing the brief rests on, and that existence check
  is the one that feels like diligence. A section-scoped reading
  of this rule fails first at an EXPECTED RESULT, which is also
  the costliest line to inherit: the executor bends its work to
  satisfy an expectation, so an unverified one is either forced to
  fit — silently, by tuning the implementation until it matches —
  or returned as a gap at the price of a round trip. The brief
  boundary is where discovery testimony becomes instruction: every
  audit finding turned into a build step gets its cited line
  opened once, there — after it, the claim is executed by someone
  who cannot tell inherited from verified.
- **Write boundaries.** Which paths the agent owns (one writer per
  working copy; parallel dispatches need disjoint, brief-named path
  sets — source: site corpus dispatched-work rule). On a SHARED copy
  commit by pathspec — `git commit -- <paths>`, not `git add` then
  `git commit`; `-A` is wrong everywhere. A path git does not yet
  TRACK is invisible to a pathspec commit ("did not match any
  file(s) known to git"), so a brief whose deliverable is a NEW
  file states the one addition that closes it: `git add -N <path>`
  first — intent-to-add registers the path against the empty blob,
  staging zero content, so the commit still carries the file's full
  body while a co-writer's staged work stays staged and
  uncommitted. Unstated, the rule is unsatisfiable for file
  creation and the executor either bridges it or halts.
  **Commit unpushed; pushing is the dispatcher's act** after
  verification.
  - **Disjointness is per FILE, and commits serialize on shared
    files:** staging is file-granular, so an agent committing its own
    work in a shared file sweeps up a co-writer's uncommitted hunks —
    a clean targeted `git add` absorbs them; edit discipline alone
    cannot prevent it. The INDEX is shared too, which is what makes
    `git add <paths>` insufficient rather than merely imperfect: a
    co-writer staging between your `git status` and your commit
    rides out under YOUR message, whatever paths you named, and
    adding your own never unstages theirs. `git commit -- <paths>`
    ignores the index for everything else, so it isolates where
    `add` cannot (observed: a five-file commit under a three-file
    message, carrying a co-writer's in-flight work).
    General form, covering the repair as well as the commit: in a
    shared repo any state read is stale by the next command, so the
    check and the act belong in ONE command, or in a form that
    cannot act on the wrong object — pathspec for a commit, an
    explicit hash for a reset, never `HEAD~1` (observed: a `reset
    --soft HEAD~1` aimed at that mixed commit un-committed a
    co-writer's newer one instead; recoverable only because
    `--soft` moves the branch pointer alone).
  - **Amend is COMMIT-granular — file disjointness does not reach
    it:** `git commit --amend` rewrites whatever commit is at HEAD,
    and on a shared copy HEAD moves between working rounds — an amend
    aimed at "my commit" has swallowed a co-writer's commit under the
    amender's message, and a follow-up rewrite has erased a
    co-writer's landed fix from HEAD and working tree with `git
    status` clean (grep for known content found it; the reflog was
    the recovery). Amend only when `git log -1 --format=%(trailers)`
    shows your own trailer; otherwise a new commit. Dispatcher mirror
    at brief time: write "never amend — always a new commit"; the
    amend-gate denies subagent amends regardless of ownership (a
    conditional amend grant in a brief is dead text), and "amend into
    <commit>" names an operation git does not offer.
  - **Disjointness also covers untracked outputs:** parallel agents
    share the session-keyed scratchpad, so a tool's DEFAULT output
    filename there (a status file, a log) is a silent
    last-writer-wins collision that later reads misattribute — the
    brief assigns per-agent filenames for any output that defaults to
    a shared path.
  - **Disjointness resolves to realization surfaces:** a write
    boundary of named paths is complete only once each commissioned
    change is resolved to the file that REALIZES it — an object
    defined elsewhere (a stored view or schema object → its
    migration; a generated artifact → its template; a config key →
    the shared settings file) collides with a walled-off lane the
    design prose never names. Resolve at brief time — the design's
    own citations point at the realizing file; an overlap found then
    is serialized or explicitly carved out, never left to surface as
    a mid-dispatch halt.
  - **The push set is the branch, never "my commits"** (a §4
    dispatcher duty, stated here because it elaborates the
    unpushed-commit rule above): on a working copy shared with any
    co-writer (peer session, agent, human), `git push` publishes
    every local commit, including a co-writer's mid-verification
    work. Before pushing on a shared copy, `git log
    origin/<branch>..<branch>` and claim each commit; an unexpected
    commit halts the push — it is a question to answer first, and a
    live push is never the diagnostic. The claim log is its own
    invocation, never chained with the push: a read-then-decide
    seam collapses when the decision is pre-committed in the same
    compound command (push-claim-reminder's FUSED-PUSH DENY lane
    denies that form; this rule covers the variants it cannot see).
  - **A shared checkout has no private red.** Where a repo's
    pre-push or pre-commit runs a REPO-WIDE suite rather than the
    pushed lane's files, a lane's commits are private but its red is
    not: a co-writer's half-finished state fails YOUR push, and your
    own transient red blocks a dispatcher's unrelated one. The brief
    states it where it applies, a lane leaving the tree red between
    commits says so in its report, and a push blocked by a foreign
    red is a finding to report — never a `--no-verify`.
  - **Escalation ladder for overlapping file sets** — overlap counts
    any agent's READ-OR-EXECUTE set against another's write set, not
    only write against write: a probe executing a file a co-writer is
    editing measures with an unstable instrument, and its findings
    inherit the half-written state. For a read-only overlapper the
    cheap resolution is isolating the READER in a worktree frozen at
    dispatch — the freeze is the point for an instrument and wrong
    for an agent that must see live state, so which one it is gets
    decided per dispatch, never defaulted. A reader worktree is
    REMOVED by the dispatcher at the booking of its findings: a
    reader has no integration moment, so the writer recipe's removal
    clause below never fires for it by construction (frozen probe
    readers have sat registered long after their sessions ended), and
    its registration lives in .git/worktrees/ where no repo-level
    check looks. Ladder: (1) same file, small overlap → serialize the
    edits (second agent touches the shared file only after the
    first's commit lands, ordering stated in the brief) or serialize
    the dispatches; (2) real parallelism wanted despite overlap →
    per-agent git WORKTREES. Portable git mechanics — shared-config
    hazards, push-denial (per-worktree pushurl poison, never the
    `git remote` porcelain), the hook-env GIT_DIR redirection class,
    hooks-reach asymmetry, provisioning probes, the config-hash
    integrity check — live in this plugin's sibling `worktree` SKILL
    (single source; this recipe carries only the dispatch-specific
    binding and must not grow a second copy).
  - **Worktree recipe (the ladder's rung 2).** Create outside the
    main tree (`git worktree add /tmp/wt-<task>-<agent> -b
    wt/<task>/<agent> <main-HEAD>`); apply the skill's push denial to
    EVERY remote — a fork's `upstream` is a live push path too, and
    the worse one; brief only cwd-relative paths; snapshot main HEAD
    before dispatch and re-check after return (mismatch = the agent
    escaped its worktree — halt, don't integrate); integrate by
    `cherry-pick <worktree-commit>` onto main after verification,
    never merge; remove the worktree after integration. Harness note:
    where the agent runner offers native worktree isolation, prefer
    it over the manual recipe — same guarantees, less plumbing.
    Worktrees cost setup + integration and only pay where overlap is
    genuine — disjoint file sets in one working copy stay the
    default.
  - **The base commit is STATED in the brief, never discovered.**
    Either flavor cuts its base from SPAWN-TIME state, so the brief
    states the required base commit and the executor's first act
    verifies it — with TWO reads, because one does not separate the
    states: `git merge-base --is-ancestor <base> HEAD` (does HEAD
    contain the base?) and `git log --oneline <base>..HEAD` (what
    landed on top?). Three states, not two: base contained and
    nothing on top is the clean start; base NOT contained means
    behind or forked, and a clean tree there takes the one
    sanctioned recovery, a fast-forward to the base; base contained
    WITH commits on top means foreign work is present — halt and
    report those commits as a gap. The ancestor check alone returns
    SUCCESS for that last state, which is the one most worth
    catching. Any other state — a dirty tree over a stale base,
    anything unlisted — halts as a gap too: never a silent rebase,
    never a base discovered by guesswork.
    A foreign commit on top does not always mean a stale build, and
    the executor can answer that at its own end with no round trip:
    `git diff --quiet <base> HEAD -- <its paths>` — an unchanged
    write set is the fast path. It is NOT sufficient alone, because
    a foreign commit can change something those files DEPEND on
    without touching them, and an IMPORT LIST IS NOT THE DEPENDENCY
    LIST — a file reading a config, a fixture or a sibling artifact
    at runtime has dependencies no import shows. Complete predicate:
    write set unchanged AND nothing in the changed set is a
    dependency of it — the executor reports the changed-file list,
    the dispatcher confirms the second half in one look. Where the
    dependency set is not certain the HALT stands: the predicate is
    a fast path for the clear case, never a licence to reason past a
    foreign commit. Re-reading the tip just before composing only
    NARROWS the window — a dispatcher cannot win a race against a
    live co-writer by reading faster.
  - **The commit plan is ordered against the repo's guards.** In a
    repo with a payload-version guard, the brief states where the
    bump commit sits, sequenced from the guard's OWN comparison
    basis (read it, not assumed): a guard that compares against
    the release state clears later same-batch commits once the
    bump is in — there, bump-first turns one shared gate into zero
    bounces for every writer behind it. Where that basis is the
    ORIGIN manifest, the exemption holds only while origin lags
    HEAD: a mid-batch push moves the basis and re-arms the guard
    for every lane still in flight, so the dispatcher pushes at
    integration only (measured: both lanes of a two-lane batch
    bounced after a mid-batch push consumed the bump). A
    plugin-payload brief also states WHO bumps the manifest and
    in which commit — the manifest is invisible from a
    write-boundary list, and both lanes of one batch returned
    that gap independently; "the dispatcher sequences the bump
    ahead of your lane" is the default filling. An item that must
    RECORD a commit's ref cannot share that commit: order it into
    a later commit or split the pathspec.
  - **Pre-authorized repair classes (optional).** The write
    boundaries may declare a repair class the executor applies
    without a round trip — "if the commit plan collides with a
    repo guard, reorder to satisfy the guard and report the
    permutation as a deviation" — the declared-exemption shape the
    corpus prescribes for guards, applied to briefs (measured: an
    executor derived exactly that reorder with evidence, halted
    per the box, and the round trip spent ratifying it changed
    nothing). Novel deviations still halt; only the named class is
    pre-authorized.
  - **A verifier step that says REPOINT confirms the knob exists.**
    Before writing "point <NAME> at a temp dir", establish that it
    is a parameter or env var and not a module constant: a hardcoded
    constant in a file outside the executor's write boundary makes
    the step unexecutable as written, and the executor either
    invents the in-process rebinding or halts. Either confirm the
    knob, or state the rebinding form in the brief.
- **Commit convention verbatim.** Title pattern + the exact
  `Co-Authored-By: Claude <executor model name> <noreply@anthropic.com>`
  trailer — spelled out, not referenced.
- **The model rides the NAME.** Every generic dispatch is NAMED
  `<model>-<slug>` — the panel renders the name, so the model is
  visible live in the UI and the title stays clean prose (no
  `<model>: ` prefix; a legacy prefix, if present, must mirror the
  model field). A name forces background mode (§2 forms, binding),
  so generic dispatches are background by construction; only
  pinned-type agents, which the gate exempts, still run unnamed or
  synchronous. Fan-outs state items × lanes × tier before
  dispatching, and
  the chosen model is named in the turn's final message (canonical
  here; the corpus routing module keeps the veto principle and
  points here) — details and enforcement: the agent-model-gate
  hook (§5).
- **What rides ONE lane.** Two items bundle when they share a
  realizing FILE and one mechanism — the fix is a single edit
  wearing two entry numbers, and splitting it gives two lanes the
  same edit to make. They split when each carries its own
  red-first arrangement: a bundle then entangles verdicts (the
  bundled-changes fact, corpus Fixing) and buys only waiting,
  since token spend is identical either way and elapsed time is
  not. A shared tool, an adjacent topic, or a common owner are
  not bundling reasons — and the mapping is decided before the
  lanes are named, because deciding it means reading each item's
  realizing file, which is also what catches an item whose work
  already landed (measured 2026-08-14: four of five proposed
  lanes were already built, found only when the bundling question
  forced the files open).
- **Gaps: surface, don't fill.** Instruct explicitly: a missing
  decision, file, or value is reported as a gap, never bridged with a
  plausible guess — a gap filled silently is designed at the executing
  tier, the exact failure the tier choice was meant to avoid.
- **Criteria state OUTCOMES first, sites second.** In the settled
  design, name the observable the change must produce, then the
  known sites — never the sites alone: a site list reaches exactly
  what somebody enumerated, while the outcome carries its own
  completeness check, and the clause has fired from both
  directions (an outcome-criterion caught a call site the brief's
  site list missed; a site-shaped brief left standing the very
  defect its lane existed to close, at a site the audit's line
  number happened not to name).
- **Sweep-shaped work carries its two surfacing mechanisms** —
  what makes the cheap-tier default safe on sweeps, instead of
  buying tier as insurance against brief defects. (a) Post-sweep
  accounting: the report dispositions EVERY hit — fixed /
  already-correct / excluded / still-wrong — never a count or a
  "class closed" claim (a class believed closed across repeated
  sweeps returned dozens of live instances on its first full
  accounting). (b) Instrument-positive: a brief commissioning a
  pattern-scoped sweep names one member the pattern provably
  catches, so a zero-hit result is distinguishable from a dead
  pattern. Where the sweep is an enumeration dispatch, the
  accounting rides §3b's coverage artifact — one home, not a
  second form.
- **A commissioned instrument's SEMANTICS are the dispatcher's to
  state** — each one left implicit is re-decided at the executing
  tier, the same judgment remade without the design context. A
  brief commissioning anything that returns a verdict — a check, a
  review, a survey — fixes at least these two. ABSENCE maps as ONE
  rule ("whatever the instrument cannot read is
  could-not-verify"); an enumeration of the absences the
  dispatcher happened to foresee leaves every other one to be
  re-judged. A COMPARISON names its GRAIN — what counts as a
  difference — which the obvious phrasing hides: "compare the line
  sequence" of two independently maintained copies commissions a
  comparison of the WRAPPING, and once they wrap differently no
  state of either text makes it green, so the brief has specced an
  unprovable check. Grain is bytes, normalized text, or parsed
  structure, named. (forms.md §3b's Exactness clause is this rule
  inside the enumeration form.)
- **Guarded write paths pre-name their gate.** Where the brief's
  write set crosses a mechanical gate (a rule-corpus path
  demanding a same-turn skill invocation, a protected config), the
  brief names the gate and how to satisfy it — an unwarned
  executor meets the deny mid-dispatch and pays the remedy there.
- **Schema-bearing external facts: raw source text only.** When the
  build depends on an external contract (API/hook schemas, wire
  formats, config semantics), the brief requires grounding on the RAW
  document text — never on a summarizer/condensed rendering (WebFetch
  summaries have contradicted the raw doc at exactly the load-bearing
  line). Contradiction between summary
  and raw text → raw text wins, surface the discrepancy.
- **Below the session model, the grounding basis names the executor
  skill load FIRST** (`dispatch-guards:executor` — conduct of
  execution, under-report principle, devbook form): the conduct
  layer travels by skill, never restated per brief. Repo
  idiom/convention lists (house style, micro-conventions) still
  ride in the brief itself; the smarter tiers infer them, the
  cheaper ones must be told.
- **Recurring procedure → consult the readiness register (§6:
  global class register + the repo's exclusions) before choosing
  the tier.** The register's consult-moment is HERE, at
  brief-writing — §6 defines the machinery, but a consult-sentence
  living only there sits outside the path dispatch-time eyes travel
  (observed: dispatch runs with the register never opened). The
  consult keys on the procedure CLASS of the work in the TARGET
  repo, never on the dispatching session's cwd.

**Brief skeleton (pasted, then filled).** The parts above are a
checklist, not a shape: a free-composed brief satisfies them in
SUBSTANCE and still misses the LABELS the mechanical lane reads, so
the requirement is discovered by denial after the whole brief is
written. Same medicine as the §2 tail (references/forms.md) —
paste the headings, fill them, and the computable lanes are
satisfied by construction:

    Title: <model>: <task>
    Working copy: <path>. Base check: <command + halt condition>.
    Scratch: the agent's OWN scratchpad.

    ## Grounding basis — read before building; the report cites
    ## what was actually read
    - the executor skill (dispatch-guards:executor) — load FIRST
    - <file> — <which part, and what it settles>

    ## Background (established; verify at the cited lines)
    <facts the executor may trust — each OPENED at brief time, or
    graded "from <source>, unverified"; a claim about the target
    repo's CURRENT state is grepped by the DISPATCHER before the
    brief ships — the executor's arrival check run one round trip
    earlier: the decision record says what should happen, only the
    repo says what already did>

    ## The settled design — implement exactly this, do not redesign
    <every decision already made, incl. placement and naming —
    enumerated from the round that settled them, none carried in
    memory: a decision the dispatcher recalls but never writes is
    not in the brief, and the executor cannot miss what it never
    received>

    ## Verifier (in order; real output pasted in the report)
    1. <red-first bite>  2. <suites>  3. <live or corpus check>
    <an EXPECTED result quoted from a source is graded like a
    Background line — opened at brief time, or "from <source>,
    unverified">

    ## Write boundaries
    <paths owned; `git commit -- <paths>`; what NOT to touch;
    whether the
    change is deployment-coupled; commit style; the amend rule>

    ## Commit plan
    <the target repo's commit-blocking guards, READ at compose
    time, and where the bump or ordering commit sits — a
    payload-version guard comparing against the RELEASE state
    clears every later same-batch commit once the bump is in,
    and where its basis is the origin manifest the dispatcher
    pushes at integration only; a plugin-payload brief names who
    bumps the manifest and in which commit. "none" (no such
    guard) is a valid filling; silence is not>

    <§2 tail block from references/forms.md, pasted verbatim>

A verifier or discovery dispatch takes its own exception above and
the READ-ONLY tail (references/forms.md) — not this skeleton.

## 4. Dispatcher duties (integration never delegates)

- **A background dispatch carries an expected-return horizon,**
  stated in the dispatching turn's final message, where its
  passing is checkable. Silence past the horizon is a finding —
  inspect or stop the agent, never more waiting. (Source:
  site corpus dispatched-work rule.)
- **Verify in the artifact, then integrate.** Run the tests, greps,
  renders YOURSELF before push/merge/publish. An agent's "done" is a
  claim, not a fact. (Source: site corpus dispatched-work rule.)
  A SPLIT report — summary message + report file (§2
  payload-vs-pointer) — is booked from the FILE: the summary is a
  label over its body (site corpus paraphrase-drift rule), and
  per-finding dispositions close only when their set reconciles
  against the body's own enumeration — a count the summary states
  that fails to reconcile against the rows is the drift announcing
  itself, caught before booking, not after. (Computable slice —
  disposition-ID set difference empty before the table closes:
  anneal-framework development-process.md practice 11; source
  label.)
- **Verdict stages route to tier ≥ producer, capped at the operator's
  reviewer default; under-bar output redoes one tier up.**
  Producer = the highest tier whose judgment is in the
  artifact, not the tier that executed it — a brief authored at tier N
  makes N the producer, whoever implemented it. Same-tier review
  catches slips, not judgment errors (verdicts have flipped only under
  a smarter or fresh reviewer; discovery shows no tier sensitivity),
  and redoing one tier up has been the cheap correction. (Source:
  references/routing.md.) The cap: fresh-context review runs at
  the operator-named default reviewer tier even over artifacts
  authored ABOVE it — a fresh context removes self-blindness, not the
  judgment ceiling, and review above the default is an operator-named
  exception, never a tier-rule inference (source: site corpus model
  routing, which names the current default). A verdict that
  decomposes into
  exhaustive mechanical enumeration plus judgment over the
  enumeration routes the ENUMERATION to a cheaper tier — that half
  is discovery — briefed with the enumeration-brief form
  (references/forms.md §3b; its boundary clause names what never
  decomposes); the grading half stays at tier ≥ producer.
- **Escalation returns to the dispatcher; a subagent never spawns
  it.** An agent needing a tier above its own reports what it could
  not settle and returns the question; the dispatcher decides and
  dispatches. An escalating agent briefs its own reviewer, inheriting
  the blind spot it means to escape (site corpus fresh-context rule),
  and it is the dispatcher that holds the design context and the spend
  view. Sideways and downward dispatches are unaffected. Enforced for
  the ask-tier only (agent-model-gate hook): hook input carries no
  caller model, so "above yourself" is not computable — the remainder
  is judgment.
- **Additions extend ownership.** A follow-up instruction to a running
  agent extends its write ownership until its closing report covers
  the addition — don't touch its paths meanwhile.
- **Ownership ends at the booked report — on both sides.** Once the
  dispatcher has booked the closing report, the agent's write grant is
  over: an agent that discovers a post-report defect REPORTS it and
  waits, it never edits on its own (a well-meant `--amend` can hit
  the dispatcher's newer HEAD — the §1 amend rule's post-report
  case). Mirror duty for the
  dispatcher: a background agent stays resumable after its report, so
  before writing in the same working copy, treat it as a live writer —
  book the report AND tell it the lane is closed, or check `git status`
  defensively before every own commit there.

## 5. Mechanical guards (global; prose rules are best-effort, hooks are not)

The guards are this plugin's hooks: mechanism and wiring in
`hooks/` (roster: `hooks/hooks.json`), site policy in
`~/.claude/dispatch-guards.json`; the operator's non-guard hooks
stay in `~/.claude/settings.json`. Each hook's docstring is the
canonical prose for its lanes, bindings, and accepted residue —
this skill deliberately does not restate them: a prose copy of a
mechanical lane list is a dependent that rots silently. On a
guard deny, fix the brief against §§1–2, never against the error
text alone; a relief valve for a false-fire class lands in §§1–2
rule text, never in softening a lane. A gate receives a decision
already made and stated — deferring the decision to the gate's
dialog is the failure; the pause exists for the operator's veto,
not for the dispatcher's choice. Standing rules for every
guard — fail-open on hook-input parse errors, a `--test`
bite-test registered in the machine-bootstrap doctor,
environment bindings stamped with as-of dates — live in
`hooks/_dispatch_common.py`.

## 6. Tier-readiness (procedure classes and the register)

§§1–5 govern single dispatches. This section makes a RECURRING
procedure permanently runnable on a cheaper tier — certify once,
dispatch cheaply thereafter. Recurring procedures only: a one-off is
dispatched per §1 and never registered (the pipeline's fixed cost
doesn't amortize on n=1).

**Certification is class-level and global.** The certified unit is
a procedure CLASS (guard/checker builds, doc-cascade renders, …),
not one repo's instance of it: target tier + the executor skill +
a form-conforming devbook of the class (executor skill §3), proven
once. The capability lives in the skill and the form, so the
certification carries to every repo whose devbook conforms — never
re-proven per repo; repos state only what is true about them
(exclusions and deviations, below). A class is **tier-ready** when
all four hold:

1. **Documented decision-complete** as a form-conforming devbook
   (executor skill §3) — a fresh context on the target tier
   executes it without making any design or placement decision;
   the roadmap form (references/forms.md §3) is its per-dispatch
   rendering.
2. **Judgment points converted** — each one either mechanized into a
   guard/check, or named as an explicit STOP-and-escalate criterion
   (naming who decides: a higher tier or the operator). Escalating is
   returning the question, never spawning the higher tier (§4).
3. **Probe evidence** — at least one real case of the class executed
   on the target tier, reviewed at tier ≥ producer (§4 for who the
   producer is), evidence recorded in the register entry. One probe
   certifies the class; full eval batteries are for certifying a
   whole operating domain, not required here.
4. **Not in the exclusion class** — a procedure whose failure would be
   silent AND outward-facing is never register-eligible, however well
   documented: the ex-ante brief cannot cover the unforeseen gap, and
   a cheaper tier fills gaps silently. Explicit rule, not a judgment
   call per case.

**First-run-watched.** The first run of a certified class in a repo
NEW to it gets its output graded — one sentence in the booking, no
register entry. A failed grade books a deviation (below), never a
silent pass-through.

**The register** — machine-readable, two grains. The CLASS register
is global: `~/.claude/readiness.json` — one entry per class with
target tier, status (`ready` | `eval-open` | `excluded`), probe
evidence (date + ref), and a fingerprint (hash or date) of the
class devbook text; consumers: the §1 consult at brief-writing and
the machine-bootstrap doctor's fingerprint check. Per-repo
`READINESS.json` at repo root carries only EXCLUSIONS (this repo's
silent-AND-outward procedures — per-repo forever, the repo knows
its own outward surfaces) and DEVIATIONS (where this repo departs
from a class certification); role line: operator corpus, file
roles. No register without a consumer — a register nothing reads is
dead weight, don't create it; the consult-moment lives in §1's brief
parts (source label: the clause there is the one rule, this is its
machinery).

**Invalidation is part of the schema.** A change to the class
devbook text (fingerprint mismatch) or to the model lineup resets
`ready` → `eval-open`. A register without invalidation decays into
silent misinformation.

**Scarcity corollary.** When the top tier is rationed, certified
classes run on their cheapest `ready` tier by default; the top tier
is reserved for design, rule-corpus work, eval grading, and the
ambiguous multi-step tail where the tier gap is widest. (The session
model remains the operator's choice — the register informs it; the
site model table governs the lineup, references/routing.md the
dispatch defaults.)

## Evolution and maintenance

On a gap noticed in use — a dispatch failure this discipline should
have prevented, or a rule it states wrongly — write the observation
to `dev-notes/dispatch-OBSERVATIONS.md` in the plugin's source repo
(github.com/Gunther-Schulz/dispatch-guards) and propose the rule
change; BACKLOG.md there carries work items. Guard fires land in the
fire log (README, "Fire log, guard modes, and the replay bench"),
which is what makes fire rates countable rather than remembered.

Where this skill is deployed as the operator's corpus half, it is
OPERATIONAL CORPUS with the operator CLAUDE.md:
`~/.claude/CLAUDE-maintenance.md` governs every edit, and each edit
lands with a JOURNAL line in the corpus repo.
