# Brief G1 — guard wave, brief-gate promotion + fingerprint-pin lane (dotfiles df-238)

Title: opus: brief gate — commit-plan lane to deny, new devbook-pin WARN lane
Working copy: /home/g/dev/Gunther-Schulz/dispatch-guards. Base check: base
commit stated in the dispatch prompt (read at dispatch time); run
`git merge-base --is-ancestor <base> HEAD`, `git log --oneline <base>..HEAD`,
`git status --porcelain` — base contained + nothing on top + clean tree
proceeds; anything else HALTS as a gap.
Scratch: your OWN scratchpad, subdirectory `g1/` — create it, write nothing
outside it there.

REGISTERED-CLASS dispatch: guard/checker builds (`guard-checker-bau`,
register ~/.claude/readiness.json, tier opus). Class devbook: dotfiles
`CLAUDE.md`, section `## Registered procedure: guard/checker builds (§6
class devbook)` — section sha256
`77c9bf3fd7dead9ae5256a7ad4df61d8e8299d4a17e9801422c2dab3d5d222b4`
(equals the register's stored fingerprint, dispatcher-verified at compose
time). Recompute from the FILE; on mismatch work from the file and report.
The devbook is READ-ONLY grounding — dotfiles is outside your write set.

## Grounding basis — read before building; the report cites what was read
- the executor skill (dispatch-guards:executor) — load FIRST
- this repo's CLAUDE.md — the staged-lane promotion discipline (how a
  staged lane earns deny) and any commit-blocking conventions
- plugin/hooks/brief-reminder.py — `missing_commit_plan` (:424, its
  docstring carries the staging sentence you are superseding),
  `missing_sections`/`_tail_kind` (the scope every lane shares),
  `_register_path`/`_register_entries`/`register_lines` (:477-590 —
  existing register plumbing the new lane reuses)
- plugin/hooks/_dispatch_common.py — `fire()`/`guard_mode()` (:255-300,
  mode-aware exit; site policy override; fire_log)
- the fire log (path per this repo's README, "Fire log, guard modes, and
  the replay bench") — the promotion evidence source
- ~/.claude/readiness.json — entry shape (`prozesse[].id`, `heimat`,
  `fingerprint`)

## Background (established; verify at the cited lines)
- The commit-plan lane ships WARN today: `missing_commit_plan` docstring
  ("Staged: it ships WARN and earns deny only through the fire-rate
  review") and `fire()`'s mode handling — dispatcher-read this session at
  the cited lines.
- Fire record grounding the promotion (AMENDED 2026-09-15 post-dispatch,
  per the lane's own verified read — this wording supersedes the
  original): the fire log holds 47 commit-plan fires, all mode=warn, and
  carries NO truth-value field, so "no false fire" is absence-of-record,
  never a measured zero. One false-fire class IS recorded elsewhere and
  REPAIRED (verifier-brief-citing-forms, 2026-08-15, 372dcc7, regression
  test :1013-1018); 39 of the 47 fires post-date that repair, and the
  desk-confirmed true positives (wave-5 set, lane E, df-3) all do. The
  promotion premise as it actually stands: 39 post-repair warn fires, at
  least six desk-confirmed true, the one known false-fire class repaired
  and test-pinned, no false fire recorded in any carrier since. That
  premise SUPPORTS the flip; the docstring's promotion record states it
  in this honest form, not as a measured zero.
- The pin-omission incident (new lane's motivation): the df-3 build brief
  2026-09-14 named a registered devbook section amended the same day and
  pinned nothing; caught by hand, no mechanism (dotfiles df-238 evidence
  slot; from the dispatcher's record, unverified against your repo).
- Installed plugin is 0.11.20, repo committed 0.11.21: repo edits are NOT
  live (plugin cache serves installPath) — your arms run the REPO binary
  directly, never the installed copy.

## The settled design — implement exactly this, do not redesign
HALF 1 — promotion: `missing_commit_plan`'s fire call takes
`default_mode="deny"` (today's shipped default for that lane is warn —
read the actual call to confirm which knob carries it and change that
knob); the docstring's staging sentence is replaced by the promotion
record (fire count, zero false fires, date, df-238). Site policy
`guard_modes` stays untouched — the flip is the SHIPPED default, per the
item's write-set.
HALF 2 — new lane `missing_devbook_pin`, WARN (staged) by shipped
default: fires on an execution-tail Agent brief (same `_tail_kind` scope
as its two siblings, verifier/discovery exempt) whose brief text names a
registered class — match: any `prozesse[].id` from the register, or the
section-name tail of any `heimat` — while containing no 64-hex token.
Absence rule, one rule not an enumeration: whatever the lane cannot read
(register missing, unparseable) → the lane stays silent and logs
nothing-to-check via its could-not-verify branch per the repo's checker
conventions. WARN text names the matched class, the pin recipe pointer
(the devbook's own fingerprint paragraph), and that the pin must be
recomputed from the FILE. ORDERING (amended 2026-09-15, ratifying the
lane's deviation): the new lane goes LAST in main(), after every deny
lane — `fire()` exits in every mode, warn included, so an early warn
lane would swallow the four shipped denies behind it; the original
"ordered before broader checks" clause transferred the named-diagnostic
rule from Report-pattern checkers to an exit-per-lane hook, where its
mechanism does not hold. A pin-less brief shadowed by a deny is denied,
repaired, and the pin WARN fires on retry — nothing lost permanently.

## Verifier (in order; real output pasted in the report)
1. Red-first, both halves, per the devbook, pinned on the EXIT DECISION
   never the message text (df-246... df-238's done-criterion): half 1 —
   the same commit-plan-less execution payload against the OLD binary
   (whole-repo snapshot per devbook step 2, its own self-check green
   first) exits WARN-shaped, against the NEW exits deny-shaped; a
   compliant payload passes both. Half 2 — a brief naming
   `guard-checker-bau` with no 64-hex token fires WARN naming the class;
   the same brief with the pin passes; a verifier-tail brief citing the
   class stays exempt (the must-not-move arm carries its own instrument,
   not the guard on trial).
2. The hook's own `--test` battery extended for both halves (same-commit
   self-check rule: each new case names its own red in the report).
3. Bump plugin.json 0.11.21 → 0.11.22 in your FINAL commit.
Expected results are dispatcher-specified.

## Write boundaries
Owned: plugin/hooks/brief-reminder.py, plugin/hooks/_dispatch_common.py
(only if the mode knob genuinely lives there — prefer the lane-local
knob), plugin.json (the bump), the hook's test file if separate, and
(GRANTED 2026-09-15 post-dispatch, closing the lane's reported gap)
tools/corpus/guards.jsonl — extend it for BOTH halves per this repo's
CLAUDE.md :155-157, in the same commits as the halves they cover.
NOT owned: hooks.json (no new hook ENTRY — the new lane rides
brief-reminder's existing wiring; if you find that impossible, STOP and
return why), SKILL.md and references (rule text is dispatcher-authored
only), dev-notes, ITEMS.md (dispatcher books; the dg item carrier is not
yours to write).
NOT live on write (installed cache serves 0.11.20) — but the repo is
SHARED with the dispatcher desk: commits unpushed, by pathspec, never
amend.

## Commit plan
Dispatcher-read at compose time: the global core.hooksPath pre-commit
applies here (machine-wide); the plugin-version drift note it prints is
informational and does not block (measured this session at commit
28119d8 in this repo). No payload-version guard blocks commits here
(read this repo's CLAUDE.md yourself and report if you find one — then
its ordering governs). Commit order: half 1, half 2, bump last —
"bump committed, UNPUSHED" is the end state; the dispatcher pushes at
integration and runs the plugin update.

    A mid-run message may not arrive before the turn ends: on a gap
    HALT THE ITEM, FINISH THE REMAINDER, REPORT — never halt the
    LANE, since "halt and wait" is not a survivable state for a
    subagent (source: §2, the delivery binding).
    Closing report (mandatory; the project's own report form if it
    defines one, else the §2 form here — never both; "none" is a
    valid slot answer, silence is not): (a) items completed w/
    evidence, (b) checks RUN w/ real output — FULL counts incl.
    skips (`N passed, M failed, K skipped`), each skip dispositioned
    (which check, why, whether the reason touches the item); a skip
    in a check YOU built is a finding, not a pass — the built branch
    did not execute, (c) gaps surfaced —
    incl. anything needing a tier above yours, returned as a question
    with its evidence, never settled at your tier,
    (d) deviations w/ reason, (e) candidate lessons, (f) files
    touched + commit hashes (unpushed) — only commits whose
    Co-Authored-By trailer is YOURS; one you cannot claim by
    trailer is "present in the tree, not mine"; a `.git/config`
    write counts as a repo write, (g) what was NOT verified,
    (h) sources actually read, of those the brief named.
    Every claim about something OUTSIDE your own work — a file you
    did not write, a mechanism, another repo, a tool's behavior —
    names the read that opened it, or carries "inferred,
    unverified"; a recommendation resting on an unopened claim
    carries the grade too.
    Drain your inbox before sending, and between parts of a
    multi-part report: every dispatcher message received up to send
    time is dispositioned or named as unhandled.
    Report channel: SendMessage to the dispatcher — your final text
    reaches no one.
    Message ≤3000 chars each: a report longer than one message is
    SPLIT into labeled parts (1/N) — do NOT write a report FILE
    (harness-blocked for subagents); supporting data goes to the
    brief's assigned DATA files, the message carries key findings
    + any such paths. A missing decision, file,
    or value is surfaced as a gap, never bridged with a guess.
    A check that got backgrounded is AWAITED before the closing
    report (TaskOutput block=true on its task id) — ending your
    turn orphans it; a report sent with a check still running is
    an INTERIM report, says so, and names what remains.
    Commits unpushed, by pathspec — `git commit -m "…" -- <paths>`
    with every flag BEFORE the `--` (after it git reads `-m` as a
    pathspec and the commit fails; `-F` for a multi-line message),
    never
    `git add` then `git commit` and never `-A`: the index is shared,
    so a co-writer staging between your `git status` and your commit
    rides out under your message whatever you added. A NEW file is
    invisible to a pathspec commit until `git add -N <path>`
    registers it (intent-to-add: zero content staged, full body
    still committed). Trailer:
    `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.
    Never amend — always a new commit: the amend-gate denies
    subagent amends regardless of ownership (source: §1 amend
    rule).
    After sending the report your write grant is over: a defect you
    find later is REPORTED, never edited or amended (source: §4
    ownership rule).

Before your first build call, one message on the report channel: which
Background line you find unopened or wrong, and which two lines of this
brief contradict each other — then continue without waiting for a reply.
