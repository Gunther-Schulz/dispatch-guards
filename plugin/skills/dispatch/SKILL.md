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

Section map — §§1, 4, 5, 6 are below and §§2, 3, 3b are the
HEADINGS OF `references/forms.md` (they open there as "## 2.",
"## 3.", "## 3b."), so a "§2" citation anywhere resolves in that
file, not in this one; the rest load on demand:

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
follows the tail block (references/forms.md) verbatim (named →
SendMessage; "final message" alone has read as final text, which
on that lane reaches no one — the §2 re-demand loop, live).

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
  the brief drifts and the agent can't detect it. A POSITION- or
  GENERATION-dependent identifier — a register number, an item id,
  a line number — travels with a CONTENT anchor beside it: the
  numbers shift when the artifact is regenerated while the brief's
  copy stands, and the executor then works from the anchor and
  reports the offset (measured: a regenerated register moved every
  number by one; the quoted wording beside it is what saved the
  lane).
- **Grounding basis as a mandatory section.** Name what the agent must
  read before building and require the final report to cite what was
  actually read.
- **Every claim the brief asserts carries a per-line provenance
  grade, and the grade follows the CLAIM, never the section or the
  FORM holding it.** "Established" is a per-line verification
  claim, never a section-level tone: every line asserting the
  target repo's CURRENT STATE — in whichever slot, wearing
  whichever form — is either OPENED at brief-write time or
  carried with its provenance and grade —
  "from <source>, unverified" — so the executor can tell which
  citations hold dispatcher weight and which are inherited (mixed
  provenance under one uniform header is the label-over-body
  drift, and an ABSENT citation is the lucky case: reading
  falsifies it; a merely STALE one reads as a near-miss the
  executor plausibly "corrects" toward). Opening a REFERENCE is
  not opening its CONTENT: proving a ref, path or ticket RESOLVES
  establishes nothing the brief rests on, and that existence check
  is the one that feels like diligence. Opening a stored ENTRY
  means the entry PLUS its neighbours: a re-grade is commonly
  written as an ADJACENT record rather than an in-place edit, so
  the original head keeps its live grade while the closure sits a
  few lines above it (measured twice — a "(DONE — <sha>)" line
  inside a body straddled by two read windows, and a re-grade in
  the preceding bullet; each cost a lane that correctly built
  nothing, and one left the closed item ranked third in a
  build order). A self-built extractor is the INSTRUMENT there and
  its boundary choice is the basis, not its output: a split on the
  entry delimiter returns exactly one entry and hides the
  neighbour that re-graded it. Where the target repo has its own
  closure or staleness check, it runs over the entry before the
  brief ships. FORM is the harder half,
  because it decides what gets read as a claim at all: a
  repo-assertion wearing a CITATION draws the grade, while the
  same assertion as a design sentence, a base commit, or a filled
  form slot reads as the dispatcher's own DECISION and draws
  nothing — and decisions are executed, not checked. Ask of each
  line what it asserts about the repo AS IT IS; the commit-plan
  slot's read-basis is that question made mechanical for one
  slot. A section-scoped reading
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
  commit by pathspec — `git commit -m "…" -- <paths>` with every
  flag BEFORE the separator, not `git add` then
  `git commit`; `-A` is wrong everywhere. A path git does not yet
  TRACK is invisible to a pathspec commit ("did not match any
  file(s) known to git"), so a brief whose deliverable is a NEW
  file states the one addition that closes it: `git add -N <path>`
  first — intent-to-add registers the path against the empty blob,
  staging zero content, so the commit still carries the file's full
  body while a co-writer's staged work stays staged and
  uncommitted — and `<path>` names a FILE, never a directory: a
  directory argument intent-to-adds every unowned untracked file
  under it, invisibly — foreign briefs included, surfacing as a
  broken stash many commands later — the write-boundary directory
  rule's add-N face. Unstated, the rule
  is unsatisfiable for file creation and the executor either
  bridges it or halts.
  **Commit unpushed; pushing is the dispatcher's act** after
  verification. On a copy shared with a writer outside the
  dispatch — peer session, operator, scheduled job — that is a
  hope rather than a boundary: their push carries the BRANCH (the
  push-set bullet below), publishing the lane's mid-verification
  work along with their own (measured: a 270-line hook rewrite on
  the remote before the dispatcher had verified any of it).
  Isolate the lane in a worktree, or say in the brief that its
  commits may be published unverified.
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
    An ADD-ONLY or non-overlapping-region grant is no exemption
    from any of this — the commit is file-granular regardless of
    where in the file the hunks sit (measured: two lanes each
    granted one config file "add only, touch no existing field";
    one lane's commit carried the other's uncommitted hunk under
    its message). And for a shared FILE no safe form exists —
    pathspec isolates against other files, never against a
    co-writer's hunks inside a named one — which makes
    serialization the remedy rather than the preference.
  - **Deployment-coupled is a different question from LIVE ON
    WRITE.** A file on an execution path resolved by PATH rather
    than by import — a git hook under `core.hooksPath`, a
    registered harness hook, a file a running daemon re-reads,
    anything under a watched directory — IS the live mechanism
    from the moment it is written: no commit, no deploy, no
    restart. A brief that boxes deployment leaves that unboxed
    (measured: a lane rewrote the machine's live pre-push gate
    while the dispatcher's own pushes ran through it). Where the
    write set touches such a path, the brief answers both.
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
    share the session-keyed scratchpad, so ANY file they write there
    collides on name alone — the brief assigns names carrying the
    agent or item slug, for every write under a shared scratch root
    and not merely for outputs whose filename a tool DEFAULTS.
    Defaulted names are the obvious half; the agent-CHOSEN name is
    the one that slips, because a rule about defaults reads as not
    applying to it (measured: three parallel lanes independently
    chose the same obvious commit-message filename in one scratchpad,
    two collisions, saved only by each file having been consumed
    before the next overwrote it — the claims gate warned AFTER each
    write landed, documenting the overwrite rather than preventing
    it).
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
    REMOVED by the dispatcher once its findings are booked AND
    interrogated — removal is terminal (recipe below), and a
    reader's findings are precisely what a follow-up question is
    for, so removing AT booking spends the channel at the moment
    it is worth most: a reader has no integration moment, so the
    writer recipe's removal clause below never fires for it by
    construction (frozen probe
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
    integrity check — live in this plugin's sibling `worktree` SKILL,
    which is LOADED before the first `git worktree add`, never
    merely cited (single source; this recipe carries only the
    dispatch-specific binding and must not grow a second copy).
    Improvised from the citation, the rung's own push-denial step
    has disabled push for the MAIN clone — remote config is shared
    across worktrees — surfacing later as an access-rights error
    that reads like a credentials problem.
  - **Worktree recipe (the ladder's rung 2).** Create outside the
    main tree (`git worktree add /tmp/wt-<task>-<agent> -b
    wt/<task>/<agent> <main-HEAD>`); apply the skill's push denial to
    EVERY remote — a fork's `upstream` is a live push path too, and
    the worse one; brief only cwd-relative paths; snapshot main HEAD
    before dispatch and re-check after return (mismatch = the agent
    escaped its worktree — halt, don't integrate); integrate by
    `cherry-pick <worktree-commit>` onto main after verification,
    never merge; remove the worktree LAST. Removal is the TERMINAL
    act: it closes the agent's resume channel (harness binding, as
    of 2026-08-15 — SendMessage to an agent whose worktree is gone
    is refused, "cannot be resumed: its worktree no longer
    exists"). Sequence: book the report, send the lane-close, ask
    whatever the report raises — THEN remove. A removed worktree
    structurally replaces the CLOSE message, since the agent can no
    longer write; it replaces no follow-up QUESTION, and that is
    the expensive half, because a booked report is the cheapest
    place a question ever gets asked. Harness note:
    where the agent runner offers native worktree isolation, prefer
    it over the manual recipe — same guarantees, less plumbing.
    Worktrees cost setup + integration and only pay where overlap is
    genuine — disjoint file sets in one working copy stay the
    default. Before choosing one, ask whether the work reaches
    OUTSIDE its own repo — a sibling repo by relative path, an
    absolute path, an installed copy. There a worktree is the WRONG
    isolation rather than the expensive one: it silently decides
    which branch of the code runs, and the lane reports green on the
    branch nobody meant to test (sibling `worktree` SKILL, the
    neighbourhood clause — single source, not copied here).
    Serialize instead, or run the suite in the main checkout.
  - **The base commit is STATED in the brief, never discovered.**
    Stated means READ at compose time — `git -C <copy> rev-parse
    --short HEAD`, its output pasted — never recalled from an
    earlier read in the same session: a remembered hash satisfies
    "stated" while naming a body that has moved, and the
    executor's check is prescribed as an ACT so it cannot go
    stale while the dispatcher's is a VALUE, which has no
    freshness (measured: co-writer commits landed between the read
    and the dispatch, and the executor halted, correctly, at the
    cost of a round trip). Where the copy has any co-writer, the
    CENSUS belongs here as well as at integration (§4): `git
    worktree list` alongside `git status` and `git log -1
    --format=%cr` — `git status` does not see worktrees, and
    "committed 2 minutes ago" is what separates a quiet copy from
    a live one; a scratch-path worktree under a foreign session id
    is a live co-writer whatever the tree says. Where the brief
    FILE is committed into the executor's own copy, the base is
    the brief's own commit, or the tolerance is path-scoped
    ("<hash>, or any later HEAD whose extra commits leave the
    target paths untouched") — a base chosen before that commit is
    self-refuting and spends a round trip ratifying the
    dispatcher's own metadata commits.
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
    bounced after a mid-batch push consumed the bump). Where the
    bump is ALREADY committed, the plan names its PUSH STATE —
    "bump committed, UNPUSHED (exemption armed)" — never merely
    that it landed: the exemption is keyed to the batch being
    unpushed, so "the bump is already in" leaves the lane unable
    to check the condition its own commits depend on, and the
    dispatcher who wrote that premise is the one who can kill it
    by pushing (measured: a brief said the bump had landed, the
    dispatcher had pushed it, and the lane's payload commits
    bounced — it halted correctly rather than reaching for
    --no-verify, at the price of a full directive round trip). A
    plugin-payload brief also states WHO bumps the manifest and
    in which commit — the manifest is invisible from a
    write-boundary list, and both lanes of one batch returned
    that gap independently; "the dispatcher sequences the bump
    ahead of your lane" is the default filling. An item that must
    RECORD a commit's ref cannot share that commit: order it into
    a later commit or split the pathspec. The slot takes the READ
    that found each guard, not the verdict alone: "none" written
    without opening the hooks path reads exactly like "none"
    written after opening it, so the word alone is satisfiable
    whether or not the work happened — the same fakeable-evidence
    gap a bare "checked" carries anywhere else, and the same cure
    (measured: a "none" filling for a repo whose commit-msg hook
    was one `core.hooksPath` read away bounced the lane it was
    written for).
  - **A verifier that cannot pass inside the write set GRANTS what
    it needs, in words.** The executor-side rule is a prohibition —
    nothing outward-facing without an explicit grant (executor
    skill §1, the box; source label). Its compose-time twin is the
    dispatcher's: read the brief's own acceptance criteria before
    shipping, and for any step that cannot be satisfied within the
    named paths, either grant that step explicitly or replace the
    criterion with one the write set can satisfy. A criterion
    demanding an act the boundary forbids grants it IMPLICITLY, in
    a place the executor has to infer — and an inferred grant is
    the ambiguity the write boundaries exist to remove (measured: a
    repo-paths-only write set whose verifier demanded a green
    deploy-check that only symlinks into the operator's real config
    could satisfy; the executor reported the gap in both directions
    rather than resolving it, which is the executor behaving
    correctly under a defect that was the dispatcher's).
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
  - **A verifier step confirms what it assumes exists — the knob
    AND the environment.**
    Before writing "point <NAME> at a temp dir", establish that it
    is a parameter or env var and not a module constant: a hardcoded
    constant in a file outside the executor's write boundary makes
    the step unexecutable as written, and the executor either
    invents the in-process rebinding or halts. Either confirm the
    knob, or state the rebinding form in the brief. A RUNTIME the
    step assumes takes the same clause: an agent shell has had
    neither a docker daemon nor usable sudo, which leaves "run this
    against a postgres container" unexecutable at that tier — so a
    step needing a container runtime, a service, or privilege
    states that as a tier/environment precondition.
- **Commit convention verbatim.** Title pattern + the exact
  `Co-Authored-By: Claude <executor model name> <noreply@anthropic.com>`
  trailer — spelled out, not referenced.
- **The model rides the NAME.** Every generic dispatch is NAMED
  `<model>-<slug>` — the panel renders the name, so the model is
  visible live in the UI and the title stays clean prose (no
  `<model>: ` prefix; a legacy prefix, if present, must mirror the
  model field). The name also selects the report LANE (§2 forms,
  binding): named = mailbox teammate, whose final text reaches no
  one, so generic dispatches are mailbox-lane by construction;
  only pinned-type agents, which the gate exempts, can run
  unnamed. Fan-outs state items × lanes × tier before
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
  already landed (measured: four of five proposed
  lanes were already built, found only when the bundling question
  forced the files open).
  A READ-ONLY fan-out has no write boundaries to join, so three
  terms size it instead: a lane's fixed load (system prompt +
  corpus + brief, re-paid per agent) stays small against its work —
  the brief-rivals-work test at lane grain; exhaustive per-item
  checking caps items per lane, because late items in a long
  enumeration get shallower checking than early ones — the
  under-report principle as a sizing bound; and the grouping axis
  (repo, section, artifact class) is NAMED in the route line, since
  no join derives it. Splitting can be token-CHEAPER, against the
  folk intuition: one lane re-reads its whole accumulated prefix
  every call while each split lane pays its startup once, so a
  read-only lane expected past ~30 tool calls is worth splitting on
  token cost alone (measured on one workload against a modeled
  single-lane arm; carry the formula, never the constant —
  `tools/lane-cost.py` measures growth and per-lane startup per
  workload and prints the crossover).
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
  inside the enumeration form.) A brief dictating a WORKED EXAMPLE
  as a mandatory assertion also names one case that separates the
  prescribed implementation from the NAIVE one: an example both
  answer alike pins the spec rather than the defect, and it reads
  as rigor while doing it (measured: a lookaround regex and a
  greedy one satisfied the briefed edge case identically, and the
  executor's own mutation battery — not the brief — found the
  discriminating neighbourhood).
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
    unverified"; a change to VISIBLE render chrome names a
    page-image sighting by the dispatcher — text-extraction checks
    are blind to colour and layout>

    ## Write boundaries
    <paths owned; `git commit -- <paths>`; what NOT to touch;
    whether the change is deployment-coupled AND whether any
    written path is live on write; commit style; the amend rule>

    ## Commit plan
    <the target repo's commit-blocking guards, each named WITH
    THE READ THAT FOUND IT — "none (hooks path read:
    core.hooksPath=hooks, empty)", or the guard's name and file
    on a hit. Then where the bump or ordering commit sits AND
    whether it is pushed; for a plugin payload, who bumps the
    manifest and in which commit. Mechanism and sequencing: the
    commit-plan bullet above. A basis-carrying "none" is a valid
    filling; a bare
    "none" and silence are not>

    <§2 tail block from references/forms.md, pasted verbatim>

A verifier or discovery dispatch takes its own exception above and
the READ-ONLY tail (references/forms.md) — not this skeleton.

## 4. Dispatcher duties (integration never delegates)

- **Every dispatch carries an expected-return horizon,** stated
  in the dispatching turn's final message, where its passing is
  checkable. Silence past the horizon is a finding — inspect or
  stop the agent, never more waiting. It binds hardest on the
  MAILBOX lane (§2): a named agent fires no completion
  notification and is absent from the agent listing, so silence
  there is the only signal either way, and SendMessage is the
  sole channel in both directions. (Source:
  site corpus dispatched-work rule.)
  Where the awaited return is itself the only ALARM — a mailbox
  dispatch, a peer handoff, any wait with no harness-tracked task —
  the waiter ARMS the horizon at the moment the wait begins, as its
  own background timer (a `sleep <horizon>` whose exit re-invokes
  the session). Unarmed, the rule can be executed only by a session
  something else happens to wake, and a dead or stranded
  counterpart produces permanent silence indistinguishable from
  work.
  The horizon does not survive the session that ARMED it. The timer
  dies with its session, cleanly closed or not, and the channel dies
  with it: SendMessage reaches a named agent only from the session
  that spawned it, and a changed session identity makes it
  unreachable outright (harness binding, as of 2026-08-18; measured
  by a peer session, not reproduced here). Nobody is then left who
  COULD demand the report. So a session ending with a dispatch in
  flight converts the horizon into a WRITTEN obligation in whatever
  the successor reads first — handoff, start brief, ledger. That
  obligation carries its own DISCHARGE, not merely the agent, its
  brief and its base commit: it TELLS the successor to settle the
  question at the ARTIFACT rather than at the sentence — is the
  commit there, is a report booked? Writing only the triple leaves
  the discharge here, in a file a successor that dispatches nothing
  never loads. A stalled dispatch is indistinguishable from an open
  item, so the disposition on finding nothing is not "still running"
  but LOST — demand, re-brief, or book it void with a reason.
  An incoming report is booked only once its SENDER resolves
  against this session's own dispatch list (agent id or brief
  name). A report from an unresolved sender is a FINDING —
  cross-talk — never a report: it closes no horizon and the wait
  for the real one continues (measured: a dispatcher waiting on its
  one subagent received a plausible result message from an agent it
  never started).
- **Verify in the artifact, then integrate.** Run the tests, greps,
  renders YOURSELF before push/merge/publish. An agent's "done" is a
  claim, not a fact. (Source: site corpus dispatched-work rule.)
  That run compares the SKIP count against the baseline, not only
  passed and failed. A skip count risen against baseline is a
  finding, never noise: it is the quiet direction of the question a
  risen failure count asks loudly, and it is how a lane's own new
  checks report never having run (measured: a passed-with-skips line
  was booked as green, the skipped checks being exactly the ones
  built to prove the item's core branch — noticed only because
  unrelated tests went red beside them, never by the report form).
  The co-writer census (§1, the base-commit clause) runs again
  here, before the integrating push. Slot (f) is graded against the
  COMMIT TRAILER before it is booked: an agent's claim to
  authorship is a claim like any other and the trailer is its cheap
  disproving probe (measured: a summarized lane re-read the tree on
  resume, booked the DISPATCHER's commit as its own, and confessed
  a write-boundary deviation for work it never did). WHICH trailer
  answers WHICH question decides it: the author trailer names a
  MODEL, so it separates tiers and nothing finer — where two
  writers in one copy share a model it does not discriminate at
  all, and read as identity it yields a confident wrong attribution
  (measured: an unexpected commit assigned to the wrong session,
  both candidates one model, identical author trailers, different
  session trailers). The session trailer, where the harness wrote
  one, is the discriminator; absent one, or with the candidates
  still indistinguishable, the trailers have NOT settled
  authorship — ask the holder rather than reading the probe's
  silence as its verdict.
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
  routing, which names the current default). A `context: fork`
  inherits its caller's FULL context, so a check produced through
  one is self-review and is graded as such, never as a
  fresh-context verification; a subagent spawn cap does not close
  that channel — the Agent tool goes away loudly under the cap
  while a fork skill keeps forking and delivering (measured).
  A verdict that decomposes into
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
  the addition — don't touch its paths meanwhile. A report already
  IN FLIGHT when the extension was sent does not cover it: the
  crossing reads as a closed lane, and neither a grep nor `git
  status` observes a WRITER — each samples a moving state and
  proves nothing about who holds it (measured: a dispatcher read a
  crossed report as final, grepped for the added test, edited both
  of the lane's exclusive files and committed their working-tree
  state under its own trailer; the reservation gate had warned,
  naming the lane as holder, immediately before). Where a claim
  gate fires and the holder looks dead, ASK the holder and wait for
  the answer — one message against an unrecoverable
  misattribution.
- **Ownership ends at the booked report — on both sides.** Once the
  dispatcher has booked the closing report, the agent's write grant is
  over: an agent that discovers a post-report defect REPORTS it and
  waits, it never edits on its own (a well-meant `--amend` can hit
  the dispatcher's newer HEAD — the §1 amend rule's post-report
  case). Mirror duty for the
  dispatcher: a named/mailbox agent stays resumable after its
  report — unless its worktree was removed, which closes that
  channel for good (§1 worktree recipe) — so
  before writing in the same working copy, treat it as a live writer —
  book the report AND tell it the lane is closed, or check `git status`
  defensively before every own commit there. The close message
  itself RESUMES the agent, so it states the boundary it needs —
  "do not edit; a defect found later is REPORTED" — or the close is
  the trigger for the post-report write it forbids (measured: a
  lane's only post-report commit followed its own lane-close
  message).
- **A handed-off run names its report CHANNEL, machine-readably.**
  Passing whole work to a peer session is neither a dispatch nor
  fact traffic: nothing returns by construction. The handoff
  carries one line — `REPORT-CHANNEL: SendMessage
  <name|operator-terminal>` — plus the cadence (at minimum: every
  decision round, and the close report), because on the peer lane
  a session's final terminal text reaches no one, and "consumer
  named" is not delivery (measured, twice within one hour on one
  desk: reports composed as final text, the operator seeing only
  an idle session and asking the driving desk where they were).
  The receiving side's mirror is the armed horizon above.

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
