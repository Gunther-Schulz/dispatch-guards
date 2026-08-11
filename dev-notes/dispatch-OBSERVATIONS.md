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

## 2026-08-07 — mint: terminal-idle-after-lane-close gets no reply (forms.md §2, race clause widened)

Live incident, twice in one session (statiker meta desk): the §4
mirror duty ("book the report AND tell it the lane is closed")
itself resumes the completed agent, which re-idles; the dispatcher
answered the first terminal idle with another courtesy message,
which resumed it into a second idle — a politeness loop the
existing race clause (demand-direction only) did not cover. The
widened clause names the terminal idle as a closed lane's expected
shape: books nothing, gets no reply. Placement basis: grep "idle
notification can RACE" (one home, forms.md §2); "lane is closed"
(one hit, SKILL.md §4 — the duty that creates the case, cross-ref
kept). Not mechanizable at this layer: incoming teammate
notifications have no hook surface to suppress on.

## 2026-08-07 — over-fire: the push gate matches "push" as a SUBSTRING of commit-message text

Live incident, cache-fix fork (leak-gate lane). An agent's `git commit`
was denied by the push guard because its heredoc MESSAGE contained the
word "push" — the commit was about a push hook, so the word was
unavoidable subject matter. The agent worked around it by moving the
message to a file and using `git commit -F`, which is a correct local
workaround and precisely the wrong training: the guard taught message
rewording rather than catching a fused push.

Why it matters more than its nuisance value: this is the
fires-on-a-non-defect shape the corpus names, on a guard whose whole
purpose is the one boundary before unerasable history. A reader who
learns to reword around it is a reader who will reword around a real
fire. The dispatcher hit the same class separately — a compound
`git push … | tail` plus a `git log` claim check in one command — where
the gate was RIGHT; the two are hard to tell apart from the deny text
alone.

Proposed: the lane should key on the command's VERB position (an
argv-level `git push`), not on the token appearing anywhere in the
command string including quoted message bodies. Naming the distinction
in the deny text would also help — "a git push in this command" vs
"the word push inside a message" are different findings.

Not fixed here: this is an observation from a consuming repo, and the
lane's own docstring is canonical for its predicate. Reported per the
skill's evolution rule rather than patched from outside.

## 2026-08-07 — a brief cut from a ranked-list head inherits the list's staleness

Dispatched (statiker meta session): implement cache-fix BACKLOG Tier B
item 17. The executing agent's first read found the entry body already
grade-marked "(DONE — f2ab6d0)" — landed by another session 70 minutes
before the dispatch — and correctly halted with zero writes. The
dispatcher had read the ranked head (which still listed the item) and
two body windows that straddled the grade header without covering it;
the brief's "Background" section then shipped the stale state as fact
("4 of 85 captures failing"), which the executor had to overturn.
Cost: one full opus dispatch spent verifying landed state.

Candidate rule (§1, near the base-commit clause): a brief cut from a
backlog/ranked-list entry states the entry's GRADE LINE as read at
cut time — the one-line body read is the staleness probe, and a head
or index line is never the basis (the corpus paraphrase-drift rule,
applied at brief-cut). Secondary find, same root, reported to the
target repo's own round: the repo's order/lint checkers both pass over
a DONE-graded bullet still holding a rank anchor, so the ranked head
can never notice its own staleness mechanically.

## 2026-08-07 — the base-check halt rule has nothing to say about commits that land DURING the dispatch

Dispatched (dotfiles): migrate this repo's own hook state out of
`~/.claude/` to XDG. The brief carried the §1 base check verbatim —
both reads, three states — and the executor ran it cleanly: base
contained, nothing on top. The dispatcher had verified the same state
independently a minute earlier.

Then a concurrent session in the same working copy landed four commits
mid-dispatch, three of them touching `claude/hooks/**`. The brief had
added a repo-specific clause — "if any touches `claude/hooks/**`, HALT
and report" — written for the START state, where it sits next to the
base check. Read at commit time it appeared to fire, and the executor
surfaced it as a decision rather than acting on it: none of those three
files was in its write set, and it judged that leaving five files (one
untracked) in a copy another session was actively committing in was the
more dangerous state. It committed and escalated the question. That
judgment was right — the dispatcher confirmed zero file overlap and
ruled no reversal — but it cost a round trip, and a cheaper tier would
plausibly have halted with the work stranded.

The gap: §1's three-state base rule is entirely about SPAWN-TIME state.
It is the right shape for that and says nothing about a co-writer
committing while the dispatch runs, which is a normal condition on a
shared working copy — the same copy the disjointness rules already
anticipate for WRITES.

Candidate rule (§1, appended to the base-commit clause): the base check
governs the START state and says so explicitly; commits landing
afterwards are judged by WRITE-SET OVERLAP, not by directory or path
shape. Overlap halts, disjoint proceeds and is reported. A brief adding
its own halt predicate states which of the two moments it binds — a
path-shaped predicate written beside the base check reads as start-state
to the writer and as continuous to the executor, and those differ
exactly when a co-writer is live.

Secondary observation, same dispatch: the dispatcher's "verify, then
integrate" duty assumes the dispatcher controls the push. Here the
concurrent session pushed the agent's commit before verification
finished. Nothing broke — the commit passed — but on a shared copy the
integration seam is not the dispatcher's to hold by convention alone,
and §4 currently reads as though it were.

## 2026-08-07 — a read-only lane's working copy grew push-denial config, unreported

During a read-only discovery dispatch into a sibling repo's MAIN
clone, both remotes' pushurl were set to `DENY-worktree-push` (the
worktree skill's every-remote recipe) at a timestamp inside the
lane's window. The lane's report declared zero repo writes; the
dispatcher's next integration push failed on the poison and removed
it after reading the evidence (main clone, `--git-dir` = `.git`, not
a worktree — the recipe's own scope is per-worktree). Two candidate
rules once attribution lands (question sent to the agent): (1) the
worktree skill's denial recipe states its scope test (`git rev-parse
--git-dir` ends in `.git/worktrees/<name>`, else DO NOT poison);
(2) §2's report form: config writes are repo writes — a lane that
touches `.git/config` reports it under files touched, read-only
briefs included.

RESOLVED same day — the lane is EXONERATED (its denial carries
checkable corroboration: no `git config` invocation, git-less probe
copies, timeline closed by the dispatcher's own unset explaining the
second mtime). The writer was a CONCURRENT SESSION's worktree lane:
`git worktree list` on the clone shows a scratch worktree belonging to
another session id, and worktrees SHARE `.git/config`, so that lane's
every-remote pushurl denial (the recipe followed faithfully) landed
repo-wide — the worktree skill's shared-config hazard playing out
across two sessions, each individually disciplined. The dispatcher
restored the denial after its own push (the other session's
established state stands). Rule candidates replace the earlier two:
(1) worktree skill: the pushurl-poison step states that in a SHARED
config it denies the whole clone — per-worktree scope needs
`extensions.worktreeConfig`; a lane on a shared clone poisons at
dispatch and REMOVES at integration, or the dispatcher owns the
toggle. (2) dispatch skill §4, the one-writer check: `git status`
does not see worktrees — the co-writer census before integrating in
any clone is `git worktree list` + status, and a scratch-path
worktree with a FOREIGN session id is a live co-writer whatever the
tree says.

## 2026-08-07 — dispositions-as-brief graduated; two §1 note candidates

The pre-registered statiker experiment (criterion recorded before the
arm ran) graded SUCCESS on all three clauses: nine repair dispositions
dispatched as a brief landed red-first with zero desk correction
passes and held clean under the following attack round, while the same
lap's desk-implemented repairs took all three of that round's
blockers. The corpus's brief-family bullet gained the fourth member
same session (dotfiles 415e3bb). Two §1 candidates from the measured
lap:
1. A repair lap's recorded dispositions are a brief SHAPE — the brief
   section that carries them states each disposition's red-first
   arrangement as the executor's first act per item.
2. GRADUATED to §1 ("Criteria state OUTCOMES first, sites second"),
   2026-08-08, after the second firing below — consulted where it
   lived, not where briefs are written, so relocation was the fix.
   Original text: criteria stated as OUTCOMES out-reach criteria stated as edit
   sites: the arm's "identical verdicts from three cwds" criterion
   found a call site the brief's site list missed, and the next
   attack round's bites on the arm's files all traced to
   edit-shaped site enumerations in the brief ("these three
   sites") rather than to the arm's execution. Candidate wording
   for §1's settled-design part: name the observable the change
   must produce, then the known sites — never the sites alone.

## 2026-08-08 — a stated base can be stale: §1's base clause says
## STATED, never that the statement is a fresh read

A dispatch into `dotfiles` carried base `3014043`, taken from the
dispatcher's own orientation read several turns earlier. By compose
time three commits had landed there from a CONCURRENT SESSION
(`b8fe3d4`, `40390ce`, `9cae041`, the newest ~2 minutes before the
dispatch). The executor ran the two prescribed reads, hit the
second disjunct — base contained, commits on top — and halted with
no files touched, which is the rule working exactly as written.

The gap is on the DISPATCHER's side and §1 does not currently close
it. The base-commit clause reads "STATED in the brief, never
discovered", aimed at an executor guessing its own base; it says
nothing about where the dispatcher's stated value comes from. A hash
recalled from an earlier read satisfies the clause literally while
being exactly the paraphrase-drift shape the operator corpus warns
about — a label over a body that moved. The cost was one round trip;
it would have been a mis-scoped edit had the three commits touched
the executor's five files instead of being orthogonal to them (the
executor checked, and reported the check, before asking).

Note the asymmetry that makes this easy to miss: the executor's
check is prescribed as an ACT ("first act, two reads"), so it cannot
go stale; the dispatcher's is a VALUE, and a value has no
freshness. Every other write-boundary decision in §1 is derived at
compose time from files the dispatcher is reading anyway; the base
hash is the one input habitually carried in memory.

Rule candidates for §1 (base-commit clause):
1. The stated base is READ at compose time, in the same reply that
   composes the brief — `git -C <copy> rev-parse --short HEAD`, its
   output pasted into the brief. A hash recalled from earlier in the
   session is not a stated base, it is a remembered one.
2. Where the target copy has any co-writer (peer session, agent,
   human), the base read and the dispatch are ADJACENT — nothing
   between them that could take a turn. The one-writer census that
   §4 already prescribes before integrating belongs here too, at
   compose time: `git worktree list` + `git log -1 --format=%cr`,
   since "committed 2 minutes ago" is what distinguishes a quiet
   copy from a live one.
3. No softening of the executor-side halt. The three-state rule
   fired on commits that turned out orthogonal, and it was still
   right to stop: the executor cannot grade orthogonality against a
   brief it did not write. Halt-and-ask cost one message; the
   alternative is an executor exercising exactly the judgment the
   tier choice was meant to keep at the desk.

## 2026-08-08 — harness bindings: sync lane unobserved; async final text delivered

Two probes from a fable desk session (dotfiles cwd), same day:
(1) an UNNAMED `general-purpose` dispatch with `run_in_background: false` launched ASYNC ("Async agent launched successfully"), contradicting the sync-on-request behavior the title-prefix lane was built for (forms.md §2, binding as of 2026-07-30).
(2) that agent's final text WAS delivered to the dispatcher, in full, inside the completion task-notification — "final text reaches no one" did not hold for this shape.
Both n=1, that day's harness version. Consequence taken now: the agent-model-gate's unnamed/title-prefix lane is retired (name-always, operator decision 2026-08-08). NOT taken: any change to the §2 channel rules — they stand pending a controlled re-probe (named/unnamed × run_in_background true/false, recording launch mode and whether the final text reaches the dispatcher). See the PARKED backlog item of the same date.

(The two entries below were authored by a peer opus desk session and
relayed by the operator; appended verbatim by the integrating
session. Their bases are the authoring session's transcript and
executed commands, as each entry states.)

## 2026-08-08 — the outcomes-vs-sites candidate re-fires, and the
## second firing was briefed by a session that had just read it

A brief closing the "installer must yield to externally-managed
symlinks" lane named its edit sites: install.sh:132, :142, and
uninstall.sh:41. uninstall.sh has TWO writes to $SETTINGS — the
hooks-removal jq at :38 and the statusline-removal jq at :41 — and the
brief named only the second, because the dispatcher took the line
number from the audit that found the defect rather than enumerating the
write sites. The executor fixed :41 exactly as briefed, then flagged
:38 as a likely scope oversight and correctly declined to fix it
unbriefed. The defect the lane existed to close therefore survived its
own repair: uninstalling would still have replaced a symlinked
settings.json with a regular file.

The outcome-shaped statement reaches all of them where the site list
reached three of four, and it is one command:
`grep -n '> "$SETTINGS"' install.sh uninstall.sh` returns five writes —
four requiring the cp-through-symlink form, plus the `echo '{}'`
bootstrap at install.sh:99 which is correct as-is. Stated as an
observable ("no write to $SETTINGS may replace the link"), the brief
would have carried its own completeness check; stated as sites, it
carried a list.

Red-first on the missed site ran the REAL previous script rather than a
model of it — `git show HEAD:uninstall.sh` against a sandbox CLAUDE_DIR
whose settings.json is a symlink: old left a regular file (link
destroyed), new left the link intact with the target emptied to `{}`.
Same fixture both sides, old is HEAD, new is the working tree.

What makes this worth recording is not the miss but its provenance.
This re-fires candidate 2 of the 2026-08-07 entry ("dispositions-as-
brief graduated; two §1 note candidates"), which reads: criteria stated
as OUTCOMES out-reach criteria stated as edit sites — name the
observable the change must produce, then the known sites, never the
sites alone. That candidate was already in this file, and the
dispatching session had READ it — the tail of this file, including that
paragraph — earlier in the same session, while appending the
base-commit entry above. It still did not reach the brief-writing
moment two dispatches later. A candidate in dev-notes is consulted by
whoever is editing dev-notes; §1 is consulted by whoever is writing a
brief. Same session, same day, same rule, wrong shelf.

Two independent lanes now, from opposite directions: the 2026-08-07
case where an outcome-shaped criterion found a call site the brief's
site list missed, and this one where a site-shaped brief left a defect
the outcome would have caught. Second firing, different failure
direction, same clause.

## 2026-08-08 — a Background section claimed dispatcher verification
## over a citation the dispatcher never opened

The same brief carried a part (3): uninstall.sh:22 removes
~/.claude/cachebust-runbook.md, so guard that removal with `[ -L ]` and
leave an externally-managed symlink alone. No such code exists.
uninstall.sh:22 is `rm "$BIN_DIR/claude-worktime"` — the binary — and
`grep -n 'runbook\|cachebust' uninstall.sh` returns nothing at all: the
uninstaller never touches the runbook anywhere. The citation came from
the audit that had swept the two repos, and the dispatcher passed it
into the brief without opening the file.

The brief's Background header read "established and verified by the
dispatcher; re-verify at the cited lines, report a mismatch as a gap".
The first half of that sentence is a verification CLAIM, made over
every line the section carries, and it was false for one of them. The
second half is what saved it: the executor read the whole file, hit the
listed STOP signal ("any cited line that no longer says what this brief
quotes"), built nothing for part (3), and returned it as a question
with its own grep as evidence.

The machinery worked, but note what it depended on. This citation was
ABSENT, so reading falsified it immediately. A citation that was merely
STALE — right file, right shape, wrong line after drift — reads as a
near-miss the executor plausibly "corrects" toward, and the same
Background sentence would have vouched for it just as strongly. The
failure mode this caught cheaply is the one it handles best.

Rule candidates for §1 (the Background/grounding part):
1. "Established by the dispatcher" is a per-line verification claim,
   not a section-level tone. A cited line is either OPENED at
   brief-write time, or it is carried with its provenance and its
   grade — "from <source>, unverified" — so the executor knows which
   citations hold dispatcher weight and which are inherited. A
   Background section whose lines have mixed provenance and one
   uniform header is the drift; the header is the label, the lines are
   the body.
2. Corollary for audit-sourced briefs specifically: findings arriving
   from a discovery dispatch are testimony, and a brief is where that
   testimony becomes an instruction. The transition is the natural
   verification point — every finding the brief turns into a build
   step gets its cited line opened once, at that moment, because after
   it the claim is executed by someone who cannot tell inherited from
   verified.

## writer-claims-gate WARNs on a claim whose work is already in HEAD

Observed 2026-08-08, live, during a two-lane dispatch. A lane's first
Edit to a file in a sibling repo fired `writer-claims-gate`: "written by
another agent (<other-agent-id>) within the claim TTL". Guard fire logged
in `dispatch-guards-fires.jsonl` at mode `warn`.

The claim was spent. Reconstructed from timestamps the gate does not
consult: the claiming agent's own guard fires are stamped ~2 h before the
lane started; the commits carrying its work landed ~50 min after those
fires; the claiming session's transcript went quiet ~1.5 h before the
lane began. So the claimed work was fully committed and merged into HEAD
while the claim went on warning.

Why it matters more than a nuisance fire. The executing lane could not
distinguish this from a live conflict using the evidence available to
it. It checked HEAD (unchanged), `git diff --stat` (only its own edit),
and `git status` (clean) — and reasoned "stale claim". That conclusion
was correct and its basis did not reach it: a clean tree proves nothing
was COMMITTED; it says nothing about a co-writer holding uncommitted
work. The lane flagged it live rather than proceeding silently, which is
the right conduct, and the question still had to be settled by the
dispatcher running an out-of-band timing comparison the lane had no way
to perform. A guard that fires on correct work and can only be cleared
from outside trains the override reflex it exists to prevent — the
check-that-fires-on-a-non-defect shape.

Proposed change (not made): before firing, test whether the claimed
work is reachable from HEAD — if the claiming agent's commits are
already merged, the claim is spent and the gate stays silent. Cheaper
variant if commit-attribution is unavailable: expire a claim when the
working tree is clean at the claimed path.

Red-first arrangement, both arms required, because this is a predicate
change to a live guard: (1) a claim stamped before a commit that
contains its work must NOT warn; (2) a claim with genuinely uncommitted
changes at the claimed path MUST still warn. Arm (2) is the over-firing
control that keeps the repair from silencing the gate — without it the
fix is indistinguishable from disabling the check.

Cross-reference: booked as a POINTER in the claude-code-cache-fix fork's
BACKLOG.md, since that is where the incident was walked. This file is
the carrier a fresh context in THIS repo reads.

- 2026-08-08 (0.7.1 batch, two parallel sonnet dispatches in one
  plugin): §1's "guarded write paths pre-name their gate" was
  loaded but inert at brief-writing — BOTH briefs omitted the
  unbumped_plugins pre-commit gate, and both executors halted on it
  independently at commit time (correct conduct, one wasted bounce
  each). The variant the rule's examples don't surface: parallel
  same-plugin writers share ONE version gate, so the bump is
  structurally the dispatcher's (bump-first commit; the gate's
  release-state comparison then clears the per-author follow-ups).
  Candidate sharpen: the §1 brief skeleton's Write-boundaries slot
  gains a "gates on this path:" prompt line, and the parallel-
  siblings case names the shared version gate + bump-first
  sequencing. Consumer: the next dispatch-skill amendment pass.

## 2026-08-09 — fire-log path may not match the README's XDG_DATA_HOME claim

Observed during dotfiles doctor hardening (dotfiles b4914c5), not
explained there: a full dotfiles doctor run appended 2 lines per run
to ~/.local/share/claude/dispatch-guards-fires.jsonl (via the replay
bench exec'ing the real guard scripts). After doctor started passing
an isolated XDG_STATE_HOME — data home untouched — to those
subprocesses, the plugin fire log stopped receiving those lines
(646→648 pre-fix, +0 post-fix, same command). If the installed
guards resolved the fire log under XDG_DATA_HOME as the README
documents, a state-home redirect should not have silenced them.
Hypothesis, unverified: the installed resolver follows
XDG_STATE_HOME (or a shared state-root helper), and the README's
XDG_DATA_HOME claim is stale — the label-over-body class. Live
logging in real sessions is unaffected (doctor's child env only;
normal-env writes confirmed). To settle: read the installed
_dispatch_common path resolution and either fix the README or the
resolver. Consumer: the next dispatch-guards maintenance pass.

## 2026-08-10 — Brief-committed-first makes the stated base self-refuting

Class: brief-form defect (§1 "base commit is STATED"), observed live.
A brief committed to the SAME working copy the executor builds in
moves HEAD past any base hash chosen before that commit — the brief
named base 9c2bb9c, the brief's own commit (5ced046) plus a channel-line
fix (98bf22e) sat on top at spawn, and the executor hit the brief's own
"base contained + commits on top = STOP" lane by construction. One full
round trip spent ratifying dispatcher-authored metadata commits. The
executor behaved correctly (followed the literal box instead of judging
the commits harmless — exactly what the box is for).
Repair that worked, sent as the round-trip answer: a TARGET-PATH-scoped
base tolerance — "valid base: <hash> OR any later HEAD whose extra
commits leave the target paths untouched; check `git log <hash>..HEAD --
<target paths>` → empty = proceed, else STOP". That is the
pre-authorized-repair-class shape (§1) applied to the base check.
Candidate §1 amendment: where the brief FILE is committed to the
executor's working copy, the write-boundary bullet should prescribe the
path-scoped tolerance clause (or name the brief's own commit as base)
instead of a bare pre-brief hash. Consumer: the next dispatch-guards
maintenance pass.

## 2026-08-11 — Shared config file across two parallel dispatches: the rule was right, the enforcement posture was not

Class: dispatcher error against §1's per-FILE disjointness, plus a
warn-only gate that would have caught it. Observed live, two agents.

What happened: two parallel sonnet dispatches were each granted
`config/models.py` ("ADD ONLY, touch no existing field") — one adding
alarm knobs, one adding a truncation knob. Agent A committed by
pathspec including that file; agent B's uncommitted hunk in the SAME
file rode out under A's message. Content correct, present once,
unpushed — but A's commit message no longer describes its contents.

The rule was NOT wrong. §1 states it exactly ("Disjointness is per
FILE... an agent committing its own work in a shared file sweeps up a
co-writer's uncommitted hunks") and prescribes serializing on overlap.
The dispatcher (opus, this session) violated it while believing an
ADD-ONLY constraint made sharing safe. It does not: `git commit --
<paths>` takes the whole WORKING-TREE state of every named path, so
"we only add, never collide" is irrelevant to what the commit captures.
Candidate §1 clarification, one sentence: an ADD-ONLY or
non-overlapping-region grant on a shared file is NOT a disjointness
exemption — the commit is file-granular regardless of where in the file
the hunks sit.

Two things the incident says about the guards themselves:

1. `writer-reservation-gate` fired, correctly, with an accurate
   explanation naming this exact failure — and blocked nothing, being
   in staging/warn mode. Enforcing, it would have prevented this. Not a
   rules gap; an enforcement-posture observation. Worth counting in the
   fire log as a would-have-caught.

2. A genuine limit the skill names but cannot cure for shared files.
   §1 says "the check and the act belong in ONE command, or in a form
   that cannot act on the wrong object", and prescribes pathspec as
   that form. Pathspec isolates against OTHER FILES; it does not
   isolate a co-writer's hunks INSIDE a named file, and no commit form
   does. Agent A did read `git diff --stat`, saw only its own content,
   and committed — B's hunk landed in the window. So for a shared file
   the read-then-act race is uncloseable, which makes serialization the
   only real remedy rather than a preferred one. The skill's wording
   ("or in a form that cannot act on the wrong object") reads as though
   a safe form always exists; for this case it does not.

Also observed, same session, unrelated to the above: a sonnet-tier
agent shell had NO docker daemon and NO usable sudo, so a brief step
requiring "run this against a postgres:17 container" was unexecutable
at that tier. The executor surfaced it as a gap rather than claiming
verification (correct behaviour). Candidate §1 note: a verifier step
requiring a container runtime states that as a tier/environment
precondition, the same way the REPOINT clause requires confirming a
knob exists before briefing it.

Consumer: the next dispatch-guards maintenance pass.
