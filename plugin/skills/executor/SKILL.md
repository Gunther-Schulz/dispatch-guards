---
name: executor
description: Conduct-of-execution discipline for a session running briefed or devbook work — grounding literalism, verify with the check's own output, gaps surface never bridge, escalation returns the question, the box, the report. Use when executing a dispatch brief or a repo devbook/runbook procedure, when reporting on executed work, or when writing or grading a repo devbook against the devbook form. Counterpart of the dispatch skill (the sending side). Not for deciding what to build or whether to dispatch — the brief carries the first, the operator corpus the second.
---

# Executor discipline — conduct, under-report principle, devbook form

_Consumer: the executing session — commonly a tier below the
dispatcher, which is why §1 runs as numbered directives and §2
demands visible artifacts rather than principles alone. Maintenance
and evolution: the closing section._

Load when executing work someone else designed: a dispatch brief, a
repo devbook or runbook procedure, a certified recurring procedure
(dispatch skill §6). Briefs to tiers below the dispatching session
name this load FIRST in their grounding basis. Also load when WRITING
or GRADING a devbook — §3 defines the form.

This skill is the receiving-side counterpart of the sibling
`dispatch` skill: that one disciplines how work is handed over, this
one disciplines how handed-over work is conducted — in ANY repo. Repo
devbooks carry only repo facts (commands, paths, boundaries) and cite
this skill for conduct; the conduct layer travels by skill, never by
per-repo restatement. Grounding for the split: every recorded
dispatch failure traces to a brief defect, none to tier capacity
(dispatch skill, core finding) — a devbook exists to move design
decisions BEFORE execution and to convert the remaining judgment
moments into attention: closed STOP lists, mandatory sections, worked
examples.

## 1. Conduct of execution

The brief or devbook is the design. Execute it with fidelity; spend
judgment on honest reporting, not on redesign.

1. **Ground first, literally.** Open every file the brief names —
   actually read them; the report cites what was read. Then check the
   brief against the reality found: different structure, missing
   file, contradicting content → STOP and report the mismatch. Never
   adapt the work to make the brief fit.
2. **Numbered steps execute by number.** In order, exactly as
   written — no reordering, merging, or improving. A step that cannot
   execute as written is a gap (rule 3), not an invitation to
   interpret.
3. **Gaps surface, never bridge.** A missing decision, file, or value
   returns as a question with what was found; it is never filled with
   a plausible guess — a gap filled silently is designed at the
   executing tier, the exact failure the handover was built to avoid
   (source: dispatch skill §1, the sending-side statement).
   Every decision made anyway is listed in its own report slot, which
   SHOULD BE EMPTY: each entry there is an automatic escalation to
   the dispatcher.
4. **"Done" is the check's own output.** A completion claim carries
   the verifier's verbatim output — never a summary of it, never an
   intermediary's exit status (a launcher or scheduler reports that
   the run happened, not what it found). When the work builds a fix
   or a checker: red before green, and the red run's output goes in
   the report. (Source: site corpus Fixing rules — this is their
   prescriptive rendering for executing tiers.)
5. **Escalation returns the question.** At a STOP signal: halt that
   item, finish everything independent of it, and report signal +
   location + the decision question + a path per outcome. Never spawn
   a higher tier yourself — the dispatcher holds the design context
   and decides (dispatch skill §4).
6. **The box.** Commit unpushed by pathspec — `git commit --
   <paths>`, never `git add` then `git commit`, never `-A`: the
   INDEX is shared on a shared working copy, so a co-writer
   staging between your `git status` and your commit rides out
   under your message whatever paths you added; pathspec ignores
   the index for everything else. A NEW file is invisible to a
   pathspec commit until `git add -N <path>` registers it
   (intent-to-add: zero content staged, full body still
   committed) — the one sanctioned `add`, and not a licence to
   stage anything else (source: dispatch skill §1). Pushing,
   merging, and publishing are the dispatcher's acts. No writes
   outside the named write boundaries.
   Nothing outward-facing (sends, posts, deployments, deletions of
   truth sources) without an explicit grant in the brief. A devbook's
   own limits section binds verbatim on top of this. (Source:
   dispatch skill §1 write boundaries — the executor-side mirror.)
7. **The report.** Close with the project's own report form if it
   defines one, else the dispatch skill's §2 form
   (`../dispatch/references/forms.md`) — never both. Every slot
   appears; "none" is a valid answer, silence is not.

## 2. The under-report principle (single home; the forms cite it)

**Shape work handed to a cheaper tier so it cannot silently
under-report.** Every obligation renders as a visible artifact whose
absence is loud: mandatory sections where "none" must be written out,
closed lists that make omissions enumerable, demanded coverage
artifacts (items walked, per-class counts, zeros stated explicitly),
verbatim check output instead of claims. The dispatcher removes
silence as an option at composition time, because at execution time a
cheaper tier fills silence with confidence.

Two forms apply this principle — each cites this section rather than
restating it: the **devbook form** (§3, below) disciplines what an
executor receives as a standing procedure; the **enumeration-brief
form** (dispatch skill `references/forms.md` §3b) disciplines what an
enumerator receives in a two-stage verdict.

## 3. The devbook form (what a conforming devbook contains)

A devbook is a repo's standing procedure written for executor
sessions — a permanently existing decision-complete brief. It keeps
REPO FACTS (commands, paths, boundaries, verifiers) and cites this
skill for conduct; conduct restated per-repo drifts. A conforming
devbook contains, mechanically checkably:

1. **Head**: the addressee (tier and fresh context assumed) and the
   normative sources as an explicit file list — never "read the
   rules".
2. **Numbered steps with per-case verification**: every case or
   procedure ends by naming the command or artifact whose own output
   proves it.
3. **The box**: an explicit limits section — a closed list of what
   the executor never decides, touches, or does.
4. **STOP signals**: a closed list of halt conditions, with the
   return-the-question behavior stated (conduct rule 5).
5. **The report form**: named — the devbook's own lettered form or a
   pointer to dispatch §2 — including "empty is valid, absent is
   not".

Mechanical check: `scripts/check_devbook_form.py <file>` — a
per-element presence detector with evidence lines; PASS requires all
five. It is a detector, not the definition: the list above is
normative, the script finds the loud absences cheaply. Consumers: a
dispatcher grading a repo's devbook for class certification (dispatch
skill §6) and the author of a new devbook.

## 4. Certification tie-in

A recurring procedure class becomes cheaply dispatchable through the
dispatch skill's §6 pipeline: this skill + a form-conforming devbook
of the class + one reviewed probe, certified once and globally;
per-repo `READINESS.json` carries only exclusions and deviations, and
the first run in a new repo gets its output graded (one sentence, no
register entry). Mechanics and register: dispatch skill §6 — cite,
never duplicate.

## Evolution and maintenance

On a gap noticed in use — an execution failure this conduct layer
should have prevented, or a rule it states wrongly — write the
observation to `dev-notes/executor-OBSERVATIONS.md` in the plugin's
source repo (github.com/Gunther-Schulz/dispatch-guards) and propose
the rule change; BACKLOG.md there carries work items.

Where this skill is deployed as the operator's corpus half, it is
OPERATIONAL CORPUS with the operator CLAUDE.md and the sibling
dispatch skill: `~/.claude/CLAUDE-maintenance.md` governs every edit,
and each edit lands with a JOURNAL line in the corpus repo.
