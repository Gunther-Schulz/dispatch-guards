# dispatch-guards — ledger

On-disk ledger for this repo: one entry per line, append-only,
chronological. Facts carry their basis, decisions carry their why
(and the rejected alternative where it is not obvious), open
questions stay listed until they close. Absence of an entry never
reads as settled.

**Consumer:** any session working in this repo — read the tail before
re-deriving something that may already be settled, and append here
rather than leaving a rationale only in a commit message. Boundaries:
work items go to `BACKLOG.md`, standing rules to `CLAUDE.md`,
maintenance journals to `dev-notes/`.

Retrofitted 2026-08-06 from `git log`; only decisions whose rationale
had no home outside a commit message were seeded, so the record
before that date is deliberately sparse rather than complete.

## Entries

- **2026-08-05 (13a21f4, first instance 2026-08-01 40f22ec) — a hook
  file ships mode 100755, and the `--test` battery cannot catch it
  when it does not.** `hooks.json` execs hooks directly via `/bin/sh`,
  so a 100644 hook dies with "Permission denied" and, being fail-open,
  gates nothing — silently. Twice: `push-claim-reminder` (0.1.12,
  reminder absent) and `dispatch-skill-gate` + `discovery-volume-`
  `reminder` (0.3.2, no dispatch ever gated; found by the operator
  reading per-call error spam, hours later). Basis for the blind spot:
  the bite-tests passed throughout both, because they invoke via
  `sys.executable`, which never consults the x-bit — so a green battery
  is not evidence a hook can launch. Mechanised at both altitudes in
  the SIBLING dotfiles repo, off this repo's read path: pre-commit
  `nonexec_hook_commands` and `bootstrap/doctor.py`
  `plugin_hook_exec_verdict` / `check_plugin_hook_files` (both verified
  present 2026-08-06).

- **2026-08-06 (7ee9b35) — the 0.5.2 skill rules were applied here
  verbatim, not designed here.** Both-divergence-directions in §1, the
  reviewer-tier cap in §4, and the register consult keying on the
  TARGET repo's procedure class were settled in a prior session and
  persisted in `dotfiles docs/directives/session-b-handoff.md` — a
  sibling repo, which a fresh context in THIS repo does not load.
  Re-opening any of them means reading that file; re-deriving them
  from the skill text will not recover the grounding (e.g. the §1
  base-check split exists because the observed live case was
  HEAD-ahead, not HEAD-behind).

- **2026-08-06 (this commit) — the "no `LEDGER.md`" deviation is
  reversed; `LEDGER.md` joins the role files.** The deviation carried
  its own revisit condition — "revisit if multi-session work here
  starts re-deriving settled ground" — and that condition has fired:
  multi-session corpus work is running in this repo now. Rejected
  alternative (the deviation's original reasoning): letting commit
  messages plus `dev-notes/` carry decisions. That holds only while
  the horizon is short — a commit message is found by someone who
  already suspects what to look for, which is exactly what a
  re-deriving session does not have.

- **2026-08-06 — RULED (was OPEN; see the closing clause): `EXECUTION_TAIL_BG` (brief-reminder.py
  :414) and the EXECUTION tail in `plugin/skills/dispatch/references/`
  `forms.md:108` have really diverged, and the commissioned drift
  detector was HALTED rather than shipped.** Measured under the
  specified normalization: 5 normalized lines vs 27; three substantive
  content divergences (the ≤3000-chars sentence rewritten around
  split-parts-not-a-file; the backgrounded-check/AWAITED sentence
  absent from the literal; the never-amend sentence absent), plus
  forms.md's `<channel line>` placeholder against the literal's
  concrete background channel line. Two decisions the detector cannot
  be built without, neither of them the executor's to make: whether
  comparison is per-line (as specced — unsatisfiable, since the two
  sides are wrapped by different rules) or whitespace-insensitive over
  the whole block (what `brief-reminder._norm` does, and why); and how
  the placeholder line maps. Both files sit outside the halted
  dispatch's write boundary, so the drift itself is also unrepaired.
  RULED 2026-08-06, same day, by the dispatching session: the
  whole-block whitespace-insensitive comparison, with the documented
  background channel line substituted for `<channel line>` — but in
  repair-first order, because the baseline is currently red for real
  reasons: sync the literal to the shipped tail (keeping the
  deliberate independent-copy design), THEN build the detector, THEN
  red-proof by mutation against a now-green baseline, and give
  `tools/check-doc-drift.py`'s `main()` the could-not-verify third
  outcome it lacks. Carrier of the full ruling and its grounding:
  `dotfiles claude/BACKLOG.md`, commit `6889d12` — a sibling repo a
  fresh context here does not load, which is why the ruling is
  restated on this entry rather than pointed at. Severity correction
  belonging with it: `EXECUTION_TAIL_BG` sits inside
  `if __name__ == "__main__"` (brief-reminder.py:371), so it is a TEST
  FIXTURE and was never emitted to an agent — the consequence is that
  this guard's bite-tests pass against a tail shape the form no longer
  produces, which is the frozen-fixture class, not misinstruction.

- 2026-08-08 SHARED-INDEX SHARPEN + STORED-BRIEF STALENESS (build-first,
  operator GO "lest fix dispatch from here now"). Two amendments, both
  in place, both from one parallel dispatch on a shared working copy.
  (1) `git add <paths>` does not isolate a shared copy — the INDEX is
  shared, so a co-writer staging between an agent's `git status` and
  its commit rides out under that agent's message whatever paths it
  added. Observed: a five-file commit under a three-file message,
  carrying the co-writer's in-flight work. `git commit -- <paths>`
  isolates because it ignores the index for everything else. The
  existing clause already NAMED the hazard ("a clean targeted git add
  absorbs them") and prescribed the very form that cannot prevent it —
  a rule that diagnosed correctly and then recommended the disease.
  Generalised in the same edit: in a shared repo any state read is
  stale by the next command, so check and act belong in ONE command or
  in a form that cannot act on the wrong object — pathspec for a
  commit, an explicit hash for a reset, never `HEAD~1` (observed: a
  `reset --soft HEAD~1` aimed at the mixed commit un-committed a
  co-writer's newer one instead). Audited across all four homes that
  prescribed `git add`: dispatch §1 + its brief skeleton, the §2
  EXECUTION tail in references/forms.md (the one pasted into every
  brief, so the highest-leverage), and executor §6 "the box".
  (2) CLAUDE.md's brief-family clause: a STORED brief is a label over
  a body written at a past date, and its grade records
  decision-completeness AS OF then. Grounding: of six backlog items
  audited, two were stale — one whose diagnosis was refuted by a
  different investigation ("rotation rewrites the live file" had cause
  and effect inverted) and one whose evidence proved a badly-written
  probe rather than a missing feature. The refuted one had SURVIVED a
  fresh-context vet with its wrong hypothesis intact, because the vet
  checked the entry's reasoning and not the world. Both capability
  patches; fire-rate review judges them.

- 2026-08-08 — SHARPEN §1 (build-first, operator GO), widening the
  commissioned-instrument bullet upward: what a brief must fix is the
  instrument's SEMANTICS, of which absence-mapping was only the first
  instance. Second instance, the one that grounded the widening: a
  COMPARISON names its GRAIN. Grounding — a brief of mine specced a
  LINE-SEQUENCE comparison between brief-reminder.py's
  EXECUTION_TAIL_BG literal and the forms.md EXECUTION tail; measured
  under that exact normalization it is 5 literal lines against 27
  forms.md lines, a WRAP difference rather than a content one, so no
  state of the two files could make the check green. The dispatcher
  specced an unprovable check — the class the corpus already names,
  authored into a brief by the person who knows the class. Amendment
  over addition: the bullet's trigger abstracted upward rather than
  growing an "…or X" list; forms.md §3b's Exactness clause is
  source-labelled from the new text as the same rule inside the
  enumeration form, not re-stated. Executor side audited, no edit —
  its gaps-surface-never-bridge conduct rule already covers an
  instrument brief arriving with its grain unstated. Verify block all
  four green (bench 40/40, bites, devbook form, doc-drift, wrap).
  Durability: CAPABILITY PATCH; fire-rate review judges it.
2026-08-08 NAME-LANE STAGING BYPASS RATIFIED (operator decision, decision round item 3; parked item leaves by this commit): the mandatory-name lane keeps deny-from-day-one — check()'s exit-2 path structurally precedes guard_mode(), the repair is compose-time and mechanical (add the `<model>-` name), which is the false-fire profile staging exists to protect against; rework of check() through fire()/guard_mode() DECLINED (generality no current lane needs). Declared exception recorded beside the staging rule in CLAUDE.md; future lanes earn the same exemption only by their own operator decision.
2026-08-08 BENCH-RED REMEDIATION COMPLETE + ESCALATION ORDERING DECIDED (operator decision round items 2+4; both halves of the 0.6.x-verify-RED item and the deny_text item leave the backlog by these refs). (a) d2fdfdb (sonnet dispatch): guards.jsonl:31 silent→block, the retired-title-lane case. (b) ac8341b (sonnet dispatch): escalation_deny() now precedes check() in main() — DECISION: an escalating subagent's FIRST bounce teaches return-the-question, never "add a name" toward a call that must not succeed; two-bounce path rejected; ordering pinned by a second inspect.getsource assert (escalation_deny < error = check) plus a no-leak corpus case (NAMED subagent ask-tier → still deny). (c) 3369ccf (sonnet dispatch): missing_channel deny_text(payload) — named dispatches get the followable repair (background channel line), the sync-flag advice stays for unnamed only; red-first via battery-against-old-signature. Verified at the desk at HEAD: both --test batteries green, replay-bench 41/41, catch 16/16, false fires 0 (first fully green bench since 0.6.x). 998c9b7 bumps 0.7.1 ONCE for the batch (unbumped_plugins compares release-state, so the per-author repair commits follow bump-first — the sequencing both executors correctly halted on; brief lesson: parallel same-plugin writers need the version-bump gate pre-named, bump owned by the dispatcher).
2026-08-08 SIX BRIEF-FORM CLAUSES MINTED (operator GO on the §1 batch at the fable desk; all six READY entries leave by c282a04, bump 6a49a47 → 0.8.0): sweep surfacing (per-hit disposition accounting + instrument-positive member), criteria-as-outcomes-then-sites (graduated from dev-notes — second firing proved the shelf was the problem, not the wording), commit-plan-vs-guards sequencing (bump position derived from the guard's OWN comparison basis — checklist finding: the first draft stated one guard's release-state mechanism as universal, scoped before landing), pre-authorized repair classes (declared-exemption shape applied to briefs), per-line Background provenance grades ("from <source>, unverified" — the phantom-citation class), §3b data-file key-set quote (jq from the file, never prose — the all-null misread class). Verified: bench 41/41 unchanged, doc-drift clean, wrap 0 violations, skill-lint clean except the dispositioned forms.md:29 dead-cite (accepted 0.7.1, observation ea63c47 in skill-craft). JOURNAL line: dotfiles corpus repo, same session.
2026-08-08 WORKTREE LIFECYCLE ENGAGED — SKILL AMENDED + REPORTING DOCTOR SHIPPED (operator standing GO; the 859f965 incident is the grounding): worktree SKILL.md "Cleanup and litter" gains two rules the incident proves and the section lacked — `git worktree list` is SHARED state with no ownership dimension (nothing in `.git` records who created a worktree, so a sweep over the whole list sweeps other sessions' work), and the plain-remove refusal on a dirty worktree IS the safety mechanism, `--force` being the entire difference between cleanup and unrecoverable loss. Basis: reproduced independently at the desk in a scratch fixture — plain remove refuses with "contains modified or untracked files, use --force to delete it"; the incident's loop verbatim destroys all three arms including the dirty one. DECISION, direct conflict created by 859f965 resolved in the text: the pre-existing branch bullet's "dispose of each by merge, cherry-pick, or an explicit drop" at worktree-cleanup time contradicted the new "do not delete branches as part of any worktree cleanup" — the bullet keeps its SURFACING duty (enumerate branches created for worktrees at integration) and loses its disposal-at-cleanup clause, because branch survival is precisely what kept the incident's committed work recoverable; branch retirement is its own decision on its own trigger. Description gains "cleaning up or removing worktrees" as a trigger — the new rules' firing moment is a sweep, and no trigger covered it. Not corpus (worktree = portable git mechanics, skill-craft alone).
2026-08-08 DOCTOR DESIGN — OWNERSHIP IS DECLARED, NEVER INFERRED (dispatcher decision at brief time, filling a gap the BACKLOG entry left open): the entry fixed the doctor's verdicts and verifier but not how it knows which worktrees are the caller's, while "what marks ownership durably" is the entry's own PARKED question. Resolved by `--owned <path>` (repeatable) with everything undeclared reported UNKNOWN, never FOREIGN — the tool cannot know. Rejected: any predicate over path shape, name prefix, directory component, branch name, or commit trailer — that is the naming-convention predicate the entry rejects up front, and left to the executor it would have been re-created inside the very tool built to prevent it. This does not prejudge the parked question: a future durable mark simply auto-populates the flag, and UNKNOWN-by-default is what makes could-not-verify honest rather than a fallback.
2026-08-08 PATHSPEC-COMMIT RULE WAS FALSE FOR FILE CREATION — SHARPENED ACROSS ALL THREE HOMES (grounding: the dispatch's own blocked commit; triage = rule fired and was WRONG, so a sharpen in its existing seat, not a new entry): `git commit -- <paths>` cannot commit a wholly-new untracked file — "error: pathspec '<p>' did not match any file(s) known to git" — so the corpus rule "never `git add` then `git commit`" was unsatisfiable for any dispatch whose deliverable is a new file. Fix minted at dispatch/SKILL.md (write boundaries), dispatch/references/forms.md (the pasted EXECUTION tail — the home that actually reaches executors), executor/SKILL.md §6 (the box, with a source label to dispatch §1): `git add -N <path>` first, intent-to-add. Basis, probed at the desk rather than taken from the agent's report: index entry is the EMPTY blob e69de29 (zero content staged), the commit still carries the file's FULL body, and a co-writer's separately staged file and staged tracked-file modification both remain staged and uncommitted through it. The rule's reason (shared index) is untouched — this is a carve-out, not a softening.
2026-08-08 SUBAGENT ESCALATION HANDLED CORRECTLY, RECORDED AS THE POSITIVE CASE: the sonnet dispatch met a plugin-payload version-bump pre-commit gate that its write boundary gave it no way to satisfy (plugin.json outside its lane), and the gate's own message advertised `--no-verify` as the audited bypass. It bumped nothing, bypassed nothing, left the co-writer's file untouched, and returned the question with three named paths. Dispatcher took path (c) — the bump and release are the dispatcher's act. Candidate lesson booked from it: a brief granting a narrow write boundary in a plugin-payload repo should say up front whether version-bump gates are expected to fire and who resolves them.
