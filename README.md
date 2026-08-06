# dispatch-guards

The dispatch discipline as a skill, plus the mechanical guards that
enforce its computable slice. Prose rules are best-effort; hooks are
not — this plugin carries both sides.

## Skills

- **`dispatch`** — the dispatch discipline itself: decision-complete
  briefs (§1), the closing-report form and brief tails
  (`references/forms.md`, §§2–3), dispatcher duties (§4),
  tier-readiness register (§6), Codex routing
  (`references/codex-routing.md`, §7). The `dispatch-skill-gate`
  hook demands this skill be loaded before any dispatch.
- **`worktree`** — portable git-worktree and git-hook mechanics for
  isolating agents and wiring hooks safely.

## Guards

| Guard | Event | What it enforces |
|---|---|---|
| `dispatch-skill-gate` | PreToolUse Agent\|Task\|Workflow | the `dispatch` skill must be loaded in the dispatching context's transcript (session-scoped) before any dispatch — replaces the old read-by-convention |
| `agent-model-gate` | PreToolUse Agent\|Task\|Workflow | explicit `model` on generic agent types; strict `<model>: ` title prefix (verified mirror of the field); `<model>-` name prefix; per-policy deny/ask tiers; Workflow launches always ask; **escalation lane** — an ask-tier dispatch *from a subagent* is denied, not asked: escalation is the dispatcher's decision, the subagent returns the question |
| `brief-reminder` | PreToolUse Agent\|Task | one reminder line before every dispatch: brief decision-complete? report channel named? |
| `subagent-push-gate` | PreToolUse Bash | denies `git`/`gh` push in a subagent context — subagents commit unpushed, the dispatcher pushes after verification |
| `amend-gate` | PreToolUse Bash | `git commit --amend` on a shared working copy: denies it flatly in a subagent context (amend is COMMIT-granular — it can swallow a co-writer's landed commit at HEAD; make a new commit instead), reminds in the main session (check `git log -1 --format=%(trailers)` shows your own trailer before amending) |
| `report-reminder` | PostToolUse Agent\|Task | one line next to every dispatch result: check the closing report, verify claims in the artifact |
| `report-enforcer` | SubagentStop | instructs a stopping subagent to actually SEND its closing report (background agents' final text reaches no one) |
| `message-payload-gate` | PreToolUse SendMessage | denies oversized string messages from a subagent to its dispatcher — payload belongs in a file, the message carries the pointer: an injected payload occupies the dispatcher's context for the rest of the session (and has coincided with full prompt-cache rewrites); dispatcher→subagent stays free |
| `dispatch-log` | PostToolUse Agent\|Task | appends one mechanical JSONL line per dispatch (`~/.local/share/claude/dispatch-log.jsonl`, `$CLAUDE_DISPATCH_LOG` override) |
| `discovery-volume-reminder` | PostToolUse Bash\|Grep\|Glob | advisory line when a search result ≥ `discovery_volume_bytes` lands in main-session context — the discovery-dispatch routing rule may apply; measures the harness's `persistedOutputSize`, since the hook-visible body is truncated |
| `report-form-gate` | PreToolUse SendMessage | **staged, default-warn** — a report-shaped subagent message (≥4 distinct `(a)`–`(h)` slot markers) missing required §2 slots a–g fires naming them; read-only (verifier/discovery) returns carry no markers and pass untouched |
| `writer-claims-gate` | PreToolUse+PostToolUse Write\|Edit | **staged, default-warn** — PostToolUse records subagent write claims (TTL `write_claim_ttl_hours`); PreToolUse fires on a cross-agent same-file write, and reminds (never denies) the main session when a live subagent claimed the file (§4 mirror duty). Claims store: `~/.local/share/claude/write-claims.jsonl` (`$CLAUDE_DISPATCH_GUARDS_CLAIMS` override) |

All guards fail open on hook-input parse errors and ship a `--test`
bite-test (`python3 hooks/<guard>.py --test`).

## Fire log, guard modes, and the replay bench

Every guard fire — deny, ask, warn, block — appends one JSONL line
to `~/.local/share/claude/dispatch-guards-fires.jsonl`
(`$CLAUDE_DISPATCH_GUARDS_FIRELOG` override): ts, guard, mode,
session/agent, truncated reason. Consumers: the fire-rate review
(fire rates become countable instead of remembered) and warn→deny
promotion decisions.

Per-guard modes via the `guard_modes` config key
(`{"<guard>": "deny"|"warn"|"off"}`): a lane in `warn` emits a
visible "would DENY" additionalContext line and logs, but does not
block — new speculative lanes ship default-warn and earn `deny`
through the fire-rate review against the log.

`tools/replay-bench.py` replays a curated corpus
(`tools/corpus/guards.jsonl`) of hook-input payloads through the
real guard scripts end-to-end (stdin → stdout JSON) and fails on
any missed catch or false fire — including the historical
false-fire regressions. It is both the deny-arm regression net and
the catch-rate/false-fire measurement; stateful guards
(writer-claims) carry their e2e inside their own `--test` instead.

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
  "discipline_doc": "dispatch skill",
  "max_message_chars": 3000,
  "discovery_volume_bytes": 50000,
  "guard_modes": {"writer-claims-gate": "warn"},
  "write_claim_ttl_hours": 6
}
```

- `models` — allowed lineup; drives the title/name prefix check.
- `deny_models` — dispatches to these tiers are refused with feedback.
- `ask_models` — every generic-type dispatch to these tiers forces the
  permission dialog (one operator yes/no per dispatch, before it starts).
  From a *subagent* the same tiers are denied outright (escalation lane):
  the dialog asks whether a dispatch is worth it, never whether the
  escalating agent should be the one deciding. Note the lane ignores the
  generic-type restriction — a pinned agent type is the same spend from
  the same context.
- `discipline_doc` — when set, reminder texts cite it (`… §1`, `… §2`);
  unset, wording stays generic.
- `max_message_chars` — payload-gate threshold for subagent→dispatcher
  messages (default 3000).
- `discovery_volume_bytes` — discovery-volume-reminder threshold for
  main-session search results (default 50000).
- `guard_modes` — per-guard deny-lane mode (`deny`/`warn`/`off`);
  unset guards keep their shipped default (`deny` for the
  established gates, `warn` for the staged report-form and
  writer-claims lanes).
- `write_claim_ttl_hours` — writer-claims freshness window
  (default 6).

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
