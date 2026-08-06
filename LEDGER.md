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

- **2026-08-06 — OPEN QUESTION: `EXECUTION_TAIL_BG` (brief-reminder.py
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
