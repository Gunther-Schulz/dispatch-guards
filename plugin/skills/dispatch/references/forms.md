# Dispatch forms — the closing report, the brief tails, the roadmap

Reference of the `dispatch` skill (operational corpus — see
SKILL.md's governance header). Load BEFORE composing any brief:
the tails below are PASTED into briefs, never recalled, and the
brief-reminder hook denies a tail-less brief pointing back here.

## 2. The report (mandatory shape; empty is valid, absent is not)

The brief prescribes this closing report; a dispatch without it is not
done. **Precedence:** a project that defines its own report form (e.g. a
project runbook's lettered sections) uses THAT form — this one is the
default for projects without one, never a second form to fill in
parallel.

**Every report line asserting the state of something OUTSIDE the
agent's own work — a file it did not write, a mechanism, another
repo, a tool's behavior — is either OPENED, with the read named,
or carried with its grade: "inferred, unverified"** (source: §1's
per-line provenance rule, in the return direction). The grade
follows the CLAIM, never the slot: (a), (b) and (f) carry their
evidence by construction, so (c), (d), (e) and (g) are where an
inference passes for an observation. A RECOMMENDATION resting on
an unopened claim carries the grade too — it is what the
dispatcher acts on. Form compliance is what hides an ungraded
inference: (c) asks for gaps and nothing more, so one shaped like
an observation fills it correctly, riding out among measurable
claims that all hold. The grade is the AGENT's to write because
the report is all its readers have: an ungraded external-state
claim is relayed onward as fact, and whoever receives the relay
cannot tell it from a measurement. What the DISPATCHER can tell
is a line carrying neither a named read nor a grade — an
incomplete report, demanded back like a missing slot.

Every slot (a)–(g) must appear — "none" is a valid answer, silence
is not; (h) rides the EXECUTION tail only:

  (a) items completed, with per-item evidence (file:line, test name)
  (b) checks/tests actually RUN, with their real output — the FULL
      counts, skips included (`N passed, M failed, K skipped`).
      A skip satisfies "real output" word for word and proves
      nothing: a skipped check differs from a check that does not
      exist only by its line in the report. So every skip is
      DISPOSITIONED — which check, why it skipped, whether that
      reason touches the item — and a skip in a check THIS lane
      built is a finding by construction: it says the built branch
      never executed, and a build whose verifier did not run is
      unverified, not green. `K > 0` with no disposition is an
      incomplete report, demanded back like a missing slot.
  (c) open points / gaps surfaced (see brief rule above), including
      anything that needed a tier above yours — returned as a question
      with its evidence, never settled at your own tier (§4)
  (d) deviations from the brief, each with its reason
  (e) findings worth turning into a rule/test (candidate lessons)
  (f) files touched + commit hashes (unpushed), established from
      the RECORD rather than from memory: the commits reported are
      those whose Co-Authored-By trailer carries the agent's OWN
      model name, and a commit it cannot claim by trailer is
      reported as "present in the tree, not mine". That trailer
      names a MODEL, so where a same-model sibling writes in the
      same copy it proves tier, never identity: the report says so
      rather than claiming the commit — mandatory on a
      shared copy, whose tree carries co-writers' work by
      construction, and doubly so after a summarization, where what
      the agent remembers doing and what the tree shows diverge
      silently. Config writes are repo writes: a lane that touched
      `.git/config` (a pushurl denial, a hooks path) reports it
      here, read-only briefs included.
  (g) what was NOT verified (honest residue)
  (h) sources actually read, of those the brief named (execution
      tail only)

An idle agent without a report gets the report demanded (SendMessage),
never booked as success — the missing report is an observed failure
mode of delegated work, and silence is never success (source:
site corpus dispatched-work rule). An idle notification can RACE a
message just sent to that agent — its summary then shows PRE-message
state, not current state: a minimal ping resumes the agent either way
and disambiguates at the cost of one message; never re-send the full
brief on a race, and never book the raced summary as where the agent
actually is. The race's mirror sits at the lane's END: the
lane-close message (§4's mirror duty) itself RESUMES the agent,
which re-idles with nothing to do — that terminal idle is a closed
lane's expected shape, not a signal: it books nothing and gets no
reply, since each reply re-resumes the agent into another idle (a
politeness loop; observed twice in one session, both after booked
reports). Stalls, watchdog kills, and mid-stream API cuts take a
STAGED path: peek at the task state, then RESUME the agent with a
narrowed close-out instruction ("finish with the evidence you have")
— kill-and-redispatch only after a resume fails, because a resume
re-enters the agent's accumulated context while a fresh dispatch
re-pays it (observed: a single dispatch survived an API cut and then
a watchdog stall on staged resumes, its accumulated context intact,
and delivered complete). The report-written-but-never-
SENT class presents as the same silence; the same demand cures it.
**Channel rule (NAMED/mailbox dispatches — the lane test is the
channel-line block below):** the closing report reaches the
dispatcher ONLY via SendMessage — a final text answer reaches no
one; the brief names this channel explicitly, and going idle
without having SENT the report counts as no report.
**Inbox drained before sending** — and between the parts of a
multi-part report: the report dispositions every dispatcher message
received up to send time, or names it explicitly as unhandled.
Composing a long report as a queue is what strands them (measured,
three times in one session: a GO sent after part 1 still stood
"open" in part 7, and two added assignments went undispositioned in
otherwise complete reports — one re-demand round each). The race
symptom is then readable from the report itself.
**Payload vs. pointer:** the channel carries the
short signal; anything beyond the report form's slots — roughly more
than a screen — goes in a FILE, and the message points to it. Basis,
context economy: an injected payload occupies the dispatcher's
context for the rest of its session, re-carried on every later turn.
A suspected prompt-cache-rewrite correlation stands recorded but
unproven — `dev-notes/payload-cache-correlation.md` in the source
repo; the gate rests on context economy alone. The
`message-payload-gate` guard enforces the rule mechanically for the
expensive direction (subagent → dispatcher).

**Brief-tail boilerplate.** A binding clause opens its block: at
the END of an invariant block it reads as transport plumbing rather
than as an instruction, and the very property that should make a
pasted tail a guarantee — being identical in every brief — is what
makes it skimmed (measured in one run of three same-form
discovery dispatches: two wrote a report file with the prohibition
standing twice in the tail's later sentences, the third, with the
same wording moved to the block's head and its consequence named,
complied). The tail is
PASTED, not recalled — free-composed briefs drop invariant clauses
(the channel and payload rules have reached executing agents only as
gate denials, at doubled composition cost); a pasted tail skips the
bounce and the report re-demand loop entirely. The tail reaches the
executing agent pasted in the DISPATCH PROMPT or inside a brief FILE
the prompt names — inline required only when no file brief exists;
duplicating the tail into both is a second copy that drifts. The
CHANNEL LINE alone is always prompt-side: it binds to `name`,
set at dispatch time, which a static file cannot know. Two blocks;
pick by dispatch kind, fill `<model>` AND the channel line — the
lane call is the dispatcher's, made at paste time,
never left to the agent (it has been misjudged agent-side; the
report-enforcer hook's docstring, soft-spot note).

Which lanes EXIST is a per-session PROBE, never a date: look at
THIS session's Agent-tool schema before the first dispatch whose
form depends on the lane. Accepts no `name` → only the synchronous
lane exists, so paste NO channel line (the final text is the
report, returning as the tool result) and the horizon rule does not
apply, a sync dispatch being unable to outlive the turn. Weigh what
that state does to the model gate, which mandates a `<model>-` NAME
on every generic dispatch and denies without one (measured, stdin →
stdout: generic type + `model` + no `name` → exit 2; the same
payload named → exit 0): where `name` cannot be expressed the
mandate is unsatisfiable, so only the pinned types the gate exempts
dispatch at all. The collision is real rather than a wording
problem, and the gate keeps its lane — the failure it guards, a
dispatch whose model is invisible where the operator watches, does
not stop being a failure because the schema moved. A session
needing a GENERIC dispatch in that state takes it to the operator;
working around a guard silently is the override reflex the guard
exists to prevent. The harness has
withdrawn `name` MID-SESSION from a session that had run named
dispatches hours earlier while a sibling session kept it, so the
divergence is per session in both directions — and a brief
carrying a mailbox channel line, composed by a session that has
gone synchronous, strands the report it asks for. Accepts `name`
→ the two lanes below.

Channel line (paste exactly one). `name` alone decides WHICH of
them, and they differ in where the agent's closing text lands.
The model gate mandates a name on every GENERIC dispatch, so the
unnamed lane is reachable only by the types that gate exempts —
pinned agent types, and modes whose model is fixed by construction
rather than chosen (a fork inherits its parent's):
- named (mailbox teammate): `Report channel: SendMessage to the
  dispatcher — your final text reaches no one.`
- unnamed (background task): `Report channel: your final text IS
  the report.`

Binding (as of 2026-08-17, harness 2.1.232 — the mailbox branch):
the Agent tool takes
no `run_in_background` parameter — its schema is
`additionalProperties: false` and lists none — so a
sync-vs-background FLAG cannot be expressed at all, and what once
read as a mode choice is made by naming. A NAMED dispatch returns
"Spawned successfully … via mailbox", promises no completion
notification, and is absent from the subagent listing: its final
text has not been observed reaching the dispatcher, and only
SendMessage delivers. An UNNAMED dispatch returns "Async agent
launched" plus an output file, and the completion task-notification
carries its final text to the dispatcher VERBATIM — including from
an agent that called no tool at all, so delivery does not depend on
the agent cooperating.

Which lane to pick: NAME the dispatch when the session must talk
across it — long builds, parallel fan-outs, teammates, anything
worth resuming — accepting that its report arrives only if the
agent SENDs it, which is what the mailbox channel line exists to
secure. Leave it UNNAMED for a short closed-form job the current
turn wants back without mailbox plumbing (probe, verifier, single
pipeline stage): the notification returns the report and the usage
metadata for free. Transcript usage entries are per-stream
snapshots — dedupe by API-call id before summing, and the
harness's subagent_tokens figure measures context, not spend.

Binding (as of 2026-08-01): the
harness HARD-BLOCKS a subagent writing report-shaped files
(REPORT.md and kin bounce with "return findings as text");
supporting DATA/evidence files still write fine. The report
therefore travels in the SendMessage itself — split into labeled
parts (1/N) when it exceeds one message — and briefs stop
assigning report file paths; data-file assignments are unaffected.
The block is measured against ONE namespace — `REPORT.md` and near
English relatives — and what it keys on is unestablished, so for a
brief in another working language it is NO backstop: a
German-named `*-bericht.md` wrote straight through. Where the
working language is not English, the brief names the assigned data
file as the ONLY permitted write path and says outright that any
further file, however named, is a deviation.

State tokens — crossings are inherent to the async channel: a
directive and an in-flight report pass each other, and each
side acts on a state the other has already moved past. Every
coordination message — a report part, an addendum, a dispatcher
directive or repair note — names the state it was composed
against: a HEAD sha, a version, or the verdict line it answers.
The token is what lets the receiver date a crossed message
against its own log; the resolution is a minimal ping naming
the newer token, never a content re-send (measured 2026-08-11:
six crossings across two sessions in one day, each resolved at
one ping with zero wrong actions — because each message
happened to quote concrete state; the convention makes the
accident a rule). One member of the class is avoidable, not
just cheap: a non-urgent directive sent to a lane while its
multi-part report is IN FLIGHT crosses the remaining parts by
construction — hold it until the final part lands; only a
directive that must STOP work (a killed premise, an abort)
justifies interrupting a report mid-series (measured: the one
same-session crossing that was not message-timing luck was a
supplement sent between parts 2/3 and 3/3).

EXECUTION tail (any dispatch that writes):

    Closing report (mandatory; the project's own report form if it
    defines one, else the §2 form here — never both; "none" is a
    valid slot answer, silence is not): (a) items completed w/
    evidence, (b) checks RUN w/ real output — FULL counts incl.
    skips (`N passed, M failed, K skipped`), each skip dispositioned
    (which check, why, whether the reason touches the item); a skip
    in a check YOU built is a finding, not a pass — the built branch
    did not execute, (c) gaps surfaced —
    incl. anything needing a tier above yours, returned as a question
    with its evidence, never settled at your tier,
    (d) deviations w/ reason, (e) candidate lessons, (f) files
    touched + commit hashes (unpushed) — only commits whose
    Co-Authored-By trailer is YOURS; one you cannot claim by
    trailer is "present in the tree, not mine"; a `.git/config`
    write counts as a repo write, (g) what was NOT verified,
    (h) sources actually read, of those the brief named.
    Drain your inbox before sending, and between parts of a
    multi-part report: every dispatcher message received up to send
    time is dispositioned or named as unhandled.
    <channel line>
    Message ≤3000 chars each: a report longer than one message is
    SPLIT into labeled parts (1/N) — do NOT write a report FILE
    (harness-blocked for subagents); supporting data goes to the
    brief's assigned DATA files, the message carries key findings
    + any such paths. A missing decision, file,
    or value is surfaced as a gap, never bridged with a guess.
    A check that got backgrounded is AWAITED before the closing
    report (TaskOutput block=true on its task id) — ending your
    turn orphans it; a report sent with a check still running is
    an INTERIM report, says so, and names what remains.
    Commits unpushed, by pathspec — `git commit -m "…" -- <paths>`
    with every flag BEFORE the `--` (after it git reads `-m` as a
    pathspec and the commit fails; `-F` for a multi-line message),
    never
    `git add` then `git commit` and never `-A`: the index is shared,
    so a co-writer staging between your `git status` and your commit
    rides out under your message whatever you added. A NEW file is
    invisible to a pathspec commit until `git add -N <path>`
    registers it (intent-to-add: zero content staged, full body
    still committed). Trailer:
    `Co-Authored-By: Claude <model> <noreply@anthropic.com>`.
    Never amend — always a new commit: the amend-gate denies
    subagent amends regardless of ownership (source: §1 amend
    rule).
    After sending the report your write grant is over: a defect you
    find later is REPORTED, never edited or amended (source: §4
    ownership rule).

READ-ONLY tail (verifier and discovery dispatches — no writes, no
commits, no report files; enumeration dispatches substitute the
data-file provision, §3b):

    NO REPORT FILE. Your findings go in your SendMessage reply — a
    file you write is not a report, is not read as one, and reaches
    no one. Split into labeled parts (1/N) past the size gate.
    Transient probe scratch goes in YOUR OWN scratchpad, never the
    dispatcher's, and is not a report file.
    <channel line>
    Return your findings in ONE message where they fit (verifier:
    verdict + basis; discovery: the N named facts, sources actually
    read). Where the basis is a check you RAN, its full counts come
    with it, skips included and dispositioned: a skipped check did
    not run, and a verdict resting on one is could-not-verify, not
    clean (source: §2 slot (b), carried into a lane that has no
    slots). A missing decision, file, or value is surfaced
    as a gap, never bridged with a guess. No repo writes, no
    interim messages.

Verifier dispatches stay exempt from the rich §1 brief form but NOT
from the read-only tail — artifact + question + that block (the
site corpus fresh-context rule's "nothing else" excludes dispatcher
REASONING; the tail is plumbing, not reasoning). Discovery
dispatches likewise take the read-only tail verbatim.

## 3. The roadmap form (for procedures the agent must execute)

Executable procedures handed to cheaper tiers take one fixed shape —
filling it is instance work (passes eval), designing it is not:

    Source:       <where this procedure is normative>
    Steps:        1. … 2. … (numbered, each checkable)
    Limits:       <box: what the agent must NOT decide/touch>
    Verification: <the command/grep/render that proves each step>

## 3b. The enumeration brief (the two-stage vet's cheap half)

A verdict that decomposes into exhaustive mechanical enumeration plus
judgment over the enumeration hands the ENUMERATION down with this
form (SKILL.md §4, verdict routing); grading stays at tier ≥
producer — the enumerator lists, the grader judges. The form is an
application of the under-report principle (executor skill §2: shape
the work so a cheaper tier cannot silently under-report); each rule
below exists because its absence produced a silent hole in a real
enumeration.

    Scope:       <the exhaustive question — every X in Y against Z>.
                 No materiality judgment: EVERY difference is listed;
                 what matters is the grader's call, not yours.
    Taxonomy:    closed difference classes; each item carries
                 exactly one label: ABSENT / REWORDED / WEAKENED /
                 RELOCATED / ADDITION / TAIL-DIFF.
    Known noise: exclusions named and defined exactly (a pattern, not
                 a vibe); excluded items are still LISTED separately,
                 never silently dropped.
    Coverage:    the report carries the coverage artifact — lines or
                 items walked and per-class counts, zeros stated
                 explicitly ("RELOCATED: 0").
    Exactness:   where byte-exactness is the requirement, check it
                 byte-exact (cmp/hash), never by reading.
    Reference:   the frozen source copy is the immutable reference;
                 declared deltas are claims-to-verify, not context.
    Quotes:      each item carries both-side quotes (source text and
                 render text).
    Boundary:    NOT for work where the noticing itself needs
                 judgment (design-fit, statistical grading,
                 falsification rounds) — that stays at the verdict
                 tier. Under-bar enumeration is redone one tier up,
                 never iterated at the failing tier (SKILL.md §4).

An enumeration dispatch is discovery-shaped — no commits, no interim
messages — but its output is a coverage artifact that outgrows the
message channel by construction (exhaustive scope × per-item quotes),
which the payload-vs-pointer rule (§2) forbids carrying in messages
anyway. The brief therefore ASSIGNS a data file for the enumeration
itself (data files pass the harness block that bounces report files —
§2 binding), and the tail's ONE-message line is satisfied by a
pointer: the file path + the per-class counts, zeros stated. The rest
of the read-only tail applies verbatim.

Where a data file was assigned, the returning message also quotes
the file's REAL key set, taken from the file itself
(`jq -r 'keys_unsorted|@csv' <file> | head -1` for JSONL), never
retyped from memory: a schema described in prose is a label over
its own body, and a dispatcher querying prose-drifted key names
gets all-null results that read as a defect in the DATA — a wrong
finding about the agent's work, manufactured by the report form.
One line in the brief, one line in the report; a dispatch assigned
no data file is never asked for a key set.
