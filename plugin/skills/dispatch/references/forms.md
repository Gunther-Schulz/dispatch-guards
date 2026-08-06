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
parallel. Every slot (a)–(g) must appear — "none" is a valid
answer, silence is not; (h) rides the EXECUTION tail only:

  (a) items completed, with per-item evidence (file:line, test name)
  (b) checks/tests actually RUN, with their real output
  (c) open points / gaps surfaced (see brief rule above), including
      anything that needed a tier above yours — returned as a question
      with its evidence, never settled at your own tier (§4)
  (d) deviations from the brief, each with its reason
  (e) findings worth turning into a rule/test (candidate lessons)
  (f) files touched + commit hashes (unpushed)
  (g) what was NOT verified (honest residue)
  (h) sources actually read, of those the brief named (execution
      tail only)

An idle agent without a report gets the report demanded (SendMessage),
never booked as success — the missing report is an observed failure
mode of delegated work, and silence is never success (source:
CLAUDE.md dispatched-work rule). An idle notification can RACE a
message just sent to that agent — its summary then shows PRE-message
state, not current state: a minimal ping resumes the agent either way
and disambiguates at the cost of one message; never re-send the full
brief on a race, and never book the raced summary as where the agent
actually is. Stalls, watchdog kills, and mid-stream API cuts take a
STAGED path: peek at the task state, then RESUME the agent with a
narrowed close-out instruction ("finish with the evidence you have")
— kill-and-redispatch only after a resume fails, because a resume
re-enters the agent's accumulated context while a fresh dispatch
re-pays it (observed: a single dispatch survived an API cut and then
a watchdog stall on staged resumes, its accumulated context intact,
and delivered complete). The report-written-but-never-
SENT class presents as the same silence; the same demand cures it.
**Channel rule (background/
teammate dispatches):** the closing report reaches the dispatcher ONLY
via SendMessage — a final text answer reaches no one; the brief names
this channel explicitly, and going idle without having SENT the report
counts as no report. **Payload vs. pointer:** the channel carries the
short signal; anything beyond the report form's slots — roughly more
than a screen — goes in a FILE, and the message points to it. Basis,
context economy: an injected payload occupies the dispatcher's
context for the rest of its session, re-carried on every later turn.
A suspected prompt-cache-rewrite correlation stands recorded but
unproven — `dev-notes/payload-cache-correlation.md` in the source
repo; the gate rests on context economy alone. The
`message-payload-gate` guard enforces the rule mechanically for the
expensive direction (subagent → dispatcher).

**Brief-tail boilerplate.** The brief's dispatch-invariant tail is
PASTED, not recalled — free-composed briefs drop invariant clauses
(the channel and payload rules have reached executing agents only as
gate denials, at doubled composition cost); a pasted tail skips the
bounce and the report re-demand loop entirely. The tail reaches the
executing agent pasted in the DISPATCH PROMPT or inside a brief FILE
the prompt names — inline required only when no file brief exists;
duplicating the tail into both is a second copy that drifts. The
CHANNEL LINE alone is always prompt-side: it binds to the
background-vs-sync call, made at dispatch time, which a static file
cannot know. Two blocks; pick by
dispatch kind, fill `<model>` AND the channel line — the
background-vs-sync call is the dispatcher's, made at paste time,
never left to the agent (it has been misjudged agent-side; the
report-enforcer hook's docstring, soft-spot note).

Channel line (both tails; paste exactly one):
- background/teammate agent: `Report channel: SendMessage to the
  dispatcher — your final text reaches no one.`
- synchronous agent: `Report channel: your final text IS the
  report.`

Binding (as of 2026-07-30): setting `name` on a dispatch forces
background mode — `run_in_background: false` is silently overridden
(probe-confirmed, same-model controlled pair). A sync dispatch sets
no `name`; model visibility rides the title prefix, and the
agent-model-gate's name lane applies only where a name exists.

The call's criteria: background suits work the session talks
across — long builds, parallel fan-outs, teammates. A short
dispatch whose result the current turn depends on (probe, verifier,
single pipeline stage) runs sync — the inline return carries the
report and the usage metadata, and skips the mailbox plumbing
(measured 2026-07-30, dedup-corrected same day: ~1.3×
cost-weighted, ~2.2× raw on a trivial task; roughly fixed per
dispatch, so it shrinks on large ones. Transcript usage entries are
per-stream snapshots — dedupe by API-call id before summing, and the
harness's subagent_tokens figure measures context, not spend).

Binding (as of 2026-08-01): the
harness HARD-BLOCKS a subagent writing report-shaped files
(REPORT.md and kin bounce with "return findings as text");
supporting DATA/evidence files still write fine. The report
therefore travels in the SendMessage itself — split into labeled
parts (1/N) when it exceeds one message — and briefs stop
assigning report file paths; data-file assignments are unaffected.

EXECUTION tail (any dispatch that writes):

    Closing report (mandatory; the project's own report form if it
    defines one, else the §2 form here — never both; "none" is a
    valid slot answer, silence is not): (a) items completed w/
    evidence, (b) checks RUN w/ real output, (c) gaps surfaced —
    incl. anything needing a tier above yours, returned as a question
    with its evidence, never settled at your tier,
    (d) deviations w/ reason, (e) candidate lessons, (f) files
    touched + commit hashes (unpushed), (g) what was NOT verified,
    (h) sources actually read, of those the brief named.
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
    Commits unpushed, targeted `git add <paths>` never `-A`, trailer:
    `Co-Authored-By: Claude <model> <noreply@anthropic.com>`.
    Never amend — always a new commit: the amend-gate denies
    subagent amends regardless of ownership.
    After sending the report your write grant is over: a defect you
    find later is REPORTED, never edited or amended (source: §4
    ownership rule).

READ-ONLY tail (verifier and discovery dispatches — no writes, no
commits, no report files; enumeration dispatches substitute the
data-file provision, §3b):

    <channel line>
    Return your findings in ONE message where they fit (verifier:
    verdict + basis; discovery: the N named facts, sources actually
    read); past the message-size gate, labeled parts (1/N) — never
    a report file. A missing decision, file, or value is surfaced
    as a gap, never bridged with a guess. No repo writes, no report
    files, no interim messages; transient probe scratch in your OWN
    scratchpad is permitted and is not a report file.

Verifier dispatches stay exempt from the rich §1 brief form but NOT
from the read-only tail — artifact + question + that block (the
CLAUDE.md fresh-context rule's "nothing else" excludes dispatcher
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
