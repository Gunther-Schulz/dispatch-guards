# PermissionRequest — an unused hook seam (harvest 2026-08-06 item 6)

Consumer: the next session designing a new guard lane — check this
seam before defaulting to PreToolUse. Status: **UNVERIFIED locally**
(basis label, corpus Grounding rule).

## The fact (survey-sourced, not locally probed)

bobmatnyc/claude-mpm pairs its PreToolUse model hook with a
`PermissionRequest` policy engine that emits real allow/deny at the
permission-dialog moment — i.e. the harness exposes (in some
version) a hook event that fires when a permission REQUEST is about
to be shown, distinct from PreToolUse which fires on every call.
Source: https://github.com/bobmatnyc/claude-mpm
(`src/claude_mpm/hooks/model_tier_hook.py` and its settings), read
by the 2026-08-06 survey agent, not by this repo's sessions.

## Why it could matter here

Every dispatch-guards lane today rides PreToolUse/PostToolUse/
SubagentStop. A PermissionRequest seam would differ in one useful
way: it fires only where the harness already decided to ask — a
policy hook there shapes DIALOGS (auto-answering, annotating,
re-routing them) instead of adding fires to every call. Candidate
use: the fable ask-lane's dialog text, or site policy that wants to
auto-allow a sanctioned command form instead of denying its raw
twin (the agentic-coding-reference allow/deny pairing, harvest
deferred list).

## Verification step (do this before building on the fact)

1. Check the shipped binary's hooks reference for a
   `PermissionRequest` (or similarly named) event and its input
   schema — the claude-code-guide agent or the release notes.
2. If present: probe with a logging-only hook registered on it;
   stamp the binding with an as-of date in _dispatch_common's
   docstring before any lane uses it.
3. If absent in our version: note the version checked here and
   re-check on harness upgrades.
