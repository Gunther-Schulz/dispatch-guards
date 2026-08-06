# Payload injections and prompt-cache rewrites — recorded, unproven

Consumer: the next session designing, promoting, or relaxing the
`message-payload-gate` lane — and any session investigating a
prompt-cache rewrite. Status: **coincidence recorded, cause not
established.**

Moved here from `plugin/skills/dispatch/references/forms.md` §2
(payload-vs-pointer) on the 2026-08-06 skill-craft review: forms.md
is loaded before every brief composition, and a basis the rule
explicitly does not rest on was being paid on every load. The rule
there keeps its one load-bearing basis (context economy) plus a
pointer to this file.

## The observation

Subagent → dispatcher payload injections have coincided with full
prompt-cache rewrites (Claude Code #27048 class, upstream). The
forensic sample shows **no single-field correlation** — no field of
the injected payload predicts the rewrite. Source of the forensic
work: claude-worktime `docs/cachebust-runbook.md`.

## Why it is not load-bearing

The payload-vs-pointer rule stands on context economy alone: an
injected payload occupies the dispatcher's context for the rest of
its session, re-carried on every later turn. That basis is
sufficient and independently true, so the gate needs nothing from
this correlation. If the correlation were later established, it
would strengthen the same rule — it would not change the lane.

## Observing it

Cache rewrites are visible via claude-worktime's ❄ marker /
`--cold`.

## What would settle it

A controlled pair: the same dispatch run twice, identical except for
payload size crossing `max_message_chars`, with the ❄ marker read on
both sides. Until that exists, any claim of causation here carries
the label "unverified".
