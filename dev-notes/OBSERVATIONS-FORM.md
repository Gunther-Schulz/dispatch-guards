# OBSERVATIONS form — the instrument-lesson carrier (template)

Role: process-/tool-related weaknesses noticed while a session is
OPERATING land in the repo of the OWNING instrument — dispatch
lessons here (`dispatch-OBSERVATIONS.md`), abw lessons in
pbs-abwaegung, office-process ones in the pbs-office backlog, work
ethics (true in every project) in the operator corpus. Never a
global pool: the one collection list that every session lengthens
and nobody drains is the measured failure this form replaces
(observed in vendor/claude-code-cache-fix: auto-booking with no
consumer, no grading, no dedup, no drain trigger — content-correct
entries, functionally a dump).

## Entry form (four mandatory slots)

1. **Incident + basis** — what happened, with a citation
   (session/journal/commit); frequency, when > 1. The counter is
   PROVENANCE for the fire-rate review, never an admission
   threshold: n=1 suffices to act on (operator decision 2026-08-15;
   mirrors CLAUDE-maintenance's "ONE observation suffices" — the
   fire-rate review is retirement machinery, not an entry gate). A
   deferral stays legitimate only when it sits on NAMED missing
   evidence; "let's collect first, until n is enough" is drift in
   prudence's costume.
2. **Class** — the defect class, not the symptom. SAME CLASS = MERGE
   into the existing entry (bump the counter, add the citation),
   never a sibling entry.
3. **Pre-formulated rule/fix text** — the wording the maintenance
   pass would apply. This slot turns the pass into mechanical
   applying+checking instead of re-derivation; an entry without it
   is half a booking.
4. **Consumer + drain seam** — which pass/round applies the entry
   (e.g. "next dispatch-guards maintenance round", "next build
   touching guard X").

## Drain (quota, never calendar)

The carrier owes a maintenance pass when bookings since the last
pass clearly outrun applying+dropping (rough tripwire 3:1 — the same
quota as the backlog retirement trigger in the operator corpus). The
pass applies the pre-formulated text OR drops it with a one-line
reason — both are an exit, the list shrinks. Applied/dropped entries
move into a `## Abgeflossen` section with evidence (commit/reason) —
one fact, one home.

## Capture seam

The session's close carries a presence line ("Harvest: <bookings
with a home>" or "Harvest: none") — the missing line is visible, the
judgment itself stays judgment. Site instance: pbs-office RUNBOOK
R13 step 3; corpus role: operator CLAUDE.md, accretion module.
