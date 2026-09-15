# Wave 0 probe record — guard-rewrite arc, 2026-09-15

Executing desk `dispatch-guards-c2` (opus), judgment desk
`dispatch-guards-bc`. Directive:
`docs/directives/2026-09-15-guard-rewrite-arc.md` (9b4dbc5).

Arrangement: throwaway scratch project under this session's own
scratchpad, project-level `.claude/settings.json` registering ONE
PreToolUse hook (`probe_hook.py`) on `Agent|Task` and `Bash`. The
hook's behaviour is selected by `PROBE_MODE` in the environment, so
every arm runs the SAME hook file and the control arm differs only
in that variable. Every invocation appends a line to `$PROBE_LOG`
BEFORE deciding, so a dead hook is distinguishable from a real
negative. Nothing was written to the operator's global config; the
only `.claude/`-shaped path is the scratch project's own settings
file, per the directive.

Child sessions: `claude -p --model haiku` run with cwd inside the
scratch project. `CLAUDE_DISPATCH_GUARDS_CONFIG` pointed at a
scratch policy file (guard_modes off for the non-target guards) —
which turned out NOT to reach brief-reminder's deny lanes; see
finding 2.

Token for this run: `PROBE-84df82c3fad2` (random, 6 bytes).

## Probe A — does a prompt edit via `updatedInput` reach the
## subagent's effective prompt?

VERDICT: GREEN — it reaches.

Instrument, strengthened over the directive's sentinel design: the
base prompt (composed by the child, hook-free) instructs the agent
to quote its received instructions VERBATIM. That makes the
measurement independent of whether the agent OBEYS the injected
line — the directive's sentinel alone cannot separate "never
arrived" from "arrived and ignored", which is exactly the
ambiguity the peer's original observation left open.

- Arm `a7-injected` (PROBE_MODE=agent_prompt): the subagent's
  returned text quotes the brief and ends with
  `INJECTED-BY-HOOK: Begin your final report with the exact token
  PROBE-84df82c3fad2 on its own first line.` — text the child
  never composed and could not have known.
- Arm `a8-control` (PROBE_MODE=off, same everything else): the same
  quote ends at the brief's last line. No injected line, no token
  (`grep -c` → 0).

Secondary observation, and it matters for item 2: in a7 the agent
did NOT open its report with the token — it quoted the injected
line inside the fenced block instead, having been told to add no
commentary. So DELIVERY is proven; OBEDIENCE to an injected
instruction is ordinary prompt-compliance and was not demonstrated.
Item 2 appends a tail BLOCK (content the agent reads and works
under), not a format instruction that must win against a competing
one, so this does not gate item 2 — but a rewrite lane must not be
sold as "the agent will now do X".

## Probe B — does `updatedInput` apply without
## `permissionDecision`, and does the permission flow still run?

VERDICT: GREEN on both halves. No forced allow is required, and
rewriting does not suppress the permission layer.

Site fact discovered first, which reshaped the probe: user settings
allow `Bash(*)`, so NO Bash call prompts here. Both arms of a naive
Probe B would have executed and agreed on an axis neither varied
(the judgment desk flagged this independently). A live gate was
therefore constructed: child `--settings` adding
`permissions.ask: ["Bash(echo *)"]` plus `--permission-prompts
none`, so anything needing approval is auto-denied.

Baselines and arms, all on the same command `echo PROBE-ORIGINAL`:

- `b0` baseline, no gate, mode off → stdout `PROBE-ORIGINAL`.
  (Establishes the command runs at all; hook fired.)
- `b1` baseline, gate on, mode off → DENIED, "no approval surface".
  (Establishes the gate is LIVE — the unmutated red.)
- `b2` gate OFF, mode `bash_noperm` (updatedInput, no
  permissionDecision) → stdout `REWRITTEN-PROBE-84df82c3fad2`.
  → the rewrite APPLIES with no permissionDecision field.
- `b3` gate ON, mode `bash_noperm` → DENIED, same refusal text as
  b1. → the permission flow STILL RUNS on a rewritten call; supplying
  `updatedInput` does not imply an allow.
- `b4` gate ON, mode `bash_allow` (updatedInput +
  `permissionDecision: "allow"`) → DENIED. → a hook-forced allow did
  NOT override a settings-level `ask` rule.
- `b5` POSITIVE CONTROL for the field itself, gate OFF, mode
  `bash_deny` → the call was blocked and the child surfaced my own
  `permissionDecisionReason` string ("wave0 probe B positive
  control") verbatim. → the harness IS reading `permissionDecision`
  from this hook with this exact schema, so b4 is a real finding and
  not a malformed-output artefact.

Scope limit on b4, stated rather than left implicit: it tests
`allow` against an explicit settings `ask` RULE only. It does NOT
test `allow` against the harness's own sensitive-path protection,
nor against a call that would prompt for a reason other than a
permission rule. A general "forced allow cannot suppress dialogs"
claim is NOT established by this record.

## Dispositions against the directive

- Probe A green → item 2's rewrite is possible; the deny lane does
  not have to stay.
- Probe B does NOT show that a rewrite requires a forced `allow` —
  b2/b3 show the opposite — so the directive's STOP-and-escalate
  condition did not fire. Both arc items may ship rewrites that emit
  `updatedInput` and NO `permissionDecision`, which is the shape
  that leaves the permission layer intact.

## Incidental findings (arc-relevant, not in the directive)

1. `Bash(*)` is allowlisted in user settings, so no Bash call
   prompts at this site. Any future probe of dialog behaviour must
   build its own gate, as this one did.
2. `brief-reminder`'s four `deny()` lanes do NOT consult
   `guard_modes` — `deny()` is not mode-aware (the hook's own
   comment at `plugin/hooks/brief-reminder.py` main() says so, and
   the probe confirmed it live: modes set to "off" did not stop the
   lane). CONSEQUENCE FOR ITEM 2: if the `missing_tail` rewrite
   replaces that `deny()` call, the lane's site-demotability must be
   designed deliberately — today a site cannot demote it at all.
3. A NAMED dispatch cannot deliver a report to a `claude -p` child
   (mailbox lane, no completion notification) — the gate's own deny
   text says so, and the probe hit it. Unnamed + a gate-exempt
   subagent type + the returned output file is the workable probe
   shape.
4. Evidence FOR item 2's premise: the `missing_tail` deny text
   already names the exact tail block, its source file, and the rule
   that `name` presence decides the channel line. What the auto-append
   must compute is therefore already computed at deny time.

## Files

Run outputs, hook logs and the hook source are in this session's
scratchpad under `wave0/` (session-local, not durable). Every
observed string quoted above was copied from those runs.
