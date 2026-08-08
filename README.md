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
- **`executor`** — the receiving side: conduct of execution for a
  session running a brief or a repo devbook (§1 — grounding
  literalism, "done" is the check's own output, gaps surface never
  bridge, escalation returns the question), the under-report
  principle (§2), and the devbook form (§3) with its mechanical
  checker (`plugin/skills/executor/scripts/check_devbook_form.py`).
- **`worktree`** — portable git-worktree and git-hook mechanics for
  isolating agents and wiring hooks safely.

All three are model-invoked — they trigger from their descriptions;
`dispatch` is additionally hook-demanded before any dispatch call.

## Guards

| Guard | Event | What it enforces |
|---|---|---|
| `dispatch-skill-gate` | PreToolUse Agent\|Task\|Workflow | the `dispatch` skill must be loaded in the dispatching context's transcript (session-scoped) before any dispatch — replaces the old read-by-convention |
| `agent-model-gate` | PreToolUse Agent\|Task\|Workflow | explicit `model` on generic agent types; mandatory `<model>-` NAME prefix on every generic dispatch (the panel renders the name; a legacy `<model>: ` title prefix, if present, must mirror the field); per-policy deny/ask tiers; Workflow launches always ask; **escalation lane** — an ask-tier dispatch *from a subagent* is denied, not asked: escalation is the dispatcher's decision, the subagent returns the question |
| `brief-reminder` | PreToolUse Agent\|Task | **denies on the computable slice of §§1-2**, reminds on the judgment half. Four deny lanes, all `Agent`-only: a BACKGROUND dispatch whose prompt names no report channel (a background agent's final text reaches no one); a brief lacking the §2 tail block — searched in the prompt *and* in any brief FILE the prompt names; a pasted tail whose channel line contradicts `run_in_background`, either direction; an execution-tail brief missing its §1 grounding-basis or write-boundaries section. Otherwise one reminder line before every dispatch (brief decision-complete? report channel named?), plus a non-blocking base advisory on `isolation: "worktree"` calls |
| `subagent-push-gate` | PreToolUse Bash | denies `git`/`gh` push in a subagent context — subagents commit unpushed, the dispatcher pushes after verification |
| `push-claim-reminder` | PreToolUse Bash | main-session push lanes: **denies a fused push** — one sharing its invocation with `git commit` or `git log`, since the read-then-decide seam only exists across separate invocations — and otherwise reminds to claim each outgoing commit (`git log origin/<branch>..<branch>`); subagent context excluded, `subagent-push-gate` already denies it |
| `amend-gate` | PreToolUse Bash | `git commit --amend` on a shared working copy: denies it flatly in a subagent context (amend is COMMIT-granular — it can swallow a co-writer's landed commit at HEAD; make a new commit instead), reminds in the main session (check `git log -1 --format=%(trailers)` shows your own trailer before amending) |
| `worktree-config-gate` | PreToolUse Bash | **staged, default-warn** — a shared-config write (`git remote add\|remove\|rename\|set-url\|set-head\|set-branches`, or a non-`--worktree` `git config` write) issued from inside a linked worktree, where it rewrites `.git/config` for every checkout including the main clone. `git remote` has no `--worktree` form at all, which is what makes it the trap. Worktree detection is git's own (`rev-parse --git-dir` vs `--git-common-dir`), run only after the token shape matches; the correct recipe (`git config --worktree …`) and writes aimed elsewhere (`--global`, `--system`, `--file`) never fire |
| `report-reminder` | PostToolUse Agent\|Task | one line next to every dispatch result: check the closing report, verify claims in the artifact |
| `report-enforcer` | SubagentStop | instructs a stopping subagent to actually SEND its closing report (background agents' final text reaches no one) |
| `message-payload-gate` | PreToolUse SendMessage | denies oversized string messages from a subagent to its dispatcher — payload belongs in a file, the message carries the pointer: an injected payload occupies the dispatcher's context for the rest of the session (it has also coincided with full prompt-cache rewrites — correlation recorded but unproven, `dev-notes/payload-cache-correlation.md`; the lane rests on context economy alone); dispatcher→subagent stays free |
| `dispatch-log` | PostToolUse Agent\|Task | appends one mechanical JSONL line per dispatch (`~/.local/share/claude/dispatch-log.jsonl`, `$CLAUDE_DISPATCH_LOG` override) |
| `discovery-volume-reminder` | PostToolUse Bash\|Grep\|Glob | advisory line when a search result ≥ `discovery_volume_bytes` lands in main-session context — the discovery-dispatch routing rule may apply; measures the harness's `persistedOutputSize`, since the hook-visible body is truncated |
| `report-form-gate` | PreToolUse SendMessage | **staged, default-warn** — a report-shaped subagent message (≥4 distinct `(a)`–`(h)` slot markers) missing required §2 slots a–g fires naming them; read-only (verifier/discovery) returns carry no markers and pass untouched |
| `writer-claims-gate` | PreToolUse+PostToolUse Write\|Edit | **staged, default-warn** — PostToolUse records subagent write claims (TTL `write_claim_ttl_hours`); PreToolUse fires on a cross-agent same-file write, and reminds (never denies) the main session when a live subagent claimed the file (§4 mirror duty). Claims store: `~/.local/share/claude/write-claims.jsonl` (`$CLAUDE_DISPATCH_GUARDS_CLAIMS` override) |

All guards fail open on hook-input parse errors and ship a `--test`
bite-test (`python3 hooks/<guard>.py --test`). Fail-open means a
broken guard goes quiet rather than bricking every call, so the
bite-tests are the compensation that matters — run them somewhere
that fails loudly (CI, a pre-push hook, or whatever health check you
already run on this machine).

## Fire log, guard modes, and the replay bench

Every guard fire — deny, ask, warn, block — appends one JSONL line
to `~/.local/share/claude/dispatch-guards-fires.jsonl`
(`$CLAUDE_DISPATCH_GUARDS_FIRELOG` override): ts, guard, mode,
session/agent, shape, truncated reason. Consumers: the fire-rate
review (fire rates become countable instead of remembered) and
warn→deny promotion decisions.

`shape` is what makes a fire *separable*: `reason` is constant per
lane, so counting fires never distinguished a false one from a true
one. It is a secret-free digest — verbs and flags only, operands
dropped, long flags stripped of any `=value` and short flags reduced
to their letter (a short flag can carry its value attached). So
`git remote set-url --push origin https://tok@host/r.git` logs as
`git remote set-url --push`, and `mysql -phunter2 -u root` as
`mysql -p -u`. Dispatch tools log their routing fields instead;
Write/Edit and SendMessage log no shape.

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

- `models` — allowed lineup; drives the name-prefix check and the legacy title-prefix mirror.
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

## What this does not ship

This plugin is the mechanical half of a larger operating discipline;
the rest lives in its author's global instruction corpus and is
deliberately not bundled. None of it blocks use — the guards run on
their shipped defaults with no config file at all (verified: full
replay bench green under an empty policy path and a bare `HOME`, no
tier denied, no tier forced to ask). But two things the skills cite
have no local counterpart:

- **The model-routing table** — which tier gets which work. The
  `dispatch` skill deliberately does not decide *whether* to
  delegate; it disciplines the handover once you have decided. That
  table is a measured, dated fact about one person's model lineup, so
  shipping the numbers as defaults would hand you someone else's
  stale cache. The shape travels, the numbers do not: rank the tiers
  you actually use on the axes that decide your dispatches — how hard
  a problem the tier handles unsupervised, output quality where taste
  matters, and what it costs you — then stamp it with a date and name
  what invalidates it (a lineup change, a pricing change). Keep it
  wherever your sessions already load instructions from.
- **`~/.claude/readiness.json`**, the tier-readiness register behind
  skill §6. The plugin never creates it, by §6's own rule: a register
  nothing reads is dead weight. Ignore §6 until some recurring
  procedure actually earns certification, then create the file at
  that moment.

Citations reading "CLAUDE.md" inside the skills are provenance
labels — they mark where a rule came from, while the rule itself is
stated in full on the page. Without that corpus you lose the
footnote, not the rule.

### A starter corpus — real, and dated

Rather than describe the missing layer abstractly, here is the
author's actual one, so the machinery is legible from a working
instance. Copy it and then correct it; do not adopt it unchanged.
**The numbers date fast** — they describe one model lineup on one
payment model, and the day either moves this table is wrong while
still reading as authoritative. That is the whole reason it is not a
shipped default.

The idea of scoring the tiers in a table like this comes from Theo
(<https://t3.gg>); the axes, the numbers, and the use made of them
here are this repo's own.

Routing table, 1–10, higher is better. Lineup as of 2026-07-31;
rankings as of 2026-07-18, unchanged pending operation evidence.

| model    | intelligence | taste |
|----------|--------------|-------|
| fable-5  | 9            | 9     |
| opus-5   | 7            | 8     |
| sonnet-5 | 5            | 7     |

*intelligence* = how hard a problem the tier handles unsupervised.
*taste* = code quality, API design, UI/UX, copy. **Cost is
deliberately not a column**: on a subscription the top tier may draw
from a separately capped pool, so cross-tier token comparisons are
the wrong currency — price your tiers by whichever budget runs out
first for you.

The rules the skills cite by name, in the shortest form that still
works. Your corpus can word them however it likes:

- **Dispatched work** — one writer per working copy; parallel
  writers need disjoint, brief-named ownership, and overlap means
  serialize. Integration (merge, push, publish) stays with the
  dispatcher, after verifying in the artifact itself. An agent's
  "done" is a claim; silence is never success.
- **Fresh-context verification** — a verifier receives the artifact
  and the question, never the dispatcher's reasoning, which would
  hand it the blind spot it exists to escape.
- **Done is the check's own output** — a completion claim carries
  the verifier's verbatim output, never a summary of it and never a
  launcher's exit status, which reports that a run happened rather
  than what it found.
- **Paraphrase drift** — a summary is a label over its body; book
  findings from the body, never from the label.
- **Whether to dispatch** — work whose design is already settled
  defaults to a dispatch, since the settled design is the brief
  already written; open judgment favours staying inline. This is the
  decision `dispatch` deliberately does not make for you.

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
