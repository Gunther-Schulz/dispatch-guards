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

## 2026-08-15 — read-only fan-outs have no join to size them, so every one is hand-grouped

**Incident + basis.** Peer testimony (opus desk, pbs-office wave,
2026-08-15), relayed via the peer channel; basis is that session's
own transcript, NOT verified here — recorded at recollection grade.
It ran a 5-lane sonnet read-only pass over ~21 items and, asked why
five, named its own grouping as the weakest point: write-disjointness
was no reason at all, because pure read assignments have no write
sets to derive a split from, so the lanes were grouped by hand.

**Class.** A gap in lane-sizing guidance, not a misapplication. §1
governs what rides one WRITE lane (shared realizing file + one
mechanism) and the route line's mapping SOURCE is a derived join over
write-boundaries — which returns nothing for read-only lanes by
construction. routing.md prices top-tier fan-out WIDTH but does not
size or group read fan-outs. So the route line can be satisfied in
form while the item→lane mapping is pure hand-grouping with no rule
behind it, which is the identity-mapping failure one level down.

**Pre-formulated text** (evidence register; §1 near the ONE-lane
clause, or routing.md). Peer-supplied, amended here — see the
correction below before applying:
"Read-only fan-outs have no write-boundary join to derive lanes
from; three terms size them: a lane's fixed load (system prompt +
corpus + brief, re-paid per agent) must stay small against its work
— the brief-rivals-work test at lane grain; exhaustive per-item
checks cap items per lane, because late items in a long enumeration
get shallower checking than early ones — the under-report principle
as a sizing bound; and the grouping axis (repo, section, artifact
class) is stated in the route line, since no join exists to derive
it. Parallel-vs-queued of the same N lanes stays token-identical;
N-vs-1 lane count does not."

**Two corrections to the relay, both checked here.** (1) The peer is
RIGHT that "token spend is identical either way" was transferred out
of its mechanism: routing.md's sentence compares PARALLEL vs QUEUED
scheduling of the same N dispatches, so it says nothing about N lanes
vs 1. Confirmed at the source. (2) The peer's own draft then repeats
the same error one clause on: it cites forms.md's "~1.3×
cost-weighted on trivial dispatches" as the per-lane fixed load. That
measurement compared the SYNC vs BACKGROUND channel for a single
dispatch — the plumbing one channel skips — never the marginal cost
of an extra lane, which is dominated by the re-paid system prompt +
corpus. The citation is also DEAD as of c6f614b: the figure was
removed from forms.md in this batch, its subject (a sync launch
lane) having ceased to exist. The pre-formulated text above therefore
carries NO number; sizing by a measured per-lane load needs a
measurement nobody has taken yet.

**MEASURED 2026-08-15, so sizing term (a) now carries a number.**
The peer mined its own five lane transcripts (no new dispatch spent)
and I RE-DERIVED the result from the same source rather than booking
the relay: `tools/lane-cost.py`, run against those transcripts.
Direction confirmed and it inverts the folk intuition — at this
workload SPLITTING WAS TOKEN-CHEAPER, because a single lane re-reads
its whole accumulated prefix every call (read cost quadratic in call
count) while splitting pays a fixed per-lane startup once.
CORRECTION to the relayed figures, found by re-deriving: its growth
constant divided TOTAL cache-creation by TOTAL calls, folding each
lane's one-time ~49k startup into the per-call growth term —
inflated 1.56x (4,689 vs 3,007 per call, measured; startup is
265,572 of the 698,604 total creation). Consequences, both material
for a sizing rule: the modeled ratio is 2.58x raw, not 3.7x, and the
crossover is ~29 tool calls per lane, not ~23. The rule of thumb is
therefore "a read-only lane expected to exceed ~30 calls is worth
splitting on token cost alone", and the correction moves AGAINST the
headline, which is why it was worth spending the re-derivation on.
Grades, kept apart: the 5-lane arm is MEASURED from real per-request
usage (deduped by requestId, last snapshot — the per-stream-snapshot
caveat); the 1-lane arm is MODELED from measured growth and has
never been run. The price weights (cache-read 0.1x, creation 1.25x)
are ASSUMED, unverified against billing; raw counts are the
measurement. Unmodelled and worth naming: a real 149-call single lane
would likely hit compaction, which the model does not represent at
all — so the modeled arm is if anything generous to the single lane.
Carry the FORMULA, never these constants: n* = sqrt(4*C_lane/(w_r*g)),
with g and C_lane measured per workload by the tool.

**Consumer + drain.** Dispatching sessions at the route-line moment;
drains on this carrier's normal quota. Applying it means choosing a
home (§1 vs routing.md) — the sizing terms are consumed while
composing a fan-out, i.e. after the dispatch skill's gate-forced
load, which argues §1 over the always-loaded routing module. The
miner GRADUATED to `tools/lane-cost.py` under the probe-used-twice
rule (peer once, here once); it carries the growth-constant trap in
its own docstring and a `--test` whose central assertion is that g
excludes per-lane startup, so the next reader cannot repeat it.

## 2026-08-08 — harness bindings: sync lane unobserved; async final text delivered

Two probes from a fable desk session (dotfiles cwd), same day:
(1) an UNNAMED `general-purpose` dispatch with `run_in_background: false` launched ASYNC ("Async agent launched successfully"), contradicting the sync-on-request behavior the title-prefix lane was built for (forms.md §2, binding as of 2026-07-30).
(2) that agent's final text WAS delivered to the dispatcher, in full, inside the completion task-notification — "final text reaches no one" did not hold for this shape.
Both n=1, that day's harness version. Consequence taken now: the agent-model-gate's unnamed/title-prefix lane is retired (name-always, operator decision 2026-08-08). NOT taken: any change to the §2 channel rules — they stand pending a controlled re-probe (named/unnamed × run_in_background true/false, recording launch mode and whether the final text reaches the dispatcher). See the PARKED backlog item of the same date.

Addendum 2026-08-15 (fable desk, PV-Georgendorf cwd, harness 2.1.232): both shapes now n=2, and the PINNED-TYPE exemption is implicated. An unnamed `claude-code-guide` dispatch (no `run_in_background` param) launched ASYNC, and its full final text was again delivered in the completion task-notification. New half: the skill text itself produced a denied call — forms.md §2 routes pinned-type dispatches to the synchronous channel line ("your final text IS the report"), the brief-reminder hook denied the mode/line contradiction (guard correct, fire logged), and the retry with the background line went through clean. So until the parked re-probe settles the channel rework, the pinned-type guidance instructs the exact form the guard bounces. Proposed rule change: forms.md's channel-line paragraph defaults pinned types to the BACKGROUND line too, keeping the sync line only where a sync launch has actually been observed; the re-probe item gains the pinned-type axis (agent type named/pinned × run_in_background). Basis: this session's transcript — deny text, retry, task-notification delivery.

Resolution 2026-08-15 (opus desk, dispatch-guards cwd, harness
2.1.232 — the controlled re-probe the entry above deferred to).
**The axis this entry and the parked item were built on does not
exist.** The Agent tool takes no `run_in_background` parameter
(schema `additionalProperties: false`, key absent), so the matrix's
flag axis is unrunnable and the older "silently overridden" binding
described a flag that is simply gone. The live axis is `name`, and
the probe separated it from agent type with the cell both earlier
observations were missing — earlier data compared generic+named
against pinned+unnamed, changing two variables at once. Cells:
generic+named → "Spawned successfully … via mailbox";
pinned+named → the SAME mailbox launch; pinned+unnamed → "Async
agent launched", output file, completion notification. So the lane
is keyed on `name`, not on the pinned-type exemption.
Delivery, the half the channel line asserts: the unnamed lane's
completion notification carried the agent's final text VERBATIM
with `tool_uses: 0` — the agent sent nothing and the text arrived
anyway, so delivery does not depend on the agent. The named lane
fired no completion notification, does not appear in the subagent
listing, and one named probe delivered nothing at all despite an
explicit SendMessage instruction.
**Consequence: the proposed rule change in the addendum above is
backwards.** For an unnamed dispatch the background line ("your
final text reaches no one") is FALSE and the sync line is TRUE;
defaulting pinned types to the background line would have made the
guidance wrong in the other direction. The real defect was in the
predicate: `is_background()` read `run_in_background is not False`,
which with the key absent is CONSTANT TRUE — every dispatch
classified background, the unnamed lane's correct line unreachable,
and `tail_mode_mismatch` denying it. That is exactly the 2026-08-15
bounce. Class: a binding whose environment moved, plus a predicate
whose premise the environment silently stopped supplying — the
check kept passing while testing less than it claimed.
Correction to the addendum above: "(guard correct, fire logged)" —
the guard was correct, the fire was NOT logged. `deny()` never
called `fire_log()`, so all six hard-deny call sites wrote nothing;
the log holds zero deny-mode entries for brief-reminder all-time
against 673 for one `fire()`-routed lane. The fire-rate review —
the repo's stated instrument for warn→deny promotion and lane
retirement — was blind to every hard deny. Fixed in the same batch,
red-first (4 log lines instead of 5 under the shipped `deny()`).
Class: an assurance wider than its predicate — the log's own
comment claims "Every guard fire — deny, ask, warn, block — appends
one JSONL line".
Same-day operational residue, same class, recorded because it bears
on the rule just written: the MAILBOX lane's problem is LATENCY, not
loss.
CORRECTION, and the correction is the finding. An earlier version of
this paragraph claimed two `general-purpose` agents "delivered
NOTHING — no message, no notification". That was FALSE and is
withdrawn: both delivered. One arrived roughly half an hour after
its trivial no-op task, long past two staged resumes; the verifier's
full report arrived after its close-out had already been issued, and
its own SendMessage had returned success all along. What the claim
actually measured was the DISPATCHER'S WAITING WINDOW, not the
channel — a not-observed booked as a not-there, in a record whose
subject was how to verify things. The permission-block hypothesis it
floated is unsupported: the agents were not blocked, they were slow.
Standing fact after correction: on the mailbox lane a report can
arrive tens of minutes after the work is done, and the dispatcher
cannot tell a slow lane from a dead one — a named agent is absent
from ListAgents' subagent listing and fires no completion
notification, so SendMessage is the only channel in both directions
and silence carries no information either way. n is small and the
arms were not blind.
Why it matters for §1 rather than being a curiosity: the model gate
mandates a `<model>-` name on every GENERIC dispatch, so generic
dispatches cannot reach the unnamed lane at all — the mandate routes
them all into the lane whose reports run late and arrive only if the
agent cooperates. It also prices the expected-return horizon rule:
the horizon is what tells a dispatcher to ACT, and acting means
inspecting or re-dispatching, never concluding loss — a horizon
passed is evidence about the wait, not about the agent. The mailbox channel
line and report-enforcer exist for exactly that exposure; this is
evidence about how much load they carry, not evidence against the
name mandate. Consumer: the next fire-rate review, alongside the
report-enforcer PARKED item; a controlled probe (what is the actual
delivery-latency distribution on the mailbox lane, and can a
dispatcher observe in-flight state at all?)
is the missing evidence.

Mechanism, both halves: forms.md §2's channel-line block and
binding rewritten to the two lanes; `mailbox_lane()` replaces
`is_background()`; six brief-reminder cases added to the replay
corpus (it had ZERO), two of which go red against the old hook —
the bounce is now pinned as a regression case. Consumer: shipped in
this batch, no drain owed.

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

## 2026-08-12 — Vier Beobachtungen aus zwei K7-Dispatches (Abwägung Georgendorf, Opus-Agenten)

Quelle: Session 91da2482 (PV Georgendorf), zwei Dispatches
(opus-abw-runden-elementfelder, opus-abw-kasten-klartext), Journal
pbs-office betrieb/journal-2026-08.jsonl.

1. **Report-Queue vs. Dispatcher-Nachricht — DREIMAL in einer Session.**
   Agenten komponieren mehrteilige Abschlussberichte als Queue und
   drainen ihre Inbox zwischen den Teilen nicht: ein GO des Dispatchers
   (nach Teil 1 gesendet) war im Schlusssatz von Teil 7 noch „offen";
   zwei Zusatzaufträge (D13, D8/D9) fehlten in kompletten Berichten
   undispositioniert — je ein voller Anmahn-Rundlauf. Vorschlag
   (§2-Tail-Klausel): vor dem Absenden des Abschlussberichts UND
   zwischen Teilen die eigene Inbox drainen; der Bericht dispositioniert
   jede bis zum Sendezeitpunkt eingegangene Dispatcher-Nachricht oder
   nennt sie ausdrücklich als unbearbeitet; Race-Symptom (Bericht
   „fertig", Nachricht unerwähnt) ist damit vom Bericht selbst
   unterscheidbar.

2. **Positions-IDs im Brief sind Etiketten über fremden Körpern.** Ein
   Brief zitierte Register-Nummern („Reg-12/Reg-13") aus einem älteren
   Prüfer-PDF; das Register war seither regeneriert, alle Nummern um
   eins versetzt. Gerettet hat die Inhalts-Anker im selben Brief
   (Kasten-Wortlaut), nach denen der Executor arbeitete. Vorschlag
   (§1-Klausel, Anwendung der Label-über-Körper-Regel): positions- oder
   generat-abhängige Identifikatoren (Registernummern, Ä-IDs,
   Zeilennummern) tragen im Brief IMMER einen Inhalts-Anker daneben;
   der Executor arbeitet bei Divergenz nach dem Anker und meldet den
   Versatz.

3. **`git commit -m "…" -- <pfade>` scheitert** — nach dem
   Pathspec-Trenner liest git -m als Pfad; zwei Sessions sind am selben
   Tag unabhängig darauf gelaufen (Dispatcher + Executor). Der §2-Tail
   sagt nur „by pathspec"; Vorschlag: Tail-Wortlaut präzisieren —
   Flags VOR dem `--` (`git commit -m "…" -- <pfade>` ist falsch
   herum; korrekt `git commit -m/-F … -- <pfade>` mit Message-Flag vor
   dem Trenner, bzw. -F bei mehrzeiligen Messages).

4. **Visuelle Chrome-Änderungen haben keine Bild-Prüfstufe.** Ein
   Farb-Stack-Leck (violetter Fließtext nach neuem framed-Feld) passierte
   Suite, Struktur-Checks, pdftotext-Zählproben und Seitenzahl-Vergleich
   unbeanstandet — pdftotext sieht Farben nicht; gefunden vom Betreiber
   per Screenshot. Vorschlag (Brief-/Verifier-Klausel): Änderungen an
   sichtbarem Render-Chrome nennen im Verifier eine SEITENBILD-Sichtung
   (pdftoppm o. ä.) durch den Dispatcher; Text-Extraktions-Checks sind
   für Farbe/Layout blind, und der Dispatcher kann Bilder sichten.

Consumer: die nächste dispatch-guards-Maintenance-Runde (Tail- und
§1-Wortlaut); Beobachtung 4 zusätzlich als Site-Regel im
pbs-abwaegung-Repo gelandet (dortiges CLAUDE.md, via laufenden Dispatch).

## 2026-08-12 — Batterie-Aufruf ist Teil des Instruments: `-k` verdeckt Fixtures, `-x` verdeckt Arme (3 Vorfälle, 3 Lanes)

1. **Vorfall + Basis (3×, zwei Tage):** (c, 13.08., Dispatch
   `opus-helfer-kopien`, von der Lane selbst gefangen und gemeldet)
   Die ANWENDUNG der Mutation ist dieselbe Arrangement-Hälfte: ein
   handgetipptes Ersetzungs-Muster traf 0×, die Batterie lief GRÜN
   über der NICHT angewandten Mutation — von „Test greift nicht"
   nicht unterscheidbar, beinahe als Rot-Beweis gebucht. Reparatur
   in der Lane: Mutation per Zeilen-Bereich aus der Datei gelesen,
   entfernter Text vor jedem Lauf ausgedruckt; der Dispatcher-eigene
   Kontroll-Biss lief 13.08. mit demselben Anwendungs-Beweis.
   (a) e1 aus Dispatch
   `opus-abw-drei-waechter`: Mutations-Batterie mit `pytest -k "antwort"`
   — der Selektor schloss genau das Fixture aus, das die Mutation fangen
   sollte; Batterie las sich grün. Gefangen durch Divergenz zweier
   Messungen (Bestand 13 Meldungen, Fixtures still). (b) e-Nachtrag aus
   Dispatch `opus-abw-sichtweite-austrag`: Batterie mit `-x` — pro
   Mutation nur der ERSTE Fehlschlag sichtbar, wodurch systematisch
   verdeckt blieb, welcher Test-Arm NIE feuert; „alle Mutationen rot"
   war wahr und trotzdem ohne Aussage über den unbewiesenen Arm
   (test_sichtweite_elementfeld…, repariert 46a5831 erst auf
   Dispatcher-Nachfrage). Dazugehörige Erwartungs-Seite: eine
   SCHWEIGE-Erwartung ist nur so scharf wie die Menge der Meldungsformen,
   über die sie schweigt — feuert der Wächter unter dem Defekt eine
   ANDERE Form, bleibt sie erfüllt.
2. **Klasse:** Instrument-Arrangement — der BATTERIE-AUFRUF (Selektor,
   Abbruch-Flags, Fehlschlag-Auswertung) ist Teil des Instruments; jede
   Verengung (Namensfilter, First-Fail-Abbruch) macht eine Stille
   unlesbar, die von einem echten Pass nicht unterscheidbar ist
   (Geschwister der Devbook-Schritt-4-Klasse „ein grüner Biss braucht
   seine Arrangement-Prüfung").
3. **Vorformulierter Fix-Text** (Devbook guard-checker-bau, Schritt 4,
   EINE Ergänzung für beide Hälften): „Die Mutations-/Biss-Batterie läuft
   über die GANZE Testdatei, nie über eine `-k`-Namensauswahl und nie mit
   `-x`: der Selektor schließt sonst das fangende Fixture aus, und der
   First-Fail-Abbruch verdeckt, welche Arme nie feuern — beides liefert
   ein Grün/Rot, das vom echten nicht unterscheidbar ist. Wo die Frage
   die Zuordnung Defekt→Arm ist, wird die FEHLSCHLAG-LISTE je Mutation
   ausgewertet; eine Schweige-Erwartung nennt ALLE Meldungsformen des
   Wächters. Und die Mutation BEWEIST ihre Anwendung — das
   Mutations-Werkzeug zeigt den entfernten/ersetzten Text oder bricht
   hart ab, wenn das Muster nicht traf: eine grüne Batterie über einer
   nicht angewandten Mutation ist von einem toten Test nicht
   unterscheidbar (gemessen 2026-08-12/13, drei Lanes: -k e1 ·
   -x Nachtrag · 0×-Muster helfer-kopien)."
4. **Konsument + Abfluss-Naht:** nächste Amendierung des
   guard-checker-bau-Devbooks (dotfiles CLAUDE.md §Registered procedure)
   — mit anderen offenen Schritt-4-Ergänzungen bündeln, jede Amendierung
   setzt den Fingerprint zurück (eval-open).

### MERGE 2026-08-13 — 4. Vorfall, neuer Mechanismus derselben Klasse: der .pyc-Cache lässt einen Arm den Nachbarn nachplappern

FB-101-Zusatz (opus-emission-telemetrie, pbs-projekt): Mutation A2
zeigte exakt A1s Trefferliste — Python validiert .pyc über
(Quell-mtime in SEKUNDEN, Quell-GRÖSSE), und A1/A2 waren byte-gleich
groß (je 12253) und liefen 0,09 s auseinander; der zweite Lauf führte
A1s Bytecode aus. Ein Nachbar-Abklatsch sieht aus wie ein normales
Ergebnis; verraten hat ihn nur die zur Mutation unpassende Liste.
Behoben an einer Stelle (PYTHONDONTWRITEBYTECODE=1 + __pycache__-Purge
vor jedem Lauf; jeder Arm druckt seine Dateigröße mit); alle drei
Batterien der Lane unter der Sperre wiederholt, Ergebnisse
unverändert. Fix-Text-Ergänzung (in Slot 3 dieser Klasse
einzuarbeiten): „Der Batterie-Treiber sperrt den Bytecode-Cache
(PYTHONDONTWRITEBYTECODE=1 + __pycache__-Purge je Lauf) — zwei
Mutationen gleicher Dateigröße innerhalb derselben mtime-Sekunde sind
für den Cache ununterscheidbar, und der zweite Arm plappert sonst den
ersten nach, grün und unauffällig."

## 2026-08-12 — writer-claims: Claims einer GESCHLOSSENEN Lane feuern gegen die Nachfolge-Lane

1. **Vorfall + Basis:** Sequentielle Dispatches in derselben Arbeitskopie
   (pbs-abwaegung): Lane A (opus-abw-drei-waechter) sauber geschlossen —
   Bericht gebucht, Commits vom Dispatcher integriert+gepusht,
   Lane-Close-Nachricht gesendet. Lane B (opus-abw-sichtweite-austrag)
   editierte danach dieselbe Testdatei; der writer-claims-Hook meldete
   WARN („this lane would DENY") gegen den Claim der TOTEN Lane A
   (Claim-TTL überlebt die Lane-Schließung). Lane B verlor einen
   INTERIM-Bogen auf die Abklärung eines Phantom-Co-Writers; der Baum
   trug nachweislich nur ihre eigenen Änderungen (HEAD identisch, kein
   fremder uncommitteter Hunk — von Lane B selbst per git diff belegt).
2. **Klasse:** Lane-Lebenszyklus ↔ Claim-Lebenszyklus-Divergenz: das
   Claim-Register kennt nur die TTL, nicht das Buchungs-Ende einer Lane
   — ein toter Schreiber liest sich für den Nachfolger wie ein lebender
   (Fehlfeuer-Klasse; im DENY-Modus würde sie legitime Serien-Dispatches
   in derselben Arbeitskopie blockieren).
3. **Vorformulierter Fix-Text:** „Die Lane-Schließung RÄUMT die Claims:
   beim Booking des Closing-Reports gibt der Dispatcher die Write-Claims
   der Lane frei (Release-Verb am Claim-Register, Teil der
   §4-Spiegelpflicht neben Buchen+Mitteilen); alternativ akzeptiert die
   writer-claims-Lane eine Dispatcher-Attestierung ‚Lane geschlossen,
   Commits integriert bis <sha>' als Claim-Ende. Bis dahin gilt: ein
   Claim-Treffer einer Lane, deren Report gebucht und deren Commits im
   eigenen Base-SHA enthalten sind, ist ein TTL-Rest — prüfen per
   git diff gegen Base, nie per weiterem Warten."
4. **Konsument + Abfluss-Naht:** nächste dispatch-guards-Maintenance-
   Runde (writer-claims-Hook + §4-Wortlaut der Spiegelpflicht).

### MERGE 2026-08-13 — same class, opposite direction: a LIVE lane's claim, dismissed as dead

Second incident of the divergence this entry names, and it completes the pair.
The 2026-08-12 case was a DEAD lane's claim firing against a successor (a
false fire). This one is a LIVE lane's claim firing correctly against the
DISPATCHER, who then talked himself past it — the true-positive direction,
and the more expensive one, because the guard did its job and the human
overrode it with a wrong belief.

1. **Incident + basis:** the dispatcher extended a lane's ownership by
   message ("this extends your ownership until you report it") to add one
   test. The lane's previous closing report crossed that message in flight.
   The dispatcher read the report as final, grepped the file, found the test
   absent, and concluded the grant was closed — both halves false: the grant
   had just been extended, and a grep at one instant samples a moving state
   rather than establishing anything about a live writer. The dispatcher then
   edited both of the lane's exclusive files and committed by pathspec, which
   takes the whole working-tree state of the named paths and absorbed the
   lane's uncommitted work under the dispatcher's trailer.
   `writer-reservation-gate` had fired a WARN immediately before that commit,
   naming the lane as holder and stating in terms that a disjoint path set is
   no defence because the commit is what serializes. The dispatcher discharged
   it by reasoning "the lane reported, its grant is closed" — precisely the
   false belief. Evidence is the lane's own: it observed FOUR different states
   of its two exclusive files within minutes (its green run; foreign
   insertions; a run where a previously-undefined symbol had become defined; an
   import that had changed again), halted rather than committing a state it
   could not account for, and returned the question. That halt is why this is
   a misattribution and not a destroyed lane.
2. **Class:** unchanged — lane lifecycle vs claim lifecycle. What the pair adds
   is that the divergence bites in BOTH directions and that neither the gate
   nor the dispatcher can resolve it from what they can see: the registry knows
   the holder and the TTL, `git status` proves modification but never
   authorship (a lesson the consuming repo's own dev-loop already records), and
   only the DISPATCHER knows whether a lane is live — which is exactly the fact
   that was wrong here.
3. **Pre-formulated fix text** (extends this entry's existing proposal rather
   than replacing it): "The claim register tracks lane STATE, not just a TTL,
   and the dispatcher moves it: booking a closing report RELEASES the lane's
   claims, and extending a lane's ownership RE-ARMS them. Then a claim hit
   means what it says in both directions — a live holder, or nothing. Until
   that exists, the dispatcher rule is: an extension makes the lane live until
   it reports ON THE EXTENSION, and a crossed report does not close it; a grep
   or a `git status` is never the evidence that a writer has finished, because
   neither observes the writer. Where the guard fires and the dispatcher
   believes the holder is dead, the cheap discharge is to ASK the holder and
   wait for its answer — one message against an unrecoverable
   misattribution."
4. **Consumer + drain seam:** next dispatch-guards maintenance round, together
   with this entry's 2026-08-12 half — the release/re-arm verb is one change
   serving both directions, and shipping only the false-fire half would leave
   the expensive direction open.

## 2026-08-13 — a COMPACTED lane booked the dispatcher's own commit as its work

1. **Incident + basis:** three parallel sonnet lanes from a cache-fix session,
   one shared working copy. Lane C (`closures-in-live`) delivered its closing
   report and was told its lane was closed. The desk then found and fixed a
   defect the lane had SURFACED but correctly not fixed (a declared grade
   missing from the instrument's vocabulary), committing it as `9ad432a`.
   Lane C's own context was summarized around that moment. On resume it
   re-read the working tree, found the fix already present, and its closing
   report's slot (f) claimed `9ad432a` as its own commit — including a
   confessed write-boundary DEVIATION for touching a third test file that the
   dispatcher, not the lane, had touched. Both claims were false and neither
   party's memory settled it: the commit trailer did
   (`9ad432a` carries `Co-Authored-By: Claude Opus 5`, the dispatcher's;
   the lane's two real commits `6ee63de`/`850f273` carry `sonnet-5`).
   Second half of the same incident, same lane: it also committed AFTER its
   report was booked and after the lane-close message — and the lane-close
   message is itself what RESUMED it.
2. **Class:** post-compaction provenance drift. An agent's slot (f) is written
   from memory of what it did, while the working tree shows what EXISTS — and
   after a summarization those two diverge silently in a shared copy. The
   report form asks for "files touched + commit hashes" as if the agent were
   the only writer, which is exactly false on a shared copy. Note the failure
   direction: it manufactured a deviation CONFESSION for work it did not do,
   so a dispatcher grading reports by trust would have booked a phantom
   boundary violation against a lane that never committed one.
3. **Pre-formulated fix text:** "Slot (f) is established from the RECORD, not
   from memory: the agent reports the commits whose trailer carries ITS OWN
   model name (`git log --format='%h %(trailers:key=Co-Authored-By)'`
   filtered to its own), and a commit it cannot claim by trailer is reported
   as 'present in the tree, not mine'. On a shared working copy this is
   mandatory, since the tree carries co-writers' work by construction. The
   mirror duty on the dispatcher: grade slot (f) against the trailer before
   booking it — an agent's claim to authorship is a claim like any other, and
   the trailer is the cheap disproving probe. Corollary for the lane-close
   message: closing a lane RESUMES it, so the close text must say 'do not
   edit; a defect found later is REPORTED' explicitly, or the close is itself
   the trigger for the post-report write it forbids."
4. **Consumer + drain seam:** next dispatch-guards maintenance round — §2 report
   form (slot f wording) and §4 mirror duty (grading slot f; close-message
   wording).

## 2026-08-13 — Ein global eingehängter Check-Schritt läuft in JEDEM Test: Fail-Loud über repo-externe Artefakte kollidiert per Konstruktion mit Temp-Fixtures

1. **Vorfall + Basis:** Dispatch `opus-helfer-kopien` (FB 3.89, Session
   ddd83862): Der Brief entschied „Skript fehlt → FEHLER, nie still" für
   einen global in `pruefe()` eingehängten Wächter, der ein Skript im
   office_repo und Helfer in zwei Nachbar-Repos liest. Spec-treu gebaut:
   119 von 818 Tests rot, weil jede Temp-Fixture (`mach_office`) ein
   office_repo OHNE tools/ baut und dev_root auf einen leeren Temp-Baum
   zeigt. Executor-STOPP mit drei GEMESSENEN Wegen (A Fixture-Chirurgie
   +17 s Suite; B durchgängig HINWEIS; C gemischt 2 failed/816 passed);
   Desk-Entscheid Weg C. Das Repo hatte die Klasse laut dreier
   conftest-Kommentare („ohne trüge JEDER Graph-Test den HINWEIS")
   vorher schon dreimal getroffen — die Brief-Komposition las diese
   Präzedenz nicht.
2. **Klasse:** Brief-Komposition für global eingehängte Wächter mit
   repo-EXTERNEN Artefakten. Der Fail-Loud-Kontrakt wird am
   Produktions-Bild entschieden, aber der Schritt läuft zuerst und
   tausendfach in der TEST-Umgebung, deren Fixtures die externen
   Artefakte per Konstruktion nicht stellen — der Abwesend-Fall des
   Wächters IST der Normalfall der Fixtures.
3. **Vorformulierter Fix-Text** (Devbook guard-checker-bau,
   Brief-Kompositions-Schritt): „Hängt der Wächter global in einen
   Lauf, der auch unter Tests steht, beantwortet der Brief VOR dem Bau:
   Was sieht dieser Schritt in der Test-Umgebung (Fixtures gelesen,
   nicht vermutet)? Für jeden repo-externen Anker (Nachbar-Repo,
   Konfig-Pfad, Werkzeug-Skript) trägt der Brief die entschiedene
   Grade des Abwesend-Falls — Fail-Loud nur dort, wo die Umgebung den
   Anker garantiert stellt; sonst die sichtbare Degradations-Grade
   (HINWEIS-Zeile je Lauf) MIT eigenem gepinntem Test. Die Präzedenz
   im Ziel-Repo (conftest-Kommentare, Geschwister-Schritte) ist
   Pflicht-Grounding der Brief-Komposition."
4. **Konsument + Abfluss-Naht:** nächste Amendierung des
   guard-checker-bau-Devbooks (dotfiles CLAUDE.md §Registered
   procedure) — mit den offenen Schritt-4-Ergänzungen bündeln;
   Amendierung setzt den Fingerprint zurück (eval-open).

## 2026-08-13 — Grad-Assertionen über den GANZEN Report unterscheiden die Grade nicht; mehrzeilige Durchreichungen tragen die Marke nur in Zeile 1

1. **Vorfall + Basis:** FB-102-Bau (opus-emission-telemetrie,
   pbs-projekt ende_check): Die Mutation „Exit!=0-Grad WARNUNG →
   HINWEIS" lief im ersten Batterie-Durchgang GRÜN durch (34 passed) —
   die Assertion prüfte `"WARNUNG" in out` über den Gesamtreport, und
   dort stand ohnehin eine WARNUNG eines anderen Checks. Erst ein
   Helfer, der den Telemetrie-EINTRAG isoliert (genau einer, sonst
   Abbruch) und den Grad an der eigenen Zeile prüft, machte alle sechs
   Mutationen bissig. Zweiter Fund im selben Bau: die durchgereichte
   Report-Ausgabe ist MEHRZEILIG, die Marke (`[telemetrie]`) steht nur
   in Zeile 1 — ein Leser, der „die Meldung" nimmt, schneidet die
   Befundzeilen stumm ab, und die Durchreich-Prüfung wird stumpf, ohne
   rot zu werden (betrifft auch den Helfer-Kopien-Präzedenzfall).
2. **Klasse:** Assertions-Schärfe in Report-Gattern — ein Prädikat,
   das am AGGREGAT prüft, ist von jedem anderen Check erfüllbar
   (dieselbe „beide Ausgänge erfüllen"-Klasse wie im Fixing-Korpus,
   hier als Report-Instanz), und Marken-Konventionen (Marke nur am
   Blockanfang) machen Ein-Zeilen-Leser still unvollständig.
3. **Vorformulierter Fix-Text** (Devbook guard-checker-bau, Schritt-4-
   Ergänzung): „Grade werden an ihrer EIGENEN Zeile geprüft, nie am
   Report — der Test isoliert den Eintrag des geprüften Schritts
   (genau einer, sonst Abbruch) und prüft Grad + Inhalt dort. Reicht
   ein Schritt einen mehrzeiligen Block durch, liest der Test den
   BLOCK bis zu seiner Endmarke, nie nur die markierte erste Zeile."
4. **Konsument + Abfluss-Naht:** nächste Amendierung des
   guard-checker-bau-Devbooks (dotfiles CLAUDE.md §Registered
   procedure) — mit den dort schon wartenden Schritt-4-Ergänzungen
   bündeln; Amendierung setzt den Fingerprint zurück (eval-open).

## 2026-08-14 — Ein gebrieftes Randbeispiel als Pflicht-Assertion pinnt die Spec, nicht den Defekt

1. **Vorfall + Basis:** FB-103-Bau (opus-befund-referenz,
   pbs-abwaegung b213761): Der Brief gab das durchgerechnete
   Randbeispiel BF22/BF2 als Pflicht-Assertion vor („Dokument enthält
   nur `% BF22` → BF2 gilt NICHT als referenziert"). Die Assertion
   ging unter der korrekten Lookaround-Regex UND unter der naiven
   `BF([0-9]+)` gleich aus — Regex-Gier ersetzt die Lookarounds im
   Beispiel-Fall. Diskriminierend war erst die Zeichen-Nachbarschaft
   (`\labelBF2`, `ABF2`); gefunden hat es die Mutations-Batterie des
   Executors (M1 überlebte den Erstlauf), nicht die Vorgabe.
2. **Klasse:** Instrument-Diskriminierung am Brief-Seam — dieselbe
   „beide Ausgänge erfüllen"-Klasse (Fixing-Korpus), hier als
   BRIEF-Instanz: eine vom Dispatcher vorgegebene Pflicht-Assertion
   erbt die Elternschaft der Spec und kann den Defekt, gegen den das
   Prädikat gebaut ist, systematisch verfehlen; sie liest sich dabei
   als Rigor.
3. **Vorformulierter Fix-Text** (Dispatch-Skill §1, Klausel
   „Criteria state OUTCOMES first" oder D5-Spec-Check Nr. 1,
   Ergänzungssatz): „Gibt der Brief ein Randbeispiel als
   Pflicht-Assertion vor, verlangt er dazu eine Assertion, die die
   vorgegebene Implementierung von der NAIVEN trennt (ein Fall, den
   beide verschieden beantworten) — sonst pinnt die Pflicht-Assertion
   die Spec, nicht den Defekt; die Mutations-Batterie bleibt der
   Nachweis."
4. **Konsument + Abfluss-Naht:** nächste Maintenance-Runde des
   Dispatch-Skills (SKILL.md §1 bzw. DEV-RUNBOOK D5 Nr. 1 im
   pbs-office opus-paket — EINE Heimat wählen, Kante im jeweils
   anderen); Quota-Drain nach OBSERVATIONS-Regel.

## 2026-08-14 — grep auf PDF ist ohne `-a` still blind; Struktur-Checks brauchen den dekomprimierten Strom

1. **Vorfall + Basis:** FB-6.18-Mechanik (sonnet-anhang-verlinkung):
   die PDF-Link-Verifikation per `grep '/Subtype /Link'` lieferte
   einen Nulltreffer, weil grep die Datei als Binär einstufte — auch
   für sicher vorhandene Strings wie `/Type` (das war die
   Positiv-Kontrolle, die die Blindheit aufdeckte). Tragfähig wurde
   der Check erst mit `qpdf --qdf --object-streams=disable` (Ströme
   dekomprimieren) plus `grep -a`.
2. **Klasse:** Zero-Hit-Suche mit totem Instrument (Fixing-Korpus,
   Non-Events) — die Binär-Einstufung ist ein Instrument-Killer, der
   exakt das Ergebnis einer echten Absenz liefert; PDF-Objektströme
   sind der zweite, unabhängige Killer derselben Prüfung.
3. **Vorformulierter Fix-Text** (executor skill, Verifikations-
   Abschnitt, ein Satz): „Ein Struktur-Grep über ein PDF (oder
   anderes Binärformat) zählt nur mit gezeigter Positiv-Kontrolle im
   selben Aufruf-Modus; für PDFs heißt das dekomprimieren
   (`qpdf --qdf --object-streams=disable`) und `grep -a` — ein
   Nulltreffer ohne Positiv ist keine Absenz-Aussage."
4. **Konsument + Abfluss-Naht:** nächste Maintenance-Runde des
   executor-Skills (Verify-with-the-check's-own-output-Abschnitt);
   Quota-Drain nach OBSERVATIONS-Regel.

## 2026-08-14 — Report-Buchung prüft den ABSENDER nicht: unaufgeforderte Fremd-Nachricht erreichte einen wartenden Dispatcher

1. **Vorfall + Basis:** Während einer Drei-Arm-Probe zum Subagent-
   Spawn-Cap (dotfiles LEDGER 2026-08-14, Commit 4a40404) empfing
   eine headless Dispatcher-Session, die auf den Report ihres einen
   Subagenten wartete, eine unaufgeforderte Nachricht mit plausiblem
   Ergebnis-Inhalt (`FORK-PROBE-EXECUTED`) von einer Absender-ID, die
   KEINEM von ihr gestarteten Agenten entsprach — plausibel der
   Hintergrund-Fork einer VORIGEN Probe-Session, der nach deren Ende
   zustellte (Cross-Session-Zustellung; Provenienz nicht
   diagnostiziert). Der Dispatcher verwarf sie aus eigenem Urteil,
   per Namensabgleich gegen seine Dispatch-Liste — keine Regel im
   Skill deckt diesen Abgleich.
2. **Klasse:** Report-Attribution — die Absender-Identität eines
   eingehenden Reports ist eine Prämisse, die nichts prüft. §4 deckt
   „Schweigen ist nie Erfolg" und den Erwartungs-Horizont, aber ein
   INHALTLICH passender Report vom FALSCHEN Absender bucht sich durch:
   er beantwortet scheinbar den offenen Horizont und beendet das
   Warten auf den echten.
3. **Vorformulierter Regel-Text** (dispatch skill §4, beim
   Horizont-Absatz): „Ein eingehender Report wird erst gebucht,
   nachdem sein Absender gegen die eigene Dispatch-Liste aufgelöst
   ist (Agent-ID oder Brief-Name); ein Report von nicht aufgelöstem
   Absender ist ein BEFUND (Cross-Talk), nie ein Report — er schließt
   keinen offenen Horizont, und das Warten auf den echten Report
   läuft weiter."
4. **Konsument + Abfluss-Naht:** nächste dispatch-guards-
   Maintenance-Runde, oder der nächste Bau an §4; Quota-Drain nach
   OBSERVATIONS-Regel.

## 2026-08-14 — Fork-Skills sind der Rest-Spawn-Kanal unter dem Cap, und ein Fork ist per Konstruktion Selbst-Review

1. **Vorfall + Basis:** Dieselbe Drei-Arm-Probe (dotfiles LEDGER
   2026-08-14, Commit 4a40404) maß: unter
   `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1` verliert ein Subagent das
   Agent-Tool hart und laut („No such tool available: Agent…"), aber
   ein `context: fork`-Skill, den der Subagent aufruft, forkt WEITER
   und liefert („completed (forked execution)"). Kein Fehlverhalten
   beobachtet — der Kanal ist nur offen, und niemand hat ihn je
   gegradet.
2. **Klasse:** Verifikations-Etikett — ein Fork erbt den VOLLEN
   Kontext seines Aufrufers und ist damit per Konstruktion keine
   frische Verifikation (er erbt die blinden Flecken mitsamt der
   Rahmung); die Cap-Mechanik schließt den Kanal nicht, also kann ein
   Executor über einen Fork-Skill etwas erzeugen, das im Report als
   unabhängige Prüfung AUSSIEHT.
3. **Vorformulierter Regel-Text** (Grading-Seite, dispatch skill §2,
   beim Fresh-Context-Bezug; Spiegel im executor-Skill denkbar, ein
   Fakt eine Heimat — Heimat entscheidet der Pass): „Ein
   `context: fork`-Skill erbt den vollen Kontext seines Aufrufers;
   eine darüber erzeugte Prüfung ist Selbst-Review und wird so
   gegradet, nie als Fresh-Context-Verifikation. Der
   Subagent-Spawn-Cap schließt diesen Kanal nicht (gemessen
   2026-08-14)."
4. **Konsument + Abfluss-Naht:** nächste dispatch-guards-
   Maintenance-Runde (Grading-Abschnitt §2); Quota-Drain nach
   OBSERVATIONS-Regel.

## 2026-08-14 — Die Re-Lese-Einheit eines gespeicherten Briefs ist der Eintrag PLUS seine Nachbarn: eine Um-Bewertung steht oft im BENACHBARTEN Bullet

1. **Vorfall + Basis:** Dispatch aus einer cache-fix-Session
   (2026-08-14, Basis 52b8912): ein Brief zitierte einen
   BACKLOG.md-Eintrag wörtlich aus der AKTUELLEN Datei zur
   Compose-Zeit — §1s Stored-Brief-Klausel („re-read a stored
   brief's premises against the current world") also dem Buchstaben
   nach erfüllt. Der Eintrag war trotzdem längst geschlossen: die
   Schließung stand fünf Zeilen darüber in einem EIGENEN Bullet
   (BACKLOG.md:3513-3517, „MECHANISM HALF DONE 2026-08-11
   (`d6647cc`)" … „PROCEDURE half: DONE separately" … „Original
   entry follows, RE-GRADED rather than left at READY"), während
   das Original-Bullet (:3518) seinen `READY`-Kopf behielt. Der
   Dispatcher-Extraktor splittete auf der Bullet-Grenze
   (`^- \*\*`) und lieferte genau EIN Bullet — die Um-Bewertung lag
   außerhalb der Sicht. Kosten: eine Sonnet-Lane (~170k Tokens),
   die korrekt NICHTS baute; der Mechanismus (`lintCaptureAliases`,
   tools/backlog-lint.mjs:1595) war seit d6647cc (2026-08-11)
   fertig samt 10 Tests. Zweitschaden: derselbe lebende `READY`-Kopf
   hob den Eintrag auf Rang 3 einer Build-Order-Ableitung.
2. **Klasse:** Re-Lese-EINHEIT unbenannt + selbstgebaute Sicht. §1
   sagt WAS neu zu lesen ist, nie in welchem UMFANG — und weil eine
   Um-Bewertung häufig als benachbarter Datensatz geschrieben wird
   statt als In-Place-Edit, ist „der Eintrag" die falsche Einheit.
   Darunter die Grounding-Klasse: der Extraktor IST das Instrument,
   seine Grenzwahl ist die Basis der Behauptung „ich habe den
   Eintrag gelesen" — und Extrahieren präsentiert sich als SCHAUEN,
   nicht als Messen, also fragt nichts nach dem diskriminierenden
   Beleg.
3. **Vorformulierter Regel-Text** (§1, brief family / stored
   brief): „Die Re-Lese-Einheit eines gespeicherten Briefs ist der
   Eintrag PLUS seine Nachbarn, nie das Bullet allein: eine
   Um-Bewertung wird häufig als BENACHBARTER Datensatz geschrieben,
   nicht als In-Place-Edit, und der ursprüngliche Kopf behält dann
   seinen lebenden Grad. Besitzt das Ziel-Repo eine eigene
   Closure-/Stale-Prüfung, läuft sie über den Eintrag, BEVOR der
   Brief rausgeht; sonst werden die Bullets davor und danach
   mitgelesen. Ein selbst gebauter Extraktor ist dabei das
   Instrument — seine Grenzwahl ist die Basis, nicht seine Ausgabe."
4. **Konsument + Abfluss-Naht:** nächste dispatch-guards-
   Maintenance-Runde (§1, brief-family-Klausel); Quota-Drain nach
   OBSERVATIONS-Regel.

## 2026-08-14 — Die Harness-Sperre gegen Report-Dateien griff einen deutschen Namen nicht: `*-bericht.md` schrieb sich durch

1. **Vorfall + Basis:** Discovery-Dispatch `sonnet-ready-inventar`
   (READY-Inventar über pbs-office FEATURE-BACKLOG.md, 14.08.). Der
   Brief trug den READ-ONLY-Tail wörtlich („never a report file") UND
   wies eine Datendatei zu. Der Agent legte zusätzlich
   `ready-inventar-bericht.md` an — 6011 Bytes, erfolgreich
   geschrieben, vom Dispatcher am Dateisystem bestätigt. Die
   Harness-Sperre, die laut forms.md §2 „REPORT.md and kin" mit
   „return findings as text" abweist, hat diesen Schreibvorgang nicht
   abgewiesen. Zweite Abweichung derselben Lane: die Datendatei landete
   im Scratchpad des DISPATCHERS statt im eigenen, obwohl der Brief
   „dein EIGENER Scratchpad" zuwies.
2. **Klasse:** Reichweite einer MECHANISCHEN Sperre, auf die ein
   Prosa-Tail sich stillschweigend stützt. GEMESSEN ist ausschließlich,
   DASS dieser Name durchging — worauf die Sperre keyed (englisch
   geformtes Muster? feste Basename-Liste? Pfad-Form?), ist unbelegt
   und gehört deshalb nicht in den Fix-Text. Die Folge steht unabhängig
   von der Ursache: in einem Brief mit nicht-englischer Arbeitssprache
   ist die Sperre kein Rückfall, und „never a report file" ist dort
   allein prosa-durchgesetzt. Schaden hier gering (die Daten waren
   korrekt), aber die Kontext-Ökonomie, die die Regel schützt, war
   umgangen — und forms.md zitiert die Sperre als Binding, also als
   etwas, worauf ein Brief sich verlassen darf.
3. **Vorformulierter Regel-Text** (forms.md §2, Harness-Binding-Absatz
   zur Report-Datei-Sperre): „Die Sperre ist an EINEM Namensraum
   gemessen (`REPORT.md` und nahe englische Verwandte). Für einen Brief
   in anderer Arbeitssprache ist sie KEIN Rückfall — ein deutsch
   benanntes `*-bericht.md` schrieb sich am 2026-08-14 durch. Wo die
   Arbeitssprache nicht englisch ist, benennt der Brief die zugewiesene
   Datendatei als EINZIGEN erlaubten Schreib-Pfad und sagt ausdrücklich,
   dass jede weitere Datei — gleich wie benannt — eine Abweichung ist."
4. **Konsument + Abfluss-Naht:** nächste dispatch-guards-
   Maintenance-Runde (forms.md §2, Harness-Binding-Absatz); Quota-Drain
   nach OBSERVATIONS-Regel.

## Abgeflossen

Angewandte oder verworfene Einträge, mit Beleg — ein Fakt,
eine Heimat. Der Eintrag WANDERT hierher, er bleibt nicht
durchgestrichen oben stehen.

### ANGEWANDT 2026-08-15 — Provenance-Grade bindet an die Behauptungs-KLASSE, nicht an die Zitat-Form

**Vorfall + Basis:** Peer-Relay, dritter Brief-Defekt derselben
Welle, gleiche Wurzel, NEUER Slot: das settled design schrieb
„Enum-Typ additiv", ohne den Konsumenten zu lesen — das Zielmodul
hält ein geschlossenes, wächter-getestetes Dict über den Enum, der
nackte Wert hätte Wächter plus Laufzeit-KeyError gerissen. Der
Executor meldete die Lücke statt zu überbrücken (die Box hielt —
das ist die Positiv-Seite und gehört zur Basis).
Zusammen mit den zwei vorher relayten (Base-Pin vom Vortag statt am
Tip gelesen; Commit-Plan-„none" ohne Hook-Pfad) sind das drei
Slots, eine Wurzel.

**Triage:** dreimal loaded-but-inert, KEIN Gap. §1 trug die Regel
bereits — und trug sogar schon die Verallgemeinerung in der
Fettung („the grade follows the CLAIM, never the section holding
it").

**Mechanismus des Nicht-Feuerns**, hier am Quelltext geprüft statt
aus dem Relay übernommen: die Fettung verallgemeinert, der
OPERATIVE Satz verengt wieder — „each cited line is either OPENED
…". Die Regel band damit lexikalisch an die ZITAT-Form, während
die teuersten Fälle Repo-Behauptungen im DESIGN-Kostüm sind. Ein
Design-Satz, ein Base-Pin, ein ausgefülltes Formularfeld
präsentieren als ENTSCHEIDUNG des Dispatchers — und Entscheidungen
werden ausgeführt, nicht geprüft. Genau das Kostüm-Prinzip des
Korpus, eine Ebene tiefer: was gebunden wird, entscheidet die
Behauptung; was geprüft wird, entscheidet die Präsentation.

**Angewandt** auf §1: die Fettung nennt jetzt auch die FORM
(„never the section or the FORM holding it"), der operative Satz
bindet an die Klasse statt an die Form („every line asserting the
target repo's CURRENT STATE — in whichever slot, wearing whichever
form"), und ein Satz benennt das Kostüm samt der drei beobachteten
Träger, de-partikularisiert. Der 0.10.23-Slot-Basis-Zusatz wird
darin als Spezialfall QUELL-ETIKETTIERT statt ein zweites Zuhause
zu eröffnen — Verallgemeinerung nach oben, wie die
Amendment-Disziplin sie vor dem Anbau verlangt.

**Reihenfolge-Selbstkritik, fürs Protokoll:** ich habe erst die
Instanz gebaut (0.10.23, Commit-Plan-Slot) und dann das Prinzip —
die Disziplin will es umgekehrt („generalize upward BEFORE
appending"). Kein Schaden, weil die Instanz unter dem Prinzip
gültig bleibt; die Lehre ist, dass drei Relays derselben Wurzel
das Prinzip schon sichtbar machten, als der erste ankam, und ich
den ersten für ein Einzelstück hielt.

**Kein Hook:** ob eine Zeile eine Repo-Behauptung ist, ist
Urteil, nicht Prädikat.

**Beleg:** dieser Commit.

### ANGEWANDT 2026-08-15 — Commit-Plan-Slot trägt seine Lese-Basis

**Vorfall + Basis:** Peer-Relay aus der Georgendorf-Welle (Session
-84), zwei eigene Brief-Defekte, von ihr selbst trianguliert und am
Artefakt belegt: (a) der Commit-Plan-Slot für pbs-website mit „none"
gefüllt, ohne den Hook-Pfad zu öffnen — das Repo trägt einen
commit-msg-Hook über `core.hooksPath`, die Lane bounced; (b) ein
Base-Pin aus einem Vortags-Brief übernommen statt am Tip gelesen,
zwei Commits drüber, der Executor hielt korrekt am Gate.
Rezitations-Prüfung hier: beide zitierten §1-Klauseln wörtlich
bestätigt.

**Triage (Relay, hier geprüft und geteilt):** loaded-but-inert, KEIN
Gap. §1 verlangt beides bereits wörtlich — „commit-blocking guards,
READ at compose time" und Background-Zeilen „grepped by the
DISPATCHER before the brief ships".

**Mechanismus des Nicht-Feuerns**, der den Sharpen trägt: die
Klausel „'none' is a valid filling; silence is not" legitimiert das
WORT, ohne seine Basis zu verlangen. Ein ungelesen hingeschriebenes
„none" ist von einem gelesenen lexikalisch ununterscheidbar — der
fakeable-evidence-Spalt, den skill-craft für „checked all edge
cases" beschreibt, hier im Brief-Formular.

**Angewandt** auf SKILL.md §1, als KONSOLIDIERUNG statt Anbau, weil
es die zweite Amendment am selben Slot an einem Tag war: der Slot
verlangt jetzt die LESE-BASIS je Guard („none (hooks path read:
core.hooksPath=hooks, empty)"), und die doppelt geführte Mechanik
(Payload-Guard-Sequenzierung) verließ den Slot in Richtung des
Regel-Bullets, wo sie ohnehin ausführlich steht. Netto 80 → 78
Wörter im Slot bei mehr Abdeckung — Pareto erfüllt statt behauptet.
Der Grund steht im Regel-Bullet, nicht im Formular: ein Formular
sagt, was auszufüllen ist, kein Formular lehrt.

**Kein Hook-Kandidat:** ob gelesen wurde, ist nicht komputierbar.
Die Basis-ANGABE wäre greppbar, falls brief-reminder je darauf
linten soll — als Kandidat notiert, nicht gebaut (der Slot ist
gerade erst gemintet; eine Lane, die auf einen Tag alten Text
lintet, feuert auf jeden Altbestand).

**Beleg:** dieser Commit.

### ANGEWANDT 2026-08-15 — Bump-Push-Lage im Commit-Plan

Slot-3-Text angewandt auf SKILL.md §1, beide Heimaten: der
Commit-Plan-Absatz (Regel + gemessener Vorfall) und der
Skeleton-Slot (`where the bump ... sits AND whether it is
pushed`). Umgesetzt statt zitiert: der Zusatz benennt den
MECHANISMUS, den Slot 1 selbst herleitet — die Ausnahme ist
auf den ungepushten Batch gekeyed, also kann die Lane die
Bedingung ihrer eigenen Commits nicht prüfen, und der
Dispatcher, der die Prämisse schrieb, ist derselbe, der sie
durch Pushen tötet. Triage laut Eintrag: loaded-but-inert,
kein Gap — daher Sharpen am bestehenden Absatz, nicht neuer
Bullet (amendment over addition).

Beleg: dieser Commit; Eintrag im Wortlaut darunter.

## 2026-08-15 — Bump-Ausnahme vom Dispatcher-Push konsumiert (statiker-Ernte-Lane)

1. **Vorfall + Basis:** Der Lane-Brief (statiker,
   docs/directives/2026-08-15-harvest-lane-brief.md) erklärte „no
   bump is yours — the dispatcher has already landed the version-bump
   commit". Der Dispatcher pushte den Bump (0.2.61, eb1cc9b) aber VOR
   dem Dispatch. Der Payload-Guard (dotfiles pre-commit,
   unbumped_plugins) keyed seine Ausnahme auf UNGEPUSHTEN Batch:
   origin trug 0.2.61 bereits, also verweigerte er beide
   Payload-Commits der Lane; die Lane haltete korrekt (kein
   --no-verify) und die Auflösung kostete einen vollen
   Directive-Roundtrip (Bump-Ownership nachträglich an die Lane,
   0.2.62 als eigener Commit 8b3438e). SKILL.md §1 (Commit-Plan)
   benennt die Klasse bereits: „a mid-batch push moves the basis and
   re-arms the guard … the dispatcher pushes at integration only" —
   der Miss war Anwendung, nicht Regel-Lücke. Aber der BRIEF-Slot hat
   keinen Platz, an dem die Push-Lage des Bumps sichtbar würde.
2. **Klasse:** Brief-Prämisse über den Guard-Zustand, die zwischen
   Brief-Schreiben und Ausführung vom Dispatcher selbst getötet wird —
   Spezialfall der stale-premise-Klasse, hier mit dem Dispatcher als
   beiden Seiten (er schrieb die Prämisse UND beging den Push).
3. **Vorformulierter Regel-Text** (SKILL.md §1, Commit-Plan-Skeleton-
   Slot, ein Zusatz-Satz): „Wo der Dispatcher den Bump vorab landet,
   nennt der Commit-Plan auch dessen PUSH-Lage — ‚bump committed,
   UNPUSHED (exemption armed)' — und der Dispatcher pusht ihn nicht
   vor der Integration; ein Brief, der nur ‚bump already landed' sagt,
   lässt die Lane die Ausnahme-Bedingung erraten."
4. **Konsument + Abfluss-Naht:** nächste dispatch-guards-
   Maintenance-Runde (SKILL.md §1 Commit-Plan-Absatz); Quota-Drain
   nach OBSERVATIONS-Regel.

## 2026-08-15 — Worktree-Entfernung verbrennt den Resume-Kanal (statiker E-Lane-Batch)

1. **Vorfall + Basis:** Nach Buchung von Lane Gs Report entfernte der
   Dispatcher zuerst den Worktree (`git worktree remove --force`)
   und sandte DANACH die Lane-Close-Nachricht (§4 Spiegel-Pflicht).
   Die Harness verweigerte die Zustellung: "cannot be resumed: its
   worktree no longer exists, and the fallback directory is not
   covered by the session's isolation fences" (SendMessage-Fehler,
   wörtlich). Ausgang hier benign (Report vollständig gebucht,
   Integration fertig, Schreibrisiko strukturell null), aber der
   Kanal ist irreversibel zu: auch eine legitime NACHFRAGE an die
   Lane (Interrogation eines gebuchten Reports — im Ziel-Repo
   ausdrücklich als billige Mint-Quelle gewertet) ist ab der
   Entfernung unmöglich.
2. **Klasse:** Reihenfolge zweier Dispatcher-Pflichten, deren zweite
   die erste irreversibel unerfüllbar macht — §1-Worktree-Rezept
   ("remove the worktree after integration") und §4-Spiegel-Pflicht
   ("book the report AND tell it the lane is closed") nennen beide
   Akte, aber keine Sequenz; die Harness-Bindung (Resume setzt den
   Worktree voraus) steht in keinem der beiden.
3. **Vorformulierter Regel-Text** (§1 Worktree-Rezept, Removal-Satz —
   Amendment, kein neuer Bullet): "Removal ist der TERMINALE Akt und
   schließt den Resume-Kanal des Agenten (Harness-Bindung, gemessen
   2026-08-15: SendMessage an einen Agenten ohne Worktree wird
   verweigert). Reihenfolge daher: Report buchen, Lane-Close senden,
   offene Nachfragen an die Lane stellen — DANN entfernen. Ein
   entfernter Worktree ersetzt die Close-Nachricht strukturell
   (der Agent kann nicht mehr schreiben), aber er ersetzt keine
   Nachfrage, und die ist das teure verlorene Stück."
4. **Konsument + Abfluss-Naht:** nächste dispatch-guards-
   Maintenance-Runde (SKILL.md §1 Worktree-Rezept; §4-Spiegel-Satz
   prüfen, ob ein Querverweis genügt); Quota-Drain nach
   OBSERVATIONS-Regel.
