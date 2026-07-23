# dispatch-guards

Mechanical guards for disciplined subagent dispatching in Claude Code.
Prose rules are best-effort; hooks are not — this plugin is the hook side
of a dispatch discipline.

## Guards

| Guard | Event | What it enforces |
|---|---|---|
| `agent-model-gate` | PreToolUse Agent\|Task\|Workflow | explicit `model` on generic agent types; strict `<model>: ` title prefix (verified mirror of the field); `<model>-` name prefix; per-policy deny/ask tiers; Workflow launches always ask |
| `brief-reminder` | PreToolUse Agent\|Task | one reminder line before every dispatch: brief decision-complete? report channel named? |
| `subagent-push-gate` | PreToolUse Bash | denies `git`/`gh` push in a subagent context — subagents commit unpushed, the dispatcher pushes after verification |
| `report-reminder` | PostToolUse Agent\|Task | one line next to every dispatch result: check the closing report, verify claims in the artifact |
| `report-enforcer` | SubagentStop | instructs a stopping subagent to actually SEND its closing report (background agents' final text reaches no one) |
| `dispatch-log` | PostToolUse Agent\|Task | appends one mechanical JSONL line per dispatch (`~/.local/share/claude/dispatch-log.jsonl`, `$CLAUDE_DISPATCH_LOG` override) |

All guards fail open on hook-input parse errors and ship a `--test`
bite-test (`python3 hooks/<guard>.py --test`).

## Mechanism vs. policy

The plugin ships generic defaults (no tiers denied, none forced to ask,
generic reminder wording). Site policy lives in
`~/.claude/dispatch-guards.json` (override path via
`$CLAUDE_DISPATCH_GUARDS_CONFIG`):

```json
{
  "models": ["sonnet", "opus", "haiku", "fable"],
  "deny_models": ["haiku"],
  "ask_models": ["fable"],
  "discipline_doc": "dispatch-discipline.md"
}
```

- `models` — allowed lineup; drives the title/name prefix check.
- `deny_models` — dispatches to these tiers are refused with feedback.
- `ask_models` — every generic-type dispatch to these tiers forces the
  permission dialog (one operator yes/no per dispatch, before it starts).
- `discipline_doc` — when set, reminder texts cite it (`… §1`, `… §2`);
  unset, wording stays generic.

## Install

```bash
claude plugin marketplace add <path-or-git-url of this repo>
claude plugin install dispatch-guards@dispatch-guards-marketplace
```

## Design notes

- One file per lifecycle event, shared logic in `_dispatch_common.py`.
- Fail-open by design: a broken guard must not brick every call — the
  bite-tests are the load-bearing compensation; register them in your
  machine-bootstrap doctor.
- Environment binding (as of 2026-07): a subagent context is marked by a
  non-empty `agent_id` in the hook input; if a harness change removes the
  field, the push gate silently treats everything as the main session.
