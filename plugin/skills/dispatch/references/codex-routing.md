# §7 Codex / gpt-5.5 routing (only when Codex CLI is installed)

Reference of the `dispatch` skill (operational corpus — see
SKILL.md's governance header). Applies only when
`command -v codex` succeeds.

- Route token-heavy mechanical work to gpt-5.5 via Codex: log
  digging, giant PDFs/specs, clear-spec implementation, data
  analysis. For investigation use `codex exec -s read-only` with a
  self-contained prompt.
- Prompt Codex simply — it is not Claude; don't prompt it as though
  it were. Tell it to say clearly when it finds nothing, naming the
  target it inspected (prevents rerun loops in the parent).
- Codex runs can exceed Bash's 10-minute timeout: pass an explicit
  timeout or run in background.
- Inside workflows/agent fan-outs, wrap it: a thin Claude wrapper
  agent (model sonnet, effort low) writes the codex prompt, runs it
  via Bash, returns the report. Label such agents with a `gpt-5.5:`
  prefix so the real worker is visible. Parallel Codex
  implementation agents need `isolation: worktree`.
