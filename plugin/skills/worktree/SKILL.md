---
name: worktree
description: Portable git-worktree and git-hook mechanics — shared-config and hook-environment hazards, hooks-reach asymmetry, per-worktree push denial, provisioning probes, cleanup — each rule from a measured incident. Use when creating or working in a git worktree, isolating an agent or task in a worktree, wiring or debugging git hooks (pre-push, pre-commit) that run tests or tools, running a test suite from a git hook, or diagnosing a corrupted repo config, wrong-author commits, or hooks that don't fire in worktrees. Not for Claude Code harness hooks (settings.json) or ordinary single-checkout git work.
---

# Worktree regiment

Mechanics that hold on any machine and any repo. Consumer: any
session working in a worktree or wiring git hooks, at any tier — the
mechanics are tier-insensitive, so each rule states its mechanism and
its measured failure shape rather than gating a sequence.

One root fact drives everything below: **a worktree shares the
repository's config, refs, remotes, and stash; only its checkout,
index, HEAD, and `.git/worktrees/<name>/` are private.** Damage done
"in a worktree" therefore usually lands in the shared repository,
where every checkout sees it.

## Config writes from a worktree hit the shared config

`git config` without `--worktree`, run anywhere in a worktree, writes
the shared `.git/config`. For a setting that should differ per
worktree:

```sh
git config extensions.worktreeConfig true   # once per repository
git -C <worktree> config --worktree <key> <value>
```

`git remote remove` in a worktree removes the remote from the whole
repository — remotes are shared. For push denial on an isolated
worktree, poison per-worktree instead, for every remote the repo
declares:

```sh
git -C <worktree> config --worktree remote.<name>.pushurl file:///dev/null/nowhere
```

Worktree pushes then fail while the main checkout pushes untouched.

## The hook environment redirects child git processes

Git exports its hook environment (`GIT_DIR` and friends) into every
hook it runs — as the relative `.git` for main-checkout operations,
but as an **absolute path** for worktree operations. Any child process
the hook spawns inherits it, and an absolute `GIT_DIR` overrides
cwd-based repo discovery: a test or tool that builds scratch git repos
in temp directories will silently operate on the real repository
instead. Measured fingerprint of this class: scratch-fixture
identities appear in the real config, commits ship mis-authored, and
`core.bare=true` materializes (`git init` guesses bare-ness from the
directory name, and a worktree's git dir is not named `.git`),
breaking every work-tree git command.

A hook that runs anything beyond plain git plumbing — a test suite, a
linter, a build — sanitizes first, after resolving the paths it needs
from the hook context:

```sh
cd "$(git rev-parse --show-toplevel)" || exit 1
unset $(git rev-parse --local-env-vars) 2>/dev/null || true
```

The mirror duty in test code: helpers that create scratch git repos
scrub `GIT_DIR`, `GIT_WORK_TREE`, and `GIT_INDEX_FILE` from their
spawn environment, so the suite is safe under any hook context its
users run it from.

## Hooks-reach is asymmetric

- A repository's `.git/hooks/*` never fires in a worktree: hook
  resolution goes to the worktree-private
  `.git/worktrees/<name>/hooks/`, which is practically always empty.
- A global `core.hooksPath` reaches every worktree (config is
  shared) — but it *replaces* per-repo `.git/hooks` entirely.
- A repo-local `core.hooksPath` overrides a global one, silently
  disabling whatever the global path provided. Before setting
  `core.hooksPath` at any level, read what is already in effect —
  `git config core.hooksPath` — and name what the new value would
  disable; a hook "added" by hooksPath has replaced every hook that
  was there before.
- The composing pattern when hooks must both stay global and reach
  worktrees: the global hook acts as a dispatcher that, after its own
  work, chains `<git-dir>/hooks/<name>` with a common-dir fallback —
  worktree-private hooks win as the override point, the repository's
  `.git/hooks` reaches worktree operations via the fallback. Pass the
  hook's stdin (ref lines) through to the chained hook; resolve via
  `--absolute-git-dir` / `--git-common-dir`, never `--git-path hooks`
  (that honors hooksPath and recurses into the dispatcher itself).

## A fresh worktree has no untracked state

Dependency trees, virtualenvs, run state, and every gitignored file
are absent. Before trusting any check executed inside a worktree,
prove the worktree resolves the project's *own code* to itself — the
predicate is per-ecosystem: an editable/develop-mode install resolves
imports to the main checkout and fails the probe; relative-path
imports resolve worktree-local and pass even with third-party
dependencies shared by symlink. Record the probe's executed output as
the isolation basis. A check that silently measures the main checkout
from inside a worktree reports on code nobody is testing.

## The integrity check that catches every config escape

Hash the shared config before the operation and compare after:

```sh
md5sum "$(git rev-parse --path-format=absolute --git-common-dir)/config"
```

One command each side, verb-agnostic — it catches any shared-state
write regardless of which mechanism leaked (config call, hook env,
tool bug). Use it around agent dispatches into worktrees, around
first-ever hook paths, and as the exoneration instrument when
attributing corruption: run each suspect mechanism between two
hashes; the writer is the one that moves it.

## Cleanup and litter

- A worktree directory under `/tmp` dies with the reboot but stays
  registered; the next `git worktree add` for that branch fails
  "already used by worktree". `git worktree prune` first.
- A worktree's branch outlives the worktree. Un-integrated branches
  accumulate silently as litter, each holding real commits nobody
  surfaces. At integration or cleanup, enumerate `git worktree list`
  and the branches created for worktrees, and dispose of each by
  merge, cherry-pick, or an explicit drop.
- Remove reader/probe worktrees at the booking of their findings;
  they have no integration moment.

## Evolution

On a gap noticed in use — a worktree/hook incident this regiment
should have prevented, or a mechanic it states wrongly — write the
observation to `dev-notes/worktree-OBSERVATIONS.md` in the plugin's
source repo and propose the rule change; the founding incidents and
each rule's validity condition live there.
