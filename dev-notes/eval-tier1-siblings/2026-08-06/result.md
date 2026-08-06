# /eval-skill — Tier 1, all three sibling skills — 2026-08-06

Skills: `dispatch`, `executor`, `worktree` (plugin/skills/*/SKILL.md)
Installed version at eval time: 0.4.2 (pin verified, sha 267f7ae3)
Descriptions last touched: all three 2026-08-05 — unchanged by the
0.4.1/0.4.2 review, which edited bodies only. The 2026-08-05 executor
eval therefore remains valid; this run supersedes nothing.

Tier applicability: (a) description-triggered for all three. Tier 2
deliberately skipped (minimum-tier rule, evaluation.md): the
behaviour signatures are observed in operation — dispatch through the
dispatch-log and the guard fire log, executor through §6
first-run-watched bookings.

**Why one joint run rather than three.** The three descriptions share
vocabulary by design (agents, briefs, worktrees). The realistic
failure is therefore not a flat miss but CROSS-FIRING between
siblings, which a per-skill run cannot see — only a shared candidate
list where all three compete makes it observable.

Competitors on the list: clippy, statiker, diagnosing-bugs,
skill-craft, update-config.

## Round 1 — 18 queries × 3 sonnet trials

All three trials returned **identical** tables. 18/18 as intended:
D1–D5 → dispatch, W1–W5 → worktree, E1–E3 → executor, and every
near-miss correct (N1 model-choice → NONE, N2 → diagnosing-bugs,
N3 → skill-craft, N4 settings.json hook → update-config, N5 ordinary
rebase → NONE).

All three flagged D3 ("four agents at once on the same repo") as a
near-tie against worktree, and all three resolved it to dispatch.

**Round 1's own defect, found before booking:** several should-trigger
queries echoed the descriptions' vocabulary ("closing report",
"wrong-author", "parallel agents"). A query built from the words being
tested measures whether a description matches itself. The
should-trigger half of round 1 is therefore partly self-confirming and
is NOT the basis of the verdict below; the near-miss half stands, since
those were not echoes.

## Round 2 — 19 paraphrased queries × 3 sonnet trials

Same skills, deliberately non-echoing phrasing ("I'm giving this
database change to a junior model", "imports inside the scratch copy
are resolving back to my main folder", "throwaway copy of the repo so
a helper can't touch what I'm editing"), plus two extra near-misses.

| query | fires | verdict |
|---|---|---|
| Q1–Q3, Q5 (dispatch) | 3/3 dispatch | clean |
| **Q4** (what goes in the returned write-up) | **2/3 dispatch, 1/3 executor** | **borderline — see below** |
| Q6–Q10 (worktree) | 3/3 worktree | clean |
| Q11–Q13 (executor) | 3/3 executor | clean |
| Q14 model choice | 3/3 NONE | clean — the disclaimer holds |
| Q15 flaky CI test | 3/3 diagnosing-bugs | clean |
| Q16 description not triggering | 3/3 skill-craft | clean |
| Q17 settings.json Stop hook | 3/3 update-config | clean — harness-hook bait rejected |
| Q18 split a PR into two commits | 3/3 NONE | clean |
| Q19 ordinary rebase | 3/3 NONE | clean |

Near-ties named by the trials: Q3 (dispatch vs worktree, all three,
resolved to dispatch) and Q2 (dispatch vs executor, one trial).

## Verdict: no description repair

Per evaluation.md, a should-trigger miss across 3/3 is a real defect;
1–2/3 is borderline noise. Q4 is the only divergence in 37 query-trials
of round 2 and it is 1/3.

Q4 is also **harmless where it lands**, which is the substantive point.
The question "what belongs in the returned write-up" genuinely sits on
the dispatcher/executor seam: dispatch's description owns "demanding or
booking a subagent's closing report", executor's owns "reporting on
executed work". Either selection reaches the SAME artifact — the §2
form — because executor §1.7 points at `../dispatch/references/
forms.md`. A tie whose branches converge on one source is not a
triggering defect; it is the single-home property working.

Repairing it would mean narrowing one description to push the report
question away, which would trade a harmless ambiguity for a real miss
on the other side.

## Limits of this measurement

- **Simulation, not the live router.** `skill-router` subagents model
  the selection step; the protocol prescribes this instrument, but a
  clean result here is not a live-router guarantee.
- **Unanimity is weaker evidence than it looks.** Three trials of one
  model on one prompt are not independent; 3/3 agreement is the
  expected outcome whenever the answer is easy, and does not establish
  robustness under a different model or a re-worded candidate list.
- **Round 1's should-trigger half is self-confirming** (above) and
  carries no weight in the verdict.
- **Query authorship.** Both sets were written by the session that had
  just read all three descriptions. Round 2 mitigates by paraphrasing,
  not by removing the author's knowledge of what each skill covers.

## Next action

Accept as clean; no description edit. Re-measure when any of the three
descriptions changes, or when a fourth sibling joins the plugin — the
cross-firing risk scales with the number of adjacent descriptions, and
that is the failure this joint form exists to catch.
