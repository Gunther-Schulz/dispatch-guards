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
- 2026-08-06 — SECOND instance of the 2026-07-30 shared-remote class,
  a different verb: `git remote set-url --push <remote> <dev-null>`,
  reached for in a worktree as the obvious way to deny push there,
  wrote `remote.<name>.pushurl` to the shared config and redirected
  the MAIN clone's pushes. Measured in a scratch repo: `git remote`
  has no `--worktree` form (`unknown option 'worktree'`), every
  subcommand writes shared config; the prescribed
  `config --worktree remote.<name>.pushurl` lands in
  `.git/worktrees/<name>/config.worktree` and leaves main untouched;
  `git config --unset-all remote.<name>.pushurl` repairs. Diagnosis:
  the rule was LOADED-BUT-INERT in the enumerated direction — the
  section named `remote remove` as the instance, so a reader who knew
  the right recipe still had no rule covering the sibling verb. Fix
  was to WIDEN to the porcelain (`git remote` has no `--worktree`
  form; `remove` and `set-url --push` demoted to examples), not to
  extend a list — plus the repair line, which the incident session
  needed and the section did not carry. → "Config writes" section;
  the compressed restatement in the dispatch skill's worktree pointer
  ("never remote-remove" → "never the `git remote` porcelain") was
  audited and widened in the same pass.
- 2026-08-06 — guard-side finding from the same incident, found by
  accident when probe commands tripped this repo's own hooks: the
  shared `is_push_command` matched `git remote set-url --push` on its
  `--push` arm (minted for `gh pr create --push`). So a config write
  was DENIED to subagents with a push-discipline message, while
  `git remote remove` — the genuinely destructive shared-state write
  of the founding incident — passed silently. Fires on a non-defect
  and misses the defect, in one matcher. → `--push` arm exempted
  after a `remote` token (token-scoped, so a real push later in the
  same invocation still matches), and the vacated lane replaced by
  `worktree-config-gate` (default-warn), which fires on the
  config-write SHAPE only when git itself reports a linked worktree.
- Exoneration method that closed the config-corruption attribution:
  config md5 before/after around each suspect mechanism — one command,
  decisive per suspect. → "Integrity check" section.

## Firing log

(append dated lines when a rule catches a real issue)
