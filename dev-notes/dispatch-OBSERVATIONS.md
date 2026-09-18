# Dispatch observations — gaps noticed in use

Per the dispatch skill's "Evolution and maintenance": a dispatch failure the
discipline should have prevented, or a rule it states wrongly, gets written here
with its evidence, and the rule change proposed. Not a changelog — each entry is
a measured incident.

## Abgeflossen

Applied or dropped entries, with evidence — one fact, one home.
The entry MOVES here; it does not stay struck through up top.

Structural addendum, 2026-08-17, corrected twice the same day:
this section originally sat in the MIDDLE of the file while new
entries grew at the tail — five live entries read, by their
position, as drained. The first fix pushed it to the file's END
and merely inverted the bug: a foreign session appended at EOF
within the hour and landed IN the drained section. Now drained
entries sit AT THE TOP and the live list at the file's end, where
appends land; `check_observations_tail` (tools/check-doc-drift.py)
pins that order. This very paragraph was itself wrong for one
commit — it kept describing the first fix after the second had
reversed it: a label outliving its own body, in the very file
whose pass is about exactly that. Found by the fresh-context
round, by no check.


### ANGEWANDT 2026-08-27 (Lane `opus-a-skill-amendments`, wave 4)
### — a dispatcher GRANT issued on the executor's LABEL

Booked in `f123de0`, applied in this wave: the pre-formulated
text stands in `plugin/skills/dispatch/SKILL.md` §1, at the end
of the per-line provenance bullet — the grant rendered as a
repo-state claim in a ruling's costume, with the
conditional-grant form and the refusal-graded-as-correct
sentence quoted across. De-particularized on landing per the
maintenance doctrine (provenance: no dates, no named
artifacts, no occasion counts in the corpus text). Entry body
below, unchanged.

**Incident + basis.** A peer desk's step-0 digest called a leak-scan
run over `..HEAD` "DEGRADED" (the scanner printed a `degraded:` line
because the base ref was empty). The judgment desk granted a one-line
edit to the plugin's laws file replacing `..HEAD` with `<base>..HEAD`.
The peer checked the scanner's `--help` before editing: an EMPTY base is
the documented form ("<old> may be EMPTY"), two tests pin it, both green
at the base sha. The granted edit would have NARROWED a full-tree scan
of the publication guard to a range scan. Not executed; grant withdrawn
on the peer's evidence (`dotfiles-2f`, lifecycle `4283d61`).

**Class.** The definitions rule (corpus, Fixing) at the DISPATCHER's
end: a wrongness claim asserts a deviation from the artifact's
definition, and here the "wrongness" arrived as a status word in a
digest — a label over a body the desk never opened. The costume is the
GRANT: it presents as a decision (executed, not graded) while it is a
repo-state claim wearing a ruling, so nothing prompted the read. The
executor's own definition-check is what saved the check; an executor
briefed to obey would have shipped it.

**Pre-formulated rule text** (skill §4, dispatcher duties, or §1
provenance): a ruling that AUTHORIZES an edit on the strength of a
report's characterization of an artifact ("degraded", "broken",
"stale") is a repo-state claim and takes the provenance grade — the
desk opens the artifact's definition (its --help, its tests, its
docstring) or grants conditionally: "if the definition agrees; if not,
report and do not edit". The peer's refusal-with-evidence is the
correct executor behaviour and is graded as such, never as a deviation.

**Consumer + drain seam.** The next dispatch-skill maintenance pass;
n=1, the executor caught it.

### ANGEWANDT 2026-08-27 (Lane `opus-a-skill-amendments`, wave 4)
### — the class devbook pin is the SECTION's sha256

Booked in `771b4a8`, corrected in `da64e10` (the pin is the
section sha256, not the whole-file blob), second half amended
in `1078183` (the injection-vs-file two-channel divergence);
applied in this wave to `plugin/skills/dispatch/SKILL.md` §1,
appended to the readiness-register consult bullet. The §6 half
of the text ("the register's probe-evidence line records that
sha") rides in the same §1 sentence rather than being restated
in §6 — one meaning, one home. Entry body below, unchanged.

**Incident + basis.** Wave-3 lane A was dispatched at 11:28:59 with
the guard/checker devbook named by path (dotfiles `CLAUDE.md`); the
judgment desk amended that devbook's step 4 at 11:30:48 (`05ebcf4`),
on lane C's finding. Lane A's grounding read falls inside the
109-second window either way. The desk asked the lane a question it
can answer without re-reading (did the passage it read contain the
new paragraph's opening words); absent an answer the register line
reads UNDETERMINED with both timestamps — never the plausible
inference. Lane C (earlier, `120c733`) ran under the pre-amendment
text, certain: the amendment exists because of what it measured.

**Class.** The register (§6) stores a fingerprint taken at
certification; a probe's brief names the devbook by path, which the
lane resolves LIVE — the same live-on-write property the corpus
records for hook files. "Which text did this probe run under" is
therefore not answerable from the register, only from timing
evidence gathered while the lane is alive, and a re-probe priced
against the wrong text is the invalidation clause silently defeated.

**Pre-formulated rule text** (§1 brief, §6 register): a brief under a
registered class names the class devbook SECTION's sha256 beside its
path — computed the way the register's fingerprint check documents
it (from the `## <ID>` heading to the next `## ` line or EOF,
splitlines keepends, joined, utf-8; the same function the doctor
uses) — and the register's probe-evidence line records that sha.
CORRECTED the same day: the first adopted form was the whole-file
blob (`git rev-parse HEAD:<path>`), which moves when ANY other
section of the file changes and is not comparable to the register's
stored fingerprint — three objects (file blob, section sha256, stored
fingerprint) were measured side by side and none matched; a pin that
cannot be compared to the thing it pins is decoration. The register's
stored hash on an `eval-open` entry is historical by its own
declaration and is not a defect; a probe whose brief carried no
pin is booked UNDETERMINED with the dispatch timestamp beside the
nearest amendment's. Adopted by the judgment desk 2026-08-27; lane B
of the same wave is the first brief carrying it.

**Second half, measured on the next two lanes (same day).** Lane B's
brief carried the pin (`f0c1fb7…`, the section's blob sha); the lane
hashed the on-disk section and matched it — the pin worked one
dispatch after adoption. But the `CLAUDE.md` INJECTED into the lane's
session prompt did NOT carry the amended step-4 paragraph while the
FILE did; lane A, asked the paragraph question, reported its copy
came from the injection and was immutable from dispatch. So a class
devbook reaches a lane through TWO channels — a snapshot fixed at
session start and the live file — which can disagree, and a lane
reading only its injection works from a stale rulebook with no signal
that it is doing so. The pin is what makes the divergence detectable.
Rule text: the pin is checked against the FILE's section hash, and a
lane that took a rule from its injection re-reads the file when the
pin does not match the injected text.

**Consumer + drain seam.** The next dispatch-skill maintenance pass
(§6 schema); the `guard-checker-bau` entry's next status move.

### ANGEWANDT 2026-08-27 (Lane `opus-a-skill-amendments`, wave 4)
### — a post-report message REANIMATES a lane

Booked in `0609f39`, amended in `9800011` (the TaskStop
clause); applied in this wave at two sites in
`plugin/skills/dispatch/SKILL.md`. §1's base-commit clause
gains the THIRD arrival read — `git status --porcelain` over
the write set plus the writer-reservation file, a HALT
whatever the base check said. §4's "Ownership ends at the
booked report" bullet gains the close-only rule, the
decisions-travel-to-the-NEXT-brief rule, the listing read
before any dispatch or message, and the never-message-a-
TaskStopped-lane rule. Entry body below, unchanged.

**Incident + basis.** Wave-3 desk `dotfiles-2f`: a "decided, build it"
message to lane B was delivered at a turn boundary AFTER lane B had
sent its closing report; the message's own text kept the grant open
("your write grant stays open until your report is booked"), so the
lane resumed and built lc-17 from the PRE-ruling design — 446
insertions in `migrate.py`, the very sentence the judgment desk had
struck. The desk, reading the report's "write grant closed" line as
current, reported the lane finished and dispatched lane B2 for the
same item. B2's prescribed arrival check (`merge-base --is-ancestor`
+ `log <base>..HEAD`) PASSED — lane B's work was uncommitted. B2 went
further unprompted: `git status` showed the file modified, six size
samples over ~30 s showed it growing, `.git/writer-reservation.json`
named the holder with `claimed_at` 22 s old; it halted before
writing. Containment: TaskStop, diffs saved to scratch, files
restored by `git show HEAD:<path> >` (never checkout/restore/stash),
caches cleared, index refreshed, status empty, blob sha equal — no
commit made, nothing in history. Cost ~10 min of lane tokens.

**Class.** Two. (a) The mailbox-delay entry above is about messages
arriving too LATE to steer; this is its mirror — arriving after the
report and steering what should have been closed. The skill's §4
already says the close message resumes the agent; the incident shows
EVERY message does, and a decision reply is a build order to a lane
whose grant text leaves the door open. (b) The §1 base check
establishes COMMITTED state and has no state for "someone is writing
right now": three states between two reads, none of them a live
co-writer. Underneath both: a lane's report line is a claim about
the past; only the agent listing says what it is doing NOW — the
desk itself named this as the rule it had applied to others all day.

**Pre-formulated rule text.** §4: after a report is BOOKED, the only
message a lane receives is the close, in the boundary form ("grant
over; do not act; a later defect is reported"); every decision the
report raised travels to the NEXT lane's brief, never back to the
reporter. Before any dispatch or any message to a lane, the listing
is read — a lane that reads `running` under a booked report is a
finding. A lane ended by TaskStop is NEVER messaged again, for any
reason, the close included: a send resumes a named agent from its
transcript, and a stopped lane's transcript ends on its last live
instruction — measured the same hour, when the judgment desk ordered
a close to the stopped lane and the peer desk correctly refused it
as a state-dependent directive whose state was false (the lane was
ABSENT from the listing, its last instruction "build"); the artifact
— absent, reverted, no commit — is the record of its termination. §1 arrival check gains a third read: `git status
--porcelain` over the write set plus the writer-reservation file
(where the reservation gate is deployed); a modified file in the
write set or a live reservation is a HALT, whatever the base check
said.

**Consumer + drain seam.** The next dispatch-skill maintenance pass
(§1 arrival check, §4 close rule); n=1, caught by the arriving lane on
first use of an unprescribed check.

### ANGEWANDT 2026-08-27 (wave-4 lane A2, the EXECUTION-tail
### remainder) — a named subagent's mailbox delivers NOTHING
### mid-run

Booked in `4c85fd1`, amended in `391ac1b` (the terminal form);
clauses (1), (3) and the §4 re-scope applied in `a3111b2`, the
channel fact as a dated binding in `references/forms.md` §2.
Clause (2) landed in this lane at the EXECUTION tail's HEAD in
`references/forms.md` — the salience position, not beside the
existing gap sentence — with `EXECUTION_TAIL_BG`
(`plugin/hooks/brief-reminder.py`) moved in the SAME commit, the
two being coupled by `check_execution_tail_fixture` on normalized
text. The restatement carries a source label to §2's delivery
binding, that block being the rule's other home. Clause (4)
needed no edit. Fully applied; the entry moves. Entry body below,
unchanged.


**Incident + basis.** Wave-3 desk `dotfiles-2f` (opus) sent six
SendMessages to a running named lane (opus, lane C, lifecycle
`120c733`) across ~40 minutes — a write-set grant, a superseded item
id, a version-bump grant, corrections. Every send returned
`success`. The lane, asked reply-only after its report (final count,
corrected from its own first answer of five): six messages, TWO
deliveries, both batched at turn boundaries, zero mid-turn — through
grounding, four red-first arrangements, the build, two bite proofs, a
blocked commit, and a ~9-minute foreground wait that was the ideal
window for one to land. The lane also retracted its own report line
"no message reached me at any point": true at the instant written,
stated with a finality it had not earned — a claim about a channel it
had no instrument to observe. The lane landed correctly only because it read the
superseded item's write-set out of the dispatcher's COMMIT in the
tree — the artifact carried what the channel did not. Mechanism
unestablished (held at the harness and flushed at a boundary, or
delivered on turn end — neither side has an instrument); observed
fact only.

**Class.** A channel premise under §4: "additions extend ownership",
"a follow-up instruction to a running agent", "ask the holder and
wait for the answer", the lane-close message — every mid-run steer
assumes delivery mid-run. The dispatcher holds `success` receipts the
whole way and is WATCHING, not steering; the dispatch reads as
steered because the lane happened to land. On a lane whose only
carrier for the steer was the message, the miss would have been
silent. The second half, the lane's own and the one that bites: the
receiving end cannot distinguish "nothing was sent" from "nothing
has been delivered YET" — both are silence from inside — so a lane
states the absence confidently in its report and the dispatcher
reads a false negative that arrived with full conviction. The delay
is the defect; the indistinguishability is why it propagates into
the record instead of being caught. One shape, three instances in
one lane that day: a grep over a path that did not exist (stderr,
empty stdout read as zero hits), a hook probe whose payload could
not fire the guard it claimed to check, and this — an instrument
that cannot register its target returns exactly what a true absence
returns (the corpus's Non-events rule, at the channel grain). A
fourth, the same day and self-reported: the desk wrote "verified by
me at the artifact" over a lane's own battery figures, having run
only `git show --stat`; it then ran the battery, every figure
matched, and corrected the provenance anyway — a true claim asserted
without its basis is indistinguishable, from the grader's side, from
a checked one, and the grade would have rested on the lane grading
itself. The instrument was not blind there; it was never run. By the
wave's close the desk's own tally was SIX (a citation to a decision
label that names a different ruling; a whole-file pin where the
register keys on a section; an item quoted for words it does not
contain) — every one caught by a lane, none by the desk first; the
desk's own class statement: a claim passed on without opening the
thing itself, hidden because the sentence is usually TRUE.

**Terminal form, measured the same afternoon (lane B2).** A lane that
halted on a question and WAITED could not be reached at all: the
desk sent the go four times, `ListAgents` showed `running`
throughout, the lane reported "no dispatcher message has reached me"
each time — it would not go idle because it was waiting, and the
queue would not flush until it went idle. A lane blocking on the
mailbox can never be unblocked through the mailbox. The artifact
channel (a GO committed to the repo's ledger) was not looked at
either. The desk stopped it and re-dispatched (B3) with B2's six
interim reports carried as pre-done groundwork; nothing lost, nothing
repeated. The one channel that never failed is the dispatch PROMPT.

**Pre-formulated rule text** (§1 brief, §4 duties): (1) everything a
lane could need mid-run is granted UP FRONT or not at all — the
brief is the complete instruction set; (2) the brief states the
channel fact: a mid-run message may not arrive before the turn ends;
on a gap HALT THE ITEM, FINISH THE REMAINDER, REPORT — never halt the
LANE, since "halt and wait" is not a survivable state for a subagent
and re-dispatching with the groundwork carried beats any wait; (3) where a lane
must be steered mid-flight, the carrier is the ARTIFACT — a committed
item body or file in its tree — never the mailbox; (4) the
expected-return horizon stays the dead-lane instrument, unchanged.
Retire or re-scope the §4 "additions extend ownership" clause to
what it can still mean: ownership extends, but the addition reaches
the lane at its next turn boundary at the earliest, and a report
already composed does not cover it.

**Consumer + drain seam.** The next dispatch-skill maintenance pass;
also the harness-binding line in the skill's §2 (`as of` date on
mailbox delivery). n=1 lane, six messages; the bite is reproducible
by any named lane asked reply-only when its messages arrived.

**ADDENDUM 2026-08-27 (wave-4 peer desk `dotfiles-2f`) — n RAISED TO
THREE LANES, and the desk supplied the third instance against
itself.** Merged here rather than filed as a sibling: same class.
Lane `opus-lifecycle-bundle`, four messages, and lane
`opus-lc44-48-49`, one — both asked reply-only afterwards, both
reading their own transcripts. Each reports the same shape as lane C:
delivery in ONE batch at a turn boundary AFTER the closing report
was sent, zero mid-turn. The class is CONFIRMED, not extended, and
the framing correction is the judgment desk's: an arrival at the end
of a lane's own send series is what "batched at turn boundaries"
already predicts, so only the PER-LANE verdict was ever in question.
TIMING, because the desk first mis-read this as a broader mechanism:
its sends to the bundle lane are stamped 17:24:20 and 17:25:26 in its
own transcript, and that lane's writer-reservation claim — an agent
tool action — is stamped 17:36:41, its report 17:40:58. So the
messages sat across a long stretch of the lane's ordinary tool
rounds. That does NOT widen the rule; it says the flush point is the
lane going idle, not each tool round, which is what "zero mid-turn"
means at this grain.
THE PER-LANE VERDICT IS REFUTED. The desk had concluded "that lane's
mailbox is dead", STOPPED the lane on that basis, and committed its
work itself (lifecycle `cbfaee6`, whose message says "because its
mailbox failed"). The channel had not failed; it delivered at the
boundary. The lane's own "INBOX drained, nothing received since the
brief" was true at compose time and stale within moments — exactly
the retraction lane C made in this entry's own body.
THE DISPATCHER-SIDE TWIN, which is what this addendum is for. The
entry's second half says the RECEIVING end cannot tell "nothing was
sent" from "nothing delivered yet". The mirror bites harder: the
SENDING end cannot tell "not delivered" from "delivered and
unacknowledged" — and a lane's own inbox line reads as the receiving
end's testimony, which is precisely what makes it convincing enough
to act on. The desk held THIS ENTRY, booked the same day, and still
drew the false negative from the same evidence shape, then took an
irreversible-ish action (stop the lane, absorb its uncommitted work)
on a channel claim it had no instrument for. The settling instrument
is the receiver's TRANSCRIPT, one reply-only question, seconds cheap
— and it is available before the stop, not only after it. Rule text
to carry at the next pass: a channel verdict is read off the
receiver's transcript, never off a report line about its inbox, and
never off the sender's silence; where a lane must be stopped, the
stop does not need the channel verdict as its reason and should not
borrow one.

### APPLIED 2026-08-23 (Lane `opus-report-provenance`) — the
### rule reached the dispatcher, not the executing agent

Booked in `dbdd81a`, applied in the same run: the pre-formulated
clause text now stands at the HEAD of both tails in forms.md §2, and
the `EXECUTION_TAIL_BG` fixture (brief-reminder.py) moved with it —
red-proven: baseline green, mutant (clause removed from the fixture
only) `[DRIFT] EXECUTION tail fixture` at normalized character 929,
restored green again. The dispatcher explicitly reversed the
original scope decision (tails excluded). The entry's body sits in
`dbdd81a`; only the evidence remains here. The CLASS lives on below
as its own entry — it did not drain with this instance.

### APPLIED 2026-08-18 (peer assignment, pbs-office desk) — four
### homes, one of them in a different form than the entry expected

The rule is minted as a POSITIVE DUTY, not an attention-prompt —
exactly the warning the entry itself carries (the skip was noticed
only because red neighbors happened to sit beside it): `forms.md:18`
slot (b) demands the full count and a disposition per skip, with the
sentence naming the non-event class (a skipped check differs from a
nonexistent one only by its line in the report); `forms.md:225`
carries the same duty verbatim in the EXECUTION tail;
`dispatch/SKILL.md:708` the dispatcher half (the integration run
compares the SKIP count against the baseline); `executor/SKILL.md:60`
the conduct half, WIDENED into rule 4 rather than placed beside it as
a new rule — with a source label to slot (b), as the skill-to-skill
audit rule demands.

DEVIATION from the pre-formulated text, deliberate: the entry says
'verbatim into both tail blocks'. The READ-ONLY tail carries no slot
list at all — slot (b) would be meaningless there. The rule
therefore sits at `forms.md:282` as a clause on the verdict's BASIS:
a skipped check did not run, and a verdict resting on it is
could-not-verify, not clean. Verifier lanes are exactly the ones
that run checks — the gap would otherwise have stayed open.

MECHANISM COUPLING, forced by the doc-drift check, not found by
hand: `brief-reminder.py:662` holds a literal fixture of the
EXECUTION tail; the slot-(b) change broke it, the check went red,
the fixture was updated to match. `check-doc-drift.py` clean
afterward.

MECHANIZATION — DECIDED, NOT BUILT: booked PARKED (BACKLOG, named
missing evidence). Reasoning on the predicate: the skip COUNT is
computable, the presence of a disposition is not, without false
fires — a report that writes '4 skipped (unrelated, pre-existing)'
DISPOSITIONS in the same sentence and would fire any second-mention
counter. A guard that fires on legitimate work trains the override
reflex (repo rule: a new lane defaults to warn, deny only by fire
rate). The report carries the disposition; a lint can at most check
its PRESENCE — the entry's own opinion, adopted here as the
decision.

### A SKIPPED test is a test that did not run, and the report form never asks about it

**1. Incident + basis.** 2026-08-18, pbs-office backlog wave
(journal `01NhRWdw-backlog-desk-1808`; build pbs-office `892ed44`,
post-review follow-up `10fb16c`). A lane built four tests meant to
prove the load-bearing branch of its item — the strict schema path.
In the main checkout **all four** skipped, because a path resolution
silently went wrong (`git rev-parse --git-common-dir` answers
relative to ITS OWN cwd, `Path.resolve()` resolves against the
Python process's cwd). The run reported '66 passed, 4 skipped' — so
GREEN. The item was thus formally built, verified and reported while
its core branch had never executed. It was not the report form that
found this but a suite run by the dispatcher in the main checkout —
and even that only because OTHER tests then went red. Without those
red neighbors, the skip would never have been noticed.

**2. Class.** Not the worktree environment (that is the occasion,
and lives in `worktree-OBSERVATIONS.md`), but the REPORT FORM: slot
(b) demands 'checks/tests actually RUN, with their real output'. A
skip satisfies that literally — it DOES stand in the real output —
and is nonetheless the opposite of what the slot is meant to prove.
A skipped test differs from a nonexistent test in nothing but its
line in the report. This is the operator corpus's non-event class (a
dead mechanism yields the same picture as a passing one), here
dressed as a number nobody reads because 'passed' sits beside it.

**3. Pre-formulated rule/fix text** (addition to `references/forms.md`,
slot (b) of the §2 form, and verbatim into both tail blocks):

> (b) checks/tests actually RUN, with their real output — including
> the **full counts, skips named**: `N passed, M failed, K skipped`.
> Every skip is DISPOSITIONED: which test, skipped for what reason,
> and whether that reason touches the item. A skip in a test THIS
> lane built is, by construction, a finding — it proves the built
> branch never executed, and a build whose verifier did not run is
> unverified, not green. `K > 0` without a disposition sentence is
> an incomplete report and is demanded back like a missing slot.

Dispatcher half, in §4 (integration): the dispatcher's own
verification run compares not only passed/failed against the
baseline but also the SKIP count. A skip count risen above the
baseline is a finding, not noise — it is the quiet direction of the
same question a risen fail count asks loudly.

**4. Consumer + drain seam.** The next dispatch-guards maintenance
round (`references/forms.md` §2 + both tails, `SKILL.md` §4).
Immediate consumer: any session booking a lane report today — ask
for the skip count by hand until the mint lands. A mechanization
candidate, but not a safe one: the count is computable, the question
'does this reason touch the item' is not — so the report carries the
disposition and a lint can at most check its PRESENCE.

## 2026-08-06 — three from one fan-out (3 × opus, two fork worktrees + one shared repo)

**APPLIED 2026-08-17 (maintenance pass)** — all three halves.
#1 → §1 'Commit unpushed': a working copy with a writer OUTSIDE
the dispatch carries no unpushed work. #2 → new §1 sub-point
'deployment-coupled is a different question from LIVE ON WRITE'
plus a skeleton slot. #3 → ladder rung 2: the worktree skill is
LOADED, never merely cited. Evidence: this commit.

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

**APPLIED (before this pass)** — the entry IS the mint record;
the widened race clause sits in forms.md §2 ('The race's mirror
sits at the lane's END'). No text still open.

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

**APPLIED (before this pass, 2026-08-10)** — the lane keys on
the VERB position; the docstring names the measured false-fire
case, two bite tests pin it. Evidence: push-claim-reminder.py
(docstring + --test).

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

**n=2, 2026-08-27, AFTER the ANGEWANDT repair — which is the finding.**
dotfiles wave-4 lane C1 (opus, guard/checker class): its first `git
commit` was DENIED WHOLE because the literal two-token string `git
push` appeared inside the commit MESSAGE, which described push
round-trips through the hook it had just changed. Nothing in that
command pushed anything. So the 2026-08-10 repair — key on the VERB
position rather than the bare token — did NOT close this: `git push`
IS the verb-position pattern, and it matched inside quoted message
text. Narrowing a textual predicate cannot separate a command from a
quoted body that describes one; only argv-level parsing can, and the
2026-08-07 proposal already said `argv-level` while the applied fix
stayed a string match. The docstring's two bite tests pin the OLD
false-fire case and are silent on this one, so the guard read green
through it.

The cost this time is worse than the nuisance, and it is the thing to
carry: the lane REWROTE ITS COMMIT MESSAGE to get past the matcher.
That is a guard editing the permanent record to satisfy its own text
predicate — the 2026-08-07 entry predicted "the guard taught message
rewording rather than catching a fused push", and the second instance
is that prediction executed on a repo's history. The training cost
compounds: this lane was doing exactly what the discipline instructs
(describing its verification honestly in the message), which is the
careful-path over-fire the 2026-08-26 CLASS entry names.

**Grade: READY repair, not an observation.** Predicate parses the
command to argv and tests the verb position of each simple command,
so a quoted or heredoc'd body is never scanned; the deny text
distinguishes "a git push in this command" from "the word push inside
a message"; and the bite battery gains BOTH of the measured
false-fire payloads — the 2026-08-07 word-in-heredoc case AND this
one, a `-m` message containing the literal `git push` — beside a
must-not-move row for a genuine fused `git push … | tail` and for a
compound push plus claim check, which the deny text alone cannot tell
apart from the false fires.

## 2026-08-07 — a brief cut from a ranked-list head inherits the list's staleness

**APPLIED 2026-08-17, MERGED with the 2026-08-14 entry 'the
re-read unit'** — same class: the re-evaluation sits outside the
reading window. Lands in the §1 provenance bullet ('Opening a
stored ENTRY means the entry PLUS its neighbours'), together with
the extractor as the instrument. Evidence: this commit.

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

**APPLIED 2026-08-17** — the write-set-overlap half was already
carried in §1 (fast path `git diff --quiet <base> HEAD -- <paths>`);
new is the compose-time CENSUS (`git worktree list` beside `git
status` and `git log -1 --format=%cr`), which also serves the
integration seam — §4 points to it, one home. Evidence: this
commit.

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

**APPLIED 2026-08-17** — candidate 1 already stood in the
worktree skill (`extensions.worktreeConfig`, `config --worktree`);
candidate 2 lands split in two: the census in §1 (cited by §4) and
'config writes are repo writes' in §2 slot (f) plus the tail.
Evidence: this commit.

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

**MERGE 2026-08-19, n=2 for this class — the same gap one axis
further: the census is a POINT IN TIME, the co-writer a HISTORY.**
Incident (cache-fix desk, two parallel lanes, dotfiles copy): the
compose-time census ran as prescribed — `git status --porcelain`
(2 files), `git worktree list` (1), `git log -1 --format=%cr`
('11 hours ago') — and reported a quiet copy. Twenty minutes later
the OPERATOR committed directly into the same copy (`8999f45`,
12:15:25) and pushed. The census was CORRECT at the moment it ran
and silently wrong afterward; nothing woke the dispatcher.
What then held the error in place instead of exposing it are two
reads, both of which were green: (1) `git diff HEAD -- <file>` was
EMPTY, read as 'unchanged' — true of a HEAD that by then CONTAINED
the change; 'identical to HEAD' says nothing about change once HEAD
itself has moved, which makes it a criterion anchored to live
state. (2) `git log origin/main..HEAD` showed ONLY the lane's own
commits — because the foreign commit had already been PUSHED and
origin had moved with it. Both commands sit in the discipline;
neither sees this case. It was the LANE that exposed it, not the
dispatcher, and by CONTENT (`git diff <foreign> <own> -- <file>`
empty) rather than by timestamp.
A third instance of the same root within the same hour, without
git: a moved mtime read as a boundary violation, then two QUIET
mtimes read as the lane having stalled (the lane was working
straight through). A state read never answers whether an EVENT
occurred, and mtime observes a write, never a change and never a
writer.
Pre-formulated rule text, §1 base-commit clause and §4 dispatcher
duties, in its register: **The census is REPEATED at the
integration seam and reads the HISTORY, not the state: `git log
<base>..HEAD` (not `origin/main..HEAD` — origin moves with a
pushing co-writer) plus `git log -1 --format=%cr`. Every commit in
it is CLAIMED individually; an unclaimed one halts integration.
And: the absence of a change is never established against HEAD,
but against the base commit NAMED in the brief — an immutable
anchor, while HEAD is one the co-writer moves.** The existing
census rule stands as it is; it covers the point in time, this
addition covers the stretch.
Consumer + drain seam: the maintenance pass under the OBSERVATIONS
quota; target sites §1 (base-commit clause) and §4
(verify-in-the-artifact duty). Nothing was lost — the pathspec form
held, the foreign commit did not travel under the lane's message;
the class cost diagnosis time and an all-clear delivered to the
operator that was wrong.

## 2026-08-07 — dispositions-as-brief graduated; two §1 note candidates

**APPLIED (before this pass)** — candidate 2 graduated into §1
('Criteria state OUTCOMES first, sites second', both fire
directions); candidate 1 (the red-first arrangement as the first
act, per disposition) sits in the operator corpus, brief-family
bullet. **Basis caveat (enumeration lane, 2026-08-17):** candidate
1's target site is in the GLOBAL operator corpus, outside this
working copy — unverifiable from here. The entry cites a source
this session cannot open; that half counts as unverified until a
session with dotfiles access reads it.

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

**APPLIED 2026-08-17** — candidates 1 and 2 → §1 base clause:
'Stated means READ at compose time', output pasted in, plus the
co-writer census. Candidate 3 needed no change (the executor halt
stands, as the entry argues). Evidence: this commit.

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

**APPLIED 2026-08-17** — the three sizing terms plus the
crossover rule of thumb (~30 tool calls per lane, a formula rather
than a constant, measured by `tools/lane-cost.py`) → §1 'What rides
ONE lane'. Evidence: this commit.

**Write-side half APPLIED 2026-09-12** — the 2026-08-17
application landed the read-only half only: the transferred
"token spend is identical either way" sentence, confirmed at
source by correction (1) below, had survived in the ONE-lane
clause's WRITE-side text, still licensing one-item-per-lane
fan-outs. Re-scoped to its parallel-vs-queued mechanism, and the
write-side bundling default landed beside it (disjoint small
items share a lane below the crossover, sequential, per-item
commits and per-item red-first arrangements; one review round
per wave). Operator-reported companion incident: an in-session
backlog drain running a full review per minor item (2026-09-11).
Corpus complement same day: calibration priced-units pull-seam
clause, routing route-line lane-count sizing (dotfiles 5bcd338).
Evidence: this commit.

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

**APPLIED (before this pass)** — mechanism shipped in the same
batch (forms.md §2 two-lanes binding, `mailbox_lane()`, six corpus
cases). The binding paragraph is switched, in today's pass, to the
PER-SESSION probe (entry 2026-08-16) and carries the stamp 'as of
2026-08-17'.

Two probes from a fable desk session (dotfiles cwd), same day:
(1) an UNNAMED `general-purpose` dispatch with `run_in_background: false` launched ASYNC ("Async agent launched successfully"), contradicting the sync-on-request behavior the title-prefix lane was built for (forms.md §2, binding as of 2026-07-30).
(2) that agent's final text WAS delivered to the dispatcher, in full, inside the completion task-notification — "final text reaches no one" did not hold for this shape.
Both n=1, that day's harness version. Consequence taken now: the agent-model-gate's unnamed/title-prefix lane is retired (name-always, operator decision 2026-08-08). NOT taken: any change to the §2 channel rules — they stand pending a controlled re-probe (named/unnamed × run_in_background true/false, recording launch mode and whether the final text reaches the dispatcher). See the PARKED backlog item of the same date.

Addendum 2026-08-15 (fable desk, PV-Georgendorf cwd, harness 2.1.232): both shapes now n=2, and the PINNED-TYPE exemption is implicated. An unnamed `claude-code-guide` dispatch (no `run_in_background` param) launched ASYNC, and its full final text was again delivered in the completion task-notification. New half: the skill text itself produced a denied call — forms.md §2 routes pinned-type dispatches to the synchronous channel line ("your final text IS the report"), the brief-reminder hook denied the mode/line contradiction (guard correct, fire logged), and the retry with the background line went through clean. So until the parked re-probe settles the channel rework, the pinned-type guidance instructs the exact form the guard bounces. Proposed rule change: forms.md's channel-line paragraph defaults pinned types to the BACKGROUND line too, keeping the sync line only where a sync launch has actually been observed; the re-probe item gains the pinned-type axis (agent type named/pinned × run_in_background). Basis: this session's transcript — deny text, retry, task-notification delivery.

Addendum 2026-09-18 (opus judgment desk, CachyOS-Setup arc;
harness as of this date). The NAMED lane has the same shape as the
unnamed one above, WITH A HAZARD THE UNNAMED SHAPE DOES NOT HAVE.
A named mailbox agent's final text DOES surface to the dispatcher --
in the `result` field of its idle notification -- and it arrives
TRUNCATED, carrying an explicit "[result truncated -- ask the agent
for the rest via SendMessage]".

n=2, two independent sightings, two sessions, same day: the
dispatching desk received it from a named verifier lane, and the
executing peer desk (cachyos-setup-39) observed the identical shape
from its own attack lane and reported it unprompted.

WHY THIS IS WORSE THAN THE SILENCE THE CHANNEL LINE PROMISES, which
is the whole reason it earns an addendum rather than a footnote: a
truncated report LOOKS COMPLETE. Silence is obvious and sends the
reader to SendMessage; a report that ends mid-sentence in a field
the reader was not told to distrust reads as the report. Measured
consequence in the dispatching session: the notification carried
findings F1 through F5 and cut off before F6 through F10, and the
lost half contained the finding that stopped an irreversible-delete
gate from being cleared. The desk did not lose it only because the
lane had ALSO sent the full report by SendMessage, per the channel
line -- i.e. the channel rule saved the case its own binding says
cannot arise.

The standing channel line for named lanes ("your final text reaches
no one") is therefore FALSE AS WRITTEN and false in the dangerous
direction: it tells the executor its final text is discarded, when
in fact a truncated prefix of it reaches the dispatcher looking
whole. An executor that believed the line and put nothing in
SendMessage would be read, partially, with no gap marker.

**Pre-formulated text.** forms.md §2, the named/mailbox channel
line, gains its own sentence: "Your final text is NOT discarded --
a TRUNCATED prefix of it reaches the dispatcher in the idle
notification's `result` field, looking complete. Put the report in
SendMessage regardless; a dispatcher reading only that field reads
a prefix and cannot tell." And the dispatcher-side rule its mirror:
a lane's `result` field is a PREFIX until the SendMessage report
arrives, never a report -- the same grade as any other truncated
view (operator corpus, Grounding: a partial view read as its whole
body).

**Consumer + drain seam.** forms.md §2 amendment at the normal
quota drain. Basis: both sessions' transcripts, 2026-09-18.

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

**APPLIED (before this pass)** — §1 carries the clause with both
fire directions ('Criteria state OUTCOMES first, sites second').

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

**APPLIED (before this pass)** — §1 provenance bullet: per-line
grading, the form half, and the transition from discovery
testimony to instruction.

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

**PARTIALLY APPLIED (before this pass), REST DROPPED** — the
cheaper variant is built: both PreToolUse lanes clear a claim whose
file no longer carries uncommitted work (`no_uncommitted_work`),
measured against three false fires. The HEAD-reachability variant is
DROPPED — it catches the same class more expensively and needs
commit attribution the clearing does not. The appended 0.7.1 bullet
(shared version gate, bump-first) is applied in the commit-plan
paragraph. Evidence: writer-claims-gate.py docstring; SKILL.md §1
commit plan.

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

**DROPPED 2026-08-17** — the hypothesis is refuted at the
source: `_dispatch_common.fire_log_path()` reads
CLAUDE_DISPATCH_GUARDS_FIRELOG, otherwise XDG_DATA_HOME, and the
README names exactly that default. The silence in the doctor run
has its cause outside this repo (the doctor's child env), not a
stale README — no text to change.

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

**APPLIED 2026-08-17** — the path-scoped tolerance already
stood as a fast path in §1; new is the sender half: where the
brief FILE is committed into the executor's copy, the brief's own
commit is the base. Evidence: this commit.

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

**APPLIED 2026-08-17** — (a) ADD-ONLY is not a disjointness
exemption, (b) no safe form exists for a SHARED file, which makes
serialization the remedy rather than a preference, (c)
container/service/privilege as an environment precondition — at
the REPOINT bullet, generalized upward there ('confirms what it
assumes exists — the knob AND the environment'). The enforcement
observation (writer-reservation in warn mode would have caught it)
stays fire-rate material, not rule text. Evidence: this commit.

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

## 2026-08-12 — Four observations from two K7 dispatches (Abwägung Georgendorf, opus agents)

**APPLIED 2026-08-17** — all four: (1) inbox drain before sending
AND between report parts (§2 plus the EXECUTION tail), (2) a
content anchor beside position-/generation-dependent IDs (§1
'Files to read'), (3) flags BEFORE the `--` (the tail and executor
rule 6; verified here by execution: `git commit -- f.txt -m "…"` →
"pathspec '-m' did not match any file(s)", the form with the flag
first commits cleanly), (4) a page-image review where render
chrome is visible (verifier slot). Evidence: this commit.

Source: session 91da2482 (PV Georgendorf), two dispatches
(opus-abw-runden-elementfelder, opus-abw-kasten-klartext), journal
pbs-office betrieb/journal-2026-08.jsonl.

1. **Report queue vs. dispatcher message — THREE TIMES in one
   session.** Agents compose multi-part closing reports as a queue
   and do not drain their inbox between parts: a dispatcher GO (sent
   after part 1) still read 'open' in part 7's closing sentence; two
   add-on assignments (D13, D8/D9) were missing, undispositioned,
   from complete reports — each costing a full demand-and-chase
   round. Proposal (§2 tail clause): drain one's own inbox before
   sending the closing report AND between parts; the report
   dispositions every dispatcher message received up to send time,
   or names it explicitly as unhandled; the race symptom (report
   says 'done', message unmentioned) becomes distinguishable from
   the report itself this way.

2. **Position IDs in a brief are labels over someone else's body.**
   A brief cited register numbers ('Reg-12/Reg-13') from an older
   reviewer PDF; the register had since been regenerated, every
   number shifted by one. What saved it was the content anchor in
   the same brief (the box's literal wording), which the executor
   worked from. Proposal (§1 clause, applying the label-over-body
   rule): position- or generation-dependent identifiers (register
   numbers, change-item IDs, line numbers) always carry a content
   anchor beside them in the brief; on divergence the executor works
   from the anchor and reports the offset.

3. **`git commit -m "…" -- <paths>` fails** — after the pathspec
   separator git reads `-m` as a path; two sessions hit this
   independently the same day (dispatcher + executor). The §2 tail
   says only 'by pathspec'; proposal: sharpen the tail wording —
   flags BEFORE the `--` (`git commit -m "…" -- <paths>` has it
   backwards; correct is `git commit -m/-F … -- <paths>` with the
   message flag before the separator, or `-F` for multi-line
   messages).

4. **Visual chrome changes have no image-review stage.** A
   color-stack leak (purple body text after a new framed field)
   passed the suite, structure checks, pdftotext count probes, and
   the page-count comparison unremarked — pdftotext does not see
   color; found by the operator via screenshot. Proposal
   (brief/verifier clause): a change to visible render chrome names
   a PAGE-IMAGE review (pdftoppm or similar) by the dispatcher in
   the verifier; text-extraction checks are blind to color/layout,
   and the dispatcher can review images.

Consumer: the next dispatch-guards maintenance round (tail and §1
wording); observation 4 additionally landed as a site rule in the
pbs-abwaegung repo (that repo's CLAUDE.md, via a running dispatch).

## 2026-08-12 — writer-claims: a CLOSED lane's claims fire against the successor lane

**APPLIED 2026-08-17 (the prose half), MECHANISM DROPPED** — both
directions of the pair land in §4 'Additions extend ownership': a
crossing report does not close the lane, and neither grep nor `git
status` observes a WRITER; when in doubt, ask the holder and wait
for the answer. The lane-STATE register (a release/re-arm verb on
the claim register) is DROPPED: 'lane closed' is not computable at
hook time, and the existing `no_uncommitted_work` clearing already
covers the false-fire direction. Evidence: this commit.

1. **Incident + basis:** sequential dispatches in the same working
   copy (pbs-abwaegung): lane A (opus-abw-drei-waechter) closed
   cleanly — report booked, commits integrated and pushed by the
   dispatcher, lane-close message sent. Lane B
   (opus-abw-sichtweite-austrag) then edited the same test file; the
   writer-claims hook reported WARN ('this lane would DENY') against
   the DEAD lane A's claim (the claim TTL outlives the lane's
   closing). Lane B lost an INTERIM round clarifying a phantom
   co-writer; the tree provably carried only its own changes (HEAD
   identical, no foreign uncommitted hunk — shown by lane B's own
   git diff).
**Firing record, 2026-09-15 (refinement candidate inside the
accepted limit).** Drain desk dotfiles-f1, lifecycle wave 1: lane
D's reservation still WARNing 38 minutes after the lane closed. The
desk read the docstring's recorded tradeoff first ("on a fan-out
that is constant" — the 2026-08-10 operator decision), so this is
not a re-litigation; the refinement it proposes sits inside the
accepted limit: the release predicate is per-COPY, so it cannot
distinguish "this writer left work" from "a sibling is mid-flight",
and only the first justifies holding. A finer-grain release is a
predicate change for this entry's existing consumer seam.

**Firing record, 2026-09-15 (b) — third firing, and the class's
inferred anchor is half-refuted at the source.** Drain desk
dotfiles-f1, same day, the CLAIMS face this time: writer-claims
WARN on test/test_items.py (lifecycle repo) naming a claim by
sonnet-lc126 ~1h after that lane's work was committed (67c461a),
pushed (contained in origin/main), its item closed (8e0f621) and
the lane idle — measured four ways by the reporting desk at the
artifact; the firing lane proceeded via the gate's own stated
condition (correct conduct, but the override-training cost this
entry names). The reporter's inference ("anchor is elapsed time,
not uncommitted state" — offered explicitly as derived, source
unread) is REFUTED at the source: check() relieves via
no_uncommitted_work() before consulting any claim
(writer-claims-gate.py:199, the 2026-08-10 relief). A firing
against a committed-clean history therefore implies the relief
was DEFEATED at fire time. Two candidate mechanisms, both
derived, undetermined: (i) own-dirt defeat — the relief keys on
the FILE being clean, not on whose dirt it carries, so the
successor's own first landed edit re-arms every stale foreign
claim on that file for its later edits (whether the successor's
own write records a superseding claim, which would silence this
path, is unread here); (ii) the relief's git call timing out
(_GIT_TIMEOUT, conservative False → relief skipped) — this
machine was measurably killing processes for memory the same
hour. RESOLVED same day, one message round plus the fire log. (i) is
REFUTED by the reporter's machine-read timeline (claims store +
git): tree-wide `status --porcelain` EMPTY at 19:33:30 local,
zero claims on the path 19:10→19:39, and the firing edit was the
successor's FIRST touch of the file — the file was clean at fire
time, so the relief's input was a clean tree and it still did
not relieve. The fire log (ts is ISO-8601 UTC — epoch parsing
returns silent false zeros, one such false zero produced and
caught by positive control during this very diagnosis) shows
EXACTLY ONE warn: 17:39:00Z, agent opus-lc120, against
asonnet-lc126's claim; the successor's 19:40:18 and 19:42:55
edits fired NOTHING — explained at the source: record_claim runs
on the victim's own first write, making the victim the path's
latest claimant, so the gate self-heals per successor. Real cost
of the class: one spurious warn per successor lane per file per
TTL window. Remaining mechanism, now the only one standing: the
relief's documented could-not-verify branch — "git unrunnable,
slow, or exiting non-zero → False, and the gate keeps firing"
(no_uncommitted_work docstring) — under measured machine load
(reporting desk running a full clone + 635-test battery + node
suites that hour; the same hour this machine killed two of the
judgment desk's timers for memory). The timeout/exit itself is
uninstrumented, WHICH IS THE DEFECT: the warn text and fire-log
record are byte-identical whether the file was dirty or the
check could not run. Slot 3 gains its sharpest fix: the warn and
its fire-log record NAME the producing branch — "live
uncommitted work at <path>" vs "could-not-verify (git timeout /
exit N)" — the third-answer rule applied to this gate's own
output; with the branch named, today's two-desk multi-round
diagnosis becomes one grep, and the fire-rate review can count
could-not-verify fires as their own line. (Correction folded in:
the stale claim's work was committed AND pushed 70 minutes
before the firing; firing lane opus-lc120.)

2. **Class:** lane lifecycle vs. claim lifecycle divergence: the
   claim register knows only the TTL, not a lane's booking-close — a
   dead writer reads to the successor exactly like a live one (a
   false-fire class; in DENY mode it would block legitimate serial
   dispatches in the same working copy).
3. **Pre-formulated fix text:** 'Closing a lane CLEARS its claims: on
   booking the closing report, the dispatcher releases the lane's
   write claims (a release verb on the claim register, part of the
   §4 mirror duty alongside book+notify); alternatively the
   writer-claims lane accepts a dispatcher attestation "lane closed,
   commits integrated up to <sha>" as the claim's end. Until then: a
   claim hit from a lane whose report is booked and whose commits
   are contained in its own base sha is a TTL leftover — check it
   via git diff against the base, never by waiting further.'
4. **Consumer + drain seam:** next dispatch-guards maintenance round
   (the writer-claims hook + §4 wording of the mirror duty).

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

**APPLIED 2026-08-17** — slot (f) is established from the RECORD
(trailer filter; 'present in the tree, not mine') in the §2 slot list
and the EXECUTION tail; §4 grades slot (f) against the trailer before
booking, and the close message carries its own boundary ('do not
edit; a defect found later is REPORTED'), because it resumes the
agent. Evidence: this commit.

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

## 2026-08-14 — A briefed edge case as a mandatory assertion pins the spec, not the defect

**APPLIED 2026-08-17** — home chosen: §1 (the instrument-semantics
bullet); no edge needed in the pbs-office devbook: a prescribed
mandatory assertion also names a case that separates the prescribed
implementation from the NAIVE one. Evidence: this commit.

1. **Incident + basis:** the FB-103 build (opus-befund-referenz,
   pbs-abwaegung `b213761`): the brief prescribed the worked-through
   edge case BF22/BF2 as a mandatory assertion ('a document
   containing only `% BF22` → BF2 does NOT count as referenced'). The
   assertion came out the same under the correct lookaround regex AND
   under the naive `BF([0-9]+)` — regex greediness stood in for the
   lookarounds in this example case. Only character-adjacency
   (`\labelBF2`, `ABF2`) discriminated; it was the executor's mutation
   battery that found this (M1 survived the first run), not the
   prescribed case.
2. **Class:** instrument discrimination at the brief seam — the same
   'both outcomes satisfy it' class (Fixing corpus), here as a BRIEF
   instance: a mandatory assertion the dispatcher prescribes inherits
   the spec's parentage and can systematically miss the defect the
   predicate is built for, while reading as rigor.
3. **Pre-formulated fix text** (dispatch skill §1, the 'Criteria
   state OUTCOMES first' clause, or D5 spec-check item 1, an added
   sentence): 'Where a brief prescribes an edge case as a mandatory
   assertion, it also demands an assertion that separates the
   prescribed implementation from the NAIVE one (a case the two
   answer differently) — otherwise the mandatory assertion pins the
   spec, not the defect; the mutation battery remains the proof.'
4. **Consumer + drain seam:** the next dispatch-skill maintenance
   round (SKILL.md §1, or DEV-RUNBOOK D5 item 1 in the pbs-office
   opus package — choose ONE home, a pointer in the other); quota
   drain per the OBSERVATIONS rule.

## 2026-08-14 — grep on a PDF is silently blind without `-a`; structure checks need the decompressed stream

**APPLIED 2026-08-17** — executor skill rule 4: a structure search
over a binary format counts only with a positive control in the SAME
invocation mode; the PDF's two stacked instrument-killers (binary
classification, object streams) are named. Evidence: this commit.

1. **Incident + basis:** the FB-6.18 mechanism
   (sonnet-anhang-verlinkung): PDF link verification via `grep
   '/Subtype /Link'` returned a zero hit because grep classified the
   file as binary — even for a string certain to be present, like
   `/Type` (that was the positive control that exposed the
   blindness). The check only became sound with `qpdf --qdf
   --object-streams=disable` (decompress the streams) plus `grep -a`.
2. **Class:** a zero-hit search with a dead instrument (Fixing
   corpus, non-events) — the binary classification is an
   instrument-killer that yields exactly the result a true absence
   would; PDF object streams are the second, independent killer of
   the same check.
3. **Pre-formulated fix text** (executor skill, verification section,
   one sentence): 'A structure grep over a PDF (or other binary
   format) counts only with a shown positive control in the same
   invocation mode; for PDFs that means decompressing (`qpdf --qdf
   --object-streams=disable`) and `grep -a` — a zero hit without a
   positive is not a statement of absence.'
4. **Consumer + drain seam:** the next executor-skill maintenance
   round (the verify-with-the-check's-own-output section); quota
   drain per the OBSERVATIONS rule.

## 2026-08-14 — report booking does not check the SENDER: an unsolicited foreign message reached a waiting dispatcher

**APPLIED 2026-08-17** — §4 horizon paragraph: an incoming report
is booked only once its SENDER resolves against the dispatcher's own
dispatch list; an unresolved sender is a finding (cross-talk), and
closes no horizon. Evidence: this commit.

1. **Incident + basis:** during a three-arm probe of the subagent
   spawn cap (dotfiles LEDGER 2026-08-14, commit `4a40404`), a
   headless dispatcher session waiting on its one subagent's report
   received an unsolicited message with plausible result content
   (`FORK-PROBE-EXECUTED`) from a sender id that matched NONE of the
   agents it had started — plausibly the background fork of a PRIOR
   probe session, delivering after that session had ended
   (cross-session delivery; provenance undiagnosed). The dispatcher
   discarded it on its own judgment, by matching the name against its
   own dispatch list — no rule in the skill covers that check.
2. **Class:** report attribution — an incoming report's sender
   identity is a premise nothing checks. §4 covers 'silence is never
   success' and the expected-return horizon, but a report that
   matches CONTENT-wise from the WRONG sender books itself through:
   it appears to answer the open horizon and ends the wait for the
   real one.
3. **Pre-formulated rule text** (dispatch skill §4, at the horizon
   paragraph): 'An incoming report is booked only after its sender
   resolves against the dispatcher's own dispatch list (agent id or
   brief name); a report from an unresolved sender is a FINDING
   (cross-talk), never a report — it closes no open horizon, and the
   wait for the real report continues.'
4. **Consumer + drain seam:** the next dispatch-guards maintenance
   round, or the next build touching §4; quota drain per the
   OBSERVATIONS rule.

### MERGE 2026-08-18 — 2nd incident, this time the GENERATING side: the channel line is phrased RELATIVE and gets inherited literally by forks

1. **Incident + basis:** opus desk 75 (pbs-office `2afbcba`, journal
   line `sonnet-zusicherung-3145`) dispatched ONE read-through review
   across five repos (FB 3.145). The executor started five forks for
   it. The desk then received SIX messages for this one item, all
   under the sender name `fork`, contradicting one another: different
   finding counts for the same repos (pbs-doc variously A=3/B=0,
   A=2/B=0, A=1/B=1) and each naming a DIFFERENT repo as still
   outstanding (once pbs-abwaegung, once pbs-wissen, once
   pbs-office). The executor named the cause itself: the forks
   inherit its full context, including the line 'Report channel:
   SendMessage to the dispatcher' from the original brief, and
   resolved 'the dispatcher' to the GRANDPARENT (the desk) instead of
   to their own creator. A second, independent instance of harm from
   the same root: three forks wrote near-identically-named result
   files into the same session scratchpad
   (`fb3145-zusicherung-durchsicht.md`,
   `fb-3145-zusicherung-durchsicht.md`,
   `fb-3145-zusicherung-liste.md` — all within two minutes, recounted
   on disk by the desk); the writer-claims gate warned about a write
   inside the claim TTL, and at least one fork's findings were
   overwritten.
2. **Class:** the same one (report attribution/cross-talk), but here
   the GENERATING side rather than the booking side. The §4 rule
   applied 2026-08-17 DID hold on the receiving side: the desk
   resolved the senders against its own dispatch list, discarded all
   six as cross-talk, booked none, and left the horizon open — the
   strongest finding was instead confirmed by the desk itself at the
   source (pbs-office FB 152). What remains open is the side before
   that: a channel line that names its recipient RELATIVELY is
   ambiguous under inheritance, and inheritance is the normal case
   for a fork, not the exception.
3. **Pre-formulated rule text** (forms.md, channel-line block, the
   named variant): 'The channel line names its recipient ABSOLUTELY,
   by agent name, never relatively: `Report channel: SendMessage to
   <dispatcher-name> — your final text reaches no one.` A relative
   reference ("the dispatcher") is inherited literally by a fork and
   resolves THERE to ITS creator's creator — the grandparent;
   measured 2026-08-18 as six contradictory reports to a dispatcher
   that had started only one agent.'
   Addendum (§1, write boundaries): 'A brief that does not explicitly
   commission fan-out forbids sub-forks — the executor hands the work
   back instead of distributing it. The reasoning belongs in the
   brief, so it is carried along rather than merely obeyed: the
   channel line AND the parent's scratch filenames are both
   inherited, so sub-forks collide in both by construction.'
4. **Consumer + drain seam:** the next dispatch-guards maintenance
   round (forms.md channel-line block + §1 write boundaries); quota
   drain per the OBSERVATIONS rule.

### MERGE 2026-09-12 — 3rd incident, the RECEIVER side: an absolute session name is unresolvable from inside a subagent

1. **Incident + basis:** the lifecycle drain desk (dotfiles-b8)
   briefed four read-only sonnet subagent lanes with a channel
   line naming its own session name as the report address. Two of
   the four hit the wall independently — a subagent resolves only
   `main`/`team-lead`, never a session name — and both worked
   around it correctly. Reported by that desk to this one
   (dispatch-guards' copy holder) with the fix direction already
   named; relayed measurement, not re-executed here — the 2-of-4
   recurrence is the dispatcher's own count.
2. **Class:** the same class, third side. Incident 1 was the
   BOOKING side (attribution of arriving reports), incident 2 the
   GENERATING side (a relative name inherited by forks), and this
   is the RECEIVER side: this entry's own pre-formulated fix —
   name the recipient ABSOLUTELY — cures inheritance ambiguity
   and is itself unresolvable where the receiver is a SUBAGENT,
   whose address space holds only its parent aliases. Absolute
   naming was the two-incident approximation; the invariant under
   all three is that the channel line is written in the
   RECEIVER's address space.
3. **Pre-formulated rule text** (forms.md, channel-line block,
   REPLACING the absolute-naming sentence from incident 2 before
   it drains): 'The channel line names an address the RECEIVER
   can resolve from its own position, verified against the
   receiver kind: a SUBAGENT resolves only `main`/`team-lead`
   (its parent), so its line says the final text IS the report or
   names `main` — never a session name; a FORK inherits context,
   so its line names its creator ABSOLUTELY by agent name, never
   "the dispatcher"; a CROSS-SESSION peer takes the absolute
   session name from ListAgents. A line correct in the sender's
   address space and dead in the receiver's fails only at report
   time, as silence or cross-talk.'
4. **Consumer + drain seam:** same as the host entry — the
   forms.md channel-line block; the two pre-formulated texts
   drain TOGETHER as one rewrite, since applying incident 2's
   text alone would re-mint this incident.

### MERGE 2026-09-15 — 4th incident, the COMPETING-LINE route: a brief's channel line loses to one in a file the brief itself cites

1. **Incident + basis:** dispatch-guards-c2 (executing desk,
   guard-rewrite arc) dispatched lane
   `sonnet-dg45-model-gate-rewrite` with a §2 tail naming
   `dispatch-guards-c2` as the report address, and a grounding
   basis listing the committed directive
   `docs/directives/2026-09-15-guard-rewrite-arc.md` (9b4dbc5).
   That directive carries its own `REPORT-CHANNEL: SendMessage
   dispatch-guards-bc` line — the EXECUTING desk's channel to the
   JUDGMENT desk, not the lane's. The lane read the committed
   file's line as binding on itself and sent its critique-pass
   escalation to the judgment desk. Nothing failed loudly: the
   dispatcher did not know an escalation existed until the desk
   ruled on it, and the desk did not know the lane had bypassed
   its dispatcher. TWO findings in one incident, and the second
   is the one that indicts this carrier: the brief ALSO named a
   session name to a SUBAGENT — exactly incident 3 above,
   re-minted by a desk that had not read this entry before
   composing; the lane hit the wall, SendMessage redirected it to
   `main`, and it reported that in its own closing message.
   Basis: this session's dispatch, the desk's ruling message, the
   lane's report. Scope beyond this arc, reported by dotfiles-89
   and folded in: every desk-delegation directive on this machine
   carries a REPORT-CHANNEL line scoped to its own receiving
   desk, so any such directive listed in a lane's grounding basis
   arms the same ambiguity.
2. **Class:** the same one, and the route is new. Incident 2's
   fix was IN FORCE and did not prevent it: the brief's line DID
   name its recipient absolutely. What the existing predicate
   does not cover is COMPETITION — a second channel line, correct
   for its own reader, reaching the lane through a file the brief
   itself commissioned it to read. A rule about how the brief's
   line is PHRASED cannot close a route where the brief's line is
   phrased correctly and simply loses. Incident 3's recurrence
   here is a second-order finding of the same shape one level up:
   the lesson existed, in this file, and did not reach the desk
   composing the brief.
3. **Pre-formulated rule text**, two halves — the author-side one
   fixes the class at its source for every future directive, the
   sender-side one covers the directives already committed:
   (a) dispatch skill §1, the grounding-basis bullet: 'Where a
   brief names a directive, handoff or runbook file in its
   grounding basis, it states which of that file's channel lines
   binds the LANE — a committed file's channel line is addressed
   to its own reader and is not automatically the lane's, and a
   lane pointed at the file will read it as its own.'
   (b) dispatch skill §4, the handed-off-run channel bullet: 'A
   directive's REPORT-CHANNEL line names its SCOPE — e.g.
   `REPORT-CHANNEL (executing desk -> judgment desk): ...` — so
   the ambiguity never reaches a brief that cites the file.'
4. **Consumer + drain seam:** same as the host entry — the
   forms.md channel-line block plus the two dispatch-skill
   bullets above; drains TOGETHER with incidents 2 and 3 as one
   rewrite, since applying any one text alone leaves the other
   routes open.


## 2026-08-14 — fork skills are the residual spawn channel under the cap, and a fork is self-review by construction

**APPLIED 2026-08-17** — §4 verdict routing: a `context: fork`
inherits its caller's full context, making it self-review, and it is
graded as such; the subagent spawn cap does not close this channel.
Evidence: this commit.

1. **Incident + basis:** the same three-arm probe (dotfiles LEDGER
   2026-08-14, commit `4a40404`) measured: under
   `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1` a subagent loses the
   Agent tool hard and loud ('No such tool available: Agent…'), but a
   `context: fork` skill the subagent invokes forks ANYWAY and
   delivers ('completed (forked execution)'). No misbehavior
   observed — the channel is simply open, and nobody has ever graded
   it.
2. **Class:** a verification label — a fork inherits its caller's
   FULL context and is therefore, by construction, not fresh-context
   verification (it inherits the blind spots along with the framing);
   the cap mechanism does not close this channel, so an executor can
   produce something via a fork skill that LOOKS, in the report, like
   an independent check.
3. **Pre-formulated rule text** (grading side, dispatch skill §2, at
   the fresh-context reference; a mirror in the executor skill is
   conceivable, one fact one home — the maintenance pass decides the
   home): 'A `context: fork` skill inherits its caller's full
   context; a check produced through it is self-review and is graded
   as such, never as fresh-context verification. The subagent spawn
   cap does not close this channel (measured 2026-08-14).'
4. **Consumer + drain seam:** the next dispatch-guards maintenance
   round (grading section §2); quota drain per the OBSERVATIONS rule.

## 2026-08-14 — a stored brief's re-read unit is the entry PLUS its neighbors: a re-grading often sits in the NEIGHBORING bullet

**APPLIED 2026-08-17, merged with the 2026-08-07 entry 'ranked-list
head'** — §1 provenance bullet: the re-read unit is the entry PLUS
its neighbors, a self-built extractor's boundary choice is the basis,
and a repo's own closure check runs before the brief goes out.
Evidence: this commit.

1. **Incident + basis:** a dispatch from a cache-fix session
   (2026-08-14, base `52b8912`): a brief quoted a BACKLOG.md entry
   verbatim from the CURRENT file at compose time — satisfying §1's
   stored-brief clause ('re-read a stored brief's premises against
   the current world') to the letter. The entry was nonetheless long
   closed: the closure sat five lines above it in its OWN bullet
   (BACKLOG.md:3513-3517, 'MECHANISM HALF DONE 2026-08-11
   (`d6647cc`)' … 'PROCEDURE half: DONE separately' … 'Original entry
   follows, RE-GRADED rather than left at READY'), while the original
   bullet (:3518) kept its `READY` header. The dispatcher's extractor
   split on the bullet boundary (`^- \*\*`) and delivered exactly ONE
   bullet — the re-grading sat outside its view. Cost: a sonnet lane
   (~170k tokens) that correctly built NOTHING; the mechanism
   (`lintCaptureAliases`, tools/backlog-lint.mjs:1595) had been done
   since `d6647cc` (2026-08-11), with 10 tests. Secondary harm: that
   same live `READY` header ranked the entry 3rd in a build-order
   derivation.
2. **Class:** the re-read UNIT unnamed + a self-built view. §1 says
   WHAT to re-read, never over what SCOPE — and because a re-grading
   is often written as a neighboring record rather than an in-place
   edit, 'the entry' is the wrong unit. Underneath it, the grounding
   class: the extractor IS the instrument, its boundary choice is the
   basis for the claim 'I read the entry' — and extracting presents
   as LOOKING, not as measuring, so nothing asks for the
   discriminating evidence.
3. **Pre-formulated rule text** (§1, brief family / stored brief): 'A
   stored brief's re-read unit is the entry PLUS its neighbors, never
   the bullet alone: a re-grading is often written as a NEIGHBORING
   record rather than an in-place edit, and the original header then
   keeps its live grade. Where the target repo has its own
   closure/staleness check, it is run over the entry BEFORE the brief
   goes out; otherwise the bullets before and after are read along
   with it. A self-built extractor is itself the instrument here —
   its boundary choice is the basis, not its output.'
4. **Consumer + drain seam:** the next dispatch-guards maintenance
   round (§1, brief-family clause); quota drain per the OBSERVATIONS
   rule.

## 2026-08-14 — the harness block against report files did not catch a German name: `*-bericht.md` went through

**CORRECTED 2026-09-11** — class mis-attributed: this lane took
a 6010-char payload-gate deny at 15:54:25 whose text prescribes a
FILE, and wrote a 6011-byte one. See the 2026-09-11 payload-gate
entry in the live list.

**APPLIED 2026-08-17** — forms.md §2, harness-binding paragraph:
the block is measured against ONE namespace and is no fallback for a
different working language; there, the brief names the assigned data
file as the sole permitted write path and explicitly calls out any
further file as a deviation. Evidence: this commit.

1. **Incident + basis:** discovery dispatch `sonnet-ready-inventar`
   (a READY inventory over pbs-office FEATURE-BACKLOG.md, Aug 14).
   The brief carried the READ-ONLY tail verbatim ('never a report
   file') AND assigned a data file. The agent additionally created
   `ready-inventar-bericht.md` — 6011 bytes, written successfully,
   confirmed by the dispatcher on the filesystem. The harness block
   that, per forms.md §2, rejects 'REPORT.md and kin' with 'return
   findings as text' did not reject this write. A second deviation
   from the same lane: the data file landed in the DISPATCHER's
   scratchpad instead of its own, even though the brief assigned
   'your OWN scratchpad'.
2. **Class:** the reach of a MECHANICAL block that a prose tail
   silently leans on. All that is MEASURED is THAT this name got
   through — what the block keys on (an English-shaped pattern? a
   fixed basename list? a path shape?) is unestablished and therefore
   does not belong in the fix text. The consequence stands
   independent of the cause: in a brief whose working language is not
   English, the block is no fallback, and 'never a report file' is
   enforced there by prose alone. The damage here was small (the data
   was correct), but the context economy the rule protects was
   bypassed — and forms.md cites the block as a binding, i.e. as
   something a brief may rely on.
3. **Pre-formulated rule text** (forms.md §2, harness-binding
   paragraph on the report-file block): 'The block is measured
   against ONE namespace (`REPORT.md` and close English relatives).
   For a brief in a different working language it is NO fallback — a
   German-named `*-bericht.md` went through on 2026-08-14. Where the
   working language is not English, the brief names the assigned data
   file as the ONLY permitted write path and states explicitly that
   any further file — whatever it is named — is a deviation.'
4. **Consumer + drain seam:** the next dispatch-guards maintenance
   round (forms.md §2, harness-binding paragraph); quota drain per the
   OBSERVATIONS rule.

## 2026-08-16 — `git add -N` with a directory argument registers foreign untracked files invisibly

**APPLIED 2026-08-17** — wording in §1 write boundaries (the add-N
clause), de-particularized: the date is out (corpus provenance rule —
in-file only a staleness stamp), the mechanism stands. Evidence: this
commit.

1. **Incident + basis:** a statiker meta session (session record
   2026-08-16, statiker repo dev-notes/OBSERVATIONS, round-3
   dispositions entry): a compound command carried `git add -N docs
   2>/dev/null` — the intent was ONE new brief file; the directory
   argument also intent-to-added FOUR foreign untracked lane briefs
   from a different workstream. Only noticed when a loud stash error
   ('Entry … not uptodate. Cannot merge') surfaced many commands
   later; undone via a path-exact `git reset --`. n=1.
2. **Class:** the directory-pathspec class (§1 already knows it for
   lock/write-set paths: 'names a FILE, never a directory'); `add -N`
   is its unnamed face — the harm is not a co-COMMIT (the pathspec
   commit stayed clean), but silent index state over foreign files,
   which breaks later operations (stash, checkout) or — worse — pulls
   them into a later broad staging.
3. **Pre-formulated fix text** (SKILL.md §1, widening the existing
   add-N clause in the write-boundaries part): after "`git add -N
   <path>` first — intent-to-add registers the path against the empty
   blob …" add: "— and `<path>` names a FILE, never a directory: a
   directory argument intent-to-adds every unowned untracked file
   under it, invisibly (foreign briefs included; measured 2026-08-16
   as a stash broken many commands later), the write-boundary
   directory rule's add-N face."
4. **Consumer + drain seam:** the next dispatch-guards maintenance
   round (SKILL.md §1, write-boundaries paragraph); quota drain per
   the OBSERVATIONS rule.

## 2026-08-16 — the report-file ban at the END of the READ-ONLY tail reads as plumbing, not as binding (statiker beat-the-books, session 11)

**CORRECTED 2026-09-11** — "position is the only variable
changed" does not hold: message size was uncontrolled, and the
payload gate's deny prescribes a file (52 denies that day). See
the 2026-09-11 payload-gate entry in the live list.

**APPLIED 2026-08-17** — the READ-ONLY tail now opens with the ban
plus its named consequence, the scratch assignment sits beside it,
and the two redundant ban half-sentences are removed; the reason (a
binding clause belongs at the block's head) is stated as one sentence
in the tail-boilerplate paragraph.
**Addendum, a finding of THIS pass:** the brief-reminder hook keyed
its READ-ONLY detection on one of the removed half-sentences ('no
repo writes, no report files'), so the restructuring broke a
dependent. The corpus's PREMISE PIN case (expects `context`, observes
`deny`) caught it — making it the red-first proof of the repair, and
the repair is a marker FAMILY (old plus new anchor), so briefs in
flight do not false-fire. Two regression cases with the new tail are
in the corpus, explicitly labeled as regression pins: measured, they
do NOT distinguish the two predicates (they were also green under the
old anchor), so they do not carry the proof. Evidence: this commit.

1. **Incident + basis:** three discovery dispatches (sonnet) in the
   same run, all three carrying the READ-ONLY tail pasted verbatim
   from `references/forms.md` §2. The first TWO nonetheless wrote a
   report FILE and reported only a pointer to it via SendMessage —
   even though the tail carries the ban twice ('never a report file',
   'no report files'). Both also wrote the file into the
   DISPATCHER's scratchpad rather than their own, even though the
   brief explicitly assigned scratch. Both reports were excellent in
   substance — which is exactly why the deviation went unnoticed. On
   the THIRD dispatch, the ban, unchanged in wording, was lifted to
   the HEAD of the brief, with its consequence named ('A file is not
   a report and will not be read as one') — this agent complied. n=2
   violation / n=1 confirmation after restructuring, all three in the
   same run, same brief form, same model, same task class. Position
   is therefore the only variable changed.
2. **Class:** a placement class within the brief — a ban sitting at
   the invariant end of a block reads as transport plumbing rather
   than as an instruction; the same class §1 already knows for the
   route-line seam, and the operator corpus for 'text between tool
   calls is not delivered'. The tail is skimmed as boilerplate because
   it is identical in every brief — exactly the property meant to
   carry it as a guarantee is what makes it invisible. NOT the class
   'executor ignores instruction': two independent agents with the
   same text, and the reversal by mere repositioning, point at the
   brief, not at the executors.
3. **Pre-formulated fix text** (`references/forms.md` §2, READ-ONLY
   tail — pull the ban line to the START of the block and state its
   consequence, instead of letting it ride along in sentences two and
   four): open the block with "NO REPORT FILE. Your findings go in
   your SendMessage reply — a file you write is not a report, is not
   read as one, and reaches no one. Split into labeled parts (1/N)
   past the size gate." followed by the existing wording, minus the
   two now-redundant ban half-sentences. The same holds, mirrored,
   for the scratch assignment: it belongs next to the ban, not in the
   brief's head section, because both concern the same seam (where
   the agent writes).
4. **Consumer + drain seam:** the next dispatch-guards maintenance
   round, `references/forms.md` §2 (READ-ONLY tail); quota drain per
   the OBSERVATIONS rule. Observation provenance: the dispatcher
   tested the restructuring as a repair within the very run, so the
   fix text has already been confirmed live once, not merely derived.

## 2026-08-16 — the harness pulls the mailbox lane's foundation out mid-session: the Agent tool loses `name` + `run_in_background` (Begehung R3, statiker meta-session)

**APPLIED 2026-08-17** — forms.md §2: which lanes EXIST is decided
by a probe of the agent schema PER SESSION, never a date; the
synchronous branch is described as its own branch (no channel-line
paste, the model gate reads `model`, the horizon does not apply), and
the probe rule sits BEFORE the channel lines, so the caveat does not
land behind the default. The mailbox branch is re-stamped 'as of
2026-08-17' — probed in this session: `name` present in the schema,
`run_in_background` absent. 'Re-probe when the schema changes' is
gone, the probe rule replaces it (one fact, one home). Evidence: this
commit.

1. **Incident + basis:** in the running statiker meta session, the
   harness updated the Agent tool's description MID-SESSION:
   '`run_in_background` and `name` are unavailable here — only
   synchronous subagents' (observed 2026-08-16; the same session had,
   hours earlier, successfully run two NAMED dispatches:
   opus-review-078/-080, both mailbox lane). forms.md §2 carries the
   lane binding dated 2026-08-15 ('naming decides the lane',
   forms.md:94-97 read) and the model gate demands a name on every
   generic dispatch. Under the new schema, the named lane is NOT
   EXPRESSIBLE: a desk composing per §2 either gets rejected by its
   own gate or pastes a mailbox channel line for a lane that does not
   exist. §2's own text names the re-probe duty ('Re-probe when the
   Agent tool's schema changes') — this entry IS that re-probe, fired
   positively.
2. **Class:** binding staleness (bindings hold as long as the
   environment holds — and the harness changes the schema
   unannounced, mid-session). A second class observed alongside: the
   convention 'the model rides the NAME' loses its carrier once
   `name` disappears — the model then rides on the `model` parameter
   alone (still present in the observed session).
3. **Pre-formulated fix text** (forms.md §2, binding paragraph +
   channel-line block): tie the lane decision to a PROBE instead of a
   date — 'Before a session's first dispatch of lane-relevant form:
   check whether the agent schema accepts `name`. If it accepts none,
   only the synchronous lane exists: no channel-line paste (the final
   text IS the report, returned as the tool result), the model gate
   reads the `model` parameter, the horizon rule does not apply (a
   sync dispatch cannot outlive the turn).' Convert both dated binding
   paragraphs to this probe; the mailbox description remains as the
   probe's other branch.
4. **Consumer + drain seam:** the next dispatch-guards maintenance
   round (forms.md §2 + the model-gate hook text); quota drain per the
   OBSERVATIONS rule. Immediate consumer: any session dispatching per
   §2 today — until the fix, the probe applies by hand (look at the
   schema, then compose).
   **Addendum, same round (the desk session's counter-probe):** the
   divergence is PER SESSION, not machine-wide — the beat-the-books-cd
   session read its live schema on request: `name` PRESENT, mailbox
   lane alive (an A3 spawn 'via mailbox' in the same window), the
   model gate firing normally; the meta session right beside it had
   lost both. Consequence for the fix text: the probe holds PER
   SESSION ('check YOUR schema'), and a session must never derive
   another session's lane from its own — not even the other way: a
   brief with a mailbox channel line, composed by a session that has
   become synchronous, strands the report.

## 2026-08-17 — an identity check keyed on a field that does not IDENTIFY (§4 slot-(f) rule, refuted an hour after its own release)

**APPLIED 2026-08-17 (written and applied in the same pass)** — §4
slot-(f) grading and §2 slot (f); the entry records the CLASS, not a
blame. Position correction, same round: it first sat under `## Offen`,
even though its own slots 3 and 4 marked it as drained — the mirror
image of the very bug this pass fixed, minted by the same commit and
found by the fresh-context round. Evidence: `5bd8e03`.
1. **Incident + basis:** the §4 rule written in this very pass names
   the commit trailer the 'cheap disproving probe' for slot (f). Its
   own author applied it an hour later to an unexpected commit in
   their own working copy — and got a WRONG attribution: both
   candidates were fable sessions, and the `Co-Authored-By` trailer
   read identically 'Claude Fable 5' for both. Corrected by a peer,
   then checked at the source (`git log -1
   --format='%(trailers:key=Co-Authored-By,valueonly)
   %(trailers:key=Claude-Session,valueonly)'` over `dbbcb76` /
   `84d0e30` / `b115a2d`): author trailer equal, session trailer
   different. A count over 60 commits further shows the session
   trailer is NOT universal (4 of 60 lack one).
2. **Class:** a discrimination question aimed at an attribution
   instrument — the field answers a DIFFERENT question (which model)
   than the one asked (which writer), and where the model is shared it
   returns an answer indistinguishable from the correct one. The
   corpus's instrument-pair rule, applied to identity rather than to
   defects: what is checked is not whether the field has a value, but
   whether two candidates LOOK different in it.
3. **Pre-formulated text:** APPLIED in this pass — §4, slot-(f)
   grading ('the author trailer names a MODEL, so it separates tiers
   and nothing finer … the session trailer, where the harness wrote
   one, is the discriminator; otherwise the trailers have NOT settled
   authorship — ask the holder') and §2 slot (f) on the agent's side.
   Deliberately NOT carried into the EXECUTION tail: the tail is
   pasted per dispatch, and the clause does not help the agent, who
   can resolve identity no better than the dispatcher can — one home
   per meaning.
4. **Consumer + drain seam:** drained in the same round; the entry
   records the CLASS, not a blame. The next round introducing an
   attribution or identity field reads it as precedent.

## 2026-08-17 — a named horizon with no armed alarm is prose that only a WOKEN session can execute (peer handoff, statiker-meta → beat-the-books desk)

**APPLIED 2026-08-17, as ONE amendment together with the sender
half below** — §4 horizon clause: where the expected return is
itself the only alarm (mailbox dispatch, peer handoff, any wait with
no harness-tracked task), the waiter arms the horizon as its own
background timer when the wait begins. Evidence: this commit.

1. **Incident + basis:** the statiker meta session handed off a run
   via the peer channel (a SendMessage handoff, desk
   beat-the-books-e9) and named the expected-return horizon (~2 h to
   the first report) — and, while composing, noticed that the horizon
   rule ('silence past it is a finding, never more waiting', corpus
   Insurance / skill §4) would be triggered by exactly the party
   whose failure it is meant to detect: the waiting session's only
   alarm IS the expected peer message. A dead or stranded peer
   produces permanent silence, indistinguishable from work. Class
   first identified as statiker P17 (Begehung R3, 2026-08-16, parked
   there for desk waits); the premise 'the wake channel is
   unreliable' is measured (the entry directly above: per-session
   mailbox-lane withdrawal, 2026-08-16). An observed stall past a
   named horizon is still outstanding (n=0 for the stall itself;
   today's arming was a manual application, not a fire).
2. **Class:** a horizon named but unenforceable — the alarm is the
   monitored party. (A neighboring class, not a merge: the
   lane-withdrawal entry measures the CHANNEL loss; this one measures
   the missing enforcement half of the horizon rule, which is absent
   even with an intact channel.)
3. **Pre-formulated rule text** (skill §4, at the horizon clause):
   'Where the expected return is itself the only alarm — a peer
   handoff, a mailbox dispatch, any wait with no harness-tracked
   task — the waiter arms the horizon at the start of the wait as its
   OWN alarm: an in-harness background timer (e.g. `sleep <horizon>`
   as a background task) whose expiry re-invokes the session. If the
   timer fires before the report, the silence is the finding the rule
   already names — follow up immediately, do not wait further. A
   horizon with no armed alarm is prose that only a woken session can
   execute.' (No new tool: a bash call; the timer machinery statiker
   P17 parks as 'machinery without a fire' — cron, systemd, an mtime
   watch — stays unbuilt.)
4. **Consumer + drain seam:** the next dispatch-guards maintenance
   round (skill §4, horizon clause); quota drain per the OBSERVATIONS
   rule. Immediate consumer: any session setting a horizon over a peer
   handoff — by hand until the mint (applied that way today,
   statiker-meta session). Cross-reference: statiker BACKLOG P17
   receives the timer as a narrowed candidate mechanism, staying
   parked there on its named evidence.

## 2026-08-17 — a peer-driven desk's report strands in the terminal final text (wave handoff, dispatch-guards desk → dotfiles-f4)

**APPLIED 2026-08-17 (text a); (b) BOOKED** — §4 now carries its
own handoff clause: `REPORT-CHANNEL: SendMessage
<name|operator-terminal>` plus a cadence, and 'consumer named' is not
delivery. Guard candidate (b) is booked as a BACKLOG entry
booked (a marker-gated stop lane as a sibling of report-enforcer,
default-warn, bite-test required) — this entry itself pre-formulated
that outcome. Evidence: this commit + BACKLOG.md.

1. **Incident + basis:** a wave desk handed off via the peer channel
   (opus, dotfiles-f4) delivered its report as its OWN session's
   final text, not via SendMessage, twice within one hour — the
   report reached nobody, the operator saw only 'idle' and asked the
   driving desk (transcript probe `5a243b52`: decision round 16:01,
   restatement 16:14 with its own wording 'since they may not have
   rendered' — the session COULD NOT check its own delivery). n=2 the
   same day, same desk. The handoff itself had named the report's
   consumer (the operator) — what is missing is the CHANNEL:
   'consumer named' reads as delivered, while final text on the peer
   lane is exactly what report-enforcer already prevents for mailbox
   subagents.
2. **Class:** the report-enforcer class one level up — the peer
   executor's report strands in final text because no mechanism at
   the turn's end demands the SEND act. (A neighboring class, not a
   merge: the alarm entry above is the RECEIVER half — detecting
   silence; this one is the sender half — never letting silence
   arise. Together the two are the peer rendering of the §2 report
   duty.)
3. **Pre-formulated text:** (a) skill §4, handoff clause (beside the
   horizon + residue-split): 'The handoff names the report CHANNEL
   machine-readably — a line `REPORT-CHANNEL: SendMessage
   <name|operator-terminal>` — and the cadence (at minimum: every
   decision round, the close report). Final text reaches nobody on
   the peer lane; "consumer named" is not delivery.' (b) guard
   candidate, default-warn: a stop lane as a sibling of
   report-enforcer — fires only when the transcript carries a
   `REPORT-CHANNEL: SendMessage <name>` marker AND the ending turn
   composes substantial final text AND no SendMessage to `<name>`
   sits in the turn; marker-gated, hence near-zero false fires.
   Silent without the marker.
4. **Consumer + drain:** the maintenance-pass round this carrier now
   owes (the banner has reported it since today: ~6 booked vs. ~1
   drained) — text (a) is a §4 amendment (skill-craft-gated, release
   pipeline), candidate (b) goes in as a parked BACKLOG entry with a
   bite-test requirement. The pass debt deliberately grows by one
   with this entry; the driving desk recommends handing the pass to
   the opus desk after wave close rather than running it on fable
   (the guard-vocabulary binding, routing module).

### APPLIED 2026-08-15 — removal is terminal; ordering and three homes

Slot-3 text applied, but the audit found ONE MORE home than the entry
named — and the third was an active contradiction, not a hole:

1. **Writer recipe** (slot-3's target): now carries the binding and
   the sequence — book, lane-close, follow-up, THEN remove. The
   mechanics live here, ONCE.
2. **Reader-worktree clause** — not named by the entry, and the
   sharpest finding: it instructed removing the reader worktree 'at
   the booking of its findings'. Booking is exactly the moment one
   follows up; the clause therefore instructed the losing order. Now:
   booked AND queried, then removed.
3. **§4 mirror duty** (slot 4 asked whether a pointer suffices): no —
   the sentence ASSERTED 'a named/mailbox agent stays resumable after
   its report', which is simply false after a removal. Not a missing
   pointer, but a statement the new binding refutes. Now carries a
   caveat plus a source label.

**Lesson beyond the incident:** an entry naming ONE target site has
not discharged the amendment-audit duty — the rule demands checking
every home of the rule, and the most expensive home was the one
nobody read as affected, because it talked about a different worktree
TYPE. Class: the same reach question as this morning's vocabulary
cascade (0.10.20), a different carrier.

**Evidence:** this commit.

## 2026-08-15 — worktree removal burns the resume channel (statiker E-lane batch)

**APPLIED 2026-08-15 — evidence: the `### APPLIED` block DIRECTLY
ABOVE** ('removal is terminal; ordering and three homes'), which
dispositions this entry. Until the 2026-08-17 pass it carried no
disposition of its own at all: its only exit signal was its POSITION
in the drained section — exactly the reading this carrier no longer
permits. The work itself had landed (plugin/skills/worktree/SKILL.md,
the cleanup clause); the gap was the RECORD, added on the
fresh-context round's finding.

1. **Incident + basis:** after booking lane G's report, the
   dispatcher first removed the worktree (`git worktree remove
   --force`) and only THEN sent the lane-close message (§4 mirror
   duty). The harness refused delivery: 'cannot be resumed: its
   worktree no longer exists, and the fallback directory is not
   covered by the session's isolation fences' (SendMessage error,
   verbatim). The outcome here was benign (report fully booked,
   integration done, write risk structurally zero), but the channel
   is irreversibly closed: even a legitimate FOLLOW-UP to the lane
   (interrogating a booked report — explicitly valued in the target
   repo as a cheap mint source) becomes impossible from the removal
   onward.
2. **Class:** the ordering of two dispatcher duties, the second of
   which irreversibly makes the first unfulfillable — the §1 worktree
   recipe ('remove the worktree after integration') and the §4 mirror
   duty ('book the report AND tell it the lane is closed') both name
   acts but no sequence; the harness binding (resume presupposes the
   worktree) sits in neither.
3. **Pre-formulated rule text** (§1 worktree recipe, the removal
   sentence — an amendment, not a new bullet): 'Removal is the
   TERMINAL act and closes the agent's resume channel (a harness
   binding, measured 2026-08-15: SendMessage to an agent with no
   worktree is refused). Ordering therefore: book the report, send
   the lane close, ask any open follow-up questions of the lane —
   THEN remove. A removed worktree structurally replaces the close
   message (the agent can no longer write), but it replaces no
   follow-up, and that is the expensive piece lost.'
4. **Consumer + drain seam:** the next dispatch-guards maintenance
   round (SKILL.md §1 worktree recipe; check whether a pointer
   suffices for the §4 mirror sentence); quota drain per the
   OBSERVATIONS rule.

### APPLIED 2026-08-15 — the provenance grade binds to the claim's CLASS, not to its citation form

**Incident + basis:** a peer relay, the third brief defect of the
same wave, same root, a NEW slot: the settled design wrote 'enum type
additive' without reading the consumer — the target module holds a
closed, guard-tested dict over the enum, and the bare value would
have broken the guard plus a runtime KeyError. The executor reported
the gap instead of bridging it (the box held — that is the positive
side and belongs in the basis). Together with the two relayed earlier
(a base pin read from the previous day rather than at the tip; a
commit-plan 'none' without opening the hook path), that makes three
slots, one root.

**Triage:** loaded-but-inert three times, NO gap. §1 already carried
the rule — and had already carried the generalization in its bolded
text ('the grade follows the CLAIM, never the section holding it').

**Mechanism of the non-fire**, checked here at the source rather than
taken from the relay: the bold text generalizes, the OPERATIVE
sentence narrows it back down — 'each cited line is either OPENED
…'. The rule was therefore lexically bound to the CITATION form,
while the most expensive cases are repo claims wearing a DESIGN
costume. A design sentence, a base pin, a filled-in form field
present as a dispatcher DECISION — and decisions are executed, not
checked. Exactly the corpus's costume principle, one level down: what
BINDS is decided by the claim; what gets CHECKED is decided by the
presentation.

**Applied** to §1: the bold text now also names the FORM ('never the
section or the FORM holding it'), the operative sentence binds to the
class rather than the form ('every line asserting the target repo's
CURRENT STATE — in whichever slot, wearing whichever form'), and one
sentence names the costume along with the three observed carriers,
de-particularized. The 0.10.23 slot-basis addition is SOURCE-LABELED
in it as a special case rather than opening a second home —
generalizing upward, as the amendment discipline demands before
appending.

**Ordering self-criticism, for the record:** I built the instance
first (0.10.23, the commit-plan slot) and the principle second — the
discipline wants it the other way around ('generalize upward BEFORE
appending'). No harm, since the instance stays valid under the
principle; the lesson is that three relays of the same root already
made the principle visible by the time the first one arrived, and I
took the first for a one-off.

**No hook:** whether a line is a repo claim is judgment, not a
predicate.

**Evidence:** this commit.

### APPLIED 2026-08-15 — the commit-plan slot carries its reading basis

**Incident + basis:** a peer relay from the Georgendorf wave (session
-84), two of its own brief defects, triangulated by itself and
evidenced at the artifact: (a) the commit-plan slot for pbs-website
filled with 'none' without opening the hook path — the repo carries a
commit-msg hook via `core.hooksPath`, and the lane bounced; (b) a
base pin carried over from a previous day's brief rather than read at
the tip, two commits behind, the executor correctly held at the gate.
Citation check here: both cited §1 clauses confirmed verbatim.

**Triage (relay, checked and confirmed here):** loaded-but-inert, NO
gap. §1 already demands both, verbatim — 'commit-blocking guards,
READ at compose time' and Background lines 'grepped by the
DISPATCHER before the brief ships'.

**Mechanism of the non-fire** that carries the sharpening: the clause
'"none" is a valid filling; silence is not' legitimizes the WORD
without demanding its basis. A 'none' written down unread is
lexically indistinguishable from one that was read — the
fakeable-evidence gap skill-craft describes for 'checked all edge
cases', here in the brief's form.

**Applied** to SKILL.md §1, as a CONSOLIDATION rather than an
addition, since this was the second amendment to the same slot in one
day: the slot now demands the READING BASIS per guard ('none (hooks
path read: core.hooksPath=hooks, empty)'), and the doubly-carried
mechanics (payload-guard sequencing) left the slot for the rule
bullet, where it already lives in full. Net 80 → 78 words in the slot
with more coverage — Pareto satisfied rather than merely claimed. The
reasoning sits in the rule bullet, not in the form: a form says what
to fill in, no form teaches.

**No hook candidate:** whether something was read is not computable.
The basis STATEMENT would be grep-able, should brief-reminder ever be
made to lint for it — noted as a candidate, not built (the slot was
only just minted; a lane linting against one-day-old text fires on
every pre-existing case).

**Evidence:** this commit.

### APPLIED 2026-08-15 — bump/push state in the commit plan

Slot-3 text applied to SKILL.md §1, both homes: the commit-plan
paragraph (rule + measured incident) and the skeleton slot (`where
the bump ... sits AND whether it is pushed`). Implemented rather than
merely cited: the addition names the MECHANISM slot 1 itself derives —
the exemption is keyed on the unpushed batch, so the lane cannot
check the condition of its own commits, and the dispatcher who wrote
the premise is the same one who kills it by pushing. Triage per the
entry: loaded-but-inert, no gap — hence a sharpening of the existing
paragraph, not a new bullet (amendment over addition).

Evidence: this commit; the entry follows verbatim below.

### MERGE 2026-08-18 — a FOURTH slot of the same root: an inherited EFFECT claim that travels as a rationale

**Incident + basis:** a language-pass build (pbs-doc
`93d576b`/`7eca7f2`, opus lane, Planungsbüro desk). The builder
reported in its closing report that the pass reads the RAW file
rather than the comment-free lines — the STRUCTURAL half, evidenced.
Attached to it was an EFFECT claim: 'in a repo with large LaTeX
comment blocks, the pass drowns in reference text'. That claim was
inferred from a docstring, never executed. The dispatcher turned it,
unchecked, into a follow-up build instruction ('use `code_zeilen`
instead of the raw file'). During the build the builder refuted it
itself (`hunspell -t` removes LaTeX comments, including `\%`
semantics; a disable probe over 20 `.tex` files: 34 candidates under
both variants, 0 files with a difference) and stopped, rather than
building a change with no effect. Cost: a follow-up round plus a
build instruction that could not be made red. The dispatcher
reproduced the refutation with four lines in seconds — the same
seconds were available while writing the brief.

**Triage: loaded-but-inert, but with a real narrowing.** §1 ties the
provenance grade to 'every line asserting the target repo's CURRENT
STATE' and states as its boundary 'every audit finding turned into a
build step gets its cited line opened once'. An EFFECT/mechanism
claim is neither: it says nothing about the current state, but about
behavior under conditions not actually present in the target repo —
and it travels as the instruction's RATIONALE, not as a citation. So
it carries no grade label and nobody opens it.

**Pre-formulated rule text** (§1, at the provenance clause): 'An
inherited claim about EFFECT or MECHANISM — what would happen, why a
change is needed — is opened, on its transition into a build
instruction, the same as a state claim: the brief names the executed
check or carries the label "unverified". It is the most expensive
class, because it travels as a RATIONALE rather than a citation and
so touches no grade slot; and because a build instruction derived
from it is regularly NOT REDUCIBLE TO RED — the builder only runs
into it at the verifier, one round too late.'

**Consumer + drain seam:** the next dispatch-guards maintenance round
(§1 provenance clause, bundled with the three prior slots). The
builder itself formulated the executor-side mirror half, and it is
sharper than the dispatcher side: a finding that asserts an EFFECT
names its executed check or carries the label — prose findings are
exercised by nothing, unlike everything else that runs during a build
anyway. It belongs in the executor skill.

## 2026-08-15 — the bump exemption consumed by the dispatcher's own push (statiker harvest lane)

1. **Incident + basis:** the lane brief (statiker,
   docs/directives/2026-08-15-harvest-lane-brief.md) stated 'no bump
   is yours — the dispatcher has already landed the version-bump
   commit'. But the dispatcher pushed the bump (0.2.61, `eb1cc9b`)
   BEFORE the dispatch. The payload guard (dotfiles pre-commit,
   unbumped_plugins) keyed its exemption on an UNPUSHED batch: origin
   already carried 0.2.61, so it denied both of the lane's payload
   commits; the lane correctly halted (no `--no-verify`), and the
   resolution cost a full directive round trip (bump ownership handed
   to the lane after the fact, 0.2.62 as its own commit `8b3438e`).
   SKILL.md §1 (commit plan) already names the class: 'a mid-batch
   push moves the basis and re-arms the guard … the dispatcher pushes
   at integration only' — the miss was in application, not a rule
   gap. But the BRIEF slot has no place where the bump's push state
   would become visible.
2. **Class:** a brief premise about guard state that is killed,
   between brief-writing and execution, by the dispatcher itself — a
   special case of the stale-premise class, here with the dispatcher
   on both sides (it wrote the premise AND committed the push).
3. **Pre-formulated rule text** (SKILL.md §1, commit-plan skeleton
   slot, an added sentence): 'Where the dispatcher lands the bump
   ahead of time, the commit plan also names its PUSH state — "bump
   committed, UNPUSHED (exemption armed)" — and the dispatcher does
   not push it before integration; a brief that says only "bump
   already landed" leaves the lane to guess the exemption's
   condition.'
4. **Consumer + drain seam:** the next dispatch-guards maintenance
   round (SKILL.md §1 commit-plan paragraph); quota drain per the
   OBSERVATIONS rule.

## 2026-08-27 — CLASS: a Background line's ASSURANCE reads as its basis — six dispatcher claims shipped true-sounding and unopened, all lane-caught; the form is the fix

**Incident + basis.** Wave-3 peer desk (opus): six grounding failures
in one wave, each a claim passed on without opening the thing itself
— a zero-hit grep over a path that did not exist, a hook probe whose
payload could not fire the guard it claimed to check, "verified by
me" over a lane's own figures, a citation to a decision label naming
a different ruling, a whole-file pin where the register keys on a
section, an item quoted for words it does not contain. Two of the six
were TRUE as sentences and unfounded as claims. Every one was caught
by the executing lane, none by the desk first (wave-3 closing digest,
lesson 1; JOURNAL 2026-08-27). The judgment desk's mid-wave form
change: every Background line carries the command and its hit
inline, or the word "unverified" — landed in §1's skeleton at
`e582e9a` (wave 4, lane A2); this is that site's carrier entry.

**Class.** §1's provenance rule already says each line is OPENED at
brief time; what it lacked was a FORM whose absence is visible — a
pledge to open relapses, an inline hit does not (corpus, Grounding:
only a form whose absence is visible binds). The executor reads the
provenance, never the assurance.

**Pre-formulated rule text.** Landed (§1 skeleton, `e582e9a`). Open
half, booked in BACKLOG (PARKED, wave-4 A2 gap 3): the new sentence
and the pre-existing "OPENED at brief time, or graded unverified"
sentence overlap; the merge is a corpus edit under
`CLAUDE-maintenance.md` and must keep the read-based basis's reach.

**Consumer + drain seam.** The fire-rate review: does the next wave's
desk ship an unopened Background line, and does a lane catch it.

drained → `43f2a99` (wave-5 head item (ii)) — the critique pass, both
halves. Executor §1 rule 1 now names the ARTIFACT the check already
implied: the lane's FIRST return is one message naming the unopened
Background line and the two contradicting brief lines. Dispatch §1
commissions it and names its channel, so the ABSENCE of that message
is dispatcher-visible. Revised in place rather than added as a new
numbered rule — renumbering would have falsified the "conduct rule 5"
cross-reference in the dotfiles devbook. The open half this entry
booked in BACKLOG (the merge of the two overlapping §1 provenance
sentences) is untouched and still open.

## 2026-08-27 — CLASS: an accepted deviation updates the lane's report and leaves the SOURCE ENTRY's done-criterion standing, now falsified

**Incident + basis.** The carriers-English backlog entry
(`BACKLOG.md`, READY 2026-08-27) specified its verifier as
`grep -rlE '[äöüß]' dev-notes` returning 0. Lane
`sonnet-d2-carriers` then proved by execution that three German
literals must STAY, because `check_observations_tail` parses them
(`check-doc-drift.py:332-334, 382-383`, plus ~8 `--test` fixtures):
full translation red on an isolated copy, anchors-only revert green,
confirmed both ways. The lane reported this correctly as a DEVIATION
under slot (d), the dispatcher accepted it and graded the lane, and
the source entry was not touched — so from the moment D2 landed
(`437159c`) the entry carried a done-criterion nothing could satisfy.
Found only because the judgment desk asked for an unrelated routing
fix to the same entry; amended at `eefffda`. Nobody was going to
re-read it otherwise: the item was, correctly, considered handled.

**Class.** The deviation form points at the BRIEF — "deviations from
the brief, each with its reason" — and the brief is derived from an
entry that no step re-opens. So a fact strong enough to overturn the
spec lands in a report, is accepted, and the entry that will generate
the NEXT brief keeps the overturned criterion. The failure is silent
in the worst way: the stale criterion reads perfectly reasonable, so
the next lane chases it and its halt or its broken checker presents
as LANE error rather than entry error. This is the spec-sentence
versus verifier-sentence disagreement one level out from code — and
the accepting desk is the only party that ever holds both halves at
once, which is why no lane can catch it.

**Pre-formulated rule text** (§4, the dispatcher's integration acts):
an accepted deviation RE-ASKS THE SOURCE ENTRY'S DONE-CRITERION
before the lane is booked closed. The integration names the source
entry, and either states that its criterion survives the deviation or
amends it in the SAME commit that books the lane. Where the source is
a lifecycle item the id is known and this is a refusal at the write
path; where it is prose, §4 carries it. Accepting a deviation without
that step books a lane closed and leaves a trap for the next one.

**Consumer + drain seam.** The next dispatch-skill maintenance pass
(§4). Scheduled companion, so this entry is not the only mover: the
judgment desk booked the sweep as wave-5 head item (vi) (dotfiles
`49d8e68`) — one discovery lane over all four carriers for verifiers
predating a deviation recorded against them. Deliberately not run
during wave 4, which is still closing.

drained → `43f2a99` (wave-5 head item (vi), PROSE HALF ONLY) —
dispatch §4 carries this entry's pre-formulated text as a dispatcher
duty: an accepted deviation re-asks its source entry's done-criterion,
the integration naming the entry and either stating that its criterion
survives or amending it in the SAME commit that books the lane. The
MECHANISM half — the refusal at the write path where the source is a
tracked item and its id is known — is NOT built: it lands in the
lifecycle repo, outside that change's write set, and stays owed.

## Offen

Live entries — the list appends grow. What stands here has not left
via the maintenance pass, for the reason named at each ENTRY; this
header does not enumerate them, so it cannot go stale against the
actual count (an earlier version said 'the three below' while five
stood here — a label outliving its own body).

## 2026-08-17 — residue: the devbook texts, home outside this copy
(drained 2026-09-14, SPLIT disposition below)

**RESIDUE (maintenance pass 2026-08-17) — home outside this working
copy:** the pre-formulated text amends the guard-checker-build
devbook in the dotfiles repo (that repo's CLAUDE.md, §Registered
procedure). This session holds the dispatch-guards copy, not
dotfiles (one writer per working copy), so the entry has NOT drained
here and is not booked as such. Seam: the devbook's next amendment
there. Check on who drives it at close: this session reports the
three texts to the dotfiles desk and to the operator; it is done
only once the devbook carries them.
**Status 2026-08-17, at this pass's close:** the TEXTS are booked in
the owning repo (dotfiles `b3571ca`, a READY entry with a LEDGER
line, checked at the source); they are not APPLIED there. An entry
booked elsewhere is not an applied one — the distinction stands here
because a booking reads, on first glance, like being done. Stays
open, consumer unchanged.
**Drained 2026-09-14 → dotfiles `4b7b032` + this repo `21e9038`,
SPLIT — not a flat "applied," which would be false in two
directions:** texts (1) and (3), plus the 2026-08-19 fourth, are
APPLIED in the dotfiles devbook (4b7b032; new section fingerprint
df2fa416…); text (1)'s mutation-proves-applied fragment landed
NOWHERE — already covered by the devbook's ONE-STEP-EARLIER
paragraph (dotfiles CLAUDE.md:862-877), amendment over addition;
text (2) is NOT in the devbook — dispatcher-side by subject, it
RE-HOMED into this repo's own dispatch §1 (21e9038, the
knob-AND-environment clause's mounted-machinery member), grading
and ruling recorded on dotfiles df-210 and df-25. A reader
hunting the devbook for text (2) is the drift this split mark
exists to prevent. Driven per the entry's own close-check: the
seam (the devbook's next amendment there) arrived 2026-09-14 and
the judgment desk holding this copy drained it.

## 2026-08-12 — the battery invocation is part of the instrument: `-k` hides fixtures, `-x` hides arms (3 incidents, 3 lanes)

1. **Incident + basis (3×, two days):** (c, Aug 13, dispatch
   `opus-helfer-kopien`, caught and reported by the lane itself)
   applying the mutation is the same arrangement half: a hand-typed
   replacement pattern matched 0×, the battery ran GREEN over the
   UNAPPLIED mutation — indistinguishable from 'the test does not
   exercise this', and it was nearly booked as a red proof. Repair in
   the lane: the mutation is read from the file by line range, the
   removed text printed before every run; the dispatcher's own
   control bite ran on Aug 13 with the same application proof.
   (a) e1 from dispatch `opus-abw-drei-waechter`: a mutation battery
   run with `pytest -k "antwort"` — the selector excluded exactly the
   fixture meant to catch the mutation; the battery read green.
   Caught by divergence between two measurements (13 findings on
   record, fixtures silent). (b) an e-addendum from dispatch
   `opus-abw-sichtweite-austrag`: a battery run with `-x` — only the
   FIRST failure per mutation was visible, which systematically hid
   which test arm NEVER fires; 'all mutations red' was true and still
   said nothing about the unproven arm (test_sichtweite_elementfeld…,
   only fixed in `46a5831` on the dispatcher's follow-up question).
   The matching expectation-side note: a SILENCE expectation is only
   as sharp as the set of report forms it is silent over — if the
   guard fires a DIFFERENT form under the defect, it stays satisfied.
2. **Class:** instrument arrangement — the BATTERY INVOCATION
   (selector, abort flags, failure evaluation) is part of the
   instrument; any narrowing (a name filter, first-fail abort) makes
   a silence unreadable that is indistinguishable from a true pass (a
   sibling of the devbook step-4 class 'a green bite needs its
   arrangement checked').
3. **Pre-formulated fix text** (devbook guard-checker-build, step 4,
   ONE addition for both halves): 'The mutation/bite battery runs
   over the WHOLE test file, never over a `-k` name selection and
   never with `-x`: the selector otherwise excludes the catching
   fixture, and first-fail abort hides which arms never fire — both
   yield a green/red indistinguishable from the real thing. Where the
   question is the defect→arm mapping, the FAILURE LIST is evaluated
   per mutation; a silence expectation names ALL of the guard's
   report forms. And the mutation PROVES its own application — the
   mutation tool shows the removed/replaced text or aborts hard when
   the pattern did not match: a green battery over an unapplied
   mutation is indistinguishable from a dead test (measured
   2026-08-12/13, three lanes: -k e1 · -x addendum · 0× pattern,
   helfer-kopien).'
4. **Consumer + drain seam:** the next amendment of the
   guard-checker-build devbook (dotfiles CLAUDE.md, §Registered
   procedure) — bundle with other open step-4 additions; every
   amendment resets the fingerprint (eval-open).

### MERGE 2026-08-13 — 4th incident, a new mechanism of the same class: the .pyc cache makes one arm parrot its neighbor

An FB-101 addendum (opus-emission-telemetrie, pbs-projekt): mutation
A2 showed exactly A1's hit list — Python validates a .pyc via (source
mtime in SECONDS, source SIZE), and A1/A2 were byte-identical in size
(12253 each) and ran 0.09s apart; the second run executed A1's
bytecode. A neighbor's parroting looks like a normal result; only the
list not matching the mutation gave it away. Fixed in one place
(PYTHONDONTWRITEBYTECODE=1 + a `__pycache__` purge before every run;
each arm now prints its own file size); all three of the lane's
batteries repeated under the lock, results unchanged. Fix-text
addition (to be worked into slot 3 of this class): 'The battery
driver locks the bytecode cache (PYTHONDONTWRITEBYTECODE=1 + a
`__pycache__` purge per run) — two mutations of equal file size
within the same mtime second are indistinguishable to the cache, and
the second arm otherwise parrots the first, green and unremarkable.'

## 2026-08-13 — a globally hooked check step runs in EVERY test: fail-loud over repo-external artifacts collides by construction with temp fixtures

1. **Incident + basis:** dispatch `opus-helfer-kopien` (FB 3.89,
   session `ddd83862`): the brief decided 'script missing → ERROR,
   never silent' for a guard globally hooked into `pruefe()` that
   reads a script in office_repo and helpers in two sibling repos.
   Built spec-faithfully: 119 of 818 tests went red, because every
   temp fixture (`mach_office`) builds an office_repo WITHOUT
   `tools/` and points `dev_root` at an empty temp tree. Executor
   STOP with three MEASURED paths (A: fixture surgery, +17s suite; B:
   a HINT throughout; C: mixed, 2 failed/816 passed); desk decision:
   path C. Per three conftest comments ('otherwise EVERY graph test
   would carry the HINT'), the repo had already hit this class three
   times before — the brief composition had not read that precedent.
2. **Class:** brief composition for globally hooked guards with
   repo-EXTERNAL artifacts. The fail-loud contract is decided against
   the production picture, but the step runs first and a thousandfold
   in the TEST environment, whose fixtures by construction do not
   provide the external artifacts — the guard's absent-case IS the
   fixtures' normal case.
3. **Pre-formulated fix text** (devbook guard-checker-build,
   brief-composition step): 'Where a guard hooks globally into a run
   that also stands under tests, the brief answers BEFORE the build:
   what does this step see in the test environment (fixtures read,
   not guessed)? For every repo-external anchor (sibling repo, config
   path, tool script), the brief carries the decided grade for the
   absent case — fail-loud only where the environment guarantees the
   anchor; otherwise the visible degradation grade (a HINT line per
   run) WITH its own pinned test. Precedent in the target repo
   (conftest comments, sibling steps) is mandatory grounding for
   brief composition.'
4. **Consumer + drain seam:** the next amendment of the
   guard-checker-build devbook (dotfiles CLAUDE.md, §Registered
   procedure) — bundle with the open step-4 additions; the amendment
   resets the fingerprint (eval-open).

## 2026-08-13 — grade assertions over the WHOLE report do not distinguish grades; multi-line passthroughs carry the marker only on line 1

1. **Incident + basis:** the FB-102 build (opus-emission-telemetrie,
   pbs-projekt ende_check): the mutation 'exit!=0 grade WARNING →
   HINT' ran GREEN through the first battery pass (34 passed) — the
   assertion checked `"WARNING" in out` over the entire report, and a
   WARNING from a different check happened to sit there anyway. Only
   a helper that isolates the telemetry ENTRY (exactly one, else
   abort) and checks the grade on its own line made all six mutations
   bite. A second finding in the same build: the passed-through
   report output is MULTI-LINE, the marker (`[telemetrie]`) sits only
   on line 1 — a reader taking 'the message' silently truncates the
   finding lines, and the passthrough check goes blunt without going
   red (also affects the helfer-kopien precedent case).
2. **Class:** assertion sharpness in report gates — a predicate
   checked against the AGGREGATE can be satisfied by any other check
   (the same 'both outcomes satisfy it' class as in the Fixing
   corpus, here as a report instance), and marker conventions (marker
   only at a block's start) make a single-line reader silently
   incomplete.
3. **Pre-formulated fix text** (devbook guard-checker-build, step-4
   addition): 'Grades are checked on their OWN line, never on the
   report — the test isolates the entry of the step under test
   (exactly one, else abort) and checks grade + content there. Where
   a step passes through a multi-line block, the test reads the
   BLOCK up to its end marker, never only the marked first line.'
4. **Consumer + drain seam:** the next amendment of the
   guard-checker-build devbook (dotfiles CLAUDE.md, §Registered
   procedure) — bundle with the step-4 additions already waiting
   there; the amendment resets the fingerprint (eval-open).

**Position addendum, 2026-08-17 (maintenance pass):** this entry was
appended at the file's END by a third session and thereby sat in the
`## Abgeflossen` section — with no disposition, so READABLE as drained
without being so. Only the position is changed, the wording stands
untouched. The trigger is structural, not personal: whoever appends
writes to the file's end — which is why the live list now sits there,
and a doc-drift check pins the order.

### MERGE 2026-08-18 — 2nd incident, a new mechanism of the same class: the message has TWO BLOCKS, and `in stderr` does not distinguish them

1. **Incident + basis:** a YAML-parse lane in the global `pre-commit`
   (dotfiles `6c1ba7b`, opus lane from the Planungsbüro desk). The
   addendum gave the lane a SECOND report section ('COULD NOT BE
   CHECKED') beside the blocking one. Its bite — removing
   ComposerError from the defect set — stayed GREEN: the assertion
   checked `"alias.yaml: ComposerError" in stderr`, which is true in
   BOTH worlds, because on misclassification the same line moves
   word-for-word into the other block; `rc==1` also stayed true
   because a second defect kept blocking. The lane read the green as
   a finding about its own assertion rather than as an acquittal,
   sharpened it (a split on the blocker header + an absence check in
   the other block), and got the red.
2. **Class:** identical to the parent entry — a predicate on the
   AGGREGATE can be satisfied by any other part of the output. NEW is
   the trigger: it is not a FOREIGN check supplying the satisfying
   line, but the mechanism under test ITSELF, via its second section.
   So the parent wording ('the test isolates the entry of the step
   under test') does not apply here: the entry IS isolated, it just
   sits in the wrong block.
3. **Pre-formulated fix text** (devbook guard-checker-build, step 4,
   to be appended to the parent addition): 'Where a mechanism emits
   more than ONE report section, the assertion names the SECTION,
   never just the text: it checks that the line sits in the expected
   block AND in no other. A misclassification between two sections
   otherwise produces the same character sequence as the correct
   outcome — the bite is then true in both worlds.'
4. **Consumer + drain seam:** unchanged — the next amendment of the
   guard-checker-build devbook (dotfiles CLAUDE.md, §Registered
   procedure), bundled with the step-4 additions waiting there.

## 2026-08-18 — a freshly built MEASUREMENT is itself an instrument, and its result reads as already finished (2 incidents, 2 lanes, one day)

1. **Incident + basis:** (a) the language-pass build (pbs-doc
   `93d576b`, opus lane): the baseline run gave 209/185 instead of
   the 183/159 named in the brief. The cause was the counting
   pipeline, not the subject — with MULTIPLE file arguments
   `hunspell` prefixes every output line with `<file>: `, so `sort
   -u` counted file-token PAIRS instead of tokens. Exposed only by
   comparing against an independently taken second count (the
   dispatcher's); without it, 209 would have been booked as a finding
   about the baseline. (b) the YAML lane (dotfiles `518a78d`, opus
   lane): the baseline was taken from a scratch copy of the tool —
   the tool itself warns that it measures the LIVE checkout. A
   'baseline from the copy' is no baseline at all for a tool like
   this.
2. **Class:** an ad-hoc measurement (a counting pipeline, a report
   diff, a baseline run) presents as LOOKING, not as measuring —
   nothing demands its proof, and its output already arrives in
   answer form. The corpus has the rule (Grounding, the instrument
   pair); what is missing here is its edge in the brief: the verifier
   slot commissions the NUMBER, never the probe on the instrument
   that produced it.
3. **Pre-formulated rule text** (§1, the verifier clause of a brief
   expecting a baseline NUMBER): 'Where a brief names an expected
   baseline number, it demands the number AND the form of its
   collection: which command, over which population, with which
   known-positive case as a control. Where the measured number
   diverges, the first hypothesis is the MEASUREMENT, not the
   baseline — and a baseline is taken BEFORE the installation, never
   from a copy afterward, where the tool measures live state.'
4. **Consumer + drain seam:** the next dispatch-guards maintenance
   round (§1 verifier clause) and the next amendment of the
   guard-checker-build devbook (dotfiles CLAUDE.md, §Registered
   procedure, step 2/5) — that is where the baseline half lives.
   Immediate consumer: any session writing a baseline number into a
   brief — by hand until the mint.

## 2026-08-18 — the devbook sentence stands as an INCIDENT NARRATIVE where an instruction is needed

1. **Incident + basis:** the YAML lane (dotfiles `518a78d`). Step 2
   of the guard-checker-build devbook demands that the OLD side
   preserve every path premise derived from `__file__` — the text
   says this, but as a narrative of two 2026-08-10 incidents ('too
   narrow in one direction … the same one level further out'). The
   lane reports explicitly: read as an instruction, it would have
   copied too narrowly; it took the whole tree via `git archive` only
   because it TRANSFERRED the narrative onto its own case. That is an
   achievement of the reader, not a property of the text.
2. **Class:** devbook form. A rule existing only as an incident
   report demands the executor derive the predicate from the
   example — exactly the design work the devbook is meant to move
   ahead of the dispatch. It goes unnoticed because a good reader
   performs it silently.
3. **Pre-formulated fix text** (devbook guard-checker-build, step 2,
   a header sentence placed before the narrative): 'The OLD side is a
   copy of the WHOLE WORKING TREE (`git archive HEAD`), not of the
   changed directory — every path premise derived from `__file__`
   must resolve inside it. The check for this is the copy's own
   self-check running GREEN, before any red from it is believed. The
   two incidents below show what "too narrow" looks like.' The
   existing narrative text stays below it — it carries the evidence.
4. **Consumer + drain seam:** the next amendment of the
   guard-checker-build devbook (dotfiles CLAUDE.md, §Registered
   procedure); the amendment resets the fingerprint (eval-open), so
   bundle with the other waiting step-2/4 additions.

## 2026-08-17 — a brief names a schema-derivation source that does not carry the LANE CLASS to be derived at all (statiker P16 lane)

1. **Incident + basis:** a build brief (statiker stop-hook lane,
   2026-08-17) instructed the executor to 'derive the blocking
   stop-hook schema from the reference plugin dispatch-guards' — but
   the plugin carries NO blocking Stop/SubagentStop lane at all
   (writer-reservation-gate only warns, report-enforcer only injects
   additionalContext). The executor ran into the dead end, correctly
   fell back to the harness SOURCE (~/dev/reference/claude-code:
   processHookJSONOutput, stopHooks.ts), and reported the deviation
   under the brief's pre-authorized repair class. No harm — but only
   because the stronger source was present locally and the executor
   found it.
2. **Class:** a brief claim about a SOURCE whose mere existence was
   checked at brief time, but not its CONTENT — the §1 rule 'opening
   a REFERENCE is not opening its CONTENT', here in the derivation
   variant: the source exists but does not carry the class meant to
   be derived from it.
3. **Pre-formulated rule text** (§1, at the
   schema-bearing-external-facts clause, or as its own item): 'A
   brief naming a DERIVATION SOURCE ("derive the schema/pattern from
   X") checks, at brief time, that X actually CARRIES the class to be
   derived — a grep for the class's signature suffices; merely
   opening the source does not. Where X does not carry the class, the
   brief names the real source or explicitly commissions the search.'
4. **Consumer + drain seam:** the next dispatch-guards maintenance
   round (§1 text); quota drain per the OBSERVATIONS rule. Immediate
   consumer: any session composing derivation briefs today — by hand
   until the mint.

## 2026-08-17 — the signal ABOUT the machinery, read as a statement about the WORK (spawn receipt; an alarm that outlives its lane)

1. **Incident + basis (two faces, each measured):** (a) an opus
   verifier dispatch acknowledged 'Spawned successfully … via
   mailbox' and died seconds later on the weekly limit — the failure
   arrived as a SEPARATE notification. A trivial sonnet lane from a
   sibling desk returned the same string and ran through fine. One
   return value, opposite outcomes: the receipt distinguishes nothing
   about the RUN. (b) two horizon timers armed in the same session
   fired AFTER their lanes had reported and closed — n=2 the same
   day, both harmless, both from the same hole: the freshly written
   §4 clause says the waiter ARMS the horizon, and stops there.
2. **Class:** a signal ABOUT the machinery (a launcher receipt, an
   alarm, a scheduler exit) is read as a statement about the WORK.
   The corpus names the general form — a launcher reports THAT it
   ran, never WHAT it found; these two are its dispatch instances and
   bite at opposite ends: a receipt that asserts too much, and an
   alarm that outlives its subject. A false alarm on the very
   instrument whose whole job is to make silence legible trains
   exactly the reflex that dismisses the next real silence.
3. **Pre-formulated text** (§4, at the horizon clause, ONE sentence
   for both halves — an arm-only rule is exactly what produced the
   false alarm): 'A spawn's return value is a launcher receipt: it
   proves the START and says nothing about the run — a lane that dies
   seconds later acknowledges the same as one that runs through, and
   its failure, if it arrives at all, comes as its own separate
   message. Conclusions about capacity, liveness, and sizing wait for
   a REPORT. And the waiter DISARMS its horizon timer the moment the
   report lands: an alarm that outlives its lane fires on a closed
   one and turns the next real silence into noise.'
4. **Consumer + drain seam:** the next §4 round; booked here and NOT
   applied, because this pass's release is already through and one
   more payload commit for a single sentence is not worth the
   round — the booking is the exit, not a deferral.

## 2026-08-17 — predicate WIDENING silently devalues old fixtures of the same form; running green is not enough (statiker mint batch, P27)

1. **Incident + basis:** while widening a verdict predicate (statiker
   P27: CLOSURE_ABSENT now accepts terminal [BIT] rounds with no
   design-changing disposition as SATISFIED), three existing suite
   sites (2 tests, 1 contract fixture) silently changed MEANING — all
   three shared a form (a bare [BIT] round, no findings, no D-line)
   that was must-fail under the old predicate and ran vacuum-green
   under the new one. The lane found them by a form SEARCH over the
   suite, not via the test run (which was green); executor report
   lesson 3, commit `522e8d2` (statiker).
2. **Class:** widening an accept set turns old fixtures of the same
   form into vacuum passes — the fixture-stops-testing class (Fixing
   corpus: a predicate GAINS a value) at the widening seam, where the
   green run hides the hole exactly.
3. **Pre-formulated rule text** (§1, at the verifier or settled-design
   clause of a build brief widening a predicate): 'A brief that
   WIDENS a verdict/gate predicate also commissions a FORM SEARCH
   over the suite, beside the test run: every existing assertion
   whose fixture carries the newly accepted form is enumerated and
   dispositioned as still-testing or vacuum-green — a green run alone
   does not distinguish the two.'
4. **Consumer + drain seam:** the next dispatch-guards maintenance
   round (§1 text); quota drain per the OBSERVATIONS rule. Immediate
   consumer: any session composing predicate-widening briefs today —
   by hand until the mint.

### A handoff naming ONE channel has a single point of failure — a fallback channel saves the report when the sender dies before it

**1. Incident + basis.** 2026-08-18, immediately after the 0.11.3
pass. A peer desk (pbs-office backlog) handed this desk three work
items and named the report channel TWICE: 'SendMessage to this
session — or to the operator in the terminal, if you prefer; they
issued the assignment and are reading along.' The interim report went
via SendMessage and LANDED (success). The CLOSING REPORT, less than
an hour later, failed: `No agent named 'planungsb-ro-schulz-96' is
reachable`, and ListAgents no longer listed any `planungsb-ro-*`
session. The sender had vanished between the two messages. Also
visible in the log: the desk called itself `planungsb-ro-schulz-7f`
in its own channel line, while the harness listed it as `-96` — two
identifiers for the same sender.

**2. Class.** Not the horizon (that is an hour old and lives in §4),
but its MIRROR on the reporting side: §4 today demands
`REPORT-CHANNEL: SendMessage <name|operator-terminal>` — ONE channel,
as an either-or. But the channel can die between assignment and
report, and then the named home is empty. Nothing was lost here
because the sender named a SECOND one on its own initiative; the
rule does not demand this. That is the positive control: the very
discipline that saved the report is not prescribed by the skill.

**3. Pre-formulated rule/fix text** (§4, at the handoff clause):

> The channel line names a FALLBACK, not just a target:
> `REPORT-CHANNEL: SendMessage <name>, fallback <operator-terminal>`.
> A peer channel can die between assignment and report — the sender
> closes, its identifier changes — and the receiver only learns this
> on sending, i.e. after the work is done. Without a named fallback,
> the finished report is then homeless, and the receiver, in doubt,
> decides it away. The fallback is always reachable: the operator.

**4. Consumer + drain seam.** The next dispatch-guards round (§4
text). Not built immediately, because this pass's release is already
through and a payload commit plus bump for one sentence is not worth
the round — the booking is the exit, not a deferral. Immediate
consumer: any session accepting a handoff today — ask for the
fallback by hand until the mint lands.

<!-- NEUE EINTRÄGE ANS DATEI-ENDE, UNTER "## Offen" — dies ist
     die lebende Liste. Abgeflossenes steht OBERHALB. Der
     doc-drift-Check erzwingt genau diese Reihenfolge, weil ein
     Anhängen am EOF sonst im abgeflossenen Abschnitt landet. -->

- 2026-08-18 **writer-reservation-gate names the WRONG repo on
  cross-repo commits** (n=2 the same evening, both from a dotfiles
  session: a subagent commit in `~/dev/Gunther-Schulz/claude-worktime`
  and a desk commit via `git -C .../claude-worktime` — both WARNs
  named the dotfiles working copy plus a foreign holder, even though
  no named path touched it; correctly reported by the subagent as a
  'misdirected/stale warning' rather than acted on). CLASS: a guard
  resolving its target from the SESSION context instead of the
  COMMAND — the working copy is read from the session's cwd, not from
  `-C <path>`/the git call's effective target; a WARN about an
  uninvolved repo is the fires-on-a-non-defect shape and trains
  dismissal of exactly the warning that will one day be real.
  PRE-FORMULATED FIX TEXT: the gate resolves the command's target
  working copy BEFORE comparing (`-C` argument, else the bash call's
  cwd) and warns only if THAT copy is reserved; the self-probe adds a
  pair: a commit with `-C` into a foreign, unreserved repo → silent, a
  commit in the reserved copy → WARN (both arms must differ).
  CONSUMER + DRAIN SEAM: the next build touching
  `writer-reservation-gate`, or the next dispatch-guards maintenance
  round.
  **n=3, 2026-08-19** (cache-fix desk, lane
  `sonnet-backlog-close-home`, commit `d2f9520` in
  `~/dev/Gunther-Schulz/dotfiles`): the WARN named
  `~/dev/vendor/claude-code-cache-fix` — the dispatching session's
  PRIMARY cwd — as the disputed working copy, while the commit
  correctly sat in dotfiles via pathspec. Third instance, third
  DIRECTION of the same root: the two 08-18 cases ran from a dotfiles
  session into a foreign repo, this one from a cache-fix session into
  dotfiles — target resolution therefore follows the SESSION, not the
  command, regardless of which repo plays which role. The
  pre-formulated fix above covers this case unchanged; nothing to
  change in it, only the counter and the citation.
  What this class additionally costs, and it is the argument for
  building the fix rather than counting further: the agent correctly
  reported the WARN as misdirected and did NOT act on it — three
  times running, the executor's discipline has now caught the
  guard's mistake, rather than the other way around. A guard that
  depends on being ignored in order not to cause harm is the
  fires-on-a-non-defect shape in its terminal stage.
  **n=4, 2026-08-23** (lane `opus-report-provenance`, three commits
  `f6b7d94`/`554e36c`/`dbdd81a` in `~/dev/Gunther-Schulz/dispatch-guards`):
  the WARN named `/home/g/wan2gp` — the DISPATCHING session's cwd, a
  repo this commit does not touch at all. Fourth instance, fourth
  configuration: session cwd repo A, command cwd repo B, and neither
  one is dotfiles. Confirms the 08-19 diagnosis with nothing new —
  target resolution follows the session, never the command — and the
  agent again reported the WARN rather than acting on it: four times
  running, executor discipline catches the guard. Nothing to change
  in the pre-formulated fix above, only the counter and the citation.

## 2026-08-20 — native worktree isolation cuts the SESSION repo; sibling-repo dispatch from a non-git cwd fails loudly at spawn

- **Incident + basis:** a dispatcher whose cwd was a non-git project
  folder dispatched a build targeting a sibling repo (dotfiles) with
  `isolation: "worktree"` — harness error "Cannot create agent
  worktree: not in a git repository", one retry cost. The
  agent-dispatch PreToolUse advisory already documents the class
  (its classes 1–3: session-repo cut, sibling-repo provisioning,
  sibling-under-isolation reclaim hazard) — but it arrives WITH the
  call it would have prevented, so it can only inform the retry,
  never the first attempt.
- **Class:** brief-composition guidance gap (SKILL.md §1 worktree
  recipe) — the recipe's "prefer native isolation" sentence does not
  say WHOSE repo native isolation cuts.
- **Pre-formulated fix text** (for §1, the worktree recipe's
  harness note): "Native isolation cuts a worktree of the SESSION's
  repo (the cwd), never the brief's target repo — from a non-git
  cwd it fails at spawn, and for a SIBLING-repo brief it is the
  wrong isolation even when it succeeds: provision the target copy
  yourself, or dispatch without isolation under shared-copy
  discipline."
- **Consumer + drain seam:** the maintenance pass (quota-triggered)
  applies or discards; consumer of the fix is any dispatcher
  composing a sibling-repo brief. Note: this file carried a foreign
  uncommitted entry at append time — this entry is left uncommitted
  with it (shared-file commit serialization).

## 2026-08-23 — CLASS: a corpus with a compression layer takes TWO edits, and nothing announces the second

- **Incident + basis, n=2, both in `references/forms.md` §2:**
  (1) 2026-08-23, this lane — a report-provenance rule commissioned
  to bind the EXECUTING agent landed in §2's prose, which that agent
  does not read; it reads a pasted tail. As landed the rule bought
  dispatcher-side grading only. Caught by the skill-craft review's
  information-flow pass (item 14: walk the lifecycle, ask WHO
  DELIVERS each step), not by any check, and the dispatcher who
  commissioned it did not notice the half was missing either.
  (2) pre-existing, recorded by §2 itself: the channel and payload
  rules "have reached executing agents only as gate denials, at
  doubled composition cost" until they were tailed. Same file, same
  failure, one earlier.
- **Class:** rule-delivery gap. Where a corpus has a COMPRESSION
  LAYER — a pasted tail, a template, a generated summary, any
  artifact that re-renders the corpus for a second audience —
  landing a rule in the corpus is half the change. The other half
  has no tell: the edit is complete, the file reads correctly, every
  check is green, and the obligated party never receives the rule.
  The generic trigger is not "forms.md" but "this rule obligates
  someone who reads a rendering of this file, not this file".
- **Pre-formulated fix text** — mechanical, because the delivery
  question is computable here where the rule's own predicate is not:
  a `check-doc-drift.py` lane that, for each §2 clause naming an
  obligation of the EXECUTING agent, asserts a corresponding clause
  in both tails. The honest bound: "clause naming an agent
  obligation" is not machine-decidable over free prose, so the
  implementable form is a declared REGISTER — §2 clauses marked as
  agent-binding carry a token the lane keys on, and the lane fails
  when a marked clause has no tail counterpart. Without the marker
  the lane would be a keyword checker over prose, which is the
  fires-on-non-defects shape this repo already names.
- **Consumer + drain seam:** the next dispatch-guards maintenance
  round. Booked as the CLASS on the dispatcher's explicit
  instruction, not as the instance — the instance drained the same
  day (see Abgeflossen, ANGEWANDT 2026-08-23) and would otherwise
  have taken the class with it.

## 2026-08-26 — CLASS: the local push record confirms the comfortable answer; only the remote's push log says what a push carried

- **Incident + basis, n=1** (cache-fix `main`, shared checkout, two
  desks): a peer desk pushed at 10:41:50 local; the judgment desk had
  committed `eee549c` ten seconds after the peer's `01eba49`, inside
  the window the pre-push suite opened. The peer's push carried it.
  The peer then VERIFIED it had not, with two executed checks: `git
  merge-base --is-ancestor eee549c 01eba49` (false — asks whether the
  foreign commit sits BELOW the pushed one; a commit that rides out
  by landing ABOVE returns false by construction) and the range
  printed by the pre-push hook (`9697603..01eba49`, resolved before
  the suite ran). Its own `git reflog show origin/main` also read
  `01eba49 … update by push`. The remote settled it the other way:
  GitHub's PushEvent for that second records `9697603..eee549c`.
  Basis: `gh api repos/<fork>/events` PushEvent log, read at the
  judgment desk; the peer re-ran it and concurred.
- **Class:** effect-site verification, push face. The §1 claim rule
  already says the push set is the branch and the claim log runs as
  its own invocation before the push; this instance is the CHECK
  AFTER the push — every local instrument (ancestry test, hook
  printout, `origin/main` reflog) records what the client believed
  at some earlier instant, and all three return the comfortable
  answer for exactly the case being ruled out. Executing an
  instrument is not executing the right one.
- **Pre-formulated fix text** (for §1's push-set bullet, one
  sentence after "an unexpected commit halts the push"): "What a
  push CARRIED is settled only at the remote — `gh api
  repos/<o>/<r>/events` PushEvent `before..head` for that push, or
  the remote branch's reflog where the host exposes one; the local
  `origin/main` reflog and the pre-push hook's printed range record
  the client's belief at hook time and read clean for a commit that
  landed during the suite." Mechanizable slice: the
  push-claim-reminder's post-push face could print the remote
  range; unbuilt, and the window it closes is seconds wide — the
  one-act rule (claim and push, uninterrupted, on a copy nobody else
  commits to) is the real fix and already stated.
- **Consumer + drain seam:** the next dispatch-guards maintenance
  round applies the sentence to §1 or discards with a reason.

## 2026-08-26 — CLASS: a report channel that names a PEER SESSION does not resolve from inside a subagent; the lane's own first-part "cannot resolve your channel" is a blocker, not a note

- **Incident + basis, n=1 (five lanes exposed, one bitten):** a peer
  desk (cache-fix-b4, opus) briefed five sonnet lanes with `Report
  channel: SendMessage to claude-code-cache-fix-b4`. That is a SESSION
  name; from inside a subagent it does not resolve. One lane said so in
  part 1 of its report and routed to `team-lead`, where four parts plus
  two re-sends sat unread; the desk demanded twice, then verified the
  work at the artifact and reported the lane as never having reported —
  correct work, wrong conclusion, in the direction that blames the
  lane. The other four lanes reached the desk anyway, which is why the
  defect stayed invisible. Desk's own correction, same day, digest
  edited in place.
- **Second instance, same day, n=2 (three lanes exposed, none
  bitten):** the begehung desk (`begehung-c7`, opus) briefed three
  router lanes for a Tier-1 eval with its OWN session name as the
  report channel; SendMessage refused it in every lane, all three
  fell back to `main` and said so, nothing lost. Same class from the
  other side of the mailbox — the dispatcher wrote its peer-visible
  name where the executor needed `main`. Recorded against the run,
  not the skill under eval. Two desks, two mints of the same costume,
  one day: the hook flag below is earning its slot.
- **Class:** channel-line resolvability. The §2 channel line binds to
  `name` at dispatch time; what it must ALSO bind to is a target the
  EXECUTOR can resolve — the dispatcher's agent name where the
  dispatcher is itself an agent, `team-lead`/`main` where it is a
  session. A session name in the line is a costume of the right form.
  Second half: the escalation ladder (demand, demand, verify at the
  artifact) is built for a STALLED lane and, run over a lane that
  delivered to the wrong mailbox, manufactures a confident wrong
  finding.
- **Pre-formulated fix text** — for forms.md §2, the channel-line
  block, one sentence after the named/unnamed pair: "The target named
  is one the executing agent can RESOLVE: a peer session's name is not
  — from inside a subagent the dispatcher is `team-lead` (or the
  dispatching agent's own name); a first-part 'I cannot resolve your
  channel' is a blocker the dispatcher answers before anything else,
  never a note." Mechanizable slice: the brief-reminder hook can flag a
  `Report channel: SendMessage to <x>` where `<x>` matches a session
  name pattern (`<repo>-<2hex>`) rather than an agent/team name.
- **Consumer + drain seam:** the next dispatch-guards maintenance
  round applies the sentence to §2 (and the hook flag, if the pattern
  holds) or discards with a reason.

- **Third instance, 2026-08-28, n=3 — AND IT REFUTES THIS ENTRY'S OWN
  PRE-FORMULATED FIX.** Wave-5 peer desk `dotfiles-a7` (opus) briefed
  an opus lane with `Report channel: SendMessage to the dispatcher` —
  a ROLE WORD, the third bad spelling after a session name and a peer
  name. The lane inferred a recipient from a plausible-sounding agent
  name and sent 3 messages to a SIBLING LANE, then 7 to `team-lead`.
  It reached the desk only after a send to `dotfiles-a7` ERRORED with
  the resolving answer: "this process's own main session … address the
  main conversation as `main` instead."
  **The correction to the fix text above: `team-lead` DOES NOT
  RESOLVE.** This entry's pre-formulated sentence offers "from inside a
  subagent the dispatcher is `team-lead` (or the dispatching agent's
  own name)"; applied literally it reproduces this incident, because
  seven sends to `team-lead` reached nobody. The address that works
  from inside a subagent is `main`.
- **The quiet half, which is the worse one and is new at n=3.** The
  n=2 begehung case had SendMessage REFUSE the bad target in every
  lane — the loud direction, nothing lost. Here all ten misdirected
  sends returned `success: true` with a routing line naming the target,
  and the lane reasonably read ten receipts as ten deliveries. A
  receipt proves the message was WRITTEN to an inbox, never that it
  reached the intended reader. So a misaddressed channel is not
  reliably self-announcing, and "no error" is not evidence of arrival.
  The available probe is one deliberate send whose ERROR carries the
  right address — cheap, and available from the lane's first turn.
- **Second mechanism gap, lane-side:** `ListAgents` is not available to
  a subagent, so the standing "lane existence is a per-session PROBE"
  rule has no instrument on that side of the boundary. The probe a
  subagent DOES have is the erroring send.
- **Revised pre-formulated fix, superseding the sentence above:** the
  brief carries the report address in the form THE EXECUTOR MUST TYPE.
  For a subagent of a main session that is `main` — not the desk's
  peer-visible session name (`<repo>-<2hex>`), not `team-lead`, and
  not a role word like "the dispatcher". Mechanizable slice, widened:
  the brief-reminder hook flags a `Report channel:` target that is a
  session-name pattern, the literal `team-lead`, or a bare role phrase
  containing "dispatcher" with no addressable token — all three are
  measured non-resolvers now.
- **Retracted same day (not a second instance): a "no messages
  received" line in a lane's final part was read as a
  dispatcher→subagent delivery failure; the lane had in fact received
  both messages, which CROSSED its closing report — the documented
  async behaviour state tokens exist to date. n stays 1, the class
  stays outbound-only. Kept from the misread, on timing grounds the
  forms already state: a mid-flight correction may arrive after the
  work it meant to change. CORRECTED SAME DAY, in place: "a brief is
  complete at dispatch" is a promise a brief in a LIVE repo cannot
  keep — the same desk amended a brief in place three times after
  dispatch, and all three messages missed the lane — measured across
  three dispatches the same day: every message ARRIVED, every one
  HOURS after the work it was meant to redirect (W1a: after its
  report; W1c: after its report and its own re-read). LATENCY, never
  loss — corrected twice at the execution desk, which twice read a
  lane's inbox line as a live measurement rather than a claim true at
  composition time; the cure was one message to the live source, not
  spent either time. The re-read point is the only half that has
  worked in time on this machine. Trigger, improved by the W1c lane
  against the version that flattered it: keyed to BEFORE EACH VERIFIER
  RUN, not before each commit — a commit-keyed rule fires only in lanes
  that commit into a shared tree and fires late; verifier-keyed it
  fires in every lane (read-only and verifier lanes included) and
  before the build; the commit stays as the backstop. The lane's own
  catch was a WRITE-SAFETY habit (re-read HEAD before committing into a
  shared public tree), not a reading discipline; the lane found the
  change only because it re-read the brief at HEAD before committing
  into a shared repo, a discipline it brought (finder: the W1c lane,
  `opus-w1c-lifecycle`, 2026-08-26). The rule that holds: a brief in a
  live repo NAMES A RE-READ POINT — re-read the brief at HEAD before
  each commit — a mechanism, where "assume no corrections" is a hope
  that fails silently in the direction where the executor builds
  against a dead design. Cheap corroboration: the brief's own stated
  line count (243) was stale by seven within the session. Pre-formulated
  §1 text: "A brief committed into a live repo carries `Re-read: this
  file at HEAD before each verifier run, and before each commit; a
  change is a gap to report, never bridged.`" The misread's own lesson stands: an unverified negative
  that agrees with a suspicion already held is where the free probe is
  owed.

## 2026-08-26 — CLASS: a dispatcher-instrument defect surfaced by an executor gate — the falsifiable gate in front of any lane the desk cannot recompute

- **Incident + basis, n=2 in one arc (corpus-ablation arc, dotfiles,
  peer desk `dotfiles-0e`, opus):** a sonnet enumeration lane was
  briefed with a mandatory instrument gate — six measured
  line-vs-normalised pairs it had to reproduce before emitting. The
  gate was DEFECTIVE: the dispatcher had compared lines-containing a
  phrase against occurrences of it, two different quantities. The lane
  computed exactly what was specced, got six equalities, HALTED
  without emitting, and ran an unrequested control of its own
  (newline→space only) that isolated the cause. Two dispatcher defects
  were found this way — the bad control table and a record-boundary
  rule reaching 12% of the target file — neither by dispatcher review,
  both within one lane round-trip.
- **Class:** dispatcher-instrument defect surfaced by an executor gate.
  Generalises §1's instrument-positive clause from sweep-shaped work
  to ANY output the dispatcher cannot independently recompute.
- **Pre-formulated rule text** — for §1, beside the sweep-shaped
  instrument-positive clause: "A brief whose output the dispatcher
  cannot independently recompute carries a FALSIFIABLE INSTRUMENT GATE
  the executor reproduces before emitting — a pre-measured pair with a
  known mover and a known non-mover. A HALT on that gate is priced as
  the gate working, never as a lane failure. The gate's own numbers
  are the dispatcher's claim and as falsifiable as anything else in
  the brief; the executor reports a discrepancy rather than adjusting
  toward the stated expectation."
- **Consumer + drain seam:** the next dispatch-guards retirement pass
  applies the sentence to §1 or discards with a reason. Landed by the
  judgment desk on the peer desk's text (its write set excluded this
  repo).

## 2026-08-26 — CLASS: the writer-reservation gate's Bash-lane WARN names the SESSION's held copy regardless of what the command touches (corrected in place the same hour — first written as a worktree→main resolution bug, which understates it)

- **Incident + basis, two independent records, OBSERVATIONAL, not
  reproduced headless:** (1) wave-2 L1 lane (opus, cache-fix
  worktree): four WARN fires all naming the same held copy
  (`…/vendor/claude-code-cache-fix`), two on commands that ran no git
  at all (a `mktemp -d` probe), one on a commit in the LIFECYCLE
  repo — the named copy was not the repository being committed to.
  Reported by the wave-2 desk (`dotfiles-a7`) from the lane's
  hook-context blocks re-read against its own record of each call.
  (2) The judgment desk's own session (cwd cache-fix, held by another
  session): every `cd <other-repo> && git commit … -- <path>` and
  every `git push` in dotfiles and dispatch-guards that day drew the
  same WARN naming cache-fix — n≈10 in the transcript. In staging
  mode that lane would DENY commands having nothing to do with the
  held copy, naming the wrong repo in the denial.
- **What the source says, and it contradicts the observation:** the
  docstring states the reservation is per-`git-dir` ("a worktree
  reserves separately"); `commit_targets()` resolves a `cd` prefix
  and returns "none" for a command with no `git commit`; the WARN
  wrapper is `_dispatch_common.py:286`. Headless probes by the
  judgment desk of the INSTALLED copy (byte-equal to source) with
  three payload shapes — `mktemp -d`; `cd dotfiles && git commit`;
  and the positive control, a plain `git commit` in the held cwd —
  were ALL silent. The positive control's silence means the probe
  environment did not reproduce the live condition, so the negatives
  are could-not-verify, not exoneration. Root cause NOT established;
  `_base_dir()` (payload cwd) and whatever runs before
  `commit_targets()` in the live PreToolUse flow are where to start.
- **Class:** a guard whose warning text is independent of the command
  it warns about — a session-level lookup wearing a per-command
  verdict's form. WARN-only today; the fix belongs BEFORE the lane
  leaves staging.
- **Reproduction step owed, first:** the gate under the live hook
  environment (a real session with a foreign holder on its cwd copy)
  with the three payloads above, stdout captured — the positive
  control must WARN before any negative is read.
- **Pre-formulated fix text**, conditional on the reproduction: the
  Bash lane emits nothing unless `commit_targets()` returns "targets"
  AND a target's git-dir carries a foreign reservation; a worktree's
  git-dir is its own. Bite: planted worktree commit under a held main
  copy → silent; non-git command in a held cwd → silent; plain commit
  in the held cwd → WARN.
- **Consumer + drain seam:** the next dispatch-guards maintenance
  round runs the reproduction, then applies the fix or records why the
  observed behaviour is intended.


**Second sighting, same day, unverified.** `dotfiles-a7` recalled across a compaction that the gate fired naming a copy other than the one written; no artifact pointer survived. Consistent with this entry; counts as testimony until re-observed with the command text.

## 2026-08-26 — CLASS: a COMPOSED figure inside an EXECUTED digest inherits the digest's standing, and the relaying desk carries it unmarked

**Incident + basis.** A peer desk's step digest (dotfiles-e0, wave 2
dotfiles slice) carried five figures; four were executed output, one
(`kind sweep`: "828 tracked files unregistered, 5 kinds claim 12") was
composed — the verb had never been invoked. The judgment desk relayed
all five to the operator in one sentence, unmarked. The peer caught it
itself ten minutes later on running the verb (executed: 264 of 275,
11 claimed — magnitude off ~3×); its FIRST run had also graded the
wrong repo (cwd persisted inside the plugin checkout; `kind sweep`
without `--repo` resolves the enclosing work tree — a clean, real
verdict about the wrong subject). Basis: the two peer messages and the
desk's operator message, this session, 2026-08-26 ~19:40Z.

**Class.** The attachment costume (corpus, Grounding) at the REPORT
seam: a derived or composed sentence attached to executed neighbours
inherits their standing; the relay (corpus, desk-delegation: a relayed
figure is marked machine-computed or estimate) fired on neither side
because the figure did not PRESENT as an estimate. The wrong-repo
half is the anchor rule (Fixing): a verb keyed to cwd measures whatever
cwd is.

**Pre-formulated rule text** (§2 report form, the figures clause):
"Every figure in a digest names the command that produced it, inline
or in a footnoted block; a figure with no command is written
`(composed)`. A dispatcher relaying a figure carries the command or
the mark with it." And for the executor skill's tool-invocation
binding: "A repo-scoped CLI (`lifecycle`, and any verb resolving the
enclosing work tree) is invoked with its explicit `--repo`/`-C`; cwd
persists across Bash calls and is not a scope."

**Consumer + drain seam.** The dispatch skill's §2 forms
(`references/forms.md`) at the next retirement pass; the executor
skill for the invocation binding. Both fire-earned: n=1 composed
figure, n=1 wrong-repo verdict, same peer, same hour.

## 2026-08-26 — CLASS: "load forms.md" leaves the tool open, and a Bash read of the plugin-cache path draws the config-directory prompt every time

**Incident + basis.** Operator report: many sessions hit a permission
prompt on `sed -n '/^## 2\./,/^## 3\./p' ~/.claude/plugins/cache/…/forms.md`
when loading the §2 report form. Executed the same hour: settings.json
allows `Bash(*)` and `Read`; the Read tool on the identical path draws no
prompt. So the prompt is the harness's `.claude/`-path-shape protection on
Bash command text (corpus, environment: the config-directory binding),
not a missing allow rule, and allow rules do not lift it (n=many sessions).

**Class.** A load instruction that names the source and not the
instrument; the reader picks the shell habit, and the shell is the one
executor the protection watches.

**Pre-formulated rule text** (SKILL.md section map and forms.md head,
wherever "load" appears): "Load with the Read tool. A Bash read (`sed`,
`cat`, `grep`) of any path under `~/.claude/` draws the config-directory
permission prompt regardless of allow rules; Read does not."

**Consumer + drain seam.** The dispatch skill's next retirement pass;
applies to every skill that says "load" of a plugin-cache file
(skill-craft's pointer form: the pointer names the instrument too).

## 2026-08-26 — CLASS: three guards over-fired on a session doing what the discipline instructs — the careful path is where the override reflex gets trained

**Incident + basis.** OBSERVED by the wave-2 execution desk
(`dotfiles-a7`, its four-slot file, booked here by the judgment desk;
entries 2–4 observed in-context, entry 6 recalled across a compaction
and held as unverified). (a) `restrict-bash-paths` blocked a read-only
probe because shell `case` branch patterns in the command text parsed
as path tokens; the same probe in Python passed; nothing was written.
(b) `worktree-config-gate` warned `git -C <wt> config --get-all
remote.origin.pushurl` — a pure READ run to VERIFY push denial — as a
shared-config write, full remediation text. (c) `brief-reminder` WARNed
a dispatch for lacking `## Commit plan` while the substance sat under
"Commit convention" in prompt and brief file. Held, unverified: (d)
brief-reminder rejecting a brief POINTER for a missing tail the named
file carried — same axis as (c), merges into it if substantiated.
None overridden; cost was attention and one rewritten probe.

**Class.** Over-fire on legitimate work (corpus, Fixing: a check that
fires on a non-defect trains the reader to discount red). Two
sub-shapes: a TEXTUAL predicate that cannot tell a shell pattern from a
path, or a read form from a write form (a, b); a STRUCTURAL predicate
over a semantic requirement satisfiable under another name or in
another place (c, d). (b) is the sharpest: the gate fires on the
command that checks the guarantee it protects.

**Pre-formulated rule text.** (a) exempt tokens in `case`/`esac`
pattern position from the path scan, or docstring the shape as a known
false fire with "rewrite the probe" as the repair. (b) exclude `--get`,
`--get-all`, `--get-regexp`, `--list`, `-l` from the shared-config-write
lane. (c) accept a declared synonym set (`Commit plan`, `Commit
convention`, `Commits`) or say in the WARN that the check is
HEADING-KEYED so the reader repairs the heading, not the substance.
(d) none until substantiated.

**Consumer + drain seam.** The three guards' next predicate change;
the retirement pass. The over-fire count is the metric: n=3 in one
session on the careful path.

## 2026-08-27 — CLASS: the writer-reservation WARN names a DIFFERENT working copy than the one being committed

**Incident + basis.** n=2, two repos, one day (wave-4 peer desk
`dotfiles-2f`, lane B0): committing in dispatch-guards, the gate
WARNed naming the DOTFILES working copy and the judgment desk's
session as holder; lane B0 saw the same on its lifecycle commits.
The WARN text reads as though it concerns the copy being committed;
it does not — it reports a reservation elsewhere on the machine.

**Class.** An instrument's label wider than its predicate (corpus,
Grounding): the reader takes "held" as "THIS copy is held" and either
halts a lane that is free, or learns to discount the warning where it
is right. Held unverified until the hook's source is read: whether
the gate enumerates all reservations or resolves the wrong git dir.

**Pre-formulated rule text.** The WARN names the copy it is about in
its first line, and says in words that it is NOT the copy being
committed where that is so; a `--test` bite plants a reservation on a
sibling copy and asserts the wording. Read the source first — the
fix follows the mechanism, not the symptom.

**Consumer + drain seam.** The reservation gate's next predicate
change; the retirement pass.

**Firing record, 2026-09-15 (n=3, new candidate mechanism).** Drain
desk dotfiles-f1, lifecycle wave 1, lane A: the gate named a repo
that was not the one being committed to, twice in one wave. The
desk offers — as probable cause, explicitly not a verdict, code
path unread — that the attribution tracks the shell's CURRENT
directory rather than the commit target. That is a concrete
candidate for this entry's open "held unverified" question; the
pre-formulated text stands, and the source read it demands now has
a specific hypothesis to confirm or kill.

## 2026-08-27 — CLASS: a check over a carrier whose entries MOVE anchors on body text, never on a heading

**Incident + basis.** Wave-4 lane A2: its own quote-fidelity battery
anchored on the observation entry's HEADING; the drain step rewrites
that heading as it moves the entry, so the check died on the very act
it was grading. The lane named the silent direction: a heading that
merely SHIFTED would have left the check reading a narrower slice and
reporting the same green. Sibling finding, same lane: a red's
divergence OFFSET is a function of the clause's PLACEMENT (1780 at
tail, 0 at head), so an offset quoted from a prior lane's red is
provenance and never an expected value (booked, BACKLOG READY).

**Class.** What a check anchors to must be immutable (corpus,
Fixing): a heading in a carrier that moves entries is live state, and
the quiet failure is the one that stays green.

**Pre-formulated rule text.** Quote-fidelity and drain checks anchor
on a body sentence that the move preserves verbatim; the check's
positive control runs AFTER a planted move, not only before.

**Consumer + drain seam.** The next dispatch-skill maintenance pass;
any brief commissioning an apply-the-text-verbatim lane.

## The brief's scope sentence is a dependents claim, and nothing prompts the search

**Incident + basis.** Wave-4 lane C1 (dotfiles, 2026-08-27). The brief
specified growing a constant's value set — `RECORD_PFADE` in
`git/hooks/pre-push` — and asserted "Nothing else changes. No new
constants, no refactor, no fallback paths." The dispatcher never ran a
dependents search on the SYMBOL. One existed:
`tools/commit-provenance.py` reads `pp.RECORD_PFADE` in production and
RESTATED its length as `"of 3"` in two selftest assertions, so the
specced change turned the shared tree red at `./dot test` and the lane
had to halt at its write boundary and return it as a question. The
search that closes it is one command —
`grep -rn --no-ignore-files 'RECORD_PFADE' . --exclude-dir=.git` — run
afterwards by the dispatcher, 4 code hits outside the owning file, all
in the one dependent. Sibling fact, same incident: the dispatcher HAD
measured a 34-file reader set for the same carrier hours earlier and
listed that very file in it, and still did not connect it — a
dependents list for the CARRIER is not a dependents list for the
SYMBOL, and holding the first is what made the second feel done.

**Class.** Changes to anything others depend on break silently wherever
dependents were not search-established first (corpus, Grounding). The
corpus states the rule at the CHANGE, and the tell it names is the
change landing without its search — but under a dispatch the change
lands at the executor while the scope claim is made in the BRIEF,
hours earlier and in a different voice. A brief sentence reads as the
dispatcher's own decision, and decisions are executed rather than
checked (dispatch skill §1, the provenance rule's FORM half), so the
one line asserting the blast radius is exactly the line no one grades.

**Pre-formulated rule text.** A brief that changes a NAME, TYPE, SHAPE,
VALUE SET or MEANING carries the dependents search for that symbol —
command and hits — in the brief itself, and each hit is dispositioned
in the write-set or named as out of scope with its reason. A bare
"nothing else changes" is the search skipped, visible in the brief. The
search is keyed on the SYMBOL, never on the artifact the symbol lives
in: a reader set for the file answers a different question.

**Consumer + drain seam.** The next dispatch-skill maintenance pass;
§1's write-boundary section, beside the realization-surfaces rule which
already resolves DESIGN prose to files and stops short of resolving
SYMBOLS to their readers.

## 2026-08-27 — CLASS: the prescribed horizon instrument — a background `sleep` whose exit re-invokes the session — was killed externally four times in one day

**Incident + basis.** Judgment desk `claude-code-cache-fix-d8`, one
session, ~9 background timers armed per §4 ("a `sleep <horizon>`
whose exit re-invokes the session"). Four were reported `killed` by
the harness within seconds to minutes of arming (task ids bngvdvjnv,
buy90ntfi, bx864f7rl, bjbg38reo; two of them back-to-back at 12:12),
none by this desk; five ran to completion. No pattern established
(not the command form, not the timing); the desk switched to the
`Monitor` tool (a polling loop emitting events, exiting on its own
horizon), which was not killed once across ~10 arms. Mechanism,
supplied by the peer desk from its own side the same evening: its
`pkill -f "sleep NNN"` to DISARM a spent horizon killed the calling
shell twice (exit 144) — the kills cluster on the retirement of a
spent timer, not on arming or firing, so the failure is in how a
timer is disarmed on a shared machine, and a timer dead at arming and
one dead at disarm are indistinguishable from the waiting end.

**Class.** The dead-lane detector itself dying silently — an armed
horizon that is killed reads, from the desk's side, exactly like one
that has not fired yet, so the wait it guards becomes unbounded
without any signal. The one thing that separated the two here was
the kill NOTIFICATION arriving; where it does not, the horizon is
gone and nobody knows.

**Pre-formulated rule text** (§4, the arming clause): the horizon
instrument is a Monitor-style poll that emits an event on the
artifact's every move AND on the horizon (so a live lane re-arms
silently and a dead one fires), armed with a timeout; a bare
background `sleep` is the fallback only where Monitor is absent, and
a `killed` notification on it is a re-arm, never a no-op. Retire the
`sleep` wording or mark it "observed killed 4/9, 2026-08-27".

**Consumer + drain seam.** The next dispatch-skill maintenance pass
(§4 arming clause); the corpus Insurance bullet's "background timer"
phrase, same fact.

## 2026-08-27 — CLASS: a translation brief changed text the repo's own checker parses, and nothing in the brief form asked which literals were load-bearing

**Incident + basis.** Peer desk `dotfiles-2f` briefed lane
`sonnet-d2-carriers` to translate the three dev-notes observation
carriers from German to English (write set: `dev-notes/` only). The
brief named files, boundaries, verifier and grounding, and said
nothing about which strings in those files something else PARSES.
`tools/check-doc-drift.py` keys `check_observations_tail` on exactly
two of them: `_LIVE_HEADING = "## Offen"` and `_DRAINED_HEADING =
"## Abgeflossen"` (333-334), matched by `drained_re`/`live_re`
(382-383), plus the `_APPEND_MARKER` constant (332) and roughly
eight `--test` fixtures built from the same literals. That marker's
text is deliberately NOT quoted verbatim here: the check matches it
by substring over the whole file, so an exact quote would plant a
SECOND append marker in the carrier it governs and move `marks[-1]`
onto this entry. An observation about a literal cannot always carry
the literal — read it at the cited line. The lane translated everything, watched "observations tail"
go red on an isolated repo copy, reverted only the two anchors, and
confirmed the pass both ways — an executed pair, not a read — and
reported the keep as a deviation. The dispatcher's independent
dependents search (repo-wide grep on the two literals, positive
control non-zero) returned the same set: agreement on a shared
coordinate, not one instrument's green.

**Class.** The dependents question, which the corpus already carries
for names, types and value sets, does not fire when the thing being
changed is PROSE — a heading, a marker, a section title that a
checker reads. A translation, a section rename, a reflow all present
as editing text for humans, so nothing prompts "what parses this?".
Here the check went red at the end, which is the cheap direction;
where no check exists the anchor drifts and the mechanism keying on
it stops firing while still reading green.

**Pre-formulated rule text** (§1, the brief's write-boundary block):
where a brief changes the TEXT of a file the target repo's own
tooling parses, it names the dependents search as a step — grep the
repo's checkers and tools for literal strings drawn from the write
set BEFORE the first edit, with a positive control. Each anchor found
is dispositioned in the brief: kept with the reason stated, or moved
in the same change together with its checker. Where the write
boundary excludes that checker, "keep the anchor" is the only
available answer and the brief says so, rather than leaving the lane
to discover it by going red.

**Consumer + drain seam.** The next dispatch-skill maintenance pass
(§1, the brief form's write-boundary block). Single home here: the
dotfiles guard/checker devbook only meets this if a translation lane
is ever run under it.

## 2026-09-10 — CLASS: a skill swept for fire-rate has no stated rule population, so two careful sweeps cannot agree on what they swept

**Incident + basis.** Corpus fire-rate review, window 08-06→09-10
(dotfiles `docs/directives/fire-rate-review-2026-09-10.md`; close
digest at the review desk `dotfiles-6d`, graded at `statiker-f0`).
Two lanes independently swept `plugin/skills/executor/SKILL.md`
for per-rule dispositions and returned DIFFERENT populations from
careful readings: 13 rules (§1's 7 + §3's 5 devbook-form elements
+ §2's 1) against 9 (§1's 7 + §2's 1 + line 112's embedded bold
sub-rule, §3 excluded with the stated reason that its elements
spec what a DEVBOOK contains, not executor conduct). The review
desk read the structure at the artifact and graded BOTH counts
defensible — the population is genuinely ambiguous. No verdict
moved (every row in both readings is FIRED or
NO-OCCASION-not-retirement), but a sweep whose population is
ambiguous cannot assert coverage: its invariant reconciles
against a count the sweeper chose, not one the artifact declares.

**Class.** The coverage-assertion form of the restated-basis
problem, one level up: a fire-rate sweep's completeness claim
needs a comparison basis the GRADED SOURCE declares, and a skill
that never states its own rule population forces every sweeper to
mint one — two honest sweeps then differ and neither is wrong.

**Pre-formulated rule text** (executor SKILL.md, a one-line
declaration; generalizes to any skill the fire-rate review
sweeps): the skill states its own rule population — a count with
the enumeration rule that produces it ("N rules: §1's numbered
list + §2's principle; §3 specs the devbook artifact, not
conduct") — so a sweep's coverage invariant reconciles against
the artifact's own declaration, and a population dispute is a
finding about the skill, never about the sweep.

**Consumer + drain seam.** The next executor-skill maintenance
pass (the declaration lands there); the next fire-rate review's
sweep briefs cite the declared population instead of minting one.

2026-09-10 — CLASS: gate-coverage boundary limits corpus relocation.
Incident + basis: the corpus-relocation ablation (dotfiles
claude/records/corpus-relocation-2026-09-10/) derived its candidate set
against this plugin's hooks.json and found the dispatch-skill-gate matcher
(Agent|Task|Workflow) leaves SendMessage handoffs outside the forced skill
load — 2,238 words of peer-channel conduct (delegation protocol, peer
traffic, horizon mechanics) therefore cannot move behind the skill and stay
always-loaded. Class: gate-coverage boundary as a relocation constraint.
Pre-formulated fix text: extend the dispatch-skill-gate matcher to
SendMessage calls whose payload is handoff-shaped (a GO, a queue pointer, a
message after which the peer is expected to act — membership by function per
the site corpus peer-traffic rule), so the forced load covers the peer
lane's compose moment; false-fire risk: plain fact-traffic sends must NOT
demand the load, so the predicate needs a handoff classifier — if that
predicate is not computable with near-zero false fires, this stays prose
and the 2,238 words stay in the corpus. Consumer + drain seam: the next
dispatch-guards design pass; ALSO gated on the operator's CULL state for
new governance machinery in the site corpus (operator GO required there).
CONSTRAINT (operator decision, first-hand 2026-09-10, statiker-f0: "i want
as little heuristic chat triggers as possible"): a classifier or heuristic
read over peer-message CONTENT is off the table for this gate — acceptable
variants are structural predicates only (tool name, first-use-per-session,
mechanically readable state), and if no structural predicate carries it,
the resolution is DON'T BUILD: the 2,238 words stay always-loaded. This
narrows the pre-formulated fix above — its handoff-classifier clause is
dead under the constraint unless the operator reverses it.

## 2026-09-10 — CLASS: the dispatcher is a co-writer too — mid-batch dispatcher acts inside a lane-held copy broke the lane's gate state and the dispatcher's own instrument

1. **Incident + basis** (two, same class, one day, statiker
   seam-bundle lane `sonnet-mint-lane-0283`, session statiker-cc):
   (a) the dispatcher pushed its own unrelated commits mid-batch;
   the push set is the branch, so the lane's already-claimed
   version-bump commit published with it, origin's manifest caught
   up to HEAD's version, and the machine-wide payload gate's
   unpushed-batch exemption died — every remaining item commit of
   the lane false-fired (lane report verbatim in session record;
   hook predicate read at dotfiles git/hooks/pre-commit:162-174;
   fix booked dotfiles df-156). The §1 claim check was FOLLOWED —
   it verifies outgoing commits are intended, not that publishing
   them now is safe for an in-flight lane. (b) the dispatcher ran
   the lane's test suite in the lane-held working copy while the
   lane was live-editing it: three consecutive runs returned 6
   failed / 482 passed / 468 passed on what looked like one tree —
   an unstable instrument read as flaky tests, resolved only by
   ListAgents showing the lane running.
2. **Class** — dispatcher-side action inside a lane's held copy
   mid-flight: a push that changes remote-derived gate state, or an
   execution that reads half-written files. The writer-reservation
   gate covers commits only; pushes and executions are ungated, and
   the push variant is invisible to the dispatcher because claiming
   the outgoing commits FEELS like the whole duty.
3. **Pre-formulated rule/fix text** — for the dispatch skill §4
   (dispatcher duties), beside the push-set bullet: "A push on a
   copy a lane still holds is deferred to the lane's close unless
   the lane's remaining commits cannot depend on remote state
   (version gates compare against origin: a mid-batch push moves
   their comparison basis). The same hold binds executing the
   lane's write-set — a suite run in a lane-held copy measures a
   half-written tree; run checks after the lane's series lands or
   in a frozen worktree."
4. **Consumer + drain seam** — next dispatch-guards maintenance
   round (skill §4 edit); the hook half drains at dotfiles df-156.

## Mailbox delivery can lag a lane's idle cycles; idle notices then testify to a stale wait

1. **Incident + basis** — 2026-09-11, dotfiles session
   (leadtest/lc-45 arc): a dispatcher's decision message
   (SendMessage, success ack) was not delivered to its lane
   across TWO of the lane's idle cycles — the lane's idle
   notices, composed after the send, still said "waiting on
   team-lead's decision". The dispatcher, per the deadlock rule,
   stopped the lane to integrate at the desk — and the artifact
   then showed the lane HAD received the ruling and committed
   (lifecycle e98c3a4) in the window between its last stale
   notice and the TaskStop. Separately, the same arc's two
   grader lanes each reported their first SendMessage report
   undelivered despite success acks and re-sent on demand.
   Addendum 2026-09-11, statiker session (statiker-4d, 0.2.87/0.2.88
   laps), n=3 more: (a) lane sonnet-lap-0287 received the desk's
   critique reply (a commit-order and red-first directive) only after
   its closing report; (b) lane sonnet-lapA-0288 wrote a five-part
   closing report without reading two queued fix messages, then acted
   on the earlier, superseded one; (c) the desk's STOP message crossed
   that lane's already-landed revert commit (a8d9d28). Each directive
   stated its precondition ("valid while …"), so each late arrival
   was reported, not executed — the precondition form is what kept
   all three harmless. The recorded cost: a dozen desk and lane turns
   spent on messages that crossed state.
2. **Class** — the skill's delivery binding (§2: batched at turn
   boundaries) understates the observed lag: delivery can miss
   turn boundaries too, and a lane's own idle-notice text is
   composed BEFORE queued mail flushes, so it testifies about a
   state the queue has already changed. Stop-then-integrate is
   correct and safe — but the stop can race a just-delivered
   order, so the desk's integration act must be idempotent
   against the lane having executed (measured: the desk's bump
   script asserted on the pre-state and failed loud instead of
   double-bumping — that assert is what made the race harmless).
3. **Pre-formulated text** — for the skill's delivery binding:
   "An idle notice is testimony about the lane's state at
   compose time, not about the queue: mail can arrive after it.
   Before acting on 'still waiting', read the ARTIFACT. A
   stop-and-integrate after undelivered sends is right, and the
   desk's integration step is written to fail loud if the lane
   already executed (assert the pre-state before mutating) — the
   race between a late delivery and the stop is otherwise
   silent double-execution."
4. **Consumer + drain seam** — next dispatch-guards maintenance
   round (skill §2/§4 delivery-binding edit).

## 2026-09-11 — CLASS: the payload gate's deny text prescribes the report FILE the READ-ONLY tail forbids; lanes obey the gate, and two applied entries mis-classed it

1. **Incident + basis** — 2026-09-11, dotfiles session
   300cbe7b: three sonnet discovery lanes (`sonnet-lucas-talk`,
   `sonnet-anthropic-dials`, `sonnet-anthropic-selection`), each
   carrying the READ-ONLY tail verbatim (it opens "NO REPORT
   FILE"), each wrote a findings file into the session scratchpad
   and sent a pointer message. The fire log explains all three:
   `message-payload-gate` denied each lane's first SendMessage
   (17305 / 4818 / 17183 chars; a second deny at 3006 for
   `sonnet-anthropic-dials`), and the deny text
   (plugin/hooks/message-payload-gate.py:54-61) reads "Write the
   full result to a FILE, then send a SHORT message: the key
   findings plus the file path." A foreign session's
   `sonnet-repair-0285` took the same deny the same hour (3844
   chars). Log total: 1427 payload-gate denies across 709 lanes
   since 2026-08-06, every one mode deny (python count over
   ~/.local/share/claude/dispatch-guards-fires.jsonl).
   Retro-check of the two APPLIED entries on this ban: the
   2026-08-14 `*-bericht.md` lane (`sonnet-ready-inventar`) took
   a 6010-char payload deny at 15:54:25 and wrote a 6011-byte
   file — the gate's remedy, not a missed harness block. The
   2026-08-16 placement entry names position as the only
   variable changed; message size was uncontrolled, and the log
   holds 52 payload-gate denies that day (not tied to that run's
   lanes — the entry does not name them).
2. **Class** — two homes prescribe opposite remedies at one
   seam: the gate (file plus short pointer, grounded in context
   economy) against the tails and their reminder text (split
   into labeled parts, "do NOT write a report FILE
   (harness-blocked for subagents)": forms.md:304-305 and :337,
   brief-reminder.py:804-805 and :980, report-form-gate.py:9).
   The mechanism speaks at the moment of sending, so it wins
   every time; moving prose inside the brief cannot outvote a
   deny. Splitting also defeats the gate's own rationale — N
   parts inject the same volume — and §4 already books a split
   report from its FILE. The "harness-blocked" clause is now
   contradicted four times (three English names today, one
   German on 08-14); what the harness blocks, if anything, is
   unmeasured. Side finding: "YOUR OWN scratchpad, never the
   dispatcher's" names no distinct place — all three files
   landed under this session's scratchpad path, which §1 says
   parallel agents share; both older entries booked that as a
   deviation.
3. **Pre-formulated fix text** — ONE remedy, worded from one
   shared constant in the gate's deny text, both forms.md §2
   tails, brief-reminder and report-form-gate: "Findings over
   the size gate go to the brief's ASSIGNED findings file (named
   by the dispatcher, lane slug in the name); the message carries
   the key findings, at most 3000 chars, plus that path. No other
   file." Every discovery brief then assigns that path (§1,
   untracked outputs). Drop "harness-blocked for subagents"
   unless re-measured with a planted REPORT.md written by a
   subagent. Bench case: a brief-reminder render and a
   payload-gate deny name the same remedy, asserted on the
   shared constant rather than on prose.
4. **Consumer + drain seam** — next dispatch-guards maintenance
   round (hook text, forms.md §2 tails, brief-reminder; the guard
   change extends tools/corpus/guards.jsonl). The two APPLIED
   entries carry a correction line pointing here.

## 2026-09-11 — CLASS: "YOUR OWN scratchpad" names no place — every lane writes the session scratchpad, so bare-named scratch collides across lanes and with the dispatcher's own

1. **Incident + basis** — 2026-09-11, dotfiles session (notify-suite
   review lap). Two opus verifier dispatches overlapping in time
   (opus-notify-review, then opus-notify-review-2), both carrying the
   READ-ONLY tail's "Transient probe scratch goes in YOUR OWN
   scratchpad, never the dispatcher's", both wrote under this
   session's scratchpad path. The second lane overwrote the first
   lane's `probe.py` at 18:23 and then deleted it, killing the re-run
   pointer for five of the first report's findings (reported by the
   first lane; confirmed on disk: `probe.py` absent, its `drip.py`,
   `ns/` and eight `probe-*` directories present). It also wrote into
   the dispatcher's own `ns-old/` (mtime 18:18:40, same as its new
   `ns-new/`). No booked verdict rested on the lost file: the
   dispatcher had reproduced or re-tested every finding. Earlier
   instances, each booked only as a side finding or as a lane
   deviation: 2026-08-14, fork result files overwritten in the shared
   scratchpad (entry "report booking does not check the SENDER");
   2026-08-14 and 2026-08-16, files "in the DISPATCHER's scratchpad
   instead of its own" (entries on the `*-bericht.md` block and on the
   tail's ban placement); 2026-09-11, "names no distinct place"
   (payload-gate entry). 2026-09-12, dotfiles drainage desk (df-151
   step 1): two lanes overlapping in time — `opus-df151-step1`
   (build) and `sonnet-df151-triage` (read-only) — both briefed with
   the tail's "YOUR OWN scratchpad" and no assigned names, both wrote
   BARE names at the top level of the one session scratchpad
   (`arm.py`, `a.txt`, `b.txt`, `old/`, `new/`, `clone/` from the
   first; `all_matches.txt`, `classify.py`, `bare.txt`,
   `anchored.txt` from the second). NOTHING COLLIDED — checked on
   disk by the dispatcher — and that is the part worth booking: the
   class's usual outcome is a NON-EVENT, so it under-reports by
   construction and gets noticed only when two lanes happen to pick
   the same obvious name. A dispatcher reading "no collision" as "the
   briefs were fine" is reading luck as design; here the dispatcher
   wrote both briefs having read this very rule's §1 counterpart and
   still assigned no slugs, because the TAIL is what the brief pastes
   and the tail says "your own". n=6.
2. **Class** — the tail assigns a PLACE the harness does not provide:
   for these named mailbox lanes the subagent's scratchpad was the
   dispatching session's scratchpad path, so "your own" and "the
   dispatcher's" are one directory. The §1 untracked-outputs bullet
   (the lane slug in every name under a shared scratch root) is the
   rule that would have held; the tail's wording is what tells a lane
   it needs no slug, and two older entries graded lanes against a
   place distinction that does not exist.
3. **Pre-formulated fix text** — forms.md §2, READ-ONLY and EXECUTION
   tails, replacing "Transient probe scratch goes in YOUR OWN
   scratchpad, never the dispatcher's": "Scratch: the session
   scratchpad is SHARED with the dispatcher and every other lane.
   Everything you write there goes under `<scratchpad>/<your agent
   name>/` — never a bare filename at its top level — and nothing
   outside that directory is yours to modify or delete." §1, beside
   the untracked-outputs bullet: the dispatcher fills that directory
   name from the dispatch's own `name`, the same value the channel
   line binds to. Re-grade the 2026-08-14 and 2026-08-16 "wrong
   scratchpad" deviations as collisions the brief invited, not lane
   disobedience. Bench case: the rendered tail contains the per-lane
   directory clause and not the "YOUR OWN scratchpad" sentence.
4. **Consumer + drain seam** — the next dispatch-guards maintenance
   round (forms.md §2 tails, and brief-reminder wherever it renders
   them); quota drain per the OBSERVATIONS rule.

## 2026-09-11 — CLASS: a horizon poll that prints on every artifact move turns healthy progress into desk wake-ups

1. **Incident + basis** — 2026-09-11, statiker session (statiker-4d),
   from the operator's "next steps" question to the 0.2.88 release:
   37 monitor notifications re-invoked the desk, and 28 of them only
   announced that a lane had committed — each a full desk turn
   re-billing the session prefix with nothing to act on (counted from
   the session transcript). The two real catches made on commit events
   (three skipped rows in one lap; a stray uncommitted edit) came from
   the desk's own sweeps, which the lane's closing report would have
   triggered anyway, and the one early correction they produced crossed
   that report in the mailbox (see the mailbox-lag entry above).
2. **Class** — the wait instrument's EMISSION rule, not its horizon:
   the desk's Monitor scripts printed each new commit, and the harness
   turns every printed line into a notification that re-invokes the
   session. §4 says only that the waiter arms a timer; nothing says
   what the poll may print. The operator corpus carries both readings
   side by side: Insurance :59-60 "a POLL that emits on the artifact's
   every move and on the horizon itself" and :91-92 "a changing
   artifact re-arms silently at zero interruption" — the first, read
   literally, produced the wake-ups; the second is the intended
   conduct.
3. **Pre-formulated fix text** — §4, after "the waiter ARMS the horizon
   at the moment the wait begins": "Where the lane's artifact is
   observable (commits, files), the poll tracks movement SILENTLY:
   movement resets the horizon and prints nothing. It prints only when
   the horizon passes with no movement, when the lane signals
   completion, or on an anomaly it can compute (a write outside the
   lane's boundary, a push, HEAD moving backwards). Every printed line
   re-invokes the session and re-bills its prefix, so a per-move print
   is a wake-up with nothing to act on." Bench case: a poll over a copy
   that receives three commits prints nothing, then prints exactly once
   when the horizon elapses with no fourth.
4. **Consumer + drain seam** — the next dispatch-guards maintenance
   round (§4, the horizon bullet). The corpus wording at Insurance
   :59-60 is the corpus maintainer's, surfaced to the operator the same
   day rather than booked here, since corpus maintenance does not read
   this file.

## 2026-09-12 — CLASS: the commissioned critique pass sits at the brief's TAIL, so three of three lanes sent it after building

**1. Incident + basis.** One dispatcher (statiker-df, statiker repo,
2026-09-12), three independent lanes, three separately written briefs,
all composed from §1's parts list: `sonnet-st34-tools`,
`sonnet-st35-arming`, `sonnet-st32-registry`. **All three sent the
commissioned critique pass AFTER implementation**, each disclosing it
unprompted as a deviation. n=3 in one day, and the lanes' own
diagnoses converge: "reading the brief's Grounding basis feels
continuous with starting to build" (st-35), and "it sits after
Verifier/Write boundaries, where grounding+building momentum has
already started — the fix is to make it physically the first
actionable instruction" (st-32 registry). The dispatcher's briefs each
placed it as the final section, after Commit plan — because §1
prescribes the critique pass in prose but the **brief skeleton has no
slot for it at all**, so its position is re-decided per brief and
lands wherever the composer finishes.

Value was NOT lost in these three (each critique still found real
defects — a six-vs-seven item-count contradiction, three wrong
Background lines, a verifier sequence whose arms could not run in the
stated order). What was lost is the pass's *purpose*: bought at the
head it costs minutes and steers the build; sent after it, it is a
correct report about work already committed.

**2. Class.** A load-bearing pre-build obligation placed at a
container's TAIL de-binds regardless of its wording — the reader has
already begun the work the obligation was meant to precede. Identical
in shape to the measured skill-craft finding (a load-bearing rule
inside an invariant block: 2 violations at tail position, full
compliance after moving it to the block's head, wording unchanged),
and to this carrier's own payload-gate entry, where lanes obeyed the
text that reached them at the moment of acting.

**3. Pre-formulated fix text.** In §1's brief skeleton, give the
critique pass a named slot at the HEAD — immediately after the
Title/Working copy/Base check/Scratch block and BEFORE
`## Grounding basis` — with its consequence named:

    ## First message — send this BEFORE reading anything but this brief
    Which Background line is unopened or wrong, and which two lines of
    this brief contradict each other? Send it on the report channel,
    then continue without waiting for a reply. Sent after your first
    edit, it is a report about work already done — which is the
    failure it exists to prevent.

And in §1's "The critique pass is commissioned, and its channel named"
bullet, append: "Its POSITION is part of the commission: at the
skeleton's head, before the grounding section. Placed after the
verifier or the write boundaries it reliably arrives post-build —
measured 3/3 on one dispatcher's batch, 2026-09-12 — because a brief
is read top-down by a reader acting on what it has read so far."

**4. Consumer + drain seam.** The dispatch skill's next maintenance
pass over §1 (the skeleton edit and the bullet amendment above are
both mechanical applications of slot 3). Drains by the retirement
quota with the rest of this carrier.

**Second site, same mechanism, opposite end of the work (n=2, one
desk, one session, 2026-09-12/13; wan2gp-71).** The same de-binding
was measured on a PRE-CLOSE obligation, in a different container:
the pasted EXECUTION tail's clause "A check that got backgrounded is
AWAITED before the closing report (TaskOutput block=true on its task
id) — ending your turn orphans it". Both lanes received that tail
VERBATIM and both ended their turn on a wake-up that could not come.
`sonnet-video-meta` closed with "I'll wait for the monitor's
notification before sending the closing report" — the monitor was the
DISPATCHER's, watching the lane's files, with no channel to the lane;
it sat idle until told to send. `sonnet-two-messages`, later the same
session, armed its OWN monitor and ended its turn holding the report
until it fired.

The two chose DIFFERENT wrong mechanisms, which is the discriminating
detail: this is not ignorance of `TaskOutput`, it is the absence of a
positive act at the close. Both lanes obeyed every other clause of
the same tail — pathspec commits, no `add`, no `--amend`, write
boundary respected, inbox drained — so the container was read. What
failed is specifically the clause whose firing moment is "I am about
to end my turn", the one moment at which a lane has no external
prompt, inside a block that never varies and is therefore skimmed as
plumbing.

**Class, widened.** A load-bearing obligation at a container's TAIL
de-binds regardless of wording, at EITHER end of the work: pre-build,
where the reader has already begun what it was meant to precede, and
PRE-CLOSE, where nothing will prompt the reader again. The pre-close
half is the worse of the two, because its failure is silent and
symmetric — a lane stopped on an awaited signal and a lane still
working are indistinguishable from outside, and from the inside the
lane believes it is waiting correctly.

**Additional fix text, same slot 3.** In `references/forms.md` §2,
the EXECUTION tail: move the awaited-check clause from the middle of
the block to its FIRST line and render it positively, consequence
named:

    Your turn ENDS on a sent report. If a check is still running,
    block on it (TaskOutput block=true on its task id) and stay in
    this turn until it returns, or SEND an interim report now that
    says so and names what remains. Nothing external will wake you:
    a turn ended while waiting is a stop, and from outside it is
    indistinguishable from work.

Rationale for position, not just wording: this carrier's own
tail-position finding and the skill-craft measurement it cites
(2 violations at tail, full compliance after moving to the head,
wording unchanged) both say the container's head is what binds.
A wording-only fix here would be the third attempt at the same
mechanism by a route already measured not to work.

## 2026-09-12 — spent horizon timers not disarmed at the wait's end (n=4, three desks)

**Incident + basis.** Two stale wakes in one judgment-desk session
(dotfiles-85): the ack-horizon Monitor for a peer kickoff fired ~25
min after the ack had arrived and been acted on; the wave-1-plan
horizon Monitor fired ~40 min after the plan digest had been graded
and wave 2 authorized. Both were one-shot sleep Monitors; both
waits had ENDED with their artifact's arrival; neither was stopped
in the arrival turn. Each fire cost a paid wake with nothing to act
on — the exact waste the poll emission rule prices.

Fourth instance, third desk (dotfiles-c6, 2026-09-13): a 30-min
Monitor armed for a peer's collision answer on a booked item fired
~28 min after that peer had answered in full and the answer had been
acted on — the desk had even ROUTED onward from it, to the party the
answer named. Same displacement, and one detail sharpens the class:
this desk had disarmed a DIFFERENT timer correctly minutes earlier
(the discovery-lane horizon, stopped in the turn its last lane
reported), so the rule was not merely loaded but actively obeyed on
one instrument while the other went unstopped.

The separator first written here — that a LANE REPORT carries its own
disarm while an inbound PEER MESSAGE does not — was REFUTED within
the hour by n=5 at the same desk: the build lane's horizon fired
stale too, and THAT wait ended on a lane report, the case the
proposed rule called safe. Corrected in place rather than appended,
and recorded because the collapse is itself the evidence: the
explanation was a rationalization that survived exactly one case.

What separates the ONE disarm that worked from the four that did not
is ARRIVAL GRAIN. The discovery horizon was stopped correctly because
its three lanes' reports converged on a single turn in which "the
wait has ended" could be a thought of its own. Every stale fire
followed a DIFFUSE arrival: a 7-part report split across many turns
by the payload gate, where no part announces itself as the last; a
peer answer arriving mid-turn and answered rather than processed; a
digest that must be graded before it can be recognised as complete. A
wait whose end has no single observable moment offers no moment at
which the disarm can be the first act — which is what every version
of this fix has assumed it has. Consequence for the fix text: keying
the disarm to the arrival TURN is unreliable by construction wherever
arrivals are multi-part. The robust form keys it to the LANE-CLOSE
act (sent exactly once per lane, a single observable moment), or
takes the timer out of the desk's hands entirely by having the wait's
instrument stop itself on the artifact it watches.

**Class.** The disarm rule exists (Insurance: "a wait that ENDS
disarms its timer in the same turn") and was LOADED — the failure
is the trigger's shape: the disarm moment coincides with the
arrival of a rich artifact (a digest demanding grading and rulings),
and composing the response displaces the disarm every time. Same
displacement mechanism as the incoming-demand rule, one instrument
down.

**Pre-formulated fix text** (for §4's wait/arming conduct, or the
corpus Insurance bullet, whichever drains first): "On the awaited
artifact's arrival, the timer's disarm is the FIRST act of the
handling turn, before any grading or reply — the arrival turn's
opening tool call, not its closing one; a disarm deferred behind
composition is the displacement class and loses to it."

**Consumer + drain.** Dispatching/judgment desks running armed
horizons; drains on this carrier's normal quota into §4 or the
corpus Insurance bullet (amendment-over-addition: the sentence
already exists, this adds the ordering anchor).

**Third instance, same day, different desk — and it compounds with a
second defect (statiker-df, 2026-09-12).** The `0.2.89 review horizon`
Monitor (baseline `494dbe5`, 35 min) fired ~2h after the review lane
had returned its ten findings, been graded, dispositioned, and
superseded by a repair lap. Same shape as the two above: the wait ENDED
on a rich artifact — a ten-finding review demanding a fail-closed
ruling — and the disarm lost to the composing. What makes this instance
worth the merge is what the stale timer FIRED WITH: not a plain
horizon expiry but `ANOMALY at minute 34: the working tree is DIRTY
under a read-only review lane`. The dirty tree was the DISPATCHER's own
two record edits, landing in the shared copy hours after the lane it
watched had finished. So the anomaly predicate was anchored to live,
mutating shared state — the check-anchor rule's false-alarm direction
(corpus Fixing: "criteria anchored to live, mutating state decay into
false alarms") — and the compound is the cost: a spent timer that
should not have been running fired a finding-shaped false positive
about a lane that no longer existed, and it reads as a real anomaly for
exactly as long as it takes to open the tree. A disarmed timer produces
no false anomaly, which is why the fix stays the disarm rather than a
better predicate; but where such a predicate is armed on a SHARED copy
at all, it is keyed to the lane's OWN write set, never to tree
cleanliness — the dispatcher writes records in that copy by design and
is not an anomaly.

## 2026-09-12 — a lane's injected gitStatus is a stale instrument the critique pass reads as current repo state

**Incident + basis.** `sonnet-repair-0289` (statiker repo) opened its
critique pass with a candidate contradiction: the brief's Background
said "manifest at 0.2.89, batch UNPUSHED, exemption armed", while the
gitStatus block injected into that lane's context showed
`8d65478 0.2.88 released: pin 0.2.87 -> 0.2.88` among recent commits
with no later bump visible. The lane flagged it before opening the
manifest — correct conduct, and the flag was a false positive.
Refuted at the artifact by the dispatcher: working-tree
`plugin/.claude-plugin/plugin.json` at `0.2.89`, `origin/main` at
`0.2.88`, `git log --oneline origin/main..HEAD | wc -l` → 43, the bump
commit `4325cbd` sitting above the truncated head gitStatus prints.
Cost: one round trip. The lane continued without waiting, so nothing
stalled.

**Class.** The harness's gitStatus block is a SESSION-START SNAPSHOT
carrying a TRUNCATED commit head, and it arrives in the register of
current repo state — same two-channel divergence the corpus already
names for CLAUDE.md injection vs. the live file (Shell and privilege,
the two-channels binding), one artifact over: injected snapshot vs.
live repo. It bites hardest on an UNPUSHED BATCH, where the facts a
brief rests on (a version bump, a base commit, "nothing pushed") are
precisely the ones sitting above the snapshot's horizon. Both failure
directions are live: the lane doubts a true premise and spends a round
trip, or — the silent one — a lane that does not ask resolves the
conflict in the snapshot's favour and builds on a state the repo left
behind.

**Pre-formulated fix text** (for §1's provenance rules, where the
brief's Background lines are governed): "A Background line asserting a
repo state the lane's injected gitStatus could contradict — a manifest
or package version, a base commit, an unpushed-batch premise, a branch
position — carries its executed read INLINE and says that the injected
gitStatus is a session-start snapshot with a truncated commit head, so
the lane can tell the snapshot from the artifact instead of grading one
against the other. The tell at compose time: the brief's premise lives
in commits above `origin/<branch>`."

**Consumer + drain.** Dispatchers briefing lanes on a working copy
with unpushed commits (the statiker maintenance arc's standing
condition, and any batched release lap); drains on this carrier's
normal quota into §1's per-line provenance rule by amendment — the
rule already demands the opened read, this names the instrument that
makes an ungraded line actively misleading rather than merely
unverified.

## 2026-09-12 — a must-not-move arm reusing a named fixture cannot fire when the gate has a FLOOR the fixture never clears

**Incident + basis.** My own brief for `opus-df151-step1` (dotfiles,
df-151 step 1, the declared-deletion gate) commissioned six counter-arm
rows, two of them — "a mass deletion of ITEMS.md in this repo still
refuses" and "a mass deletion of BACKLOG.md in an UNMIGRATED repo still
refuses" — built on the repo's existing `frz_repo` fixture, named in
the brief by name. That fixture writes 40-line files
(`git/hooks/pre-commit:3636-3639`, helper `md_zeilen` at :3485), while
the gate under test continues at `weg_n <= MASS_DELETION_MIN` with
`MASS_DELETION_MIN = 200` (:850, :899). Both arms would have returned
the empty list whether or not the exemption being built existed — a
green byte-identical to a working must-not-move row, on the two rows
that carry the exemption's SCOPE conditions (the repo-identity check
and the not-in-table check). The neighbouring block 16a in the same
file solves the same problem with `md_zeilen(947)`, so the magnitude
was one screen away. Caught by the lane's commissioned critique pass
before its first build call, confirmed at the artifact by this desk
rather than booked on the lane's word; the lane repaired the
arrangement in scope (fixture size plus a positive control in the same
fixture) and flagged rather than asked. n=1, cost zero — the critique
pass paid for itself on its first use at this desk.

**Class.** The brief specified each arm by its QUESTION and reused a
fixture by NAME, and nothing in the brief form asks whether that
fixture's MAGNITUDE reaches the checked predicate at all. It is the
devbook's "a bite that stays GREEN needs its arrangement checked
exactly as a red does" landing one level earlier — on the dispatcher's
brief rather than on the executor's run — and a sibling of the
2026-08-12 battery-invocation entry, which is the same failure from the
INVOCATION side (selector and abort flags narrowing the instrument).
The must-not-move row is where it bites hardest and hides best: its
expected result is a NON-EVENT, so a dead arrangement and a working
scope condition return the same silence, and the row's whole purpose is
to certify that the change did not widen what the gate allows.
Threshold gates are the general shape — any predicate with a floor, a
ceiling, a minimum count, a ratio, or a size gate below which it
declines to look.

**Pre-formulated fix text** (SKILL.md §1, widening the bullet "A
commissioned instrument's SEMANTICS are the dispatcher's to state",
which already fixes ABSENCE mapping and COMPARISON grain — a third item
beside them, not a new bullet): "And MAGNITUDE, wherever the checked
predicate has a floor, ceiling or ratio below which it declines to
look: an arm specified by its question and handed an existing fixture
BY NAME inherits that fixture's size, which was chosen for a different
predicate. A must-not-move row is where this is invisible — its
expected result is a non-event, so an arrangement that could never
reach the predicate returns exactly what a working scope condition
returns. The brief states the magnitude that clears the threshold, or
names the positive control that proves the arrangement live in the same
fixture; the compose-time tell is a brief naming a fixture helper it
did not size."

**Consumer + drain.** Any dispatcher commissioning counter-arm or
must-not-move rows against a gate with a numeric floor — the
guard/checker-build class by construction, and every brief reusing a
repo's existing test fixtures. Drains on this carrier's normal quota
into §1 by amendment, as a third clause of the instrument-semantics
bullet.

## 2026-09-13 — devbook step 2 assumes the CLI can be safely exercised; a guard whose ONLY CLI path is a production write is uncovered

**Incident + basis.** lc-73 (lifecycle drain desk dotfiles-b8, opus
lane under `guard-checker-bau`): the devbook demands the red-first
run at CLI altitude against the old binary, but the only CLI path
reaching the refusal under test was `migrate --merge` — against the
real target (statiker) a production write ingesting 25 closure
bodies into another desk's carrier, forbidden by the lane's write
boundary; `--report-only` does not reach the refusal. The lane
returned the contradiction with evidence rather than inventing a
route. Resolution, executed and verified: the red ran against a
PINNED COPY of the production artifact — statiker at 865e0a2, each
copied file sha256-equal to that commit's blobs — old binary 17,
new 20, the delta naming the exact decayed entries. Relayed from
the drain desk's closing digest; arrangement details in lifecycle's
wave-directive pause note (b0b1639).

**Class.** Devbook step 2's "the red runs the OLD binary on a real
payload" silently assumes an exercisable CLI. Where the only route
to the refusal IS the production write, the step as written forces
a boundary violation or a unit-level red — the exact under-proof it
forbids. The pinned-copy arrangement is the general resolution, and
it needs its own premise check (sha256-equality to the pinned
commit) or the copy is a new unproven arrangement.

**Pre-formulated fix text** (dotfiles root CLAUDE.md, Registered
procedure §2 — NOTE: editing that section resets guard-checker-bau
to eval-open by fingerprint, so this drains deliberately, bundled
with the next devbook amendment, never as a drive-by): "Where the
only CLI route to the refusal is a PRODUCTION write, the red runs
against a pinned copy of the production artifact, each file shown
sha256-equal to the pinned commit's blobs before any red from it
counts — the copy is an arrangement, and an unproven arrangement's
red is indistinguishable from the defect's."

**Consumer + drain seam.** The guard/checker devbook (dotfiles root
CLAUDE.md §2), at its next amendment window; fingerprint-reset cost
named above. Cross-repo consumer, so this entry stays here until
that window opens.

## 2026-09-13 — one-writer governs COMMITS; transient mutate-and-restore probes interleave invisibly on a shared copy

**Incident + basis.** Same session, one lane, one file, two
parties, both obeying one-writer: prove-rows (mutate-and-restore by
design) ran while a suite graded the same checkout — three suite
failures graded a momentarily mutated source, plus a stat-cache `M`
over a byte-identical file. That is the LOUD direction. The QUIET
direction, named by the lane after close: a bite arm reading
"restored clean" over a co-writer's live mutation is
byte-indistinguishable from a correct restore, and `git
update-index --refresh` defeats the stat cache but not a concurrent
writer. Relayed from the drain desk's closing digest; measured
in-session, 2-party interleave on one path.

**Class.** The one-writer rule's unit is the COMMIT, so every
red-first bite, positive control, and prove-rows-style probe — real
bytes in real tracked files for real seconds — sits outside it by
construction. Two compliant parties interleave with neither
instrument reporting it; each sees an inexplicable result and
re-runs. Sibling of the devbook's bite-window clause (scope the
injection narrowly), which bounds the window but never RESERVES it.

**Pre-formulated rule text** (dispatch skill §4, the one-writer
rule, widening): "A mutate-and-restore probe is a WRITE for this
rule's purpose: for its window it takes the same exclusivity a
commit takes — the copy's reservation where the gate is deployed,
an announced probe window where it is not — and a verifier's
verdict over a copy carrying another party's probe window is
could-not-verify, never a result."

**Consumer + drain seam.** Dispatch skill §4 amendment (this repo),
normal quota drain; the devbook's step-4 bite clause gains a
cross-reference in the same pass, priced with the fingerprint reset
above so both CLAUDE.md edits ride one window.

## 2026-09-13 — a discovery lane wrote a REPORT FILE despite the read-only tail's explicit ban, and into the DISPATCHER's scratchpad

**Incident + basis.** Three parallel discovery lanes, identical
read-only tails pasted verbatim from forms.md, each carrying "NO
REPORT FILE. Your findings go in your SendMessage reply — a file you
write is not a report, is not read as one, and reaches no one" plus
"Transient probe scratch goes in YOUR OWN scratchpad, never the
dispatcher's". Lane `sonnet-pstack-conduct` returned a SendMessage
carrying six headline bullets and a POINTER to
`<dispatcher-session-scratchpad>/pstack-conduct-knowledge-findings.md`,
778 lines — the substance in a file, the message a summary of it.
The other two lanes on the same tail complied, one splitting into 14
labelled parts. So the tail's text is not the defect; a lane can read
that exact prohibition and still take the file exit under output
volume. Measured this session; the file was read and its content was
good, which is what makes the deviation cheap to miss.

Second occurrence, same day, different desk (dotfiles-c6, ECC
reference read): lane `sonnet-ecc-enforcement`, same pasted
read-only tail, returned a SendMessage of headline bullets plus a
pointer to `<dispatcher-session-scratchpad>/ecc-enforcement-findings.md`
(113 lines) and called the file "the deliverable" in its own
message — the two sibling lanes on the identical tail are still
out at time of writing. Its content was likewise good and properly
graded, and the dispatcher booked from the file body. n=2 for the
file exit under the current tail text. The lane also ANSWERED the
scratch half when the deviation was put to it: the path it wrote
to "was the one listed as mine in my system prompt" — corroborated
at the artifact, since the file sits under the DISPATCHER's session
id. That is entry 2026-09-11 ("YOUR OWN scratchpad names no place")
measured from the lane's side rather than the desk's: the clause
asks for a place the harness does not give the lane, so a compliant
lane cannot satisfy it and a desk flagging it is flagging its own
rule. The desk's flag was withdrawn on that half.

**Class.** The ban is stated as a PROHIBITION with its reason
("reaches no one"), and the reason is false for a lane whose
dispatcher shares a filesystem — the file DID reach the dispatcher,
so the stated rationale argues against the rule at exactly the moment
the lane weighs it. Second half: the volume pressure that produces
the file exit is real (778 lines against a message-size gate), and
the tail names the split-into-parts remedy in the same breath, so the
lane chose between two sanctioned-looking exits. Sibling of §2's
payload-vs-pointer rule, which governs a SENDER's long content; this
is the read-only lane's version, where no pointer is admissible
because the dispatcher must book from the message.

**Pre-formulated rule text** (forms.md, READ-ONLY tail, replacing
the "NO REPORT FILE" sentence): "NO REPORT FILE, and no pointer to
one. Findings travel IN your SendMessage replies — split into
labelled parts (1/N) as many times as fidelity needs; there is no
volume at which a file becomes the right answer. A message naming a
path instead of carrying the finding is an unbooked report: the
dispatcher grades what arrives in the channel, and a lane that
cannot fit its findings in parts has a slice too large, which is the
dispatcher's defect to report, not the lane's to route around."

**Consumer + drain seam.** forms.md §2's read-only tail (this repo),
normal quota drain. Rides the same window as the one-writer widening
above if that opens first — both are single-paragraph edits in the
dispatch skill's own text.

## 2026-09-13 — two incidents from the sc-8 dispatch (statiker desk session 1b204567)

1. ROSTER × MODEL-GATE DEADLOCK for a teammate-dispatched verifier. Incident+basis: the sc-8 lane, mandated by its target repo to dispatch a fresh-context self-review before commit, was refused BOTH ways — named spawn ('Teammates cannot spawn other teammates — the team roster is flat') and unnamed generic spawn (agent-model-gate: every generic dispatch is NAMED; ENFORCED_TYPES covers every fit type, hooks/agent-model-gate.py:133); a fork is self-review by definition. Class: a repo-mandated verifier is structurally undispatchable from any teammate lane; the desk must run it, and no rule says so. Pre-formulated fix text: dispatch skill §4 escalation bullet gains one sentence — 'A verifier a repo's own rules mandate is dispatched by the DISPATCHER when the executing lane is a teammate: the flat roster and the model gate jointly bar every lane-side spawn, so the brief for such work names the desk as the review's dispatcher up front.' Consumer+drain: the next dispatch-skill amendment pass; fire log carries the two refusals.
2. COMMIT PLAN WRITTEN WITHOUT THE GUARD READ (dispatcher's own defect, same lap). Incident+basis: the sc-8 brief said 'no manifest bump' without reading unbumped_plugins() — the lane's first commit bounced and cost a full directive round trip; §1's commit-plan bullet already mandates the read ('sequenced from the guard's OWN comparison basis (read it, not assumed)') and the slot demands the read beside the verdict. Class: existing rule, loaded-but-inert at brief-compose — the slot was filled with a verdict and no read. Pre-formulated fix text: none new — the rule exists; candidate sharpen only if it fires again: the brief-reminder hook's commit-plan lane could demand a read token ('hooks path read:'-style) for the BUMP slot the way it does for guards. Consumer+drain: fire-rate review; count this as firing one.

## 2026-09-13 — a WATCH instrument's `git fetch` inside another party's copy is a write-shaped call presenting as a read; it claimed and renewed the writer reservation

**Incident + basis.** A judgment desk armed an artifact horizon as
a poll running `git -C <peer copy> fetch` every 60 s inside the
working copy the arc directive assigned to the drain desk. The
reservation gate's claim trigger classified each fetch as a
write-shaped call, so the desk's reservation (first claimed by a
directive commit) was RENEWED every minute for ~2.5 h while the
desk wrote nothing — the drain desk's build lanes hit the WARN
against a holder that was not writing, and the stale WARN became
one input to a confident-wrong cross-desk accusation (retracted on
trailer measurement the same hour). Neither desk had priced the
fetch as a write: it presents as reading the remote. Judgment-desk
session 746f6a5f (dotfiles), drain-wave arc, 2026-09-13; reservation
file read back before release confirmed session id and TTL renewal.
Same incident, fire-rate provenance for the reservation gate
(staging WARN per its spec): 2 true fires the same day (a third
desk's direct carrier commits — WARN correct, proceeded past on a
pathspec-isolation reading later withdrawn), plus the stale-holder
false-fire class above.

**Class.** Exclusivity claimed by an instrument that only observes:
the reservation's claim trigger keys on write-SHAPED commands, and
a watch/poll built from repo-local git plumbing (`fetch`, and any
maintenance verb that touches `.git/`) is write-shaped without
being a write in the rule's sense. Two failures from one cause: the
copy's owner is warned about a phantom co-writer (discount-reflex
training), and the watcher holds an exclusivity token it never
needed. Kin of, not same class as, the transient-probe entry above
(that one: real writes needing MORE exclusivity; this one: a
non-write claiming exclusivity it should not have).

**Pre-formulated rule text** (dispatch skill §4, the wait/horizon
conduct, addition beside the poll rule): "A horizon poll observes
the artifact WITHOUT write-shaped calls in a copy another party
owns: a remote is watched by `ls-remote` against the URL or by a
fetch in the watcher's OWN clone, never by `fetch -C` into the
watched copy — inside a reservation-gated copy such a call claims
and renews the watcher's reservation, warning the owner about a
holder that is not writing." Gate-side half (reservation lane,
next build touching it): the claim classifier exempts
read-intent plumbing (`fetch`, `ls-remote`, `rev-parse`, `log`,
`status`) or keys on worktree/index mutation rather than command
shape — with the counter-arm run both directions (a fetch must not
claim; a commit must still claim).

**Consumer + drain seam.** Dispatch skill §4 amendment (this repo),
normal quota drain; the reservation gate's claim classifier at its
next build, counter-arm per the guard devbook.

## 2026-09-13 — the unfilled `<model>` placeholder ships, and the lane fills it wrong

**Incident + basis.** The ethos-prep execution brief (statiker meta
session 1b204567) pasted the §2 execution tail with the trailer
line still reading `Co-Authored-By: Claude <model> …` — the
placeholder unfilled. The sonnet lane filled it with the
DISPATCHER's model: both its commits (ethos 8f33156, 5b24acb)
carry "Claude Fable 5" trailers, verified at the artifact via
`git log --format=%(trailers)`. The dispatcher's compose error,
not the lane's: forms.md already rules "fill `<model>` AND the
channel line … at paste time".

**Class.** A pasted-tail placeholder is invisible boilerplate at
compose time — the very invariance that makes pasting safe makes
an unfilled slot unnoticeable — and the fill the lane improvises
corrupts the trailer-as-ownership instrument downstream: slot (f)
claims, the writer-claims machinery, and any tier audit key on a
model name that is now wrong (here: a sonnet lane's work reading
as top-tier). Kin of the recorded nondeterministic-trailer issue
(lanes omitting the trailer); this variant WRITES one, wrong,
which is worse — present-and-wrong passes every presence check.

**Pre-formulated fix.** Mechanical, meets the bar: brief-reminder
(or a sibling PreToolUse(Agent) check) WARNs when the dispatch
prompt contains a literal `<model>` (angle-bracket placeholder)
anywhere in its text — computable, near-zero false fires (a
legitimate brief has no reason to ship literal `<model>`), and
the counter-pair is trivial (fires on this brief's text; silent
on the same tail with "Claude Sonnet" filled).

**Consumer + drain seam.** brief-reminder's next build in this
repo; normal quota drain. Until then: dispatcher-side, the tail's
trailer line is composed with the concrete model name the moment
the route line names the tier.

## 2026-09-13 — authorship asserted without its discriminator, twice in one day, rule loaded and inert both times

**Incident + basis.** Two desks, same machine, same day, same
class, both retracted on measurement. (i) The drain desk read a
commit's Co-Authored-By model name as an IDENTITY and accused the
judgment desk of three boundary crossings; the discriminating
session trailer was in its own terminal output, printed and
unread; retracted after `git log --format='%(trailers)'` showed
two different sessions (its own retraction message names the
mechanism). (ii) A second desk read the session trailers of
NEIGHBORING commits and let that provenance bleed onto three
trailer-less lifecycle-CLI commits between them, asserting "your
amend-reason" to the judgment desk as fact; conceded on the same
measurement shape (its concession names the bleed). Both desks
held the rule — the author trailer separates tiers and nothing
finer — and neither applied it at the assertion moment: the rule
fires when trailers are READ, and both incidents asserted
authorship without a read. Judgment-desk session 746f6a5f
(dotfiles), drain-wave day; the trailer-less-commit enabler is
booked as dotfiles df-172 (CLI commits carry no session trailer).

**Class.** Attribution asserted where the discriminator was absent
or unread — the loaded rule is keyed to trailer-reading and the
failure happens upstream of any read, so it cannot fire (anchored
to a moment the failure path never produces). The costume both
times: surrounding evidence (a model name, neighbors' trailers, a
held reservation) supplies a plausible author, and plausibility
ships as identity.

**Pre-formulated rule text** (dispatch skill, the author-trailer
rule, sharpen — anchor moved to the CLAIM): "An authorship claim
about a specific commit carries its discriminator in the same
breath: the commit's own session trailer read back, or the named
holder asked. A model-name trailer, a neighboring commit's
provenance, or a reservation naming a session are not
discriminators for THIS commit; over a trailer-less commit the
honest claim is 'author unrecoverable from the artifact', and the
route is asking, not inferring."

**Consumer + drain seam.** Dispatch skill amendment (this repo),
normal quota drain; fire-rate provenance n=2 same-day for the
existing trailer rule's inertness.

## 2026-09-13 — CLASS: "open the claim before repeating it" is read as IS IT TRUE, and a true fact carries a wider verdict out unchecked (n=3, one desk, one session)

**Incident + basis.** One desk (dotfiles-c6) relayed three findings to
peers in one session. Each rested on a fact that was true, measured,
and in two cases cross-checked on a second instrument. Each carried a
verdict WIDER than its fact, and each was refuted by the receiving
peer within one round:
(i) to statiker-fd — "a 7th ethos module is silently never loaded and
nothing goes red", from two hardcoded MODULE_ORDER lists and a
word-boundary grep showing zero directory enumeration under plugin/
(all true). Refuted: dotfiles doctor's `corpus_import_targets_verdict`
already guards membership in BOTH directions, and the desk had been
reading the fresh-install path while calling it this machine's loading
path. Missing probe: `ls -la ~/.claude/CLAUDE.md`, one command.
(ii) to dotfiles-b8 — "36 tests never execute, their subjects
uncovered", from the repo's OWN declared verify command erroring on
two bare sibling imports (true, reproduced, and confirmed on a second
runner). Refuted: the same discovery WITHOUT `-t .` runs 368, OK; the
arithmetic closes exactly (334 − 2 placeholders + 36). Missing probe:
run the other invocation, one command. It is a documentation defect,
which routes to a twenty-line pass, not the lane the desk's severity
implied.
(iii) its own booked observation — a stale-timer separator
(lane-report vs peer-message), refuted within the hour by the next
instance, which ended on a lane report and fired stale anyway.

**Class.** NOT a gap. The rule exists in TWO homes and both name this
case: dispatch skill §4 ("A claim is opened before it is REPEATED, not
only before it is merged… repeating a claim to the operator, to
another agent, or into a booking puts it where someone acts on it"),
and the corpus's refutation-probe rule, whose scope line says
"Load-bearing includes DELIVERED". Loaded-but-inert, three times, in
one session, by a desk that quotes both rules in its own messages.

The mechanism of the non-firing is the word OPEN. Opening a claim is
performed as a truth check — read the file, run the command, confirm
the fact — and all three facts PASSED that check. What went unexamined
was the claim's SCOPE: what else could produce this observation, and
which paths the finding does not reach. A true fact silences the probe
by satisfying it, and the wider verdict rides out attached to the fact
rather than as a claim of its own — the attachment costume, one level
up from the sentence. The costume is reinforced by the channel: a
finding being SENT reads as delivering information, not as resting
work on a premise, while the receiver builds on it immediately.

**Pre-formulated rule text** (dispatch skill §4, appended to the
existing "opened before it is REPEATED" clause): "Opening establishes
the fact, never the verdict's REACH — and a true fact is the shape
that silences this rule, because the check it invites passes. Before a
finding travels, the second question is asked in its own words: what
would make this NOT a defect, and which command answers that? In the
measured cases the answer was one command every time — the OTHER
invocation, the OTHER load path, the OTHER instance of the class — and
none of them was about whether the fact was true. A finding relayed
with its fact opened and its reach unopened is sent with the reach
named as unverified, or it is not sent yet."

**Consumer + drain seam.** Dispatch skill §4 (this repo), normal quota
drain; bundles with the other §4/§1 entries of this date — all are
single-paragraph edits to the same two sections. Note for whoever
drains it: the corpus's Grounding module carries the reach test
already, in general form; what is missing is its rendering at the
RELAY moment, which is where §4 speaks.

## 2026-09-13 — CLASS: a red/green probe keyed on SEVERITY is satisfied by the fixture's own unrelated failure, and scores the old binary green

**Incident + basis.** A guard/checker lane building a doctor verdict
wrote its defect-visible probe as `any(WARN/FAIL)` over doctor's
readiness rows. Its fixture pointed DOTFILES at a temp tree, so the
register's deployed-path check emitted an unrelated FAIL — present on
BOTH arms. The predicate was therefore satisfied by the old binary
too, and the red/green pair scored the OLD side GREEN. Caught by the
lane itself, only because the old side going green was unexpected;
re-anchored on a row ABOUT the property (`"bar" in m and "k=0" in m`),
after which old went red and new stayed green. Self-reported in the
closing report rather than quietly repaired. Dispatcher-side note: the
same shape is already recorded one layer down in doctor's own `_cnv`
comment ("a needle merely naming the file is not a needle"), so this
is that rule reproduced one layer out by a reader who had not met it.

**Class.** Sibling of the payload-is-the-instrument entry: there the
probe's PAYLOAD could not register the change; here the probe's
PREDICATE cannot distinguish the change from the fixture's ambient
noise. Both return byte-identically what a true absence returns, and
both read as diligence. The generating condition is a fixture whose
environment differs from the real target in some way the instrument's
predicate is broad enough to catch — which is every fixture, since
that difference is what makes it a fixture.

**Pre-formulated rule text** (dotfiles class devbook, "## Registered
procedure", step 2, beside the existing red-arm clauses): "A red/green
arm is keyed on the ROW that asserts the property under test, never on
a severity, a count, or `any(...)` over an output stream: a fixture
differs from the real target by construction, and any difference loud
enough to emit a row satisfies a severity predicate on BOTH arms. The
old side going green is the tell, and it is only a tell if the
arrangement predicted red — so the arm names, before it runs, which
row it expects and on which side."

Two smaller candidates from the same lane, same home: (i) the step-4
docstring self-probe is written for TEXTUAL predicates and has no
meaning for a structural one — the lane stated it not-applicable
rather than running an unfalsifiable arrangement, and the clause could
name which predicate kinds it binds; (ii) `isinstance(True, int)` is
True in Python, so a JSON `true` certifies as an integer — pinned in
that lane's battery, and worth a line wherever a JSON integer field is
validated.

**Consumer + drain seam.** THE REALIZING WRITE IS NOT IN THIS REPO:
the guard/checker class devbook lives in dotfiles root CLAUDE.md, and
amending it moves the section sha256, which resets `guard-checker-bau`
to eval-open per §6 invalidation. That cost is why this is booked
rather than applied inline — it wants batching with the next devbook
amendment, not a fingerprint churn of its own. Obligation stays with
the sender (dotfiles-c6) until it lands there; the check that would
reveal it is `readiness-fingerprint-check` going stale against a
devbook that gained this clause without a re-probe.

## 2026-09-13 — CLASS: the live-on-write clause enumerates FIRST-ORDER execution paths, so a file that is live only TRANSITIVELY reads as safe

**Incident + basis.** A brief for a doctor/register build asserted as
an established Background line: "bootstrap/doctor.py is NOT
live-on-write (invoked, not hook-wired), so an intermediate state is
safe." The executing lane opened it and returned it as wrong in its
critique pass, before building: `tools/readiness-fingerprint-check.py:61`
exec_module()s bootstrap/doctor.py, and `git/hooks/pre-commit:1262-1295`
loads that tool in EVERY repo on this machine through the global
`core.hooksPath`. A syntactically broken doctor.py therefore breaks
co-writers' commits machine-wide for the duration of an edit window.
Dispatcher (dotfiles-c6) conceded at the artifact; lane kept the file
parseable at every intermediate state as its own mitigation.

**Class.** NOT a gap — §1 already carries "Deployment-coupled is a
different question from LIVE ON WRITE" (adopted from this carrier's
own earlier entry, "### 2. The brief boxed DEPLOYMENT and missed
LIVE-ON-WRITE"). This is loaded-but-inert, and the mechanism of the
non-firing is the clause's ENUMERATION: it lists first-order
execution paths — a git hook under core.hooksPath, a registered
harness hook, a file a running daemon re-reads, anything under a
watched directory. A CLI imported BY one of those matches no item on
the list, so a reader checking the list correctly concludes "not
live-on-write" and is wrong. The dispatcher reasoned from the file's
CATEGORY (it is a CLI, invoked not wired) instead of from its
callers, which is exactly what an enumeration invites. The corpus's
own rule predicted it: enumerated triggers always have gaps, and the
fix is to abstract upward rather than append the next variant.

**Pre-formulated rule text** (dispatch skill §1, replacing the
enumeration's closing clause in the deployment-coupled bullet): "The
question is not whether the file SITS on an execution path but
whether anything on one REACHES it — a CLI a git hook imports, a
module a registered hook exec_module()s, a library a watched process
loads are each live on write at one remove, and the reach is
established by reading the file's CALLERS, never by classifying the
file. Where the write set touches such a path, the brief answers
both, and the executor keeps the file loadable at every intermediate
state."

**Consumer + drain seam.** Dispatch skill §1 amendment (this repo),
normal quota drain; rides the same window as any other §1 edit.

## 2026-09-13 — CLASS: a one-item lane's base-check HALT collides with the tail's "never halt the LANE"

**Incident + basis.** Same dispatch. The pasted EXECUTION tail opens
"on a gap HALT THE ITEM, FINISH THE REMAINDER, REPORT — never halt
the LANE, since 'halt and wait' is not a survivable state for a
subagent", while the brief's own base check says "Base contained WITH
commits on top = foreign work present: report the commits as a gap
and HALT." The lane hit exactly that state (three peer commits on
top, all disjoint from its write set, tree clean) and named the
contradiction in its critique pass: a ONE-ITEM lane has an empty
remainder, so halting the item IS halting the lane — the thing the
tail forbids. It resolved by proceeding with a stated deviation,
reasoning that the three reads exist for collision detection and the
evidence dissolved the collision, and that uncommitted edits in a
shared copy are the more dangerous terminal state. Dispatcher
ratified.

**Class.** A brief-level stop instruction and the invariant tail
disagree about what a stop MEANS, and the disagreement is invisible
whenever a lane carries more than one item — the remainder absorbs
it. The base check's HALT was written for the multi-item case
without noticing that the single-item case is the common one for
guard/checker builds.

**Pre-formulated rule text** (dispatch skill §1, base-commit clause,
replacing the bare "and HALT"): "…report the commits as a gap and
STOP BEFORE WRITING — a base-check stop is a report-and-hold at the
lane's head, never a lane termination: nothing has been built yet, so
the lane reports what it found and waits for one message. Where the
foreign commits are disjoint from the write set and the tree is
clean, the lane may proceed on a STATED deviation rather than spend a
round trip, because leaving edits uncommitted in a shared copy is the
more dangerous terminal state."

**Consumer + drain seam.** Dispatch skill §1 base-commit clause (this
repo), normal quota drain; bundles with the entry above — both are
single-paragraph §1 edits.

## 2026-09-13 — a denied fused command leaves a half-completed intent with no carrier

**Incident + basis.** Session dotfiles-c6 (df24cc0c, self-reported
in a push-set claim exchange with this desk, corroborated by the
artifact): push-claim-reminder correctly DENIED a fused
commit-and-push; the recovery re-ran only the commit half, and the
push intent evaporated — commit 79d2183 sat unpushed ~40 min in
the shared copy until a peer's claim question surfaced it. The
guard worked exactly as designed; the gap is POST-denial: a deny
that splits a compound intent voids BOTH halves, the session
re-runs the half nearest the denial, and the other half becomes an
obligation with no output — nothing observes "push still owed"
(the unobserved-trigger class; whether the dotfiles unpushed
Stop-hook could have caught a sibling-repo push is unverified
here).

**Class.** Guard-denial recovery drops the denied command's OTHER
half. Generic to every deny over a compound form: the deny reads
as being about the objectionable half, so the legitimate half is
silently orphaned with it.

**Pre-formulated fix.** In-message, zero new false fires (deny
path only): the FUSED-PUSH deny text names the full recovery —
"this denial voided BOTH halves of your command; re-run as TWO
invocations: the claim log, then the push itself." Second rung
only if the class re-fires: a Stop-hook sweep for unpushed
commits in repos the session touched.

**Consumer + drain seam.** push-claim-reminder's next build in
this repo; normal quota drain.

## 2026-09-13 — a horizon watch keyed to an artifact the WATCHER also moves fires on the watcher's own writes

**Incident + basis.** The drain desk's lane horizon was keyed to
"has HEAD moved" on the shared checkout; the desk's own carrier
booking moved HEAD, and the horizon fired on its owner's write —
a false wake read by the one party who trusts the instrument
(drain-desk digest, lc-86 close, 2026-09-13; re-anchored at that
desk to the lane's write set the same day). Same family, other
polarity, judgment desk, same day: a remote-delivery watch whose
change-branch emitted NO stdout line, so the artifact-moved case
arrived only as a bare task-completion notice — the interesting
outcome was the silent one.

**Class.** The watch's trigger set is not partitioned by AUTHOR or
by CHANNEL: a delta-keyed anchor (correct per the corpus anchor
rule) still over-fires when the watcher's own writes land in the
watched set, and under-informs when an outcome branch emits
nothing. The corpus rule covers WHERE the anchor points; this is
WHO moves it and WHAT each branch says.

**Pre-formulated rule text** (dispatch skill §4, the poll/horizon
rule, sharpen): "The watch condition excludes the watcher's own
writes — key it to the LANE's write set or the peer's commit
identity, never to bare movement of a shared artifact — and every
outcome branch of the poll, the expected completion included,
emits its own named line: an exit whose interesting case is
silent reports as a bare completion notice and reads as nothing."

**Consumer + drain seam.** Dispatch skill §4 amendment (this
repo), normal quota drain.

## 2026-09-13 — a process-wait pattern that matches the waiter's own command line never terminates and reports the target as eternally running

**Incident + basis.** A lane's wait loop was `until ! pgrep -f
'tools/prove-rows.py'`; the pattern string sits in the waiter's
own command line, so pgrep matched the waiter itself — the loop
could not terminate by construction and reported the peer's
prover as running three times after it had exited. Nineteen
minutes lost. Found by the lane itself; fixed with a pattern that
cannot match the waiter plus a positive control (drain-desk
digest, lc-86, 2026-09-13).

**Class.** The instrument is a member of its own match set — the
self-matching probe, kin of the zero-hit-search family but
inverted: an eternal HIT that reads as "still running" instead of
a false zero. Waiting looks identical to working, so nothing
prompts the second look (the corpus wait rule's silence hazard,
here with the anchor matching the anchor-holder).

**Pre-formulated rule text** (dispatch skill §4, beside the poll
rule): "A process-wait's match pattern is proven to EXCLUDE the
waiter (the classic form: bracket one character, `[t]ools/...`,
or match on pid provenance) and shown live on a positive control
before the wait is trusted; a wait that cannot distinguish the
target from itself reports the target running forever."

**Consumer + drain seam.** Dispatch skill §4 amendment (this
repo), normal quota drain; merge candidate with the existing
wait/anchor entries at the pass rather than a third sibling.

## 2026-09-13 — the push-claim gate false-fired on JS array code inside a heredoc; routed around, which is the trained-override tell

**Incident + basis.** An executing lane's python heredoc contained
the literal text of a JS call it was analyzing, and the subagent
push-gate fired on that string inside the heredoc — nothing was
pushing, nothing ran (earlier links of the chain included). The
lane routed around it by writing the program to a scratch file and
executing that: correct conduct, trivially available, and exactly
the workaround habit that trains the override reflex the guard
lanes exist to avoid. Relayed from lane opus-cf339-absence-scan,
report part 4a lesson 2 (2026-09-13); the false-fire predicate is
matching a method-call substring in a compound command's raw text
rather than a push-shaped invocation.

**Class.** A guard predicate over RAW command text matching a
token that ordinary program-text payloads carry — the same
raw-string-parse family as the mark recorder's shlex miss
(dotfiles df-172) from the other direction: there a real commit
went unclassified, here a non-push classified as one. Both are
the assertion-site paraphrase-drift shape: a match over rendered
text standing in for a parse.

**Pre-formulated rule/fix text** (the gate's lane, next build
touching it): the push-detection predicate anchors on a
git-invocation shape (command word + subcommand token after shell
splitting), never on a substring anywhere in the raw text; heredoc
bodies are excluded from the scan the way quoted strings should
be. Red pair: a heredoc carrying `x.push(` must NOT fire; a real
`git push` in the same compound MUST.

**Consumer + drain seam.** The gate's next build (this repo,
hooks/); fire-log correlation at the next fire-rate review — a
false-fire class with a trivial workaround under-reports itself,
so the lane-report path (this entry) is its only reliable counter.

## 2026-09-13 — outgoing-commit author anomaly invisible in the claim log

- **Incident + basis:** a stray `git config user.email t@t; git config
  user.name t` (a probe script's failed `cd` left it running in the
  real dotfiles checkout) re-authored 24 commits `t <t@t>` across every
  live writer, 23 pushed before detection (dotfiles 6fc5bee..0d4450a,
  2026-09-13). The driving desk's own push-claim logs PRINTED the
  anomalous author twice (`%an` = "t") and the desk read past it both
  times — claim-log readers key on sha + subject; author is a dead
  column with no salience.
- **Class:** claim check blind to anomalous metadata fields; the
  config write itself is the silent member of the failed-cd class
  (nothing surfaces it until an artifact carries it).
- **Pre-formulated fix:** push-claim-reminder gains an AUTHOR check —
  each outgoing commit's author name/email compared against the
  resolved expected identity (git config, global scope), WARN naming
  the mismatching commits before the push. Near-zero false fires: the
  expected set is the operator's own identity; lanes and desks commit
  under it by construction.
- **Consumer + drain seam:** the guard set's next design pass (dg
  items); merges with any existing claim-check entry rather than a
  sibling.

## 2026-09-13 — size-gate pressure defeats the read-only tail's split clause

- **Incident + basis:** a sonnet discovery lane (statiker-c8's
  runsweep, 2026-09-13) meeting the message size gate wrote a findings
  FILE — the exact act the read-only tail forbids in its first line —
  instead of splitting into labeled parts as the same tail instructs,
  and wrote it into the DISPATCHER's scratchpad rather than its own.
  Content verified independently at the artifact by the dispatcher;
  the deviations cost verification, not correctness.
- **Class:** an obligation stated as prose loses to the pressure that
  makes it relevant — the size gate is what makes splitting necessary,
  and it is also what makes a file feel like the natural fallback; the
  tail's "split into labeled parts (1/N)" clause carries no mechanism
  at the moment it must fire. The foreign-scratchpad half is the §1
  scratch-assignment clause under-applied at brief time.
- **Pre-formulated fix:** two halves. (a) Tail text: the split clause
  gains its explicit negative at the decision point — "past the size
  gate the answer is MORE MESSAGES, never a file" — placed beside the
  gate mention, not the file prohibition. (b) Mechanism candidate: the
  payload/claims gate warns on a report-shaped file landing in a
  scratchpad whose session key is not the writer's own.
- **Consumer + drain seam:** the guard set's next design pass; merge
  with the scratch-collision entry's family if a shared mechanism
  emerges rather than a sibling.

## 2026-09-13 — CLASS: the reservation protocol's claim, warn, and release all key on tool-surface events, and the writers most likely to collide sit outside all three

**Incident + basis.** Reported by the lifecycle drain desk
(dotfiles-b8) after a peer asked whether its holding of the
lifecycle copy is machine-readable anywhere; verified at this desk
against `hooks/writer-reservation-gate.py` (0.11.14 installed
cache) and the live state file before booking. Three findings, one
mechanism. F1: the WARN is PreToolUse(Bash) keyed on a literal
`git commit` in command position (verdict(): "no `git commit`
invocation in command position" → silent) — every lifecycle
carrier verb commits INSIDE Python (`lifecycle item add` runs
`git commit -q` as a subprocess), so the commits most likely to
collide on a shared carrier are invisible to the gate,
symmetrically for both parties. F2: the CLAIM is
PostToolUse(Write|Edit) only — `write_reservation` has exactly one
caller, `on_write`, gated on `_WRITE_TOOLS` — so a desk doing its
work through Bash verbs claims nothing and its held copy reads as
free to every other writer; the docstring's argument against an
explicit claim step (prose instructions get skipped) is sound and
still leaves this hole, because the automatic design assumes the
holder edits with Write/Edit. F3, observed live: b8's copy's
`.git/writer-reservation.json` names
`aopus-lc90-closemoot-6559040df1c9af56`, claimed 12:57:33Z, TTL
5400 s — a lane killed mid-report by the account limit; release
runs on Stop/SubagentStop, which a killed lane never reaches, so
a dead agent held the copy for its full TTL and the one commit
shape the gate CAN see warned the copy's real holder about a
corpse. A check firing on a non-defect — the override-training
shape. CORRECTION folded in, same day, this desk: an earlier
belief that a monitor's `git fetch` had renewed a reservation is
refuted by the same source read — no Bash-side claim or renew
path exists; the observed persistence was a stale file outliving
its writer, i.e. F3's class, not a fetch-claims mechanism —
making that desk the SECOND F3 instance (n=2, both read as
liveness from the outside). Version reach, settled same day
(dotfiles-b8, `diff -q`): the gate file is byte-identical between
the installed 0.11.14 cache and the committed 0.11.16 mirror, so
F1/F2 hold against the committed version too — no re-check owed
at redesign time. The cache holds 0.11.7–0.11.14 while the mirror
is at 0.11.16: the install is two versions behind, measured.

**Class.** A protocol whose claim/warn/release are all derived
from HARNESS TOOL EVENTS covers exactly the writers who use those
tools, and the population that motivated it (shared-carrier
writers) works through subprocesses. Same family as the corpus
"applying one behaviour to every member of a category": the sweep
is keyed to the members' shared idiom (Write/Edit, literal `git
commit`), not to the invariant every member carries (the
repository's own state changing).

**Pre-formulated fix direction** (design, not text — the realizing
surface is this repo's hook and its judgment):
the invariant every writer moves is the REPO, not the tool call —
candidates: claim on any Bash whose cwd/`-C` resolves into a
reserved copy (coarse, over-claims readers), or a HEAD/index
mtime watch at warn time (reads the repo's own record, catches
subprocess commits), plus an expiry-aware release: an expired
reservation whose holder is dead (session/agent id no longer
listed) is CLEARED at the next gate evaluation, not merely
treated as silent — a dead holder's file should not need a human
delete. F3's live instance is the red-first case; F1's carrier
verb is the must-catch; a read-only `git status` in a foreign
copy is the must-not-claim control.

**Consumer + drain seam.** This repo's maintainer at the next
guard iteration (writer-reservation-gate redesign), normal quota
drain. Grading carried from the reporter, verified here: F1/F2
structural (read off the wiring), F3 observed live; frequency
unestablished — one collision today, costing a wrong author in a
lane's state model and a push-gate surprise. F3's operational
cost measured same day (b8, lc-91): a build lane found the dead
lane's 55-minute-old claim on the shared copy and displaced its
prover run to a `git archive HEAD` snapshot — correct conduct,
real displaced work; the dispatcher re-ran the prover on the
live copy to close the verification hole (63 PROVEN, 0 FAIL).
Third instance same afternoon, and the three are DIFFERENT
failures wearing one warning (b8's framing, adopted): a dead
holder's claim outliving it; a live-looking claim no mechanism
had renewed; and a REAL main-session holder at 81 of 90 TTL
minutes, where the warning is arguably correct — and arrives
with no way to tell it from the other two. The third case is
the redesign's priority: a reader who has seen two false alarms
discounts the true one, which is the guard's own target failure
reconstituted inside the guard. The fix direction above gains a
requirement from it: the WARN names WHICH evidence grounds it
(holder alive? claim renewed by what act, when?), so the three
cases stop sharing one sentence.

## 2026-09-13 — a brief's reservation-HALT clause contradicts its own shared-checkout clause, and on a declared multi-writer repo the HALT is the wrong key

**Incident + basis.** The df-178 lane surfaced it as a gap
(closing report c2, this desk's brief): line 12 declared any live
foreign reservation a HALT while lines 114-115 prescribed the
pathspec mitigation for "live co-writers" — under the first, the
second can never apply, since a live co-writer IS a live foreign
reservation whenever the claim mechanism sees them at all. The
same brief's HALT fired at intake on a peer desk's claim in a
repo whose OWN law declares multi-writer pathspec discipline
(dotfiles CLAUDE.md); the lane held read-only until release, then
re-ran the full gate — correct conduct over a contradictory spec.
Second half, same lane, closing report e2: the HALT is
time-bounded, not terminal — the reservation record is cheap to
poll and its release observable, which turned a halted item into
a finished one with no dispatcher round-trip.

**Class.** A brief clause keyed to a MECHANISM's artifact
(reservation presence) rather than to the fact it proxies (write
overlap) contradicts the clause written for the fact, and
over-fires wherever the repo's declared discipline already
handles co-writers. Same over-firing family as the gate entry
above, at the BRIEF layer.

**Pre-formulated rule text** (brief-form, §1 write-boundary
block): "On a repo whose own law declares multi-writer pathspec
discipline, a live foreign reservation is a SERIALIZATION input,
not a HALT: hold write-set writes while it stands (read-only and
scratch work continue), poll the record, and proceed through the
full intake gate on release — HALT only when the holder's write
set overlaps yours or cannot be established."

**Consumer + drain seam.** This desk's future guard-checker
briefs immediately (applied from this entry forward); dispatch
skill §1 amendment on the normal quota drain.

## 2026-09-13 — CLASS: the announcement-stall detector rests on a WAITING side, and a symmetric close removes the waiter

**Incident + basis.** The lifecycle drain desk went idle after its
lc-103 closing digest while the READY set it owns was nonempty and
schedulable; the stall was detected by the OPERATOR watching an
idle terminal (their words: "i dont see any activity there") — the
party the kind split says should never be the detector. Neither
desk was waiting BY CONSTRUCTION: the drain desk's digest ended
"nothing blocking", the judgment desk's reply handed the queue
back ("the remaining READY is yours to drain") and declared its
own desk drained — a handoff in a status-close costume, sent by a
desk that had cited the membership-by-function rule the same
afternoon. The corpus rule this instantiates already records that
end-of-turn discipline fails while loaded (closure momentum at
the firing moment); its prescribed fix — the waiting side's armed
horizon — assumes a waiting side exists, and a SYMMETRIC close
(both parties report settled, neither owes the other a return)
removes it.

**Class.** Stall detection keyed to a WAITER fails exactly at role
boundaries: the moment a queue is handed over is the moment the
sender stops waiting, so the handoff most likely to stall is the
one least likely to be watched. The fix must ride with the party
that CANNOT rely on itself — a timer armed before the stall can
exist.

**Pre-formulated rule text** (two halves; dispatch skill §4 for
the second, the wave-directive template for the first):
(a) "A desk that OWNS a nonempty ready queue arms a SELF-HEARTBEAT
at role start — a session-local recurring timer (cron), predicate-
guarded: ready head schedulable AND no hold declared in the arc
directive -> resume the drain; else no-op. Disarmed at role end,
in the same act that closes the role. The timer pre-exists any
stall by construction, which is what end-of-turn discipline
cannot do." (b) "A message that hands a queue and ends the
sender's waiting IS a handoff whatever it reads like; the sender
arms the recurring horizon plus a one-shot idle subscription
BEFORE the turn that sends it ends — the anchor is the handing
sentence, not the message's register."

**Consumer + drain seam.** Wave-directive template (lifecycle
docs/directives) at the next wave start; dispatch skill §4
amendment on the normal quota drain; applied by this desk's own
sends from this entry forward.


## 2026-09-13 — a brief targeting skill references omits the corpus gates the write-set trips

**Incident + basis.** The dg-41 lane (and the dg-38 lane before it,
same day) hit a machine-local same-turn gate on its first Edit
under `plugin/skills/dispatch/references/`: skill-craft invocation
plus a CLAUDE-maintenance.md read are demanded per turn before
skill-payload edits. Neither brief named it; each lane lost turns
discovering mid-build what the dispatcher already knew (lane
reports, this date).

**Class.** A brief's environment section covers the TARGET repo's
guards but not the MACHINE's — write-set-triggered gates are
invisible in the repo the brief grounds against, so the executor
meets them as surprises however decision-complete the brief reads.

**Pre-formulated rule text** (brief-composition, §1 adjacent): "A
brief whose write-set touches a skill payload
(`plugin/skills/*/…`) names the machine-local corpus gates the
first edit will trip — the skill-craft in-turn invocation and the
CLAUDE-maintenance read — as a grounding step, not left as a
mid-build discovery."

**Consumer + drain seam.** This desk's own briefs from this entry
forward; §1 amendment candidate at the next forms/skill release
batch (rides dg-35/36/37's seam).

## 2026-09-13 — the mandated trailer drops silently in heredoc-composed commits

**Incident + basis.** The dg-41 lane composed its commit message
in a heredoc, appended no trailer, and noticed only after the
commit landed — with amend correctly closed to it by the
amend-gate, the repair had to travel to the dispatcher (dispatcher
amended, e63ab6f). The tail mandates the trailer; nothing checks
it before the commit call.

**Class.** An obligation whose only enforcement is downstream
claim-time reading (push-claim keys on the trailer) fails at
compose time and is unrepairable by its author — the one writer
who CAN fix it cheaply is barred from amend by design.

**Pre-formulated rule text** (tail amendment, one line beside the
trailer mandate): "Before the commit call, confirm the trailer is
IN the composed message — a missing trailer is unrepairable at
your seat, since amend is denied."

**Consumer + drain seam.** The EXECUTION tail in
references/forms.md at the next forms release batch (dg-35/36/37
seam); this desk's briefs paste the amended tail from then on.

## 2026-09-13 — CLASS: a fingerprint-fence check built from the checking desk's own view misses the lanes another desk pins — n=2 in one day, both directions

**Incident + basis.** Edit direction, this desk: a registered
devbook section was edited while a peer desk's live lane pinned
its fingerprint. The editor's fence check was an INFERENCE from
the item's subject matter ("lc-38 is a pointer-migration item,
not a guard build") — and the item was a migration item by
subject while being a guard build BY ITS BRIEF, dispatched
explicitly as the class re-probe. The dispatching desk's words:
"a fact only this desk has"; the subject matter is exactly the
wrong instrument. No harm resulted for two reasons that are net,
not luck: the brief's read-from-FILE-never-trust-the-pin
instruction (exercised live earlier the same day), and the
dispatcher steering by artifact plus a state-token ping on
noticing. Hold direction, same day, roles reversed: a fence's
lift condition named one dependent lane when a peer desk's lane
pinned the same fingerprint (the df-192 second-dependent
correction). Two firings, one class, opposite verbs.

**Class.** A registered section's pin set is DISTRIBUTED STATE:
each dispatching desk holds its own lanes' pins in its dispatch
record, and no desk can enumerate another's. Any fence act —
holding an edit, or deciding an edit is safe — that derives the
pin set from the actor's own view plus inference is reading a
label where only the record answers. Same family as
warm-from-the-listing (routing module, 2026-09-13): a property
only the holder's record carries, inferred from an outside
surface.

**Pre-formulated rule text** (dispatch skill §6, beside the
fingerprint-invalidation clause): "Before editing a registered
section, one line to each desk that dispatches its class: 'does
a live lane pin this section?' — the dispatch record is the only
instrument for the pin set, and an item's subject matter answers
a different question. The reply is cheap, the fork it prevents
is not; the read-from-file binding in briefs is the NET for the
miss, never the licence for skipping the ask. And the ask closes
only the edit-time question: a lane that read the section BEFORE
the edit holds stale text however correct both desks were, and no
ask reaches that window — the lane's REPORTED fingerprint is the
one instrument that dates the two channels against each other
(measured 2026-09-13: lc-38's lane reported the pre-amendment
hash from a read that predated the landed edit, correct on both
ends and stale anyway; the report is what surfaced it)."

**Consumer + drain seam.** This desk's registered-section edits
immediately (applied from this entry forward); dispatch skill §6
amendment on the normal quota drain.

## 2026-09-13 — the stored-brief detector: run the entry's own done-criterion as a probe before treating the entry as a proof

**Incident + basis.** lifecycle lc-38 (relayed by the drain desk
with the worked example claimed as its own): the item's text
described a live defect; a sibling item (lc-86) had removed that
defect between the entry's grade date and its dispatch. The
dispatching desk re-read the entry AND the ledger decision and
treated "the decision is answered" as the premise check — while
the premise that decided the item was whether the defect still
REPRODUCED. The lane's grounding round ran the entry's own
done-criterion as a probe, four minutes, and it answered the
whole item: the criterion already passed, so the item was done
and the build was the wrong act.

**Class.** A stored entry's premise can be killed by a sibling
landing between grade date and dispatch, and NEITHER entry can
know — nobody holds both halves, which is why the stale-premise
rule does not fire on its own here (the corpus's stored-brief
bullet states the exposure; what it lacks is a cheap detector).
Re-reading the entry and its citations confirms the entry's
internal consistency, never its premise: the reasoning stays
plausible while being refuted in the tree.

**Pre-formulated rule text** (dispatch skill §1, beside the
stored-entry provenance clause): "A stored entry's DONE-CRITERION
doubles as its staleness detector: run it as a PROBE before
treating the entry as a proof — at brief time, or as the lane's
first act. Where the criterion already passes, the item is done
and the build is the wrong act; the probe costs minutes and
answers what no amount of re-reading the entry's reasoning can,
because the reasoning stays plausible while the tree has moved."

**Consumer + drain seam.** Dispatch skill §1 amendment on the
normal quota drain; both dispatching desks apply it from this
entry forward (the drain desk is the worked example, at its own
insistence).

## 2026-09-13 — slot-(e) lessons with out-of-boundary homes default to dying in chat; the enumeration slips, never the individual lesson

**Incident + basis.** The drain desk caught itself twice in one
session leaving a lane's slot-(e) candidate lessons unrouted —
lc-38's pair surfaced hours late with "sitting in chat with no
carrier, the two-exits failure with my name on it", then lc-115's
second candidate was "about to" repeat it identically. The desk's
own framing, adopted as the datum: routing slot (e) is evidently
not done reliably from memory, and what slips is the ENUMERATION
(walking every lesson to a carrier or a decline), never the
judgment on any individual lesson once looked at.

**Class.** The closing-report form makes the LANE enumerate its
lessons (slot (e) demands them), but no form makes the RECEIVING
desk enumerate their dispositions — the obligation has output on
one side of the channel only, so its absence on the grading side
is invisible (the obligation-with-no-output shape). Lessons whose
home is the grader's own boundary get booked in stride; the ones
needing ROUTING to another desk are exactly the ones with no
carrier at hand, so they cost a decision plus a message and lose
to momentum.

**Pre-formulated rule text** (dispatch skill §4, the
report-grading duty): "Grading a closing report includes
dispositioning slot (e) BY COUNT: each candidate lesson is
booked, routed to the desk whose boundary holds its home, or
declined with a line — and the digest that grades the report
states the count (e.g. 'slot (e): 3 — one booked, one routed, one
declined'). A graded report whose digest is silent on slot (e)
has not been graded; the count is the visible output the
obligation otherwise lacks."

**Consumer + drain seam.** Dispatch skill §4 amendment on the
normal quota drain; both desks apply the count-in-digest form
from this entry forward (fire-rate datum: n=2, one desk, one
session, self-caught both times).

## 2026-09-13 — a write set is incomplete until the brief has asked whether the change emits a new diagnostic ident

**Incident + basis.** Lifecycle lc-112 (drain desk's digest, graded
at the judgment desk): the lane shipped correct code, but the change
emitted a NEW diagnostic ident whose registry file sat outside the
lane's write boundary — so the lane left `--test` at FINDING and two
arms red, unable to reach the file that closes them. The code was
right; the write set was wrong, and nothing in the brief form asks
the question that would have caught it at brief time.

**Class.** Write-boundary resolution (the dispatch skill's
"disjointness resolves to realization surfaces" clause) enumerates
the files that realize the COMMISSIONED changes — but a change can
also emit a SIDE ARTIFACT the design prose never names: a new
diagnostic ident, an enum member, a registered key, anything a
registry or roster elsewhere must learn about. That realization
surface belongs to the change as much as the edited file does, and
a boundary drawn without asking leaves the lane provably unable to
finish green — the failure surfaces as red arms at close, priced as
a round trip instead of one brief-time question.

**Pre-formulated rule text** (dispatch skill §1, the write-boundary
resolution clause): "A write set is incomplete until the brief has
asked whether the change EMITS a new diagnostic ident, key, or
member some registry must learn about — the registry file is a
realization surface of the change, inside the boundary or named as
the dispatcher's own residue. A lane that ships correct code and
cannot reach the file that makes its checks green was boxed by this
omission, not by its work."

**Consumer + drain seam.** Dispatch skill §1 amendment on the
normal quota drain (measured: lc-112, one lane, correct code with
two arms red at close).

*Amended same day, three more fires plus the discriminator (drain
desk dotfiles-93, wave 1):* lc-33 and lc-68 amended at brief time,
lc-34 checked and CLEARED — and the clearing is what sharpened the
rule into a one-command check for this repo family: a FINDING emit
site mechanically requires a registered roster row (roster.py
enforces it), a COULD NOT VERIFY emission requires none, and a
whole-package grep for the bracketed idiom vs the plain phrase
separates the two ('COULD NOT VERIFY [' zero hits package-wide,
plain form eight in one file). The pre-formulated text gains its
cheap discriminator: ask the emit-KIND, not just whether output is
new.

*Second face, same wave (drain desk's close report, lc-79):* a
VOCABULARY addition is the same under-declaration one level up — a
new value in a closed vocabulary needs every CONSUMER of that
vocabulary in the write set (the renderers, checkers and counters
that switch on it), and the consumer list is computable from the
code the same way the roster requirement is. The class is
therefore two-faced and both faces are checks, not judgment: a new
diagnostic ident asks its registry; a new vocabulary value asks
its consumers.

## 2026-09-13 — the mailbox's loss is asymmetric by BLOCKING, not by message kind: only a directive the lane would block on announces its loss

(Amended same day: the first version keyed the asymmetry to
message KIND — directive vs state update — and the drain desk
measured a counter-case within hours. The split that holds is
whether the lane would BLOCK without the message.)

**Incident + basis.** Two measurements, one day, both lifecycle.
(1) lc-112: the dispatching desk sent the lane 3+ messages; at
least one was lost. The lane's closing report named two gaps the
desk's own record showed ALREADY CLOSED — its snapshot was missing
the update that closed them. (2) lc-81, the counter-case: the desk
sent the lane a RULING (the unresolved branch must write `true`);
send returned success; the lane's closing report says "no
dispatcher message received after the brief", and it shipped
`false` — deciding the question ALONE, declaring the choice as a
deviation with grounds. From the desk's side that is
indistinguishable from a lane that received the ruling and argued
against it; the only tell was one slot-(d) sentence true of the
brief and false of the lost message.

**Class.** Message loss is symmetric at the channel and asymmetric
at the failure — but the axis is BLOCKING, not kind. A lost
message the lane would BLOCK on self-announces: the work does not
appear, the horizon fires. A lost state update announces nothing
(the lane reports confidently off the stale snapshot), and a lost
directive that settles a question the lane can decide alone is
exactly as silent: the lane decides, ships, and reports the
decision as its own, and the dispatcher reads a DEVIATION where
there was a COUNTERMAND. The lc-81 case carries a second finding
that cuts against the obvious fix: the lane was RIGHT and the
lost ruling was WRONG — the lane held two artifact facts the desk
did not (no live scan existed for the `false` to relax; the false
branch was loud by design, dissolving the asymmetry the ruling
rested on). "Deliver directives more reliably" is therefore not
straightforwardly an improvement when the directive is a desk
overruling a lane that has read the code the desk has not — the
desk verified both facts at the artifact, accepted the lane's
version, and recorded the self-overrule in the closure reason
rather than taking it quietly.

**Pre-formulated rule text** (dispatch skill §4, beside the
silence-handling duties; the blocking half is the drain desk's
text verbatim): "State updates whose staleness would change what
a lane REPORTS travel by ARTIFACT, never only by message — the
lane re-reads the artifact at report time, so a lost message
costs nothing. A dispatcher grading a report checks each reported
GAP against its OWN record before acting on it: a gap the record
shows closed is a staleness finding about the channel, not a work
item. And a lost directive announces itself ONLY where the lane
would otherwise BLOCK on it: where the directive settles a
question the lane can decide alone, its loss is as silent as a
lost state update — the lane decides, ships, and reports the
decision as its own, and the dispatcher reads a deviation where
there was a countermand. The detector is the same one either way:
a directive whose content is not ALSO in the brief file was never
reliably sent."

**Consumer + drain seam.** Dispatch skill §4 amendment on the
normal quota drain (measured: lc-112, ≥1 of 3+ lost, two stale
gaps reported; lc-81, a lost countermand shipped as the lane's
own deviation — and the countermand was wrong at the artifact).

## 2026-09-13 — the write-boundary join is only as trustworthy as the slot it joins over: prose hides a cycle, short-but-pure paths read complete

**Incident + basis.** Drain desk's pre-dispatch join over the
lifecycle ready set, two catches before any lane opened, neither
by a check (reported in b8's findings digest; graded here). (a)
UNSCHEDULABLE CYCLE rendered as healthy work: lc-47 blocked on
"the compaction verb does not exist yet"; lc-58's amended
criterion demanded landing in the same change as lc-47. Each
entry's render was correct alone — lc-58 read SCHEDULABLE, lc-47
read READY-blocked — while neither could ever schedule. The cycle
hid because lc-47's write-set was PROSE, so the join never
collided the two (merged into lc-111 at the drain desk, not
booked as a sibling). (b) The QUIET direction: lc-60's slot was
pure paths and simply SHORT — lanes.py + firelog.py named, but
the verb needs a parser entry in cli.py and its render lives in
judgment.py. The join under-reports collisions and reads
complete; no prose to spot.

**Class.** The routing module's mapping-source rule derives the
item→lane mapping from a join over write-boundary slots — so the
join inherits every slot failure, and the two directions differ
in visibility: a prose slot at least LOOKS unjoinable, while a
short pure-paths slot looks exactly like a complete one. The
same slot failure's LANE-side face was measured the same day
(the ident-registry entry above: correct code, two arms red,
boxed by the omission) — one slot defect, two consumers, neither
seam checking completeness. The cycle case adds the blocker
slot: an evidence predicate produced by the very change it gates
is a coupling wearing a blocker's syntax, and both renders stay
individually correct while jointly dead.

*Amended same day (drain desk dotfiles-93, wave 1): even a
CORRECT join's collision output answers only WHO collides, never
whether the colliding items are the SAME WORK.* lc-80 and lc-95
shared CLAUDE.md in the join's own evidence lines, and the
collision was read as a serialization fact while lc-80 duplicated
part (i) of lc-95 — found at booking time, one lane spent on work
another entry covered. A collision on the same file is also a
duplicate-content PROBE: the two bodies get compared before both
are dispatched, and the intake join's carrier search covers items
naming the same file AND section, not only the realizing file
read alone.

**Pre-formulated rule text** (routing reference, the
mapping-source line; drain-desk text for the blocker half
verbatim): "The join over write-set slots names which items
collide only where each slot lists a path to EVERY realization
surface; a join over a slot that is prose, or pure-paths-but-
short, under-reports and reads complete — the join's output
carries the slot's grade, never better. And an evidence
predicate whose truth is produced by the very change it gates is
not a blocker, it is a coupling: render it as one item or an
ordered pair, never as two entries each individually healthy."

**Consumer + drain seam.** Routing-reference amendment on the
normal quota drain (measured: two shapes in one join, drain
desk, lifecycle ready set; the lane-side face same day in the
entry above).

## 2026-09-13 — a grounding-basis path that does not exist reads as the most ordinary line in the brief; a watcher's dead-baseline control caught it

**Incident + basis.** Drain desk's lc-56 brief (reported in b8's
findings digest; graded here): the grounding section named
test/test_ledger.py as "the existing test idiom you extend". The
file does not exist. Nothing in brief-writing surfaced it — the
brief had already DISPATCHED. What fired was the lane watcher's
dead-baseline assert (the baseline-is-its-own-positive-control
rule): the named file hashed to ABSENT at arming. Corrected at
the artifact, lane repointed.

**Class.** §1's provenance rule grades repo-state claims, and a
bare path in the grounding list IS one — "read this file" asserts
existence plus the asserted role — but it wears the costume
drawing least scrutiny: a file list reads as pointers, not as
claims, so no line in it ever gets the grade. The catch came from
an instrument built for a DIFFERENT failure (a dead lane watcher),
which is the cross-instrument divergence detector working: a
positive control that resolves its anchors at arming grades every
path it is handed, whoever wrote it.

**Pre-formulated rule text** (dispatch skill §1, the
grounding-basis clause; drain-desk text verbatim): "a brief's
grounding-basis paths are RESOLVED against the tree before
dispatch — a named file that does not exist is a repo-state
claim, and it reads as the most ordinary line in the brief."

**Consumer + drain seam.** Dispatch skill §1 amendment on the
normal quota drain (measured: lc-56, caught post-dispatch by a
watcher's arming control, not by brief-writing — the cost of the
gap is one round trip plus a lane working under a false premise
until the watcher armed).

## 2026-09-13 — a mutating instrument in a brief's baseline list defeats the same brief's private-copy prohibition: the list wins

**Incident + basis.** Fifth occurrence today of prove-rows walking
a shared live tree (drain desk's lane watcher, reported in b8's
digest; graded here): FOREIGN WRITE fired on
plugin/cli/lifecycle_core/lanes.py, then items.py, then retire.py
— walk order — each byte-identical to HEAD by the time of the
look (sha256 against `git show HEAD:<path>`, not git status; no
damage, every restore byte-identical). Attribution holds because
only two lanes were running and the lc-56 lane declined to run
the tool live and said so in its grounding return. Four of the
five occurrences trace to one structural cause: the dispatching
brief lists `python3 tools/prove-rows.py` under "Verification —
baselines", among unittest/audit/absence-scan. Both of today's
briefs ALSO carried an explicit "any mutate-and-restore
instrument runs in a private copy" paragraph — authored by the
same desk that wrote the devbook sentence warning of exactly
this — and the list won, twice.

**Class.** Template-shaped, not reader-shaped. A baseline list is
read as a sequence of commands to run on the tree as found, and a
prohibition stated elsewhere in the same document does not reach
into the list — the scope-sentence-was-the-defect shape one level
up: not a too-narrow rule but a rule contradicted by the FORM of
the document carrying it. A reader following the list is behaving
correctly; the list is what is wrong. Instrument note, grading
the watcher this carrier booked earlier today: the same per-lane
own-files watcher caught this walk AND the false grounding-basis
path — two distinct defect classes, one instrument, inside an
hour. Its discriminating property is watching each lane's OWN
files and treating everything else as foreign; a whole-repo
watcher would have read the walk as lane liveness.

**Pre-formulated rule text** (dispatch skill §1, brief
composition; drain-desk text verbatim): "A MUTATING INSTRUMENT
NEVER APPEARS IN A BRIEF'S BASELINE LIST. A baseline list is read
as a sequence of commands to run on the tree as found; anything
that writes to a tracked file belongs in its own labelled block
with the private-copy requirement attached to the command itself,
never in a list whose other members are read-only. A prohibition
stated elsewhere in the same brief does not cure this — measured
2026-09-13, two briefs carrying both the list and the
prohibition, the list won."

**Consumer + drain seam.** Dispatch skill §1 amendment on the
normal quota drain (n=5 in one day, 4 template-traced). The
mechanizable slice — an in-file MUTATES_TRACKED_FILES marker a
brief-composition check can refuse to pair with a baseline list —
is a lifecycle item, booked at the drain desk by the two-exits
rule.

*Amended same day, sixth instance (drain desk dotfiles-93, wave 1,
booked into lifecycle lc-100):* the same structural cause — the
tool listed among ordinary baselines — reproduced under a THIRD
desk and a different executor VENDOR (codex terra), which is what
promotes the diagnosis from a desk habit to a rule about the
template. Two facts the first five instances could not supply:
the lane ran in a PRIVATE CLONE, so the stray edit the walk left
never reached the shared copy — clone-by-default observed working
as isolation before the tool defends itself — and concurrency
corrupts the prover's OWN verdict, not only its neighbours (exit
3 "unreliable" in the shared tree, exit 0 for the same tree in
isolation, every arrangement holding).

## 2026-09-13 — a brief's Fix-prose contradicted the item text it summarized, and following it literally would have re-shipped a reverted over-fire

- Incident + basis: the doctor-bundle brief (statiker-fd desk, this date) restated df-168's fix as an UNSCOPED could-not-verify rule; built literally it reproduces the exact 6-of-7 false-positive over-fire becf593 reverted the day before. The lane caught the contradiction because the brief's own grounding section named the ITEMS.md requirement text as binding evidence; it built the item-consistent narrower version and reported the deviation (lane report slot d.2, commit 8dbfd3c).
- Class: brief paraphrase-drift against the stored item body — the §1 files-listed-never-paraphrased rule reaching the dispatcher's OWN summary prose, which reads as instruction, not as a paraphrase to grade.
- Pre-formulated rule text (for the brief form, §1): 'Where a brief summarizes a booked item's fix, the item's requirement text is BINDING and the brief's prose illustrative — the brief says so, and a contradiction between them is a grounding finding the lane reports, never a judgment call it makes quietly.'
- Consumer + drain seam: the forms release batch (with dg-35/36/37 and the two 2026-09-13 entries already queued).

## 2026-09-13 — cheap isolation defeats the one-lane clause: when parallelism stops costing, singletons become the default nobody chooses

**Incident + basis.** Drain desk dotfiles-93's close-time
self-grade (wave 1, reported in its four-question close review):
lc-61, lc-80 and lc-118 ran as three singleton lanes where the
one-lane clause says bundle — three disjoint small items, each
small against a lane's fixed cold start, three cold starts paid
for elapsed time the desk did not need. Its own diagnosis, adopted
as the datum: "clone isolation made parallelism easy, which is
exactly how that clause gets skipped." The desk had the join, read
it correctly, proved disjointness — and still split, because
nothing resisted.

**Class.** The earlier identity-mapping entries blame an absent or
unread join; this instance had a CORRECT join in hand and split
anyway. The driver is economic, not informational: the one-lane
clause's enforcement was always the FRICTION of safe parallelism
(overlap risk, worktree setup), and per-lane clone isolation
removes the friction without touching the fixed per-lane cold
start — so the visible cost of splitting drops to zero while the
real cost (N cold starts) is unchanged and invisible at dispatch
time. Better isolation tooling therefore INCREASES identity-
mapping pressure; the spend readout at close is the only surface
where the cost reappears.

**Pre-formulated rule text** (dispatch skill, the ONE-lane
clause): "Isolation ease is not bundling license: a clone or
worktree per lane removes the RISK of parallelism, never its
per-lane fixed load — disjointness proves parallel is SAFE, the
one-lane clause asks whether it is WORTH a cold start, and the
two questions are answered separately. Small disjoint items
default to one bundled lane; the split is what carries the named
reason."

**Consumer + drain seam.** Dispatch skill §1/§3 amendment on the
normal quota drain (measured: wave 1, one desk, self-caught at its
own close review — the close-time spend question's first live
catch).

## 2026-09-15 — the session trailer discriminates SESSIONS, not lanes

**Incident + basis.** Lifecycle drain wave A (drain desk
dotfiles-a8, judgment desk dotfiles-89): two parallel opus lanes of
ONE session produced commits with byte-identical trailer blocks —
Co-Authored-By AND Claude-Session — verified by the drain desk via
`git interpret-trailers --parse` + diff (zero lines differing);
mechanism confirmed independently at dotfiles-89 on lifecycle
1caa4dc, whose Claude-Session names the PARENT session's URL. A
lane's own report also misstated the sibling as carrying NO session
trailer — right conclusion, wrong stated reason, caught by the
desk checking its instrument before the claim.

**Class.** Attribution-label reach: §4's "the session trailer,
where the harness wrote one, is the discriminator" holds between
SESSIONS only — every lane of one session inherits that session's
URL, so the discriminator is the same value by construction exactly
where a wave's sibling commits need telling apart. Sibling of
dotfiles df-217 (briefed-identical Co-Authored-By) and of the
label-the-checked-party class (dotfiles pre-push, 2026-08-10).

**Pre-formulated rule text** (dispatch skill §4, the trailer
clause): after "The session trailer, where the harness wrote one,
is the discriminator" append: "— between SESSIONS only: every lane
of one session inherits that session's URL, so sibling lanes of one
desk carry byte-identical session trailers by construction, and
within-session attribution rests on disjoint write sets and each
lane's own claim, never on any trailer."

**Consumer + drain seam.** Dispatch skill §4 amendment on the
normal quota drain; dotfiles df-217 carries the tail's claim-rule
half and cites this entry.

**Firing record, 2026-09-15 (second independent measurement, new
direction).** Drain desk dotfiles-f1, lifecycle wave 1: three lane
commits (bc35cea, 72598bf, 73f59a9) byte-identical on BOTH
trailers, re-verified at the judgment desk. Two sharpenings the
first measurement did not carry. POPULATION: for a within-session
fan-out the §4 fallback clause ("candidates still
indistinguishable") is not an edge case but the WHOLE population —
a reader meeting "the session trailer is the discriminator" takes
it as generally available, and for sibling lanes it never is.
DIRECTION: found by a LANE from the claiming side — bc35cea
carries lane B's exact trailer block and is another lane's work,
so the trailer FALSELY CLAIMS where the rule's text anticipates
only failing to claim; the lane identified its commits by content
and write-set disjointness, which held only because the wave's
boundaries were disjoint by construction. Same cause set touches
dotfiles' pre-push guard comment, which recorded the trailer as
unreliable via non-determinism only; inheritance is the second,
systematic cause (comment amended same day).

**Incident + basis.** Same wave, measured in both directions with
neither lane disobeying its brief: lane A's `rm -rf` + `git clone`
at a generic scratchpad path destroyed lane B's private clone
(reflog empty — repository object destroyed, not rewound;
attributed by mtime pair `.git/config`/`.git/HEAD`); lane B's
probe residue later crossed into the tree lane A was measuring.
The brief said "your OWN scratchpad, never another session's" and
assigned no slugs — both lanes SATISFIED the clause, because both
words key to the SESSION grain while the collision is lane against
lane. The skill's slug rule (§1, untracked outputs) already exists;
the skeleton's Scratch line does not force it, so a compliant-
reading brief ships the collision.

**Class.** Boundary clause keyed one grain too coarse: a scope word
("own", "another session's") at the session grain over a hazard at
the lane grain reads green at exactly the moment it does not hold.
Same family as the directory-grain allowance concealing undeclared
artifacts (dotfiles CLAUDE.md).

**Pre-formulated rule text.** (a) Brief skeleton, Scratch line:
"Scratch: <own scratchpad>/<lane-slug>/ — per-lane subdirectory
assigned HERE; parallel lanes of one session share one session-
keyed scratchpad, so an unslugged path collides lane-against-lane
while reading compliant." (b) Mechanical half, hook candidate
(computable predicate, near-zero false fires — booked as dg item
in this repo's carrier): at dispatch, refuse two live lanes of one
session whose assigned scratch paths are not distinct.

**Consumer + drain seam.** Dispatch skill §1 amendment on the
normal quota drain; the hook half drains through this repo's item
carrier (see the dg booking of the same date).

## 2026-09-15 — a mutate-and-restore tool's venue constraint travels IN the instruction that names it (n=3)

**Incident + basis.** Three instances in one day, one wave
(lifecycle drain, wave A): two round-1 briefs listed
`tools/prove-rows.py` among ordinary verification commands — both
lanes independently routed it to a private clone — then the DESK
that had just read both reports ran it on the live shared checkout,
killed it mid-arm, and left an injected mutation in `migrate.py`
(found by sha256 of all 64 tracked files against HEAD blobs,
restored from the committed blob). The desk's own diagnosis: not a
missing fact — its brief stated the hazard in one item and the
co-writer in the next, then said "run it as a verifier"; all
premises present, the JOIN missing, with the venue instruction
pointing the wrong way. A follow-up booking (lifecycle lc-133)
sharpened the class: the tool's restore runs at the END of each
arm, so an interrupted run leaves the mutation live — the hazard is
not misuse alone, it is the tool's crash shape.

**Class.** Venue constraint separated from the instruction that
triggers the act. Two lanes making the join correctly is not
evidence the brief was sound — the reader who fails is the one
holding the most context, because the join feels already made. The
dotfiles guard/checker devbook carries the executing-side rule
(mutate-and-restore runs in a private snapshot); this entry is the
BRIEF side: nothing in §1 makes the venue ride the command list.

**Pre-formulated rule text** (dispatch skill §1, the verifier
bullet or its own line): "A verification command that MUTATES and
restores a tracked file (a prove-rows, a mutation walk) carries its
venue constraint IN the same line that names it — 'run in a private
clone/snapshot, never the shared checkout' — never in a separate
hazard note: the instruction and its constraint separated is how
three parties in one wave, two of them warned, put the tool on the
live tree or nearly did."

**Consumer + drain seam.** Dispatch skill §1 amendment on the
normal quota drain; the crash-shape half drains through lifecycle
lc-133 (that repo's tool).

## 2026-09-15 — a brief's red-first step aims at the symbol the finding names, not where the defect lives (n=2, one desk, one sitting)

**Incident + basis.** Two dispatch briefs written by one desk
(statiker-d4, the run-3 contract-repair arc) in one sitting each
specified their red-first step at the wrong object, and each lane's
commissioned critique pass caught it before the first build call.
Lane 1 (sonnet-launch-probe): the brief said reproduce S2 by
driving `verdict()` with hand-built leg dicts — but the defect
lives in `leg_background_resume()`'s marker-to-dict CONSTRUCTION,
which hand-built dicts bypass by construction; the reproduction
could never go red. Lane 2 (sonnet-driver-probe): the brief said
"run the NEW battery against the OLD implementation" — while item 1
of the same brief IS the extraction of the function the battery
targets, so the old file has no such function and the step names
something that does not exist. Desk verified both at the code
before confirming; reported by the desk itself as a shared blind
spot rather than fixed twice quietly (statiker LEDGER, 2026-09-15
arc; relayed and booked by the driving desk statiker-9c).

**Class.** Red-first altitude keyed to the finding's NAMED SYMBOL
rather than to the defect's location or the old code's actual
state. The finding names a symbol; the brief author reaches for
that symbol; the symbol is the wrong object — once a reader
function when the bug was in its input constructor, once a function
the "old" side cannot contain because the brief's own first item
creates it. The corpus's instruments-sharing-an-author rule with
the brief's author as the shared author: invisible from inside any
single brief, visible only across the set. The commissioned
critique pass is the measured catch mechanism (2 for 2 here,
both pre-build).

**Pre-formulated rule text** (dispatch skill, the brief's
red-first/verification bullet): "The red-first step is specified at
the altitude where the DEFECT lives, not at the symbol the finding
names. Compose-time check, per red-first step: name the function
AND state what it is being fed, then ask whether the defect can
reach that input — and where the brief itself creates or extracts
the target, say explicitly which side of that change the 'old'
arrangement is."

**Consumer + drain seam.** Dispatch skill amendment on the normal
quota drain; until then the compose-time check is brief-author
prose.

## Symptom claims cross handoffs ungraded — the provenance rule reads as repo-state-only

**Incident + basis.** The 2026-09-16 Marvel Rivals freeze handoff
carried "sits in ntsync_schedule burning 1 CPU tick in 5.5 seconds"
and a "250 ms band" as measurements; the receiving session built a
trigger design on them within minutes, and the band later proved to
be three MangoHud frametimes mixed with two GPU-idle run lengths
from a different instrument — never one measurement. The
retrospective (CachyOS-Setup
docs/directives/2026-09-16-freeze-investigation-retrospective.md,
"Also owed, smaller") names the mechanism: §1's per-line provenance
grade is written against claims about the TARGET REPO's state, and
symptom/measurement claims escape it because they arrive as
narrative, in a finding's register, in sections no grade covers.

**Class.** Label-over-body / ungraded-inheritance: a claim kind the
provenance rule's wording does not reach, crossing the brief
boundary with inherited standing. Same family as §4's "a claim is
opened before it is REPEATED"; this is its brief-compose-time twin
for measurement claims.

**Pre-formulated text.** Widen §1's provenance bullet: "The grade
covers every claim of FACT the brief asserts — repo state,
MEASUREMENTS, symptom descriptions, environment behavior — not only
repo-state citations: a number, band, duration or rate carries the
instrument that produced it and the read that verified it, or 'from
<source>, unverified'; a symptom description names its reporter and
is quoted, never paraphrased (a paraphrased symptom is the
label-over-body drift at the definition the work rests on)."

**Consumer + drain seam.** Dispatch skill §1 amendment at the
normal quota drain; the freeze retrospective is the incident record.

## 2026-09-18 — CLASS: §1's critique-pass bullet says "every brief" while §1's own exception clauses already exempt two dispatch kinds, 520 lines earlier

**Incident + basis.** A lifecycle read lane (dispatched by the peer
desk lifecycle-7e for lc-192, the migrate.py read — a DISCOVERY
dispatch) reported in its critique pass that two lines of its brief
contradicted each other: the pasted READ-ONLY tail closes "No repo
writes, no interim messages" (references/forms.md:361-363, read at
the source repo, not the cache) while SKILL.md:601 commissions the
critique pass on "Every brief — small ones included … returned on
the tail block's channel". The lane named both lines, resolved it as
specific-beats-boilerplate, sent the critique anyway, and flagged
rather than guessing. Relayed to this desk by lifecycle-7e; both
passages opened here before the entry was written.

**The relayed statement located it wrongly, and the correction is
the finding.** The report framed it as tail-versus-§1 and proposed
widening the tail to "no interim messages except the commissioned
critique pass". That fix points the wrong way. SKILL.md:76-79 —
the discovery-dispatch exception — ALREADY says "no report files, no
interim messages", for its own measured reason (each extra output
medium re-writes the answer; the cost driver is output volume). The
tail is a faithful restatement of that exception. The over-reaching
sentence is the critique-pass bullet's word "every", which is
already bounded by two exception clauses sitting ~520 lines above
it, with no local signal at the bullet that the scope was ever
narrowed. Widening the tail would have ADDED a critique pass to
every discovery and verifier lane — contaminating verifier
independence, which §1:70-74 exists to protect — on the strength of
a contradiction correctly observed and wrongly diagnosed.

**Class.** A universal quantifier written in a rule bullet whose
scope was already carved out elsewhere in the same file, far enough
away that neither site reads as qualified from the other. Distinct
from the two existing collision entries above (2026-09-13, the
base-check HALT and the reservation HALT): those are a DESK's brief
contradicting the tail, repairable in that desk's next brief. This
one is the SKILL contradicting itself, so every discovery and
verifier brief composed from it inherits the contradiction, and the
lane's critique pass has been reporting the instrument's own defect
back to desks that could only read it as their own.

**It bites in the silent direction.** A lane resolving it the other
way simply sends no critique pass, and an absent critique message is
indistinguishable from a brief with nothing wrong in it — which is
exactly the signal the bullet exists to make dispatcher-visible.

**Pre-formulated rule text** (SKILL.md, the critique-pass bullet's
opening, replacing "Every brief — small ones included — asks"):
"Every EXECUTION brief — small ones included — asks for ONE message
before the lane's first build call … . Verifier and discovery
dispatches are exempt by the exceptions at the head of this section
and take the read-only tail's 'no interim messages' unchanged: a
verifier has no Background lines to grade and the pass would carry
dispatcher reasoning into the one dispatch kind that must not
receive it; a discovery lane's brief contradiction is reported in
its single findings message instead."
The tail at references/forms.md:361-363 is CORRECT AS WRITTEN and
is not edited.

**Consumer + drain seam.** Dispatch skill §1 amendment at the normal
quota drain. Until it lands, a desk composing a discovery or
verifier brief states the exemption in one line, because the lane
reads the bullet before it reads the exceptions.

## 2026-09-18 — the named channel line names a ROLE, and the desk's natural fill of that role is the one an in-process lane cannot use as given

**Incident + basis, n=2 the same day, two desks, DIVERGENT
outcomes.** The mailbox channel line reads `Report channel:
SendMessage to the dispatcher — your final text reaches no one.`
(references/forms.md:183-184). Both desks filled "the dispatcher"
with their own session name; both lanes were IN-PROCESS subagents.
(a) A lifecycle read lane reported the send REFUSED with "this
process's own main session" and routed to `main` instead.
(b) This desk's own verb-enumeration lane reported the opposite in
its closing line — the name "turned out to resolve to my own
dispatcher" — having delivered all ten parts to `main`.

**Which of the two the harness does is UNSETTLED HERE, and the
entry says so rather than picking.** Both accounts are the lanes'
testimony; neither desk executed the send itself, and no probe was
run. The observations agree on everything the finding needs — the
filled address was not usable as written, `main` was, and each lane
had to work that out mid-run — and disagree only about whether the
failure is a refusal or a silent redirection. A refusal is loud and
costs a retry; a silent redirection would mean the two spellings
are interchangeable for in-process lanes and the whole thing is
cosmetic. That is the discriminating question, and it is one probe:
one in-process lane instructed to send to its parent's session name
and to report the tool result verbatim.

**The sharpening, because the relayed version overstated it.** The
form does not produce an unresolvable address — it produces NO
address: "the dispatcher" is a role name, and the slot leaves the
`to` value to the composing desk. What the entry records is that
the desk's natural fill (its own session name, the thing it knows
itself by) is at best ambiguous and at worst refused for the
commonest lane kind, and nothing in the form says so. The failure
is dispatcher-side and the form is what permits it.

**Class.** A form slot whose fill is under-specified for the
default case, where the obvious fill fails and the correct one
(`main`) appears nowhere in the form. Adjacent to the existing
sync-vs-mailbox lane-probe machinery, which tells a desk WHICH
channel line to paste and never what to address it to.

**Pre-formulated rule text** (references/forms.md, the named
channel-line variant): "- named (mailbox teammate): `Report
channel: SendMessage to <the dispatcher's address> — your final
text reaches no one.` The address is `main` for an IN-PROCESS lane
(a subagent of this session): a send aimed at the parent session's
own name refuses as 'this process's own main session'. For a
CROSS-SESSION peer it is that session's name as ListAgents prints
it."

**Consumer + drain seam.** references/forms.md channel-line block,
normal quota drain; bundles with the entry above, both being
single-block edits to the same skill.
