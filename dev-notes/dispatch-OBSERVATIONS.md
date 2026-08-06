# Dispatch observations — gaps noticed in use

Per the dispatch skill's "Evolution and maintenance": a dispatch failure the
discipline should have prevented, or a rule it states wrongly, gets written here
with its evidence, and the rule change proposed. Not a changelog — each entry is
a measured incident.

## 2026-08-06 — three from one fan-out (3 × opus, two fork worktrees + one shared repo)

Context: three parallel lanes dispatched from a cache-fix session; two in git
worktrees of one repo, one in the operator's dotfiles repo. All three delivered.
The failures below are the dispatcher's, and two of them are holes in the rules
rather than slips against them.

### 1. "Commit unpushed" is not enforceable on a working copy a PEER SESSION shares

The strongest observation of the three, because it defeats a rule that reads as
airtight. §1 says commits are unpushed and pushing is the dispatcher's act after
verification; §5 denies subagent pushes mechanically. Both held. The agent's
commit reached the remote anyway — a **peer session** working in the same repo
ran its own `git push`, and the push set is the branch, so it published the
agent's mid-verification work along with its own three commits.

Measured: the lane's `git/hooks/pre-push` rewrite (270 lines) was on the dotfiles
remote before the dispatcher had verified any of it; `git rev-list --count
origin/main..HEAD` returned 0 where the dispatcher expected 1.

The existing rule covers this from the PUSHER's side (claim each outgoing commit;
an unexpected commit halts the push) and that rule is what the peer skipped. What
is missing is the DISPATCHER's side: when the assigned working copy is shared
with any writer outside the dispatch — a peer session, the operator, a scheduled
job — "unpushed" is a hope, not a boundary. Proposed rule text for §1's write
boundaries: *a working copy shared with a writer outside this dispatch cannot
hold work unpushed; either isolate the lane in a worktree, or accept that its
commits may be published before verification and say so in the brief.* The
worktree ladder already exists for overlap between AGENTS; this extends its
trigger to overlap with sessions the dispatcher does not control.

### 2. The brief boxed DEPLOYMENT and missed LIVE-ON-WRITE

The same lane edited two hooks. The brief explicitly boxed one — build and test
the Claude PreToolUse hook, do not register or deploy it, registration is the
operator's act — precisely to keep a half-built guard from denying legitimate
work mid-session. It said nothing about the other, because deployment was the
axis in mind.

But global `core.hooksPath` pointed at the repo's `git/hooks/` directory, so that
file **is** the live gate for every `git push` on the machine, active from the
moment it is written — no commit, no deploy, no restart. The machine's last check
before public history was under construction while the dispatcher's own pushes
ran through it. Nothing went wrong; that is luck, not design.

Proposed: the write-boundary section asks not only *what is deployment-coupled*
but *what is live on write* — anything on an execution path resolved by PATH
rather than by import (git hooks under `core.hooksPath`, harness hooks already
registered, files a running daemon re-reads, anything under a watched directory).
The two questions have different answers and only one of them was being asked.

### 3. The worktree push-denial recipe, applied without loading the worktree skill

§1's ladder says to create per-agent worktrees and "apply the skill's push denial
to EVERY remote". The dispatcher did the obvious thing — `git remote set-url
--push <remote> no-push-from-worktree`, run inside each worktree — and disabled
push for the MAIN clone, because remote config is shared across worktrees. It
surfaced later as `Please make sure you have the correct access rights`, which
reads like a credentials problem and cost a detour before the cause was obvious.

The worktree skill documents this ("per-worktree pushurl poison, never
remote-remove"). The gap is not the rule, it is the seam: the dispatch skill
names the worktree skill as the single source and the dispatcher improvised the
one step it delegates. Proposed, small: the ladder's rung 2 says the worktree
skill is LOADED before the first `git worktree add`, not merely cited — the same
form the plugin already uses to make the dispatch skill's own load mandatory.

### What worked, recorded so it is not lost in the failures

The §2 report form carried its weight. Both fork lanes used slot (g) to name
what they had NOT executed, and in both cases that slot held the most valuable
sentence in the report: one flagged that its "dossier output is unchanged" claim
was code-reading rather than executed (and, when asked, executed it WITH a
planted control, since a byte-identical diff is a non-event a dead comparison
also produces); the other flagged that one of its mutations had survived,
meaning the bite file had a hole, rather than quietly adding the case. Neither
would have surfaced in a free-composed report.
