# worktree skill — observations (maintenance; never loaded by the skill)

Consumer calibration: written for top-tier sessions (Fable/Opus) —
evidence-register principles with exact commands only where the
procedure is fragile (hook sanitize line, pushurl poison, integrity
hash). Re-review density if a cheaper tier becomes a consumer.

Durability: the rules are BINDINGS to git's own worktree/hook
semantics (shared config+refs+remotes, hook env export, hooksPath
resolution, init's dir-name bare-guess) — staleness-checked against
git behavior, not fire-checked. The integrity-check section is
enforcement structure. No capability patches as of minting.

## Founding incidents (2026-07-30 .. 2026-08-05, all measured)

- 2026-07-30 — `git remote remove` run in a clippy isolation worktree
  removed the remote from the operator's main repo (remotes are
  shared); main-tree push failed "No configured push destination".
  Verified fix became the per-worktree pushurl poison. → "Config
  writes" section.
- 2026-08-05 — repo-local `core.hooksPath`, set to activate a tracked
  suite hook, silently replaced the machine's global hook dispatcher
  (a fixture-leak scanner) in exactly the repo it protected; one push
  went out unscanned. → hooksPath rules in "Hooks-reach".
- 2026-08-05 — first suite run under a worktree pre-push hook: git's
  exported absolute GIT_DIR redirected the suite's scratch-repo
  helpers into the real repo — core.bare=true (init's dir-name
  bare-guess) + fixture identity t/t@t written to shared config, one
  real commit pushed mis-authored. Reproduced and fixed same day
  (unset `git rev-parse --local-env-vars`); main-checkout hooks were
  immune (relative GIT_DIR re-resolves in each scratch cwd). → "Hook
  environment" section, both directions of the fix.
- 2026-08-05 — hooks-reach measurements: `.git/hooks` never fired in
  a worktree until a global dispatcher gained a common-dir fallback
  (bite-tested red-first); /tmp worktree registrations survived a
  reboot ("already used by worktree"); a native-isolation probe found
  five stale worktree branches holding un-integrated commits. →
  "Hooks-reach" chaining pattern + "Cleanup and litter".
- Exoneration method that closed the config-corruption attribution:
  config md5 before/after around each suspect mechanism — one command,
  decisive per suspect. → "Integrity check" section.

## Firing log

(append dated lines when a rule catches a real issue)
