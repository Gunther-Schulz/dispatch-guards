# /eval-skill executor — 2026-08-05

Skill path: plugin/skills/executor/SKILL.md (source repo; evaluated
pre-install at the 0.3.4 landing)
Installed version: n/a at eval time (0.3.3 installed; executor ships
with 0.3.4)
Tier applicability: (a) description-triggered — "Use when executing a
dispatch brief or a repo devbook/runbook procedure…". Tier 1 run per
the backlog entry's named verifier; Tier 2 deliberately skipped
(minimum-tier rule, evaluation.md — the entry names Tier 1, and the
skill's conduct signature will be observed in operation via the §6
first-run-watched convention).

## Tier 1

3 × sonnet skill-router trials, parallel, same input. Competitors:
dispatch, worktree, clippy, daneel. Trial A was cut by an API error
AFTER delivering its complete 10-row table; rows agree with B and C
on all queries.

| # | query (gist) | fires | verdict |
|---|---|---|---|
| S1 | brief from main session, work through + report | 3/3 | clean |
| S2 | run the PR-round runbook procedure | 3/3 | clean |
| S3 | subagent, settled design, steps 1–6 exactly | 3/3 | clean |
| S4 | writing a runbook for opus sessions — sections? | 3/3 | clean |
| S5 | does DEPLOY-RUNBOOK.md conform to the form? | 3/3 | clean |
| S6 | execute filled roadmap, decide nothing extra | 3/3 | clean |
| N1 | dispatch to sonnet or inline? | 0/3 (none) | clean |
| N2 | write a brief for a sonnet agent | 0/3 (dispatch) | clean |
| N3 | CI "build executor" failing on arm64 | 0/3 (daneel) | clean |
| N4 | review this code for bugs | 0/3 (none) | clean |

No misses, no spurious fires; the "executor"-keyword bait (N3) was
rejected by all trials. No description repair needed.

## Tier 2

Skipped (see applicability above).

## Next action

Accept-as-clean; ship in 0.3.4. Conduct-signature evidence accrues in
operation (first-run-watched bookings).
