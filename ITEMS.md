schema: 2
baseline: 39
added: 21
compacted: 0

## dg-1
grade: READY
requirement: READY 2026-08-27 (wave-4 peer desk, from lane `opus-lc44-48-49`'s finding on an instrument it does not own) — `report-form-gate` scores a message ABOUT a report as a report, and its obvious repair is unsafe — record: BACKLOG.md:10
goal: UNKNOWN
write-set: UNKNOWN
done-criterion: UNKNOWN
evidence: BACKLOG.md:10-55
blocked-by: decision regrade: was READY under the old carrier: READY is judged, never inherited
amend-reason: 2026-10-05 lc-312: the migrated question was shared by every item of its branch, so one ledger answer cleared all of them; it now names this item
amended-blocked-by: 2026-10-05 decision regrade: was READY under the old carrier: READY is judged, never inherited (item dg-1)
amend-reason: 2026-10-07 2026-10-07 re-grade pass: slots filled from the legacy body and a same-day premise check against the repo
amended-goal: 2026-10-07 general-maintenance
amended-write-set: 2026-10-07 plugin/hooks/report-form-gate.py,tools/corpus/guards.jsonl
amended-done-criterion: 2026-10-07 Verifier: those five arms as gate-level payload tests (the real binary over stdin, not the predicate alone), plus the false-fire probe ... run the gate against its OWN docstring and against this entry's text; both must stay quiet. Done-criterion: the five arms pass at gate level, the two self-matching probes are quiet, and the existing report-form bites stay green.
amended-evidence: 2026-10-07 RELAYED from the read-only lane sonnet-regrade-enum, 2026-10-07 (premise token PREMISE-LIVE): Python read of plugin/hooks/report-form-gate.py -> line 55: `_SLOT_RE = re.compile(r"\(([a-h])\)")` (unchanged; body cited :55) and line 59 `return set(_SLOT_RE.findall(message))`. Positive control: same read found REPORT_MIN_SLOTS = 4 at :53. Designed replacement regex `(?:^|(?<=[.;:!?]\s))` has 0 hits in the file. Not exercised: I did not run the gate on the ping payload (read-only lane). | Original body: BACKLOG.md blob bb93897, the line range in the first evidence line above.
amended-blocked-by: 2026-10-07 NONE
promote-reason: 2026-10-07 was READY under the old carrier and its premise is confirmed live today; the legacy body states design, verifier and write-set, now carried in the slots
promoted-by: 2026-10-07 dispatch-guards-99 (opus desk, operator-delegated 2026-10-07: all decisions as the desk recommends)

## dg-5
grade: PARKED
requirement: PARKED 2026-08-27 (wave-4 peer desk, lane A2 gap 3) — §1's `## Background` slot now states two overlapping demands in adjacent lines — record: BACKLOG.md:122
goal: UNKNOWN
write-set: UNKNOWN
done-criterion: UNKNOWN
evidence: BACKLOG.md:122-136
blocked-by: dg-47

## dg-7
grade: PARKED
requirement: PARKED 2026-08-26 — depth-2 dispatch: a desk-tier middle agent that fans out, under the same hook-controlled robustness and operator transparency as depth 1 (operator decision: worth trying; robust or not at all) — record: BACKLOG.md:191
goal: UNKNOWN
write-set: UNKNOWN
done-criterion: UNKNOWN
evidence: BACKLOG.md:191-225
blocked-by: decision does the operator open a depth-2 trial with CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH raised above 1, so one planted grandchild dispatch can show whether the gates see it
not-derivable: 2026-10-07 the spawn-depth value is an operator-pinned setting (dotfiles claude/settings.json:7); reversing a pin is never derivable by a desk, and no ledger line or directive opens the trial

## dg-8
grade: READY
requirement: READY 2026-08-20 — audit every hook's `--test` for the recompose-instead-of-invoke shape: a bite that rebuilds a function's callees by hand cannot see that function lose its wiring — record: BACKLOG.md:226
goal: UNKNOWN
write-set: UNKNOWN
done-criterion: UNKNOWN
evidence: BACKLOG.md:226-269
blocked-by: decision regrade: was READY under the old carrier: READY is judged, never inherited
amend-reason: 2026-10-05 lc-312: the migrated question was shared by every item of its branch, so one ledger answer cleared all of them; it now names this item
amended-blocked-by: 2026-10-05 decision regrade: was READY under the old carrier: READY is judged, never inherited (item dg-8)
amend-reason: 2026-10-07 2026-10-07 re-grade pass: slots filled from the legacy body and a same-day premise check against the repo
amended-goal: 2026-10-07 general-maintenance
amended-write-set: 2026-10-07 plugin/hooks/
amended-done-criterion: 2026-10-07 Verifier / red-first, per hook touched: delete the emitting call site from `main()` in a scratch copy → the new bite must go RED; restore → green ... Done when every hook is either covered by an end-to-end bite or recorded here as deliberately exempt with its reason, and the count of each is stated rather than implied.
amended-evidence: 2026-10-07 RELAYED from the read-only lane sonnet-regrade-enum, 2026-10-07 (premise token PREMISE-UNCHECKABLE): Settling needs a per-hook mutation experiment (delete emitting call, watch the bite) - not read-only. Partial read-only signal: Python scan of each hook's text after '"--test"' counts `main()` calls: agent-model-gate 5, amend-gate 2, brief-reminder 8, discovery-volume 1, dispatch-log 3, dispatch-skill-gate 3, message-payload 1, push-claim 1, report-enforcer 5, report-form 2, report-reminder 1, subagent-push 1, worktree-config 1, writer-claims 3, writer-reservation 3, _dispatch_common 0 (library). A main() call in the test does not show it covers each emitted output. Searched LEDGER.md and ITEMS-DONE.md for 'recompose', 'end-to-end bite', 'liveness net': 0 hits each (control: other keywords hit in LEDGER.md) - no audit record found. | Original body: BACKLOG.md blob bb93897, the line range in the first evidence line above.
amended-blocked-by: 2026-10-07 NONE
promote-reason: 2026-10-07 was READY under the old carrier and its premise is confirmed live today; the legacy body states design, verifier and write-set, now carried in the slots
promoted-by: 2026-10-07 dispatch-guards-99 (opus desk, operator-delegated 2026-10-07: all decisions as the desk recommends)

## dg-9
grade: PARKED
requirement: READY 2026-08-20 — §1 brief rule: read the REAL instance before shipping a parser for a format the brief describes only in prose — record: BACKLOG.md:270
goal: UNKNOWN
write-set: UNKNOWN
done-criterion: UNKNOWN
evidence: BACKLOG.md:270-312
blocked-by: decision regrade: was READY under the old carrier: READY is judged, never inherited
blocker-exercise: 2026-10-07 live 1 | accept arm: the same test over the installed 0.11.26 directory exits 0 (run 2026-10-07); refuse arm: the predicate as written exits 1 today, 0.11.27 not being installed
amend-reason: 2026-10-05 lc-312: the migrated question was shared by every item of its branch, so one ledger answer cleared all of them; it now names this item
amended-blocked-by: 2026-10-05 decision regrade: was READY under the old carrier: READY is judged, never inherited (item dg-9)
amend-reason: 2026-10-07 2026-10-07 re-grade pass: slots filled from the legacy body and a same-day premise check against the repo
amended-goal: 2026-10-07 general-maintenance
amended-write-set: 2026-10-07 plugin/skills/dispatch/SKILL.md
amended-done-criterion: 2026-10-07 Verifier: doc-drift green, the 69-column wrap block, and a reader test — the widened bullet covers the register case without naming it. Done when the clause is in §1 and the plugin is released.
amended-evidence: 2026-10-07 RELAYED from the read-only lane sonnet-regrade-enum, 2026-10-07 (premise token PREMISE-LIVE): plugin/skills/dispatch/SKILL.md:666 `- **Schema-bearing external facts: raw source text only.** When the` - bullet present; normalized phrase search over SKILL.md: 'real instance' 0, 'no fixture exists' 0, 'on disk' 0 (control: 'Schema-bearing external facts' 1 hit, same instrument). Widening clause absent. | RELAYED, adjacent record: LEDGER.md:172 states the lesson ('LEHRE, an den Skill-Text zu geben: ... die reale Instanz lesen') but does not record it landed. | Original body: BACKLOG.md blob bb93897, the line range in the first evidence line above.
amended-blocked-by: 2026-10-07 NONE
promote-reason: 2026-10-07 was READY under the old carrier and its premise is confirmed live today; the legacy body states design, verifier and write-set, now carried in the slots
promoted-by: 2026-10-07 dispatch-guards-99 (opus desk, operator-delegated 2026-10-07: all decisions as the desk recommends)
amend-reason: 2026-10-07 the build landed; the entry records its commit and waits only on the release its done-criterion names
amended-evidence: 2026-10-07 BUILT 2026-10-07 at 6571f0a,bf3befe. MEASURED by the desk: the schema-bearing bullet names the internal twin (real instance on disk, or say none exists); wrap, lint and drift clean. RECALLED from the earlier slot: legacy body in BACKLOG.md blob bb93897, premise confirmed live the same day by the read-only re-grade lane.
amend-reason: 2026-10-07 built today; the only thing left is the release its done-criterion names, so the blocker is now that release
amended-blocked-by: 2026-10-07 evidence test -d $HOME/.claude/plugins/cache/dispatch-guards-marketplace/dispatch-guards/0.11.27  # built and verified; waits only on the 0.11.27 release reaching the installed plugin (operator act). A release that skips 0.11.27 needs this path edited

## dg-10
grade: READY
requirement: READY 2026-08-20 — `_dispatch_common.fire()` hardcodes `hookEventName: "PreToolUse"`, so the next non-PreToolUse lane that reaches for it ships a guard whose injection never lands — record: BACKLOG.md:313
goal: UNKNOWN
write-set: UNKNOWN
done-criterion: UNKNOWN
evidence: BACKLOG.md:313-352
blocked-by: decision regrade: was READY under the old carrier: READY is judged, never inherited
amend-reason: 2026-10-05 lc-312: the migrated question was shared by every item of its branch, so one ledger answer cleared all of them; it now names this item
amended-blocked-by: 2026-10-05 decision regrade: was READY under the old carrier: READY is judged, never inherited (item dg-10)
amend-reason: 2026-10-07 2026-10-07 re-grade pass: slots filled from the legacy body and a same-day premise check against the repo
amended-goal: 2026-10-07 general-maintenance
amended-write-set: 2026-10-07 plugin/hooks/_dispatch_common.py
amended-done-criterion: 2026-10-07 fire() takes the hook event as a parameter defaulting to PreToolUse; a bite asserts that a call naming another event emits that event in hookSpecificOutput.hookEventName and that the default is unchanged; replay-bench totals unchanged with 0 mismatch. The Stop-lane consumer the legacy verifier named was reverted (286484a), so no consumer change is in scope.
amended-evidence: 2026-10-07 RELAYED from the read-only lane sonnet-regrade-enum, 2026-10-07 (premise token PREMISE-LIVE): plugin/hooks/_dispatch_common.py:266 `def fire(reason: str, source: str = "dispatch-guards", payload: dict | None = None, default_mode: str = "deny")` - no `event` parameter; :284 `"hookEventName": "PreToolUse",` inside fire(); also :161 and :202 in the deny/ask payloads. handoff-report-gate.py missing (reverted at 286484a), so the 'local duplicate' half of the body is moot; the latent defect stands. | RELAYED, adjacent record: LEDGER.md:172 records handoff-report-gate reverted (0b666fc -> 286484a); no entry closes the fire() parameter. | Original body: BACKLOG.md blob bb93897, the line range in the first evidence line above.
amended-blocked-by: 2026-10-07 NONE
promote-reason: 2026-10-07 was READY under the old carrier and its premise is confirmed live today; the legacy body states design, verifier and write-set, now carried in the slots
promoted-by: 2026-10-07 dispatch-guards-99 (opus desk, operator-delegated 2026-10-07: all decisions as the desk recommends)

## dg-11
grade: READY
requirement: READY 2026-08-20 — two unlabeled restatements in the forms.md EXECUTION tail (corpus-harmony F7 + F13) — record: BACKLOG.md:353
goal: UNKNOWN
write-set: UNKNOWN
done-criterion: UNKNOWN
evidence: BACKLOG.md:353-404
blocked-by: decision regrade: was READY under the old carrier: READY is judged, never inherited
amend-reason: 2026-10-05 lc-312: the migrated question was shared by every item of its branch, so one ledger answer cleared all of them; it now names this item
amended-blocked-by: 2026-10-05 decision regrade: was READY under the old carrier: READY is judged, never inherited (item dg-11)
amend-reason: 2026-10-07 2026-10-07 re-grade pass: slots filled from the legacy body and a same-day premise check against the repo
amended-goal: 2026-10-07 general-maintenance
amended-write-set: 2026-10-07 plugin/skills/dispatch/references/forms.md,plugin/hooks/brief-reminder.py
amended-done-criterion: 2026-10-07 Verifier: `python3 tools/check-doc-drift.py` green ... the 69-column wrap block ..., and a reader test — each labeled clause names the section it borrows from. Done when both labels are in the tail and the plugin is released.
amended-evidence: 2026-10-07 RELAYED from the read-only lane sonnet-regrade-enum, 2026-10-07 (premise token PREMISE-LIVE): git show 3150a14:plugin/skills/dispatch/references/forms.md: EXECUTION tail starts :281; skip-count clause :290-294 and pathspec/shared-index clause :322-332 carry no `(source: ...)` parenthetical (the only labels in the tail are :286 `(source: §2, the delivery binding)`, :334-335 `(source: §1 amend rule)`, :337-338 `(source: §4 ownership rule)`). The third item: forms.md:82 `An idle agent without a report gets the report demanded (SendMessage),` still present; 'demanded via SendMessage' 0 hits (normalized; control: 'the report demanded (SendMessage)' 1 hit). Line number is 82, not the body's 52 (file grew). Desk is editing the file concurrently; read is of 3150a14. | Original body: BACKLOG.md blob bb93897, the line range in the first evidence line above.
amended-blocked-by: 2026-10-07 NONE
promote-reason: 2026-10-07 was READY under the old carrier and its premise is confirmed live today; the legacy body states design, verifier and write-set, now carried in the slots
promoted-by: 2026-10-07 dispatch-guards-99 (opus desk, operator-delegated 2026-10-07: all decisions as the desk recommends)

## dg-12
grade: PARKED
requirement: READY 2026-08-20 (unparked same day — both named conditions met) — "site corpus" vs "operator corpus": one referent, two terms, and a grep-audit on either misses the other (corpus-harmony F12) — record: BACKLOG.md:405
goal: UNKNOWN
write-set: UNKNOWN
done-criterion: UNKNOWN
evidence: BACKLOG.md:405-453
blocked-by: decision regrade: was READY under the old carrier: READY is judged, never inherited
blocker-exercise: 2026-10-07 live 1 | accept arm: the same test over the installed 0.11.26 directory exits 0 (run 2026-10-07); refuse arm: the predicate as written exits 1 today, 0.11.27 not being installed
amend-reason: 2026-10-05 lc-312: the migrated question was shared by every item of its branch, so one ledger answer cleared all of them; it now names this item
amended-blocked-by: 2026-10-05 decision regrade: was READY under the old carrier: READY is judged, never inherited (item dg-12)
amend-reason: 2026-10-07 2026-10-07 re-grade pass: slots filled from the legacy body and a same-day premise check against the repo
amended-goal: 2026-10-07 general-maintenance
amended-write-set: 2026-10-07 plugin/skills/dispatch/SKILL.md,plugin/skills/dispatch/references/routing.md,plugin/skills/executor/SKILL.md
amended-done-criterion: 2026-10-07 Verifier: after the sweep, `grep -o "operator corpus"` over `plugin/skills/` returns exactly the carve-outs named above and nothing else — stated as a number before the edit ... Done when that count matches and the plugin is released.
amended-evidence: 2026-10-07 RELAYED from the read-only lane sonnet-regrade-enum, 2026-10-07 (premise token PREMISE-LIVE): Python normalized count of 'operator corpus' now: dispatch/SKILL.md 4 (:3, :67, :99, :1110), forms.md (3150a14) 0, routing.md 1 (:107), executor/SKILL.md 1 (:3), worktree/SKILL.md 0 = 6; body measured 6 operator ('SKILL.md 9/4, forms.md 2/0, routing.md 1/1, executor 1/1'). Sweep not done: count unchanged (site-corpus count rose 13 -> 15 by my count: 9+2+3+1, routing.md 1->3, so another hand added 'site corpus' but replaced no 'operator corpus'). Whether the 4 SKILL.md hits include the two named carve-out footers needs a read I did not do. | Original body: BACKLOG.md blob bb93897, the line range in the first evidence line above.
amended-blocked-by: 2026-10-07 NONE
promote-reason: 2026-10-07 was READY under the old carrier and its premise is confirmed live today; the legacy body states design, verifier and write-set, now carried in the slots
promoted-by: 2026-10-07 dispatch-guards-99 (opus desk, operator-delegated 2026-10-07: all decisions as the desk recommends)
amend-reason: 2026-10-07 the build landed; the entry records its commit and waits only on the release its done-criterion names
amended-evidence: 2026-10-07 BUILT 2026-10-07 at 6571f0a. MEASURED by the desk: six replacements; a wrap-aware count of the old term over plugin/skills reads 0, predicted before the edit. RECALLED from the earlier slot: legacy body in BACKLOG.md blob bb93897, premise confirmed live the same day by the read-only re-grade lane.
amend-reason: 2026-10-07 built today; the only thing left is the release its done-criterion names, so the blocker is now that release
amended-blocked-by: 2026-10-07 evidence test -d $HOME/.claude/plugins/cache/dispatch-guards-marketplace/dispatch-guards/0.11.27  # built and verified; waits only on the 0.11.27 release reaching the installed plugin (operator act). A release that skips 0.11.27 needs this path edited

## dg-13
grade: PARKED
requirement: PARKED 2026-08-20 — a PDF-extraction recipe sits among the executor's format-agnostic conduct rules (corpus-harmony F14) — record: BACKLOG.md:454
goal: UNKNOWN
write-set: UNKNOWN
done-criterion: UNKNOWN
evidence: BACKLOG.md:454-487
blocked-by: external the executor skill's next consolidation pass decides the PDF recipe's home (a references file, a lens outside this repo, or retirement); fire-silence alone does not discriminate, and the cut belongs to consolidation

## dg-14
grade: PARKED
requirement: PARKED 2026-08-20 (was READY 2026-08-17; BUILT, then REVERTED at `286484a`) — a marker-gated Stop lane for handed-off desks — record: BACKLOG.md:488
goal: UNKNOWN
write-set: UNKNOWN
done-criterion: UNKNOWN
evidence: BACKLOG.md:488-576
blocked-by: external a real transcript of a session RECEIVING a peer handoff is in hand to define the ending turn against; the reverted build (286484a) failed on a hand-built fixture and on telling receiving from reading

## dg-16
grade: PARKED
requirement: PARKED 2026-08-15 — the channel lanes read the PROMPT as a flat substring haystack, and three shapes slip through — record: BACKLOG.md:599
goal: UNKNOWN
write-set: UNKNOWN
done-criterion: UNKNOWN
evidence: BACKLOG.md:599-629
blocked-by: external the next guard fire-rate review reads the channel lane's fires and rules whether a prose channel sentence stays an accepted form; tightening the predicate before that risks denying legitimate briefs

## dg-18
grade: READY
requirement: PARKED 2026-08-15 — report-enforcer asks the stopping agent a question it may not be able to answer: which LANE it is in — record: BACKLOG.md:643
goal: UNKNOWN
write-set: UNKNOWN
done-criterion: UNKNOWN
evidence: BACKLOG.md:643-679
blocked-by: evidence false  # the named missing evidence in the source body
amend-reason: 2026-10-07 2026-10-07 re-grade pass: slots filled from the legacy body and a same-day premise check against the repo
amended-goal: 2026-10-07 general-maintenance
amended-write-set: 2026-10-07 plugin/hooks/report-enforcer.py
amended-done-criterion: 2026-10-07 A probe records whether the SubagentStop hook input (or the stopping agent's own context) carries the dispatch name. If it does, the hook selects the lane branch itself and the self-classification text goes; if it does not, the docstring's soft-spot note states the probe and its result instead of calling the question unestablished. Either way a bite pins the outcome.
amended-evidence: 2026-10-07 RELAYED from the read-only lane sonnet-regrade-enum, 2026-10-07 (premise token PREMISE-LIVE): plugin/hooks/report-enforcer.py:17 `Known soft spot: the LANE judgment is delegated to the stopping` ... :20 `subagent can even observe its own lane is unestablished` - docstring still states the open question; :72 `If you are a NAMED/mailbox agent` and :83 `If you are an UNNAMED subagent` - branch still self-classified. The body's CORRECTION (vocabulary repaired, NAMED/mailbox vs UNNAMED) is visible at :5-10. Probe not run. | Original body: BACKLOG.md blob bb93897, the line range in the first evidence line above.
amended-blocked-by: 2026-10-07 NONE
promote-reason: 2026-10-07 the named missing evidence is a probe a lane can run, not a wait: the item now asks for the probe and for either outcome's repair
promoted-by: 2026-10-07 dispatch-guards-99 (opus desk, operator-delegated 2026-10-07: all decisions as the desk recommends)

## dg-23
grade: PARKED
requirement: PARKED 2026-08-08 — worktree LIFECYCLE: nobody removes worktrees, and the sweep that does has no ownership predicate. Named missing evidence: whether this generalises beyond one repo, and a false-fire rate for any retirement trigger before… — record: BACKLOG.md:788
goal: UNKNOWN
write-set: UNKNOWN
done-criterion: UNKNOWN
evidence: BACKLOG.md:788-833
blocked-by: external a second repo records unowned worktrees accumulating, or a candidate retirement trigger gets a measured false-fire rate; until then only the reporting doctor ships

## dg-24
grade: PARKED
requirement: PARKED 2026-08-05 — worktree skill: name the failure SHAPE of a missing dependency tree (hang, not error) — record: BACKLOG.md:834
goal: UNKNOWN
write-set: UNKNOWN
done-criterion: UNKNOWN
evidence: BACKLOG.md:834-889
blocked-by: evidence false  # the named missing evidence in the source body
blocker-exercise: 2026-10-07 live 1 | accept arm: the same test over the installed 0.11.26 directory exits 0 (run 2026-10-07); refuse arm: the predicate as written exits 1 today, 0.11.27 not being installed
amend-reason: 2026-10-07 2026-10-07 re-grade pass: slots filled from the legacy body and a same-day premise check against the repo
amended-goal: 2026-10-07 general-maintenance
amended-write-set: 2026-10-07 plugin/skills/worktree/SKILL.md
amended-done-criterion: 2026-10-07 The clause lands inside the existing section 'A fresh worktree has no untracked state', scoped to the ecosystem it was measured in (Node: a missing dependency tree presents as a hang, not an error), saying outright that other ecosystems are unobserved. Exit (b) of the entry's two is the one taken. Released with the next version.
amended-evidence: 2026-10-07 RELAYED from the read-only lane sonnet-regrade-enum, 2026-10-07 (premise token PREMISE-LIVE): plugin/skills/worktree/SKILL.md:99 `## A fresh worktree has no untracked state` present (body cited :87; file moved); regex /900|node_modules|hang|wedge/ over SKILL.md -> only 2 unrelated hits (:99 heading text, :201); dev-notes/worktree-OBSERVATIONS.md /node_modules|900|hang|wedge/ -> 4 hits, all unrelated ('unchanged', 'git log -L'); control: that file has 63 'worktree' hits. Clause absent; no second-ecosystem record found. | Original body: BACKLOG.md blob bb93897, the line range in the first evidence line above.
amended-blocked-by: 2026-10-07 NONE
promote-reason: 2026-10-07 the entry offered two exits and exit (b), scoping the clause to the measured ecosystem, needs no further evidence
promoted-by: 2026-10-07 dispatch-guards-99 (opus desk, operator-delegated 2026-10-07: all decisions as the desk recommends)
amend-reason: 2026-10-07 the build landed; the entry records its commit and waits only on the release its done-criterion names
amended-evidence: 2026-10-07 BUILT 2026-10-07 at 7d91eae. MEASURED by the desk: clause inside the existing section, scoped to Node, other ecosystems stated unobserved. RECALLED from the earlier slot: legacy body in BACKLOG.md blob bb93897, premise confirmed live the same day by the read-only re-grade lane.
amend-reason: 2026-10-07 built today; the only thing left is the release its done-criterion names, so the blocker is now that release
amended-blocked-by: 2026-10-07 evidence test -d $HOME/.claude/plugins/cache/dispatch-guards-marketplace/dispatch-guards/0.11.27  # built and verified; waits only on the 0.11.27 release reaching the installed plugin (operator act). A release that skips 0.11.27 needs this path edited

## dg-26
grade: READY
requirement: PARKED 2026-08-10 — replay-bench corpus does not cover writer-claims-gate (0 cases), and relief may not be expressible there at all — record: BACKLOG.md:899
goal: UNKNOWN
write-set: UNKNOWN
done-criterion: UNKNOWN
evidence: BACKLOG.md:899-924
blocked-by: decision the missing decision named in the source body: answer it, then re-grade
amend-reason: 2026-10-05 lc-312: the migrated question was shared by every item of its branch, so one ledger answer cleared all of them; it now names this item
amended-blocked-by: 2026-10-05 decision the missing decision named in the source body: answer it, then re-grade (item dg-26)
amend-reason: 2026-10-07 2026-10-07 re-grade pass: slots filled from the legacy body and a same-day premise check against the repo
amended-goal: 2026-10-07 general-maintenance
amended-write-set: 2026-10-07 tools/replay-bench.py
amended-done-criterion: 2026-10-07 The bench carries a declared exclusion set (writer-claims-gate and writer-reservation-gate, each with its reason: stateful) and VERIFIES it: a hook under plugin/hooks with zero corpus cases that is not in the set fails the run, and so does a set member that has cases. Red-first: remove one member from the set and the bench goes red naming it.
amended-evidence: 2026-10-07 RELAYED from the read-only lane sonnet-regrade-enum, 2026-10-07 (premise token PREMISE-LIVE): tools/corpus/guards.jsonl: 67 cases, hook counts brief-reminder 17, subagent-push-gate 11, agent-model-gate 10, amend-gate 7, message-payload-gate 6, report-form-gate 6, dispatch-skill-gate 4, push-claim-reminder 3, worktree-config-gate 3 - 0 for writer-claims-gate and writer-reservation-gate. tools/replay-bench.py:14-17 now declares 'Boundary: STATELESS guards only. `writer-claims-gate` is EXCLUDED' (partial decision, prose docstring only; regex EXCLUDED|exclusion -> that 1 hit, so no code verifies it, and writer-reservation-gate is not named there). | Original body: BACKLOG.md blob bb93897, the line range in the first evidence line above.
amended-blocked-by: 2026-10-07 NONE
promote-reason: 2026-10-07 the missing decision is made: a declared exclusion the bench verifies. The bench already states the stateless boundary in its docstring, and extending the fixture model to seed gate state would rebuild what each gate's own --test already does
promoted-by: 2026-10-07 dispatch-guards-99 (opus desk, operator-delegated 2026-10-07: all decisions as the desk recommends)

## dg-27
grade: PARKED
requirement: PARKED 2026-08-10 — two probe-craft clauses for the class devbook, batched to spare the register fingerprint — record: BACKLOG.md:925
goal: UNKNOWN
write-set: UNKNOWN
done-criterion: UNKNOWN
evidence: BACKLOG.md:925-965
blocked-by: external the dotfiles desk amends the registered-procedure devbook section (dotfiles CLAUDE.md), where these four probe-craft clauses land; the write is outside this repo

## dg-28
grade: READY
requirement: PARKED 2026-08-10 — neutralize the remaining `CLAUDE.md` mentions in HOOK docstrings and one runtime string for outside sharing — record: BACKLOG.md:966
goal: UNKNOWN
write-set: UNKNOWN
done-criterion: UNKNOWN
evidence: BACKLOG.md:966-979
blocked-by: decision regrade: fill goal, write-set, done-criterion and evidence, or drop
amend-reason: 2026-10-05 lc-312: the migrated question was shared by every item of its branch, so one ledger answer cleared all of them; it now names this item
amended-blocked-by: 2026-10-05 decision regrade: fill goal, write-set, done-criterion and evidence, or drop (item dg-28)
amend-reason: 2026-10-07 2026-10-07 re-grade pass: slots filled from the legacy body and a same-day premise check against the repo
amended-goal: 2026-10-07 general-maintenance
amended-write-set: 2026-10-07 plugin/hooks/agent-model-gate.py,plugin/hooks/brief-reminder.py,plugin/hooks/discovery-volume-reminder.py,plugin/hooks/dispatch-log.py,plugin/hooks/push-claim-reminder.py,plugin/hooks/subagent-push-gate.py
amended-done-criterion: 2026-10-07 No hook docstring or runtime string names the operator's CLAUDE.md as if every site had one: each mention reads 'site corpus' (the skills' surviving term, dg-12) or names the file as this site's example. The runtime string at discovery-volume-reminder.py:85 changes with a bench or bite case pinning the new text; every hook --test and the bench stay green.
amended-evidence: 2026-10-07 RELAYED from the read-only lane sonnet-regrade-enum, 2026-10-07 (premise token PREMISE-LIVE): Python count of literal 'CLAUDE.md' per hook file: agent-model-gate 7, brief-reminder 8, discovery-volume-reminder 3, dispatch-log 1, push-claim-reminder 1, subagent-push-gate 1, all others 0 (six files now vs body's five). discovery-volume-reminder.py:85 `"context — the discovery-dispatch rule may apply (CLAUDE.md "` still in the runtime string. Trigger: this repo is PUBLIC per CLAUDE.md '## Carve-outs' (gh visibility claim recorded there; not re-run), which bears on the trigger but whether a 'decision to publish' was taken is judgment. | Original body: BACKLOG.md blob bb93897, the line range in the first evidence line above.
amended-blocked-by: 2026-10-07 NONE
promote-reason: 2026-10-07 its trigger (the plugin shared outside this site) has fired: the repo is public
promoted-by: 2026-10-07 dispatch-guards-99 (opus desk, operator-delegated 2026-10-07: all decisions as the desk recommends)

## dg-29
grade: READY
requirement: READY — A file handoff between two live writers is evidenced by a commit hash, never by a stated intention — record: BACKLOG.md:980
goal: UNKNOWN
write-set: UNKNOWN
done-criterion: UNKNOWN
evidence: BACKLOG.md:980-1009
blocked-by: decision regrade: was READY under the old carrier: READY is judged, never inherited
amend-reason: 2026-10-05 lc-312: the migrated question was shared by every item of its branch, so one ledger answer cleared all of them; it now names this item
amended-blocked-by: 2026-10-05 decision regrade: was READY under the old carrier: READY is judged, never inherited (item dg-29)
amend-reason: 2026-10-07 2026-10-07 re-grade pass: slots filled from the legacy body and a same-day premise check against the repo
amended-goal: 2026-10-07 general-maintenance
amended-write-set: 2026-10-07 plugin/skills/dispatch/SKILL.md,plugin/hooks/brief-reminder.py
amended-done-criterion: 2026-10-07 Verifier: brief-reminder's own bite tests — a handoff message naming no hash draws the advisory; one naming a hash does not. Done-criterion: the clause in §1 beside the one-writer rule, and its bite pair green.
amended-evidence: 2026-10-07 RELAYED from the read-only lane sonnet-regrade-enum, 2026-10-07 (premise token PREMISE-LIVE): dispatch/SKILL.md normalized phrase search: 'commits first' 0, 'names the hash' 0, 'a handoff of a file' 0, 'file handoff' 0, 'stated intention' 0; control: 'clean tree' 1 hit and 'serialize' 5 hits in the same file. Nearest text: SKILL.md 'disjointness is per file, and commits serialize on shared files' - the body-named clause (releasing party commits first, names the hash; receiver verifies clean tree) is not present. The closest LEDGER entry (:186) adds the DISPATCHER as co-writer, a different clause. | Original body: BACKLOG.md blob bb93897, the line range in the first evidence line above.
amended-blocked-by: 2026-10-07 NONE
promote-reason: 2026-10-07 was READY under the old carrier and its premise is confirmed live today; the legacy body states design, verifier and write-set, now carried in the slots
promoted-by: 2026-10-07 dispatch-guards-99 (opus desk, operator-delegated 2026-10-07: all decisions as the desk recommends)

## dg-33
grade: PARKED
requirement: `push-claim-reminder`'s REMINDER lane matches the raw command while the DENY lane strips heredoc bodies, so any commit whose MESSAGE mentions pushing draws a push advisory — record: dotfiles BACKLOG.md:2256-2293 (frozen legacy carrier, blob c95b4af2)
goal: general-maintenance
write-set: plugin/hooks/push-claim-reminder.py
done-criterion: Both lanes read the same stripped command; the red is demonstrated over a stated green baseline; every existing `--test` case stays green; released and pinned, since a hook change reaches running sessions only through a release.
evidence: RELOCATED from dotfiles df-61 under df-167 (operator decision 2026-09-12, relayed through judgment desk dotfiles-85 from drain desk dotfiles-49; authorization chain is relayed-under-standing-delegation, NOT stated first-hand at this desk). Premise RE-ASKED at this artifact 2026-09-12 and CONFIRMED LIVE: deny lane calls is_fused_push(strip_heredoc_bodies(cmd)) at push-claim-reminder.py:177, while the reminder lane's check() calls is_push_command(cmd) on the raw command — no strip. Original body: dotfiles BACKLOG.md:2256-2293.
blocked-by: evidence test -d $HOME/.claude/plugins/cache/dispatch-guards-marketplace/dispatch-guards/0.11.27  # built and verified; waits only on the 0.11.27 release reaching the installed plugin (operator act). A release that skips 0.11.27 needs this path edited
blocker-exercise: 2026-10-07 live 1 | accept arm: the same test over the installed 0.11.26 directory exits 0 (run 2026-10-07); refuse arm: the predicate as written exits 1 today, 0.11.27 not being installed
amend-reason: 2026-10-07 the build landed; the entry now records its commit, which the earlier park left only in the commit history
amended-evidence: 2026-10-07 BUILT 2026-10-07 at 4c6adcab1e2e. MEASURED by the desk at the artifact: check() reads is_push_command(strip_heredoc_bodies(cmd)); bench 67 of 67, all hook bite-tests exit 0. RELAYED from lane sonnet-dg44-43-33 (report booked): red-first against the unmodified hook, the new bite asserted and corpus line 66 read expected silent, observed context. RECALLED from the earlier slot: relocated from dotfiles df-61, premise confirmed live 2026-09-12 at push-claim-reminder.py:177.

## dg-34
grade: READY
requirement: WORKFLOW-HARVEST SKILL: mine chat history for recurring task shapes and feed them into the runbook-to-certify-to-execute-cheap pipeline — record: dotfiles claude/BACKLOG.md:1051-1116 (frozen legacy carrier, blob 0e5fa2e2)
goal: general-maintenance
write-set: plugin/skills/ (new workflow-harvest skill), plugin/.claude-plugin/plugin.json
done-criterion: skill shipped in a dispatch-guards version bump + one harvested runbook landed in its owning repo + verifier (1) evidence recorded
evidence: RELOCATED from dotfiles df-127 under df-167 (operator decision 2026-09-12, relayed through judgment desk dotfiles-85 from drain desk dotfiles-49; relayed-under-standing-delegation, NOT first-hand at this desk). Premise RE-ASKED at this artifact 2026-09-12 and CONFIRMED LIVE: plugin/skills/ contains only 'dispatch' (plus its siblings) and no harvest skill exists — the skill is unbuilt. The item's stated trigger (the executor-skill landing) has SHIPPED, so it is unblocked. Original body: dotfiles claude/BACKLOG.md:1051-1116.
blocked-by: NONE
amend-reason: 2026-09-15 2026-09-15 form repair, judgment desk authorized: the slot's first entry was prose ('plugin/skills/ (new workflow-harvest skill)') so the wave join could not read it and the item sat outside every lane while grading READY. The boundary doctrine says a write-set names files that exist or ones the entry itself creates, so the skill's own subtree is the parseable form — trailing slash, the directory entry the join reads. Nothing invented: the path is derived from the skill name the requirement already states, and no layout beyond the subtree is asserted
amended-write-set: 2026-09-15 plugin/skills/workflow-harvest/,plugin/.claude-plugin/plugin.json

## dg-37
grade: PARKED
requirement: enumeration and matrix briefs: the bucket field carries the BARE TOKEN and nothing else; all qualification goes in the evidence field. forms.md §3b declares closed vocabularies but never field-exclusivity, and the gap let a lane decorate the enum — the one real FAIL-OPEN in a 25-row matrix was invisible to every tally, caught by a Counter, invisible to a read — record: dotfiles claude/records/df151-matrices-2026-09-12.md
goal: general-maintenance
write-set: plugin/skills/dispatch/references/forms.md,plugin/.claude-plugin/plugin.json,LEDGER.md
done-criterion: forms.md §3b carries the bare-token sentence; ships in a version bump per the release flow; the JOURNAL line rides the same session in dotfiles per the dispatch-guards convention
evidence: 2026-09-12, df-151 discovery wave: lane B wrote its reasoning INTO the enum field under a brief that declared the vocabulary but not exclusivity; the carrier doctrine's open-vocabulary decay reproduced in a data file. Matrices and reading caveat preserved at dotfiles claude/records/. Booked by the judgment desk after the drainage desk's cost-test veto correctly refused a dotfiles-side booking (wrong reader path) and correctly refused --source operator on a desk's ask (testimony, not the decision). Write-set collides with dg-35/dg-36 — the three bundle into one forms.md release
blocked-by: evidence test -d $HOME/.claude/plugins/cache/dispatch-guards-marketplace/dispatch-guards/0.11.27  # built and verified; waits only on the 0.11.27 release reaching the installed plugin (operator act). A release that skips 0.11.27 needs this path edited
blocker-exercise: 2026-10-07 live 1 | accept arm: the same test over the installed 0.11.26 directory exits 0 (run 2026-10-07); refuse arm: the predicate as written exits 1 today, 0.11.27 not being installed
amend-reason: 2026-10-07 the build landed; the entry now records its commit
amended-evidence: 2026-10-07 BUILT 2026-10-07 at 75450728f6be. MEASURED by the desk: section 3b Taxonomy carries the bare-token sentence; journal line at dotfiles db353a5. RECALLED from the earlier slot: df-151 discovery wave 2026-09-12, matrices at dotfiles claude/records/.

## dg-39
grade: NEW
requirement: the unbumped-plugins pre-commit guard is machine-local (dotfiles git/hooks pre-commit, unbumped_plugins() at :233) while the discipline it enforces — no plugin-payload commit without a version bump, because claude plugin update compares versions only and a stale install fails silently — is plugin-release discipline that every stack repo needs. A stack user who installs the plugins and authors their own gets no such guard. Candidate home: this plugin's guard set (it already owns release-adjacent guards), shipped as an adoptable git-hook the way lifecycle ships its git-hooks; fired twice for real on 2026-09-13 (the sc-8 lane's bounce and its documented multi-commit exemption)
goal: tend
write-set: UNKNOWN
done-criterion: UNKNOWN — set at design: whether the guard ships here or beside skill-craft's release machinery is the placement question, decided against both repos' guard rosters
evidence: operator second-look ask 2026-09-13 (statiker session 1b204567); the guard's two real fires same date (sc-8 lane bounce, exemption sequence per dispatch skill commit-plan bullet); dotfiles git/hooks/pre-commit read by the sc-8 lane at :233, :2013-2030
blocked-by: decision which repo homes the shipped guard, this plugin or skill-craft's release tooling, decided against both guard rosters

## dg-40
grade: READY
requirement: decide the one-writer default flip: lanes isolated-by-default in worktrees with a typed shared-copy escape (the noodle AllowPrimaryCheckout shape, inverted) vs the current warn-gradient on a shared copy; record: statiker dev-notes/grokbot-space-comparison-2026-09-13.md, steal item 3
goal: general-maintenance
write-set: plugin/skills/dispatch/SKILL.md, plugin/hooks/, dev-notes/
done-criterion: decision recorded with the reservation-gate fire tally since 2026-08-06 as its basis (absorption-class incidents caught vs missed vs silent); either the ladder default flips or the warn-gradient is re-affirmed with that tally cited
evidence: writer-reservation-gate.py docstring: per-copy WARN, granularity rationale, motivating absorption incident 2026-08-06; comparison doc steal item 3
blocked-by: evidence the next guard-set design pass opens (maintenance batches to a consuming seam) and the fire tally is computed there
amend-reason: 2026-09-13 operator sharpened the question mid-review: the noodle shape (isolation always, typed escape) is the heavy pole; our stack wants a per-lane discriminator between heavy and light, and the item now asks for that design rather than a binary flip
amended-requirement: 2026-09-13 design the lane-isolation DISCRIMINATOR, not a default flip (operator steer 2026-09-13: heavy machinery vs light needs a discriminator, never always-type-X): name the computable per-lane properties that route a lane to worktree isolation (heavy) vs shared copy under the warn-gradient (light). Candidate inputs the design weighs: write-set overlap with a live writer (the existing ladder trigger), shared-FILE overlap (already worktree-mandatory, no safe form exists), co-writer class on the copy (peer session, operator, scheduled job), lane duration. Record: statiker dev-notes/grokbot-space-comparison-2026-09-13.md steal item 3
amended-done-criterion: 2026-09-13 discriminator recorded with the reservation-gate fire tally since 2026-08-06 as evidence (absorption-class incidents caught vs missed vs silent); the ladder text re-keyed to the discriminator; each routing outcome carries a named basis, no unconditional default in either direction
amend-reason: 2026-09-15 2026-09-15 blocker examined at the judgment desk's request; the repair it authorized was NOT executed, see the ledger line of this date
amended-evidence: 2026-09-15 writer-reservation-gate.py docstring: per-copy WARN, granularity rationale, motivating absorption incident 2026-08-06; comparison doc steal item 3. MEASURED 2026-09-15 (dispatch-guards-c2, while checking this entry's blocker at the judgment desk's request): the fire log HAS the raw tally — 751 writer-reservation-gate rows, ALL mode=warn, 2026-08-10 to 2026-09-15, none before 08-10 (command: read ~/.local/share/claude/dispatch-guards-fires.jsonl, count by the 'guard' field — note the field is 'guard', NOT 'source'; a filter on 'source' returns a false ZERO, which is how this was nearly mis-measured). CONSEQUENCE FOR THIS ENTRY'S BLOCKER: the raw half of the named missing evidence is computable NOW and is not waiting on any design pass. What is NOT derivable from a fire log is the half the done-criterion actually asks for — absorptions MISSED and SILENT — because a fire log records fires and never non-fires, so that half needs a different instrument, not a later seam. The blocker's broken predicate therefore hides a live measurement plus a genuine instrument gap

## dg-42
grade: READY
requirement: dispatch-time scratch-disjointness gate: refuse two live lanes of one session whose assigned scratch paths are not distinct — the lane-grain hole in the session-grain Scratch wording, measured 2026-09-15 when lane A's rm -rf + clone at a generic scratchpad path destroyed lane B's private clone (reflog empty) and lane B's probe residue crossed back. Entry with pre-formulated skeleton text: dev-notes/dispatch-OBSERVATIONS.md 2026-09-15 scratch entry
goal: general-maintenance
write-set: hooks/,plugin/skills/dispatch/SKILL.md
done-criterion: red-first: a replayed two-lane dispatch with identical assigned scratch paths is refused naming both lanes; distinct-slug pair passes; predicate needs the Scratch assignment machine-readable, so the skeleton line change lands in the same item; bite registered per this repo's guard conventions
evidence: wave-A measurement relayed by dotfiles-a8 2026-09-15, mechanism verified at dotfiles-89 (mtime attribution, reflog empty); dispatch skill section 1 slug rule exists but skeleton does not force it
blocked-by: NONE
amend-reason: 2026-10-07 the slot named hooks/, a path under no tracked directory; the guards live under plugin/hooks/
amended-write-set: 2026-10-07 plugin/hooks/,plugin/skills/dispatch/SKILL.md

## dg-47
grade: PARKED
requirement: the dispatch SKILL.md is ~17k tokens (68500 bytes measured 2026-09-15) and is re-billed into the prefix of every session that loads it; a skill-craft Pareto pass to cut it. Operational corpus, so governed by CLAUDE-maintenance: a structural restructure lands first, then takes a fresh-context vet before push. Record: docs/directives/2026-09-15-guard-rewrite-arc.md item 3
goal: general-maintenance
write-set: plugin/skills/dispatch/SKILL.md
done-criterion: SKILL.md materially smaller with no rule lost — established by a section-level audit of what left, not by byte count alone; fresh-context vet passed before push
evidence: 68500 bytes measured 2026-09-15 (directive item 3); the re-billed-prefix cost is the operator corpus's session-depth rule
blocked-by: decision a corpus-maintenance session with its own operator GO

## dg-48
grade: PARKED
requirement: deny() does not consult guard_modes, so brief-reminder's other three deny lanes (deny_text, tail_mode_mismatch, missing_sections) and push-claim-reminder's cannot be demoted by a site AT ALL. The hook's own main() comment states this and the Wave 0 probe confirmed it live (modes set to off did not stop the lane). This arc makes only missing_tail mode-aware, by ruling; whether deny() should consult the modes globally is open. Record: Wave 0 probe record finding 2 plus judgment-desk ruling 1 scope line, 2026-09-15
goal: general-maintenance
write-set: plugin/hooks/_dispatch_common.py,plugin/hooks/brief-reminder.py
done-criterion: each of the three lanes either gains a mode-aware exit or carries a stated reason in its docstring for staying hard
evidence: plugin/hooks/brief-reminder.py main() comment: the four deny() lanes are unaffected since deny() does not consult the modes at all; Wave 0 probe record finding 2 (live confirmation)
blocked-by: decision should deny() consult guard_modes globally, given a fire-rate case for demoting any of the other three lanes

## dg-52
grade: READY
requirement: dev-notes/dispatch-OBSERVATIONS.md owes a maintenance pass: the session-start banner reported roughly 32 booked against roughly 0 drained over the last +30 percent stretch (33 commits), and this arc added a 4th incident to the channel-line entry on top of that. The carrier drains by applying each entry pre-formulated rule text or discarding it with a one-line reason, both recorded exits. Judgment-desk ruling at arc start 2026-09-15: flagged rather than ridden past, and booked as its own item at arc close rather than interleaved into a BUILD run
goal: general-maintenance
write-set: dev-notes/dispatch-OBSERVATIONS.md,plugin/skills/dispatch/SKILL.md,plugin/skills/dispatch/references/forms.md
done-criterion: every entry in the carrier is either APPLIED (its pre-formulated rule text lands in the named consumer, with the commit ref recorded) or DISCARDED with a one-line reason; the channel-line entry drains as ONE rewrite covering incidents 2, 3 and 4 together, since applying any single text alone leaves the other routes open, per that entry own drain note
evidence: session-start banner 2026-09-15: maintenance pass owed, booked ~32 vs drained ~0 over 33 commits; the channel-line entry own slot 4 states the three texts drain together; this arc added the 4th incident at e75221c
blocked-by: NONE

## dg-53
grade: PARKED
requirement: Fire the goal question at the DISPATCH seam and log each firing, so lifecycle's drift-treatment arm counts dispatch-seam crossings from the record. Pointer: lifecycle docs/directives/2026-09-24-refocus-design-round.md §7 judge ruling 2 ('lc-277 stays OPEN on its dispatch seam') and lifecycle lc-277. The 2026-09-24 round reported this booked here; a slot search (goal-seam / goal seam / lc-277) found no entry — this books the named absence. Booked by the judgment desk tmp-ad placing lc-277's obligation per 2026-10-04 design round 2 D5.
goal: general-maintenance
write-set: plugin/hooks/brief-reminder.py
done-criterion: A dispatch from a governed repo prints the goal question at brief time and appends a fire-log line that lifecycle tools/fire-window-tally.py counts as a goal seam (seam=dispatch); red-first: a dispatch without the print is shown refused-or-reminded before the change, counted after.
evidence: RELAYED (lifecycle-4f, 2026-10-04 design round 2 D5): lifecycle's drift-treatment arm window closes 2026-10-18 (DERIVED there from the directive's 4 weeks) and D5 rules no mid-window arm change — build after the arm reports, or on the judgment desk's explicit lift
blocked-by: NONE
blocker-exercise: none-yet 2026-10-04
amend-reason: 2026-10-04 typed blocker supplied for the PARKED grade; the add's NONE was a shape break
amended-blocked-by: 2026-10-04 evidence [ "$(date +%F)" \> "2026-10-18" ]  # the drift-treatment arm window has closed; an earlier lift is the lifecycle judgment desk editing this blocker (D5, lifecycle docs/directives/2026-10-04-refocus-design-round-2.md: no arm change mid-window)
