# This repo had NO legacy closure home. The absence was STATED at
# migration time (`--from-done NONE`), never inferred from a missing
# file: the archive below is empty because there was nothing to
# archive, which is a different fact from nothing having been read.

schema: 2

## dg-31
grade: DONE
requirement: PARKED 2026-09-12 — _dispatch_common.py flagged by the pre-commit x-bit/shebang guard: mode 100755, no shebang, and the guard claims hooks.json execs it directly — record: BACKLOG.md:1042
goal: UNKNOWN
write-set: UNKNOWN
done-criterion: UNKNOWN
evidence: BACKLOG.md:1042-1061
blocked-by: NONE
blocker-moot: regrade: fill goal, write-set, done-criterion and evidence, or drop
closed-reason: 2026-09-12 Resolved by a THIRD answer neither branch named: the guard was RIGHT by its own design. Direction B (exec bit, no shebang) deliberately sweeps every 0755 file under a payload root, per the docstring a drain-wave lane updated the same day, motivated by the measured 2026-08-17 incident where a lane copied THIS file's 0755-no-shebang pattern to a new library and hung a session on `./file --test`. So neither of the entry's branches held: hooks.json does not exec it (executed grep over the installed hooks.json: 16 entries, this file absent) AND the guard does not over-include. The mode was the defect; the file now carries 100644 and the guard goes green. Basis: LEDGER.md:180, judgment desk, 2026-09-12.
closed-ref: 69cead0

## Archive (pre-migration)


<!-- CLOSURES READ FROM THE `--from` CARRIER ITSELF (lc-18/lc-19). The
     design modelled closures as a separate `--from-done` FILE; a real
     carrier states them in its own `## Done` section or with a closure
     grade word. These bodies are VERBATIM from the source, at the line
     ranges named beside each one, and they are archived rather than
     written as items: a closure that migrates back as open work is the
     one migration defect that is silent. -->

<!-- BACKLOG.md:1064-1092 — §4 row 1 + lc-18: ungraded, under the carrier's own closure heading — the heading is the closure statement, and the body is archived verbatim -->
- 2026-08-20 — **the machine doctor leaked guard-bite fires into the
  real fire log; found here, fixed in dotfiles, verified here.** Booked
  as cross-repo RESIDUE the same day and discharged the same day.
  The incident: two new bites in this repo appended 33 records to
  `~/.local/share/claude/dispatch-guards-fires.jsonl`, 24 of them on a
  lane that had never run against real work — corrupting the exact
  instrument the warn→deny promotion reads. This repo's half (per-bite
  `CLAUDE_DISPATCH_GUARDS_FIRELOG` pin plus an `XDG_DATA_HOME` pin on
  the CLAUDE.md sweep loop) protects this repo's verify block only.
  The machine-wide half was `bootstrap/doctor.py`'s `_hook_test_env`,
  which redirected `XDG_STATE_HOME` and nothing else while the fire log
  resolves from `XDG_DATA_HOME` — so every doctor sweep across every
  repo with a firing bite leaked. Ours was the repo that noticed; the
  exposure was machine-wide.
  Fixed by the dotfiles desk (`818329c`: `XDG_DATA_HOME` and
  `XDG_CACHE_HOME` pinned into the same throwaway root beside
  `XDG_STATE_HOME`).
  **Verified HERE by executing their function, not by booking their
  report** — the peer's "done" is a claim like any other: called
  `_hook_test_env(<temp root>)` and confirmed all three XDG roots
  resolve inside the throwaway, then resolved the fire-log path under
  that env and confirmed it is not the real log. Their own evidence
  (full doctor run, record count 2380 before and after, delta 0) is
  consistent with it and is theirs, not re-run here.
  Standing check retained for the next release, since a fix verified
  once is not a fix verified forever: fire-log record count before and
  after a full doctor run; a non-zero delta with null session ids is
  the leak returning.


<!-- BACKLOG.md:1093-1104 — §4 row 1 + lc-18: ungraded, under the carrier's own closure heading — the heading is the closure statement, and the body is archived verbatim -->
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


<!-- BACKLOG.md:1105-1122 — §4 row 1 + lc-18: ungraded, under the carrier's own closure heading — the heading is the closure statement, and the body is archived verbatim -->
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


<!-- BACKLOG.md:1123-1180 — §4 row 1 + lc-18: ungraded, under the carrier's own closure heading — the heading is the closure statement, and the body is archived verbatim -->
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



<!-- BACKLOG.md:1181-1196 — §4 row 1 + lc-18: ungraded, under the carrier's own closure heading — the heading is the closure statement, and the body is archived verbatim -->
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


<!-- BACKLOG.md:1197-1204 — §4 row 1 + lc-18: ungraded, under the carrier's own closure heading — the heading is the closure statement, and the body is archived verbatim -->
- 2026-08-11 — **commit-plan origin-basis + who-bumps, and the
  state-token convention**: realized cfdbc6e (dispatch §1 bullet +
  skeleton slot + brief-reminder warn text; forms.md §2 paragraph;
  executor §1.7 — both sides audited per the corpus rule). Booked
  and realized same day (504b2fc the booking); incident lineage in
  the entry bodies at that ref.



<!-- BACKLOG.md:1205-1217 — §3.1: `DONE` is the closed vocabulary's own word — a closure MOVES to the done home; it never enters the open carrier, and it never inherits a grade the source did not carry -->
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


