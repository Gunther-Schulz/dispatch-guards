---
name: dispatch
description: Brief, report, and integration discipline for delegating work to subagents — decision-complete briefs, closing-report and roadmap forms, dispatcher duties, tier-readiness register, Codex routing. Use when dispatching or delegating work to another agent (Agent/Task/Workflow tools), writing a dispatch brief, running parallel agents or agent worktrees, demanding or booking a subagent's closing report, integrating or pushing agent commits, or certifying a recurring procedure for a cheaper tier. Not for deciding WHETHER to dispatch — the model-routing table in the operator corpus governs that.
---

# Dispatch discipline — briefs, reports, and guards for delegated agent work

_Editing this skill? It is OPERATIONAL CORPUS (together with the
operator CLAUDE.md): read `CLAUDE-maintenance.md` (deployed at
`~/.claude/CLAUDE-maintenance.md`) first — it governs every edit
here; each edit lands with a JOURNAL line in the corpus repo
(dotfiles), and the fire-rate review covers this skill._

Load when delegating substantial work to another agent (builds,
migrations, multi-file edits, research with consequences) —
mandatory when the target tier is below the session model (§§1
and 3 target that case; §§2, 4 and 5 apply to every dispatch; §6
certifies RECURRING procedures for a cheaper tier once, via a
per-project register — for the dotfiles repo the procedure text
lives in the repo-root CLAUDE.md; §7 routes Codex work when that
CLI is installed). The dispatch-skill-gate hook in this plugin
demands this load before any dispatch.

Citations reading "CLAUDE.md" name the operator's global corpus
(`~/.claude/CLAUDE.md`), the layer every session loads; this
skill is that corpus' dispatch half. Companion to the model table
there ("Model routing for dispatches"). "Cheaper tier" means any
tier below the session model, whatever the current lineup calls
it.

Section map — §§1, 4, 5, 6 are below; the rest load on demand:

- §2 report form + brief tails: `references/forms.md` — load it
  BEFORE composing any brief (the tails are pasted, never
  recalled).
- §3 roadmap form: `references/forms.md` (same file).
- §7 Codex / gpt-5.5 routing: `references/codex-routing.md` —
  only when `command -v codex` succeeds.

Core finding (trial-day evidence 2026-07-17, operator-confirmed
in operation 2026-07-23, restamped 2026-08-02: dispatch-log
counts 183 dispatches over six days, verified green builds across
tiers, every recorded failure traces to a brief defect, none to
tier capacity; the log keeps accumulating for future restamps):
**template/roadmap-filling PASSES, free design FAILS** — the
dispatcher's job is to remove design freedom, not to write longer
prompts.

## 1. The brief (decision-complete, or don't dispatch)

A brief is decision-complete only when a fresh context could execute it
without making any design or placement decision (source: CLAUDE.md
model routing).

**Exception — verifier dispatches:** a fresh-context verifier gets the
artifact and the question ONLY, never your reasoning (source:
CLAUDE.md fresh-context rule); the rich brief form below is for EXECUTION
dispatches — applying it to a verifier contaminates the independence
that is its point.

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
  instead of a fakehome mirror.
- **Files to read, listed — never paraphrased.** Bind the source files
  (specs, decision docs, the code to change); a paraphrase carried in
  the brief drifts and the agent can't detect it.
- **Grounding basis as a mandatory section.** Name what the agent must
  read before building and require the final report to cite what was
  actually read.
- **Write boundaries.** Which paths the agent owns (one writer per
  working copy; parallel dispatches need disjoint, brief-named path
  sets — source: CLAUDE.md dispatched-work rule). Targeted
  `git add <path>`, never `-A`. **Commit unpushed;
  pushing is the dispatcher's act** after verification.
  **Disjointness is per FILE, and commits serialize on shared
  files:** staging is file-granular, so an agent committing its own
  work in a shared file sweeps up a co-writer's uncommitted hunks —
  a clean targeted `git add` absorbs them; edit discipline alone
  cannot prevent it. **Amend is COMMIT-granular — file disjointness
  does not reach it:** `git commit --amend` rewrites whatever commit
  is at HEAD, and on a shared copy HEAD moves between working
  rounds — an amend aimed at "my commit" has swallowed a co-writer's
  commit under the amender's message, and a follow-up rewrite has
  erased a co-writer's landed fix from HEAD and working tree with
  `git status` clean (grep for known content found it; the reflog
  was the recovery). Amend only when `git log -1
  --format=%(trailers)` shows your own trailer; otherwise a new
  commit. Dispatcher mirror at brief time: write "add a commit;
  amend only if HEAD is yours" — "amend into <commit>" names an
  operation git does not offer.
  **Disjointness also covers untracked outputs:**
  parallel agents share the session-keyed scratchpad, so a tool's
  DEFAULT output filename there (a status file, a log) is a silent
  last-writer-wins collision that later reads misattribute — the
  brief assigns per-agent filenames for any output that defaults to
  a shared path. **Disjointness resolves to realization surfaces:**
  a write boundary of named paths is complete only once each
  commissioned change is resolved to the file that REALIZES it — an
  object defined elsewhere (a stored view or schema object → its
  migration; a generated artifact → its template; a config key →
  the shared settings file) collides with a walled-off lane the
  design prose never names. Resolve at brief time — the design's
  own citations point at the realizing file; an overlap found then
  is serialized or explicitly carved out, never left to surface as
  a mid-dispatch halt. **The push set is the branch, never "my
  commits":** on a working copy shared with any co-writer (peer
  session, agent, human), `git push` publishes every local commit,
  including a co-writer's mid-verification work. Before pushing on a
  shared copy, `git log origin/<branch>..<branch>` and claim each
  commit; an unexpected commit halts the push — it is a question to
  answer first, and a live push is never the diagnostic.
  Escalation ladder for overlapping file sets — overlap counts any
  agent's READ-OR-EXECUTE set against another's write set, not only
  write against write: a probe executing a file a co-writer is
  editing measures with an unstable instrument, and its findings
  inherit the half-written state. For a read-only overlapper the
  cheap resolution is isolating the READER in a worktree frozen at
  dispatch — the freeze is the point for an instrument and wrong
  for an agent that must see live state, so which one it is gets
  decided per dispatch, never defaulted. A reader worktree is
  REMOVED by the dispatcher at the booking of its findings: a
  reader has no integration moment, so the writer recipe's
  removal clause below never fires for it by construction (two
  frozen probe readers sat registered for days after their
  sessions ended, found 2026-08-01), and its registration lives
  in .git/worktrees/ where no repo-level check looks. Ladder:
  (1) same file, small overlap → serialize the edits (second agent
  touches the shared file only after the first's commit lands,
  ordering stated in the brief) or serialize the dispatches;
  (2) real parallelism wanted despite overlap → per-agent git
  WORKTREES. Portable git mechanics — shared-config hazards,
  push-denial (per-worktree pushurl poison, never remote-remove),
  the hook-env GIT_DIR redirection class, hooks-reach asymmetry,
  provisioning probes, the config-hash integrity check — live in
  this plugin's sibling `worktree` SKILL (single source; this
  recipe carries only the dispatch-specific binding and must not
  grow a second copy).
  Recipe: create outside the main tree
  (`git worktree add /tmp/wt-<task>-<agent> -b wt/<task>/<agent>
  <main-HEAD>`); apply the skill's push denial to EVERY remote —
  a fork's `upstream` is a live push path too, and the worse one;
  brief only cwd-relative paths; snapshot main HEAD before dispatch
  and re-check after return (mismatch = the agent escaped its
  worktree — halt, don't integrate); integrate by `cherry-pick
  <worktree-commit>` onto main after verification, never merge;
  remove the worktree after integration. Harness note: where the
  agent runner offers native worktree isolation, prefer it over the
  manual recipe — same guarantees, less plumbing. Either flavor cuts
  its base from SPAWN-TIME state, so the brief STATES the required
  base commit and the executor's first act verifies it
  (`git merge-base --is-ancestor <base> HEAD`) — the one sanctioned
  recovery on a stale base is a fast-forward to the stated base over
  a clean tree; anything else halts as a gap, never a silent rebase
  or a base discovered by guesswork. Worktrees cost
  setup + integration and only pay where overlap is genuine —
  disjoint file sets in one working copy stay the default.
- **Commit convention verbatim.** Title pattern + the exact
  `Co-Authored-By: Claude <executor model name> <noreply@anthropic.com>`
  trailer — spelled out, not referenced.
- **The model rides the surface the panel renders.** A named
  (background) dispatch carries it in the name — `<model>-…` — and
  the title then DROPS the `<model>: ` prefix (the panel renders the
  name; a doubled prefix is noise). An unnamed (sync) dispatch keeps
  `<model>: ` in the title — a name would force background mode.
  Fan-outs state count × tier before dispatching, and the chosen
  model is named in the turn's final message (source: CLAUDE.md
  veto-gate conventions) — details and enforcement: the
  agent-model-gate hook (§5).
- **Gaps: surface, don't fill.** Instruct explicitly: a missing
  decision, file, or value is reported as a gap, never bridged with a
  plausible guess — a gap filled silently is designed at the executing
  tier, the exact failure the tier choice was meant to avoid
  (source: CLAUDE.md).
- **Schema-bearing external facts: raw source text only.** When the
  build depends on an external contract (API/hook schemas, wire
  formats, config semantics), the brief requires grounding on the RAW
  document text — never on a summarizer/condensed rendering (WebFetch
  summaries have contradicted the raw doc at exactly the load-bearing
  line). Contradiction between summary
  and raw text → raw text wins, surface the discrepancy.
- **For the cheapest viable tier, add idiom/convention lists** (house
  style, micro-conventions) in the brief itself; the smarter tiers
  infer them, the cheaper ones must be told.
- **Recurring procedure → consult the readiness register (§6) before
  choosing the tier.** The register's consult-moment is HERE, at
  brief-writing — §6 defines the machinery, but a consult-sentence
  living only there sits outside the path dispatch-time eyes travel
  (observed: dispatch runs with the register never opened).

**Brief skeleton (pasted, then filled).** The parts above are a
checklist, not a shape: a free-composed brief satisfies them in
SUBSTANCE and still misses the LABELS the mechanical lane reads, so
the requirement is discovered by denial after the whole brief is
written. Same medicine as the §2 tail one level up — paste the
headings, fill them, and the computable lanes are satisfied by
construction:

    Title: <model>: <task>
    Working copy: <path>. Base check: <command + halt condition>.
    Scratch: the agent's OWN scratchpad.

    ## Grounding basis — read before building; the report cites
    ## what was actually read
    - <file> — <which part, and what it settles>

    ## Background (established; verify at the cited lines)
    <facts the executor may trust, each with its basis>

    ## The settled design — implement exactly this, do not redesign
    <every decision already made, incl. placement and naming>

    ## Verifier (in order; real output pasted in the report)
    1. <red-first bite>  2. <suites>  3. <live or corpus check>

    ## Write boundaries
    <paths owned; targeted `git add`; what NOT to touch; whether the
    change is deployment-coupled; commit style; the amend rule>

    <§2 tail block from references/forms.md, pasted verbatim>

A verifier or discovery dispatch takes its own exception above and
the READ-ONLY tail (references/forms.md) — not this skeleton.

## 4. Dispatcher duties (integration never delegates)

- **Verify in the artifact, then integrate.** Run the tests, greps,
  renders YOURSELF before push/merge/publish. An agent's "done" is a
  claim, not a fact. (Source: CLAUDE.md dispatched-work rule.)
  A SPLIT report — summary message + report file (§2
  payload-vs-pointer) — is booked from the FILE: the summary is a
  label over its body (CLAUDE.md paraphrase-drift rule), and
  per-finding dispositions close only when their set reconciles
  against the body's own enumeration — a count the summary states
  that fails to reconcile against the rows is the drift announcing
  itself, caught before booking, not after. (Computable slice —
  disposition-ID set difference empty before the table closes:
  anneal-framework development-process.md practice 11; source
  label.)
- **Verdict stages route to tier ≥ producer; under-bar output redoes
  one tier up.** Producer = the highest tier whose judgment is in the
  artifact, not the tier that executed it — a brief authored at tier N
  makes N the producer, whoever implemented it. Same-tier review
  catches slips, not judgment errors (verdicts have flipped only under
  a smarter or fresh reviewer; discovery shows no tier sensitivity),
  and redoing one tier up has been the cheap correction. (Source:
  CLAUDE.md routing evidence.)
- **Escalation returns to the dispatcher; a subagent never spawns
  it.** An agent needing a tier above its own reports what it could
  not settle and returns the question; the dispatcher decides and
  dispatches. An escalating agent briefs its own reviewer, inheriting
  the blind spot it means to escape (CLAUDE.md fresh-context rule),
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
rule text, never in softening a lane. Standing rules for every
guard — fail-open on hook-input parse errors, a `--test`
bite-test registered in the machine-bootstrap doctor,
environment bindings stamped with as-of dates — live in
`hooks/_dispatch_common.py`.

## 6. Tier-readiness (standing procedures and the register)

§§1–5 govern single dispatches. This section makes a RECURRING
procedure permanently runnable on a cheaper tier — certify once,
dispatch cheaply thereafter. Recurring procedures only: a one-off is
dispatched per §1 and never registered (the pipeline's fixed cost
doesn't amortize on n=1).

A procedure is **tier-ready** for a cheaper tier when all four hold:

1. **Documented decision-complete** in the roadmap form (§3) — a fresh
   context on the target tier executes it without making any design or
   placement decision.
2. **Judgment points converted** — each one either mechanized into a
   guard/check, or named as an explicit STOP-and-escalate criterion
   (naming who decides: a higher tier or the operator). Escalating is
   returning the question, never spawning the higher tier (§4).
3. **Probe evidence** — at least one real case executed on the target
   tier, reviewed at tier ≥ producer (§4 for who the producer is),
   evidence recorded in the register
   entry. One probe certifies one procedure; full eval batteries are
   for certifying a whole operating domain, not required here.
4. **Not in the exclusion class** — a procedure whose failure would be
   silent AND outward-facing is never register-eligible, however well
   documented: the ex-ante brief cannot cover the unforeseen gap, and
   a cheaper tier fills gaps silently. Explicit rule, not a judgment
   call per case.

**The register** — per project, machine-readable (dotfiles instance:
`claude/readiness.json`; consumer: bootstrap doctor incl. fingerprint
invalidation): one entry per procedure with target tier,
status (`ready` | `eval-open` | `excluded`), probe evidence (date +
ref), and a fingerprint (hash or date) of the normative procedure
text. No register without a consumer — a register nothing reads is
dead weight, don't create it; the consult-moment lives in §1's brief
parts (source label: the clause there is the one rule, this is its
machinery).

**Invalidation is part of the schema.** A change to the procedure text
(fingerprint mismatch) or to the model lineup resets `ready` →
`eval-open`. A register without invalidation decays into silent
misinformation.

**Scarcity corollary.** When the top tier is rationed, registered
procedures run on their cheapest `ready` tier by default; the top tier
is reserved for design, rule-corpus work, eval grading, and the
ambiguous multi-step tail where the tier gap is widest. (The session
model remains the operator's choice — the register informs it; the
CLAUDE.md model table governs dispatch defaults.)
