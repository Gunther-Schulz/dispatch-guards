# Dispatch observations — gaps noticed in use

Per the dispatch skill's "Evolution and maintenance": a dispatch failure the
discipline should have prevented, or a rule it states wrongly, gets written here
with its evidence, and the rule change proposed. Not a changelog — each entry is
a measured incident.

## Abgeflossen

Angewandte oder verworfene Einträge, mit Beleg — ein Fakt,
eine Heimat. Der Eintrag WANDERT hierher, er bleibt nicht
durchgestrichen oben stehen.

Struktur-Nachtrag 2026-08-17, am selben Tag zweimal korrigiert:
Dieser Abschnitt stand zunächst in der MITTE der Datei, während neue
Einträge hinten anwuchsen — fünf lebende Einträge lasen sich über ihre
Position als abgeflossen. Der erste Fix schob ihn ans Datei-ENDE und
kehrte den Fehler bloß um: eine fremde Session hängte binnen einer
Stunde am EOF an und landete IM abgeflossenen Abschnitt. Jetzt steht
Abgeflossenes OBEN und die lebende Liste am Datei-Ende, wo angehängt
wird; `check_observations_tail` (tools/check-doc-drift.py) hält die
Reihenfolge fest. Dieser Absatz selbst war einen Commit lang falsch —
er beschrieb den ersten Fix weiter, nachdem der zweite ihn umgedreht
hatte: ein Etikett, das seinen eigenen Körper überlebt, in der Datei,
deren Pass genau davon handelt. Gefunden von der Frisch-Kontext-Runde,
von keinem Check.


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

### ANGEWANDT 2026-08-23 (Lane `opus-report-provenance`) — die
### Regel erreichte den Dispatcher, nicht den ausfuehrenden Agenten

Gebucht in `dbdd81a`, angewandt im selben Lauf: der vorformulierte
Klausel-Text steht jetzt am KOPF beider Tails in forms.md §2, und die
Fixture `EXECUTION_TAIL_BG` (brief-reminder.py) ist mitgewandert —
rot-bewiesen: Basis gruen, Mutant (Klausel nur aus der Fixture
entfernt) `[DRIFT] EXECUTION tail fixture` bei normalisiertem Zeichen
929, restauriert wieder gruen. Der Dispatcher hat die urspruengliche
Scope-Entscheidung (Tails ausgeschlossen) ausdruecklich revidiert.
Der Eintragskoerper steht in `dbdd81a`; hier bleibt nur der Beleg.
Die KLASSE lebt weiter unten als eigener Eintrag — sie ist nicht mit
dieser Instanz abgeflossen.

### ANGEWANDT 2026-08-18 (Peer-Auftrag pbs-office-Desk) — vier
### Heimaten, eine davon in anderer Form als der Eintrag vorsah

Die Regel ist als POSITIVE PFLICHT gemintet, nicht als Aufmerksamkeits-
Aufforderung — genau die Warnung, die der Eintrag selbst mitgibt (der
Skip fiel nur auf, weil zufällig rote Nachbarn danebenstanden):
`forms.md:18` Slot (b) verlangt die volle Zählung und je Skip eine
Disposition, mit dem Satz, der die Nicht-Ereignis-Klasse benennt (ein
übersprungener Check unterscheidet sich von einem nicht existierenden
nur durch seine Zeile im Report); `forms.md:225` trägt dieselbe
Pflicht wörtlich im EXECUTION-Tail; `dispatch/SKILL.md:708` die
Dispatcher-Hälfte (Integrationslauf vergleicht die SKIP-Zahl gegen die
Baseline); `executor/SKILL.md:60` die Konduktions-Hälfte, in Regel 4
GEWEITET statt als neue Regel danebengestellt — mit Quellen-Label auf
Slot (b), wie die skill→skill-Audit-Regel es verlangt.

ABWEICHUNG vom vorformulierten Text, bewusst: der Eintrag sagt
„wörtlich in beide Tail-Blöcke". Der READ-ONLY-Tail führt gar keine
Slot-Liste — dort wäre Slot (b) sinnlos. Die Regel steht deshalb in
`forms.md:282` als Klausel über die BASIS des Verdikts: ein
übersprungener Check ist nicht gelaufen, ein darauf ruhendes Verdikt
ist could-not-verify, nicht clean. Verifier-Lanes sind genau die, die
Checks laufen lassen — die Lücke wäre sonst offen geblieben.

MECHANISMUS-KOPPLUNG, vom doc-drift-Check erzwungen, nicht von Hand
gefunden: `brief-reminder.py:662` hält eine wörtliche Fixture des
EXECUTION-Tails; die Slot-(b)-Änderung riss sie, der Check ging rot,
Fixture nachgezogen. Danach `check-doc-drift.py` sauber.

MECHANISIERUNG — ENTSCHIEDEN, NICHT GEBAUT: als PARKED gebucht
(BACKLOG, genannte fehlende Evidenz). Begründung am Prädikat: die
Skip-ZAHL ist computierbar, die Anwesenheit einer Disposition nicht
ohne Fehlfeuer — ein Report, der „4 skipped (unrelated, pre-existing)"
schreibt, DISPONIERT im selben Satz und würde von jedem
Zweit-Erwähnungs-Zähler angefeuert. Ein Wächter, der auf legitime
Arbeit feuert, trainiert den Override-Reflex (Repo-Regel: neue Lane
default-warn, deny per Feuerrate). Der Bericht trägt die Disposition,
ein Lint höchstens ihre Anwesenheit — die Meinung des Eintrags, hier
als Entscheidung übernommen.

### Ein ÜBERSPRUNGENER Test ist ein nicht gelaufener Test, und die Berichtsform fragt ihn nicht ab

**1. Vorfall + Basis.** 2026-08-18, pbs-office-Backlog-Welle
(Journal `01NhRWdw-backlog-desk-1808`; Bau pbs-office `892ed44`,
Nachreview-Nachzug `10fb16c`). Eine Lane baute vier Tests, die den
tragenden Zweig ihres Postens belegen sollten — den strengen
Schema-Pfad. Im Haupt-Checkout skippten **alle vier**, weil eine
Pfad-Auflösung still danebenging (`git rev-parse --git-common-dir`
antwortet relativ zu SEINEM cwd, `Path.resolve()` löst gegen den cwd
des Python-Prozesses auf). Der Lauf meldete „66 passed, 4 skipped" —
also GRÜN. Der Posten war damit formal gebaut, verifiziert und
berichtet, während sein Kern-Zweig nie ausgeführt worden war.
Gefunden hat es nicht die Berichtsform, sondern ein Suite-Lauf des
Dispatchers im Haupt-Checkout, und auch der erst, weil danach ANDERE
Tests rot gingen. Ohne die roten Nachbarn wäre der Skip nie
aufgefallen.

**2. Klasse.** Nicht die Worktree-Umgebung (die ist der Anlass und
liegt in `worktree-OBSERVATIONS.md`), sondern die BERICHTSFORM: Slot
(b) verlangt „checks/tests actually RUN, with their real output".
Ein Skip erfüllt das wörtlich — er STEHT in der echten Ausgabe — und
ist trotzdem das Gegenteil dessen, was der Slot belegen soll. Ein
übersprungener Test unterscheidet sich von einem nicht existierenden
Test in nichts außer der Zeile im Report. Das ist die
Nicht-Ereignis-Klasse des Operator-Korpus (ein toter Mechanismus
liefert dasselbe Bild wie ein bestandener), hier in der Kleidung
einer Zahl, die niemand liest, weil daneben „passed" steht.

**3. Vorformulierter Regel-/Fix-Text** (Ergänzung in
`references/forms.md`, Slot (b) der §2-Form, und wörtlich in beide
Tail-Blöcke):

> (b) checks/tests actually RUN, with their real output — including
> the **full counts, skips named**: `N passed, M failed, K skipped`.
> Jeder Skip wird DISPOSITIONIERT: welcher Test, aus welchem Grund
> übersprungen, und ob dieser Grund den Posten berührt. Ein Skip in
> einem Test, den DIESE Lane gebaut hat, ist per Konstruktion ein
> Befund — er belegt, dass der gebaute Zweig nicht ausgeführt wurde,
> und ein Bau, dessen Verifizierer nicht lief, ist unverifiziert,
> nicht grün. `K > 0` ohne Dispositions-Satz ist ein unvollständiger
> Bericht und wird nachgefordert wie ein fehlender Slot.

Dispatcher-Hälfte, in §4 (Integration): der eigene Verifikationslauf
vergleicht nicht nur passed/failed gegen die Baseline, sondern auch
die SKIP-Zahl. Eine gegenüber der Baseline gestiegene Skip-Zahl ist
ein Befund, kein Rauschen — sie ist die leise Richtung derselben
Frage, die eine gestiegene Fail-Zahl laut stellt.

**4. Konsument + Abfluss-Naht.** Nächste
dispatch-guards-Maintenance-Runde (`references/forms.md` §2 + beide
Tails, `SKILL.md` §4). Sofort-Konsument: jede Session, die heute
einen Lane-Bericht bucht — die Skip-Zahl per Hand nachfragen, bis
der Mint steht. Mechanisierungs-Kandidat, aber kein sicherer: die
Zahl ist computierbar, die Frage „berührt dieser Grund den Posten"
ist es nicht, also trägt der Bericht die Disposition und ein Lint
höchstens ihre ANWESENHEIT.

## 2026-08-06 — three from one fan-out (3 × opus, two fork worktrees + one shared repo)

**ANGEWANDT 2026-08-17 (Wartungs-Pass)** — alle drei Hälften.
#1 → §1 „Commit unpushed": eine Arbeitskopie mit einem Schreiber
AUSSERHALB des Dispatches trägt kein Unpushed. #2 → neuer
§1-Unterpunkt „Deployment-coupled ist eine andere Frage als LIVE ON
WRITE" plus Skeleton-Slot. #3 → Leiter-Sprosse 2: das worktree-Skill
wird GELADEN, nie bloß zitiert. Beleg: dieser Commit.

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

**ANGEWANDT (vor diesem Pass)** — der Eintrag IST das
Mint-Protokoll; die geweitete Race-Klausel steht in forms.md §2
(„The race's mirror sits at the lane's END"). Kein Text offen.

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

**ANGEWANDT (vor diesem Pass, 2026-08-10)** — die Lane
keyed auf die VERB-Position; der Docstring nennt den gemessenen
Fehlfeuer-Fall, zwei Biss-Tests pinnen ihn. Beleg:
push-claim-reminder.py (Docstring + --test).

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

**ANGEWANDT 2026-08-17, GEMERGT mit dem
2026-08-14-Eintrag „Re-Lese-Einheit"** — gleiche Klasse: die
Um-Bewertung liegt außerhalb des Lesefensters. Landet im
§1-Provenance-Bullet („Opening a stored ENTRY means the entry PLUS
its neighbours"), zusammen mit dem Extraktor als Instrument. Beleg:
dieser Commit.

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

**ANGEWANDT 2026-08-17** — die Write-Set-Overlap-Hälfte
trug §1 schon (Fast-Path `git diff --quiet <base> HEAD -- <paths>`);
neu ist der Compose-Zeit-CENSUS (`git worktree list` neben `git
status` und `git log -1 --format=%cr`), der zugleich die
Integrations-Naht bedient — §4 verweist darauf, eine Heimat. Beleg:
dieser Commit.

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

**ANGEWANDT 2026-08-17** — Kandidat 1 stand bereits im
worktree-Skill (`extensions.worktreeConfig`, `config --worktree`);
Kandidat 2 landet zweigeteilt: der Census in §1 (von §4 zitiert) und
„Config-Writes sind Repo-Writes" im §2-Slot (f) samt Tail. Beleg:
dieser Commit.

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

**MERGE 2026-08-19, n=2 für diese Klasse — dieselbe Lücke eine Achse
weiter: der Census ist ein ZEITPUNKT, der Mitschreiber ein VERLAUF.**
Vorfall (cache-fix-Desk, zwei parallele Lanes, dotfiles-Kopie): der
Compose-Zeit-Census lief wie vorgeschrieben — `git status --porcelain`
(2 Dateien), `git worktree list` (1), `git log -1 --format=%cr`
("11 hours ago") — und meldete eine ruhige Kopie. Zwanzig Minuten
später committete der OPERATOR direkt in dieselbe Kopie (`8999f45`,
12:15:25) und pushte. Der Census war zum Zeitpunkt seiner Ausführung
KORREKT und danach still falsch; nichts weckte den Dispatcher.
Was den Fehler dann festhielt statt aufzudecken, sind zwei Lesungen,
die beide grün waren: (1) `git diff HEAD -- <datei>` war LEER, gelesen
als "unverändert" — wahr über einen HEAD, der die Änderung inzwischen
ENTHIELT; "identisch mit HEAD" ist keine Aussage über Veränderung,
sobald HEAD sich bewegt, und ist damit ein Kriterium, das auf lebenden
Zustand ankert. (2) `git log origin/main..HEAD` zeigte NUR die
Lane-Commits — weil der Fremd-Commit bereits GEPUSHT war und origin
mitgewandert ist. Beide Kommandos stehen in der Disziplin; keines
sieht diesen Fall. Aufgedeckt hat es die LANE, nicht der Dispatcher,
und zwar über den Inhalt (`git diff <fremd> <eigen> -- <datei>` leer)
statt über Zeitstempel.
Dritter Beleg derselben Wurzel in derselben Stunde, ohne git: eine
bewegte mtime als Grenzverletzung gelesen, dann zwei RUHENDE mtimes
als Lane-Stillstand gelesen (die Lane arbeitete durch). Ein
Zustandsabruf beantwortet nie, ob ein EREIGNIS stattfand, und mtime
beobachtet einen Schreibvorgang, nie eine Änderung und nie einen
Schreiber.
Vorformulierter Regel-Text, §1 Base-Commit-Klausel und §4
Dispatcher-Pflichten, in dessen Register: **Der Census ist am
Integrations-Seam ZU WIEDERHOLEN und liest den VERLAUF, nicht den
Zustand: `git log <base>..HEAD` (nicht `origin/main..HEAD` — origin
wandert mit einem pushenden Mitschreiber) plus `git log -1
--format=%cr`. Jeder Commit darin wird EINZELN beansprucht; ein
unbeanspruchter hält die Integration an. Und: die Abwesenheit einer
Änderung wird nie gegen HEAD festgestellt, sondern gegen den im Brief
GENANNTEN Basis-Commit — ein unveränderlicher Anker, während HEAD
einer ist, den der Mitschreiber bewegt.** Die vorhandene Census-Regel
bleibt wie sie ist; sie deckt den Zeitpunkt, dieser Zusatz die
Strecke.
Konsument + Abfluss-Seam: der Wartungs-Pass unter der
OBSERVATIONS-Quote; Zielstellen §1 (Base-Commit-Klausel) und §4
(Verify-in-the-artifact-Pflicht). Nichts ging verloren — die
Pathspec-Form hielt, der Fremd-Commit reiste nicht unter der Nachricht
der Lane mit; die Klasse kostete Diagnose-Zeit und eine an den
Operator ausgelieferte Entwarnung, die falsch war.

## 2026-08-07 — dispositions-as-brief graduated; two §1 note candidates

**ANGEWANDT (vor diesem Pass)** — Kandidat 2 ist nach §1
graduiert („Criteria state OUTCOMES first, sites second", beide
Feuerrichtungen); Kandidat 1 (je Disposition die Rot-zuerst-Anordnung
als erster Akt) steht im Operator-Korpus, brief-family-Bullet.
**Basis-Vorbehalt (Enumerations-Lane 2026-08-17):** Kandidat 1s
Zielstelle liegt im GLOBALEN Operator-Korpus, also außerhalb dieser
Arbeitskopie — von hier aus nicht prüfbar. Der Eintrag ist gegen eine
Fundstelle zurückgezogen, die diese Session nicht öffnen kann; die
Hälfte gilt als unverified, bis eine Session mit dotfiles-Zugriff sie
liest.

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

**ANGEWANDT 2026-08-17** — Kandidat 1 und 2 → §1
Base-Klausel: „Stated means READ at compose time", Ausgabe gepastet,
plus der Co-Writer-Census. Kandidat 3 verlangte keine Änderung (der
Executor-Halt bleibt, wie der Eintrag begründet). Beleg: dieser
Commit.

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

**ANGEWANDT 2026-08-17** — die drei Sizing-Terme plus die
Crossover-Faustgröße (~30 Tool-Calls je Lane, Formel statt Konstante,
gemessen von `tools/lane-cost.py`) → §1 „What rides ONE lane". Beleg:
dieser Commit.

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

**ANGEWANDT (vor diesem Pass)** — Mechanismus im selben
Batch geschifft (forms.md §2 Zwei-Lanes-Binding, `mailbox_lane()`,
sechs Korpus-Fälle). Der Binding-Absatz ist im heutigen Pass auf die
PRO-SESSION-Probe umgestellt (Eintrag 2026-08-16) und trägt den
Stempel „as of 2026-08-17".

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

**ANGEWANDT (vor diesem Pass)** — §1 trägt die Klausel mit
beiden Feuerrichtungen („Criteria state OUTCOMES first, sites
second").

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

**ANGEWANDT (vor diesem Pass)** — §1-Provenance-Bullet:
Pro-Zeilen-Grade, die FORM-Hälfte, und der Übergang von
Discovery-Testimony zur Anweisung.

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

**TEILS ANGEWANDT (vor diesem Pass), REST VERWORFEN** — die
billigere Variante ist gebaut: beide PreToolUse-Lanes entlasten einen
Claim, dessen Datei keine uncommittete Arbeit mehr trägt
(`no_uncommitted_work`), gemessen gegen drei Fehlfeuer. Die
HEAD-Erreichbarkeits-Variante wird VERWORFEN — sie fängt dieselbe
Klasse teurer und braucht Commit-Attribution, die die Entlastung nicht
braucht. Das angehängte 0.7.1-Bullet (geteiltes Version-Gate,
Bump-first) ist im Commit-Plan-Absatz angewandt. Beleg:
writer-claims-gate.py Docstring; SKILL.md §1 Commit-Plan.

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

**VERWORFEN 2026-08-17** — die Hypothese ist am Quelltext
widerlegt: `_dispatch_common.fire_log_path()` liest
CLAUDE_DISPATCH_GUARDS_FIRELOG, sonst XDG_DATA_HOME, und README nennt
genau diesen Default. Die Stille im Doctor-Lauf hat ihre Ursache
außerhalb dieses Repos (Kind-Env des Doctors), nicht in einem
veralteten README — kein Text zu ändern.

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

**ANGEWANDT 2026-08-17** — die pfad-skopierte Toleranz stand
als Fast-Path schon in §1; neu ist die Absender-Hälfte: wo die
Brief-DATEI in die Kopie des Executors committet wird, ist der
Brief-Commit selbst die Basis. Beleg: dieser Commit.

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

**ANGEWANDT 2026-08-17** — (a) ADD-ONLY ist keine
Disjunktheits-Ausnahme, (b) für eine GETEILTE Datei existiert keine
sichere Form, weshalb Serialisierung das Mittel ist und nicht die
Präferenz, (c) Container/Dienst/Privileg als Umgebungs-Vorbedingung —
am REPOINT-Bullet, dort nach oben verallgemeinert („confirms what it
assumes exists — the knob AND the environment"). Die
Enforcement-Beobachtung (writer-reservation im Warn-Modus hätte
gefangen) bleibt Feuerraten-Material, kein Regeltext. Beleg: dieser
Commit.

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

**ANGEWANDT 2026-08-17** — alle vier: (1) Inbox-Drain vor
dem Senden UND zwischen Report-Teilen (§2 plus EXECUTION-Tail),
(2) Inhalts-Anker neben positions-/generat-abhängigen IDs (§1 „Files
to read"), (3) Flags VOR dem `--` (Tail und executor-Regel 6; hier
ausgeführt geprüft: `git commit -- f.txt -m "…"` → „pathspec '-m' did
not match any file(s)", die Form mit Flag davor committet sauber),
(4) Seitenbild-Sichtung bei sichtbarem Render-Chrome (Verifier-Slot).
Beleg: dieser Commit.

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

## 2026-08-12 — writer-claims: Claims einer GESCHLOSSENEN Lane feuern gegen die Nachfolge-Lane

**ANGEWANDT 2026-08-17 (Prosa-Hälfte), MECHANISMUS
VERWORFEN** — beide Richtungen des Paares landen in §4 „Additions
extend ownership": ein kreuzender Report schließt die Lane nicht, und
weder grep noch `git status` beobachtet einen SCHREIBER; bei Zweifel
den Halter fragen und die Antwort abwarten. Das Lane-STATE-Register
(Release-/Re-Arm-Verb am Claim-Register) wird VERWORFEN: „Lane
geschlossen" ist zur Hook-Zeit nicht komputierbar, und die
Fehlfeuer-Richtung deckt die bestehende `no_uncommitted_work`-
Entlastung. Beleg: dieser Commit.

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

**ANGEWANDT 2026-08-17** — Slot (f) wird aus dem RECORD
etabliert (Trailer-Filter; „present in the tree, not mine") in
§2-Slotliste und EXECUTION-Tail; §4 gradet Slot (f) vor der Buchung
gegen den Trailer, und die Close-Nachricht trägt ihre eigene Grenze
(„do not edit; a defect found later is REPORTED"), weil sie den
Agenten resumiert. Beleg: dieser Commit.

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

## 2026-08-14 — Ein gebrieftes Randbeispiel als Pflicht-Assertion pinnt die Spec, nicht den Defekt

**ANGEWANDT 2026-08-17** — Heimat §1 gewählt (Bullet zur
Instrument-Semantik), Kante im pbs-office-Devbook nicht nötig: eine
vorgegebene Pflicht-Assertion nennt dazu einen Fall, der die
vorgeschriebene von der NAIVEN Implementierung trennt. Beleg: dieser
Commit.

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

**ANGEWANDT 2026-08-17** — executor-Skill Regel 4: eine
Struktur-Suche über ein Binärformat zählt nur mit Positiv-Kontrolle im
SELBEN Aufruf-Modus; die zwei gestapelten Instrument-Killer des PDF
(Binär-Einstufung, Objektströme) sind benannt. Beleg: dieser Commit.

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

**ANGEWANDT 2026-08-17** — §4 Horizont-Absatz: ein
eingehender Report wird erst gebucht, wenn sein ABSENDER gegen die
eigene Dispatch-Liste auflöst; ein unaufgelöster Absender ist ein
Befund (Cross-Talk), schließt keinen Horizont. Beleg: dieser Commit.

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

### MERGE 2026-08-18 — 2. Vorfall, diesmal die ERZEUGENDE Seite: die Kanal-Zeile ist RELATIV formuliert und wird von Forks wörtlich geerbt

1. **Vorfall + Basis:** Opus-Desk 75 (pbs-office `2afbcba`,
   Journal-Zeile `sonnet-zusicherung-3145`) dispatchte EINE
   Lese-Durchsicht über fünf Repos (FB 3.145). Der Executor startete
   dafür fünf Forks. Beim Desk gingen daraufhin SECHS Nachrichten zu
   diesem einen Posten ein, alle unter dem Absendernamen `fork`, die
   einander widersprachen: verschiedene Fund-Zahlen für dieselben
   Repos (pbs-doc mal A=3/B=0, mal A=2/B=0, mal A=1/B=1) und je eine
   ANDERE Angabe, welches Repo noch ausstehe (einmal pbs-abwaegung,
   einmal pbs-wissen, einmal pbs-office). Der Executor benannte die
   Ursache selbst: die Forks erben seinen vollen Kontext samt der
   Zeile „Report channel: SendMessage to the dispatcher" aus dem
   Original-Brief und lösten „the dispatcher" auf den GROSSVATER
   (das Desk) statt auf ihren Erzeuger auf. Zweiter, unabhängiger
   Schaden derselben Wurzel: drei Forks schrieben fast gleichnamige
   Ergebnis-Dateien in denselben Session-Scratchpad
   (`fb3145-zusicherung-durchsicht.md`,
   `fb-3145-zusicherung-durchsicht.md`,
   `fb-3145-zusicherung-liste.md` — alle innerhalb zweier Minuten,
   vom Desk auf Platte nachgezählt); der writer-claims-Gate warnte
   über einen Write innerhalb der Claim-TTL, und die Funde
   mindestens eines Forks wurden überschrieben.
2. **Klasse:** dieselbe (Report-Attribution/Cross-Talk), hier aber
   die ERZEUGENDE Seite statt der buchenden. Die 2026-08-17
   angewandte §4-Regel HAT auf der Empfangsseite gehalten: das Desk
   löste die Absender gegen seine Dispatch-Liste auf, verwarf alle
   sechs als Cross-Talk, buchte keine und ließ den Horizont offen —
   der stärkste Fund wurde stattdessen vom Desk selbst am Quelltext
   bestätigt (pbs-office FB 152). Offen ist die Seite davor: eine
   Kanal-Zeile, die ihren Empfänger RELATIV benennt, ist unter
   Vererbung nicht eindeutig, und Vererbung ist beim Fork der
   Normalfall, nicht die Ausnahme.
3. **Vorformulierter Regel-Text** (forms.md, Kanal-Zeilen-Block, die
   benannte Variante): „Die Kanal-Zeile benennt ihren Empfänger
   ABSOLUT, mit dem Agent-Namen, nie relativ: `Report channel:
   SendMessage to <dispatcher-name> — your final text reaches no
   one.` Ein relativer Bezug („the dispatcher") wird von einem Fork
   wörtlich geerbt und dort auf DESSEN Erzeuger — den Großvater —
   aufgelöst; gemessen 2026-08-18 als sechs widersprüchliche Reports
   an einen Dispatcher, der nur einen Agenten gestartet hatte."
   Zusatz (§1, Schreib-Grenzen): „Ein Brief, der Fan-out nicht
   ausdrücklich beauftragt, verbietet Sub-Forks — der Executor gibt
   die Arbeit zurück statt sie zu verteilen. Die Begründung gehört in
   den Brief, damit sie mitgetragen statt nur befolgt wird:
   Kanal-Zeile UND Scratch-Dateinamen des Elternteils werden geerbt,
   Sub-Forks kollidieren also per Konstruktion in beidem."
4. **Konsument + Abfluss-Naht:** nächste dispatch-guards-
   Maintenance-Runde (forms.md Kanal-Zeilen-Block + §1
   Schreib-Grenzen); Quota-Drain nach OBSERVATIONS-Regel.

## 2026-08-14 — Fork-Skills sind der Rest-Spawn-Kanal unter dem Cap, und ein Fork ist per Konstruktion Selbst-Review

**ANGEWANDT 2026-08-17** — §4 Verdict-Routing: ein
`context: fork` erbt den vollen Kontext des Aufrufers, ist damit
Selbst-Review und wird so gegradet; der Subagent-Spawn-Cap schließt
diesen Kanal nicht. Beleg: dieser Commit.

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

**ANGEWANDT 2026-08-17, gemergt mit dem
2026-08-07-Eintrag „ranked-list head"** — §1-Provenance-Bullet: die
Re-Lese-Einheit ist der Eintrag PLUS seine Nachbarn, die Grenzwahl des
selbstgebauten Extraktors ist die Basis, und eine repo-eigene
Closure-Prüfung läuft vor dem Versand. Beleg: dieser Commit.

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

**ANGEWANDT 2026-08-17** — forms.md §2,
Harness-Binding-Absatz: die Sperre ist an EINEM Namensraum gemessen und
für eine andere Arbeitssprache kein Rückfall; dort nennt der Brief die
zugewiesene Datendatei als einzigen erlaubten Schreib-Pfad und jede
weitere Datei ausdrücklich als Abweichung. Beleg: dieser Commit.

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

## 2026-08-16 — `git add -N` mit Verzeichnis-Argument registriert fremde untracked Dateien unsichtbar

**ANGEWANDT 2026-08-17** — Wortlaut in §1
Write-Boundaries (add-N-Klausel), de-partikularisiert: das Datum ist
raus (Korpus-Provenance-Regel — in-file nur Staleness-Stempel), der
Mechanismus steht. Beleg: dieser Commit.

1. **Vorfall + Basis:** statiker-Meta-Session (Session-Record
   2026-08-16, statiker-Repo dev-notes/OBSERVATIONS, Round-3-
   Dispositions-Eintrag): ein Compound-Command trug `git add -N
   docs 2>/dev/null` — Absicht war EINE neue Brief-Datei; das
   Verzeichnis-Argument intent-to-addete zusätzlich VIER fremde
   untracked Lane-Briefs eines anderen Workstreams. Aufgefallen
   erst als lauter Stash-Fehler ("Entry … not uptodate. Cannot
   merge") viele Kommandos später; rückgängig per pfadgenauem
   `git reset --`. n=1.
2. **Klasse:** Verzeichnis-Pfadspec-Klasse (§1 kennt sie für
   Lock-/Write-Set-Pfade: "names a FILE, never a directory");
   `add -N` ist ihr ungenanntes Gesicht — der Schaden ist nicht
   ein Mit-COMMIT (Pathspec-Commit blieb sauber), sondern
   stiller Index-Zustand über fremden Dateien, der spätere
   Operationen (stash, checkout) bricht oder — schlimmer — sie
   in ein späteres breites Staging zieht.
3. **Vorformulierter Fix-Text** (SKILL.md §1, Widening der
   bestehenden add-N-Klausel im Write-Boundaries-Teil): nach
   "`git add -N <path>` first — intent-to-add registers the path
   against the empty blob …" ergänzen: "— and `<path>` names a
   FILE, never a directory: a directory argument intent-to-adds
   every unowned untracked file under it, invisibly (foreign
   briefs included; measured 2026-08-16 as a stash broken many
   commands later), the write-boundary directory rule's add-N
   face."
4. **Konsument + Abfluss-Naht:** nächste dispatch-guards-
   Maintenance-Runde (SKILL.md §1, Write-Boundaries-Absatz);
   Quota-Drain nach OBSERVATIONS-Regel.

## 2026-08-16 — Das Report-File-Verbot am ENDE des READ-ONLY-Tails wird als Klempnerei gelesen, nicht als bindend (statiker beat-the-books, Session 11)

**ANGEWANDT 2026-08-17** — der READ-ONLY-Tail eröffnet mit
dem Verbot samt genannter Folge, die Scratch-Zuweisung steht daneben,
die zwei redundanten Verbots-Halbsätze sind entfernt; der Grund
(bindende Klausel gehört an den Blockanfang) steht als ein Satz im
Tail-Boilerplate-Absatz.
**Nachtrag, Fund DIESES Passes:** der brief-reminder-Hook keyed seine
READ-ONLY-Erkennung auf einen der entfernten Halbsätze („no repo
writes, no report files"), also riss die Umstellung einen Dependent.
Gefangen hat es der Korpus-Fall PREMISE PIN (erwartet `context`,
beobachtet `deny`) — er war damit der Rot-zuerst-Beweis der Reparatur,
und die Reparatur ist eine Marker-FAMILIE (alter plus neuer Anker),
damit Briefe im Flug nicht fehlfeuern. Zwei Regressions-Fälle mit dem
neuen Tail sind im Korpus, ausdrücklich als Regressions-Pins
etikettiert: gemessen unterscheiden sie die beiden Prädikate NICHT
(sie waren unter dem alten Anker ebenfalls grün), also tragen sie den
Beweis nicht. Beleg: dieser Commit.

1. **Vorfall + Basis:** Drei Discovery-Dispatches (sonnet) im selben
   Lauf, alle drei mit dem wörtlich gepasteten READ-ONLY-Tail aus
   `references/forms.md` §2. Die ersten ZWEI schrieben trotzdem eine
   Report-DATEI und meldeten per SendMessage nur einen Zeiger darauf —
   obwohl der Tail das Verbot zweimal trägt ("never a report file",
   "no report files"). Beide schrieben die Datei zudem in das
   Scratchpad des DISPATCHERS, nicht ihr eigenes, obwohl der Brief
   Scratch explizit zuwies. Inhaltlich waren beide Reports
   ausgezeichnet — genau deshalb fällt die Abweichung nicht auf.
   Beim DRITTEN Dispatch wurde das Verbot unverändert im Wortlaut,
   aber an den KOPF des Briefs gehoben, mit genannter Folge ("A file
   is not a report and will not be read as one") — dieser Agent hielt
   es ein. n=2 Verstoß / n=1 Bestätigung nach Umstellung, alle drei
   im selben Lauf, gleiche Brief-Form, gleiches Modell, gleiche
   Aufgabenklasse. Damit ist die Position die einzige veränderte
   Variable.
2. **Klasse:** Platzierungs-Klasse im Brief — ein Verbot, das im
   invarianten Block-Ende steht, wird als Transport-Klempnerei
   gelesen und nicht als Anweisung; dieselbe Klasse, die §1 für den
   Route-Line-Seam und der Operator-Korpus für "Text zwischen
   Tool-Calls wird nicht ausgeliefert" schon kennt. Der Tail wird als
   Formalie überflogen, weil er in jedem Brief identisch ist — genau
   die Eigenschaft, die ihn als Garantie tragen sollte, macht ihn
   unsichtbar. NICHT die Klasse "Executor ignoriert Anweisung": zwei
   unabhängige Agenten mit demselben Text und die Umkehr durch reine
   Umstellung zeigen auf den Brief, nicht auf die Ausführenden.
3. **Vorformulierter Fix-Text** (`references/forms.md` §2,
   READ-ONLY-Tail — die Verbots-Zeile an den ANFANG des Blocks
   ziehen und die Folge nennen, statt sie in Satz zwei und vier
   mitlaufen zu lassen): den Block eröffnen mit "NO REPORT FILE.
   Your findings go in your SendMessage reply — a file you write is
   not a report, is not read as one, and reaches no one. Split into
   labeled parts (1/N) past the size gate." Danach der bestehende
   Wortlaut ohne die beiden jetzt redundanten Verbots-Halbsätze.
   Gleiches gilt spiegelbildlich für die Scratch-Zuweisung: sie
   gehört neben das Verbot, nicht in den Kopfteil des Briefs, weil
   beide dieselbe Naht betreffen (wohin schreibt der Agent).
4. **Konsument + Abfluss-Naht:** nächste dispatch-guards-
   Maintenance-Runde, `references/forms.md` §2 (READ-ONLY-Tail);
   Quota-Drain nach OBSERVATIONS-Regel. Beobachtungs-Herkunft: der
   Dispatcher hat die Umstellung im Lauf selbst als Reparatur
   getestet, der Fix-Text ist also bereits einmal live bestätigt und
   nicht nur hergeleitet.

## 2026-08-16 — Harness entzieht der Mailbox-Lane mid-session die Grundlage: Agent-Tool verliert `name` + `run_in_background` (Begehung R3, statiker meta-session)

**ANGEWANDT 2026-08-17** — forms.md §2: welche Lanes
EXISTIEREN, entscheidet eine Probe am Agent-Schema PRO SESSION, kein
Datum; der synchrone Zweig ist als eigener Zweig beschrieben (kein
Channel-Line-Paste, Model-Gate liest `model`, Horizont entfällt), und
die Probe-Regel steht VOR den Channel-Zeilen, damit der Vorbehalt
nicht hinter dem Default landet. Mailbox-Zweig neu gestempelt „as of
2026-08-17" — in dieser Session geprobt: `name` im Schema vorhanden,
`run_in_background` abwesend. „Re-probe when the schema changes" ist
entfallen, die Probe-Regel ersetzt sie (ein Fakt, eine Heimat). Beleg:
dieser Commit.

1. **Vorfall + Basis:** In der laufenden statiker-Meta-Session
   aktualisierte der Harness die Agent-Tool-Beschreibung MID-SESSION:
   "`run_in_background` and `name` are unavailable here — only
   synchronous subagents" (beobachtet 2026-08-16, dieselbe Session
   hatte Stunden zuvor zwei NAMED-Dispatches erfolgreich gefahren:
   opus-review-078/-080, beide Mailbox-Lane). forms.md §2 trägt die
   Lane-Bindung datiert 2026-08-15 ("naming decides the lane",
   forms.md:94-97 gelesen) und der Model-Gate verlangt einen Namen
   auf jedem generischen Dispatch. Unter dem neuen Schema ist die
   benannte Lane NICHT AUSDRÜCKBAR: ein Desk, der nach §2
   komponiert, wird entweder vom eigenen Gate abgewiesen oder
   pastet eine Mailbox-Channel-Zeile, deren Lane nicht existiert.
   Der §2-Text selbst nennt die Re-Probe-Pflicht ("Re-probe when
   the Agent tool's schema changes") — dieser Eintrag IST diese
   Re-Probe, positiv gefeuert.
2. **Klasse:** Binding-Staleness (Bindings gelten, solange die
   Umgebung gilt — und der Harness ändert das Schema unangekündigt
   mid-session). Zweitklasse mitbeobachtet: die Konvention "das
   Modell reitet auf dem NAMEN" verliert ihren Träger, wenn `name`
   entfällt — das Modell reitet dann allein auf dem
   `model`-Parameter (in der beobachteten Session weiterhin
   vorhanden).
3. **Vorformulierter Fix-Text** (forms.md §2, Binding-Absatz +
   Channel-Zeilen-Block): die Lane-Entscheidung an eine
   PROBE koppeln statt an ein Datum — "Vor dem ersten Dispatch
   einer Session mit Lane-relevanter Form: prüfe, ob das
   Agent-Schema `name` akzeptiert. Akzeptiert es keins, existiert
   nur die synchrone Lane: kein Channel-Zeilen-Paste (der finale
   Text IST der Report, kehrt als Tool-Result zurück), Model-Gate
   liest den `model`-Parameter, Horizon-Regel entfällt (ein
   Sync-Dispatch kann den Turn nicht überleben)." Beide
   datierten Binding-Absätze auf diese Probe umstellen; die
   Mailbox-Beschreibung bleibt als der andere Probe-Zweig.
4. **Konsument + Abfluss-Naht:** nächste dispatch-guards-
   Maintenance-Runde (forms.md §2 + model-gate-Hook-Text);
   Quota-Drain nach OBSERVATIONS-Regel. Sofort-Konsument: jede
   Session, die heute nach §2 dispatcht — bis zum Fix gilt die
   Probe per Hand (Schema ansehen, dann komponieren).
   **Nachtrag, gleiche Runde (Gegen-Probe der Desk-Session):** Die
   Divergenz ist PRO SESSION, nicht maschinenweit — die
   beat-the-books-cd-Session las ihr Live-Schema auf Anfrage:
   `name` VORHANDEN, Mailbox-Lane lebendig (A3-Spawn "via mailbox"
   im selben Fenster), Model-Gate feuert normal; die Meta-Session
   daneben hat beides verloren. Konsequenz für den Fix-Text: die
   Probe gilt PRO SESSION ("prüfe DEIN Schema"), und eine Session
   darf die Lane einer anderen nie aus der eigenen ableiten — auch
   nicht andersherum: ein Brief mit Mailbox-Channel-Zeile, von der
   synchron-gewordenen Session komponiert, strandet den Report.

## 2026-08-17 — Ein Identitäts-Check, gekeyed auf ein Feld, das nicht IDENTIFIZIERT (§4-Slot-(f)-Regel, eine Stunde nach ihrem eigenen Versand widerlegt)

**ANGEWANDT 2026-08-17 (im selben Pass geschrieben und angewandt)** —
§4 Slot-(f)-Grading und §2 Slot (f); der Eintrag hält die KLASSE fest,
nicht eine Schuld. Positions-Korrektur derselben Runde: er stand
zuerst unter `## Offen`, obwohl seine Slots 3 und 4 ihn als
abgeflossen auswiesen — das Spiegelbild des Fehlers, den dieser Pass
behob, gemintet vom selben Commit und gefunden von der
Frisch-Kontext-Runde. Beleg: 5bd8e03.
1. **Vorfall + Basis:** Die in diesem Pass geschriebene §4-Regel nennt
   den Commit-Trailer die „billige widerlegende Probe" für Slot (f).
   Ihr eigener Autor wandte sie eine Stunde später auf einen
   unerwarteten Commit in der eigenen Arbeitskopie an — und bekam eine
   FALSCHE Zuordnung: beide Kandidaten waren fable-Sessions, der
   `Co-Authored-By`-Trailer trug bei beiden identisch „Claude Fable 5".
   Korrigiert von einem Peer, danach an der Quelle geprüft
   (`git log -1 --format='%(trailers:key=Co-Authored-By,valueonly)
   %(trailers:key=Claude-Session,valueonly)'` über dbbcb76 / 84d0e30 /
   b115a2d): Autoren-Trailer gleich, Session-Trailer verschieden. Eine
   Zählung über 60 Commits zeigt zudem, dass der Session-Trailer NICHT
   universell ist (4 von 60 ohne).
2. **Klasse:** Diskriminierungs-Frage an ein Attributions-Instrument —
   das Feld beantwortet eine ANDERE Frage (welches Modell) als die
   gestellte (welcher Schreiber), und es liefert bei geteiltem Modell
   eine Antwort, die von der richtigen nicht unterscheidbar ist. Die
   Instrument-Paar-Regel des Korpus, angewandt auf Identität statt auf
   Defekte: geprüft wird nicht, ob das Feld einen Wert hat, sondern ob
   zwei Kandidaten darin verschieden AUSSEHEN.
3. **Vorformulierter Text:** ANGEWANDT in diesem Pass — §4,
   Slot-(f)-Grading („der Autoren-Trailer nennt ein MODELL, trennt
   also Tiers und nichts Feineres … der Session-Trailer, wo die
   Harness einen schrieb, ist der Diskriminator; sonst haben die
   Trailer die Autorschaft NICHT geklärt — den Halter fragen") und
   §2-Slot (f) auf der Agenten-Seite. Bewusst NICHT in den
   EXECUTION-Tail übernommen: der Tail wird je Dispatch gepastet, die
   Klausel hilft dem Agenten nicht, der die Identität so wenig
   auflösen kann wie der Dispatcher — eine Heimat je Bedeutung.
4. **Konsument + Abfluss-Naht:** in derselben Runde abgeflossen; der
   Eintrag hält die KLASSE fest, nicht eine Schuld. Nächste Runde, die
   ein Attributions- oder Identitäts-Feld einführt, liest ihn als
   Präzedenz.

## 2026-08-17 — Ein genannter Horizont ohne bewaffneten Wecker ist Prosa, die nur eine GEWECKTE Session ausführen kann (Peer-Handoff statiker-Meta → beat-the-books-Desk)

**ANGEWANDT 2026-08-17, als EINE Amendierung mit der
Sender-Hälfte darunter** — §4 Horizont-Klausel: wo die erwartete
Rückkehr selbst der einzige Wecker ist (Mailbox-Dispatch,
Peer-Handoff, jede Wartestellung ohne harness-verfolgte Task),
bewaffnet der Wartende den Horizont beim Warte-Beginn als eigenen
Hintergrund-Timer. Beleg: dieser Commit.

1. **Vorfall + Basis:** Die statiker-Meta-Session übergab einen
   Run per Peer-Kanal (SendMessage-Handoff, Desk
   beat-the-books-e9) und nannte den Erwartungs-Horizont (~2 h
   bis zum ersten Report) — und stellte beim Komponieren fest,
   dass die Horizont-Regel („Schweigen jenseits davon ist ein
   Befund, nie weiteres Warten", Korpus Insurance / Skill §4)
   von genau der Partei ausgelöst würde, deren Ausfall sie
   erkennen soll: der einzige Wecker der wartenden Session IST
   die erwartete Peer-Nachricht. Ein toter oder gestrandeter
   Peer erzeugt permanentes Schweigen, ununterscheidbar von
   Arbeit. Klasse zuerst identifiziert als statiker P17
   (Begehung R3, 2026-08-16, dort für Desk-Waits geparkt); die
   Prämisse „Wake-Kanal unzuverlässig" ist gemessen (Eintrag
   direkt oberhalb: Mailbox-Lane-Entzug pro Session,
   2026-08-16). Ein beobachteter Stall jenseits eines genannten
   Horizonts steht noch aus (n=0 für den Stall selbst; die
   Bewaffnung heute war Hand-Anwendung, kein Feuer).
2. **Klasse:** Horizont genannt, aber unvollstreckbar — der
   Wecker ist die überwachte Partei. (Nachbarklasse, nicht
   Merge: der Lane-Entzugs-Eintrag misst den KANAL-Verlust;
   dieser hier die fehlende Vollstreckungs-Hälfte der
   Horizont-Regel, die auch bei intaktem Kanal fehlt.)
3. **Vorformulierter Regel-Text** (Skill §4, an die
   Horizont-Klausel): „Wo die erwartete Rückkehr selbst der
   einzige Wecker ist — Peer-Handoff, Mailbox-Dispatch, jede
   Wartestellung ohne harness-verfolgte Task — bewaffnet der
   Wartende den Horizont beim Warte-Beginn als EIGENEN Wecker:
   ein In-Harness-Hintergrund-Timer (z. B. `sleep <Horizont>`
   als Background-Task), dessen Ablauf die Session re-invoziert.
   Feuert der Timer vor dem Report, ist das Schweigen der
   Befund, den die Regel bereits benennt — nachgefasst wird
   sofort, nicht weiter gewartet. Ein Horizont ohne bewaffneten
   Wecker ist Prosa, die nur eine geweckte Session ausführen
   kann." (Kein neues Werkzeug: ein Bash-Call; die
   Timer-Maschinerie, die statiker P17 als „machinery without a
   fire" parkt — cron, systemd, mtime-watch — bleibt ungebaut.)
4. **Konsument + Abfluss-Naht:** nächste
   dispatch-guards-Maintenance-Runde (Skill §4,
   Horizont-Klausel); Quota-Drain nach OBSERVATIONS-Regel.
   Sofort-Konsument: jede Session, die einen Horizont über
   einen Peer-Handoff stellt — bis zum Mint per Hand (heute so
   angewandt, statiker-Meta-Session). Querverweis: statiker
   BACKLOG P17 erhält den Timer als verengten
   Kandidat-Mechanismus, bleibt dort auf seiner genannten
   Evidenz geparkt.

## 2026-08-17 — Der Report eines Peer-getriebenen Desks strandet im Terminal-Finaltext (Wave-Handoff dispatch-guards-Desk → dotfiles-f4)

**ANGEWANDT 2026-08-17 (Text a); (b) GEBUCHT** — §4 trägt
jetzt eine eigene Handoff-Klausel: `REPORT-CHANNEL: SendMessage
<name|operator-terminal>` plus Kadenz, und „Konsument benannt" ist
keine Zustellung. Der Guard-Kandidat (b) ist als BACKLOG-Eintrag
gebucht (marker-gated Stop-Lane als Geschwister von report-enforcer,
default-warn, Biss-Test-Pflicht) — diesen Ausgang hatte der Eintrag
selbst vorformuliert. Beleg: dieser Commit + BACKLOG.md.

1. **Vorfall + Basis:** Ein per Peer-Kanal übergebener Wave-Desk
   (opus, dotfiles-f4) lieferte zweimal binnen einer Stunde
   seinen Report als FINALTEXT der eigenen Session ab statt per
   SendMessage — der Bericht erreichte niemanden, der Operator
   sah nur „idle" und fragte beim treibenden Desk nach
   (Transkript-Probe 5a243b52: Entscheidungsrunde 16:01,
   Restatement 16:14 mit eigener Formulierung „since they may
   not have rendered" — die Session KONNTE ihre Zustellung
   nicht prüfen). n=2 am selben Tag, derselbe Desk. Der
   Handoff selbst hatte den Report-Konsumenten benannt
   (Operator) — was fehlt, ist der KANAL: „Konsument benannt"
   liest sich als zugestellt, während Finaltext auf der
   Peer-Lane genau das ist, was report-enforcer für
   Mailbox-Subagenten schon verhindert.
2. **Klasse:** report-enforcer-Klasse eine Ebene höher — der
   Peer-Executor-Report strandet im Finaltext, weil kein
   Mechanismus am Turn-Ende den SENDE-Akt verlangt.
   (Nachbarklassen, kein Merge: der Wecker-Eintrag oberhalb
   ist die EMPFÄNGER-Hälfte — Schweigen erkennen; dieser hier
   die Sender-Hälfte — Schweigen gar nicht erst entstehen
   lassen. Beide zusammen sind die Peer-Rendering der
   §2-Report-Pflicht.)
3. **Vorformulierter Text:** (a) Skill §4, Handoff-Klausel
   (neben Horizont + Residuen-Split): „Der Handoff nennt den
   Report-KANAL maschinenlesbar — eine Zeile
   `REPORT-CHANNEL: SendMessage <name|operator-terminal>` —
   und die Kadenz (mindestens: jede Entscheidungsrunde, der
   Close-Report). Finaltext erreicht auf der Peer-Lane
   niemanden; ‚Konsument benannt' ist keine Zustellung."
   (b) Guard-Kandidat, default-warn: Stop-Lane als
   Geschwister von report-enforcer — feuert nur wenn das
   Transkript einen `REPORT-CHANNEL: SendMessage <name>`-
   Marker trägt UND der endende Turn substanziellen Finaltext
   komponiert UND kein SendMessage an <name> im Turn liegt;
   Marker-gated, dadurch nahe null False-Fires. Ohne Marker
   stumm.
4. **Konsument + Drain:** die fällige Maintenance-Pass-Runde
   dieses Carriers (Banner meldet sie seit heute: gebucht ~6
   vs gedraint ~1) — Text (a) ist ein §4-Amendment
   (skill-craft-gated, Release-Pipeline), Kandidat (b) geht
   als geparkter BACKLOG-Eintrag mit Bite-Test-Pflicht. Die
   Pass-Schuld wächst mit diesem Eintrag bewusst um eins; der
   treibende Desk empfiehlt, den Pass nach Wellenschluss an
   den opus-Desk zu geben statt ihn auf fable zu fahren
   (Guard-Vokabular-Bindung, routing-Modul).

### ANGEWANDT 2026-08-15 — Removal ist terminal; Reihenfolge und drei Heimaten

Slot-3-Text angewandt, aber der Audit fand eine Heimat MEHR als der
Eintrag nannte — und die dritte war ein aktiver Widerspruch, kein
Loch:

1. **Writer-Rezept** (Slot-3-Ziel): trägt jetzt die Bindung und die
   Sequenz — buchen, Lane-Close, Nachfragen, DANN entfernen. Die
   Mechanik steht hier, EINMAL.
2. **Reader-Worktree-Klausel** — vom Eintrag nicht genannt, und der
   schärfste Fund: sie wies an, den Reader-Worktree „at the booking
   of its findings" zu entfernen. Buchung ist genau der Moment, in
   dem man nachfragt; die Klausel instruierte also die verlierende
   Reihenfolge. Jetzt: gebucht UND befragt, dann entfernen.
3. **§4-Spiegel-Pflicht** (Slot 4 fragte, ob ein Querverweis
   genügt): nein — der Satz BEHAUPTETE „a named/mailbox agent stays
   resumable after its report", was nach einer Entfernung schlicht
   falsch ist. Kein fehlender Zeiger, sondern eine Aussage, die die
   neue Bindung widerlegt. Jetzt mit Vorbehalt plus Quell-Etikett.

**Lehre über den Vorfall hinaus:** ein Eintrag, der EINE Zielstelle
nennt, hat die Amendment-Audit-Pflicht nicht erledigt — die Regel
verlangt, jede Heimat der Regel zu prüfen, und die teuerste Heimat
war die, die niemand als betroffen las, weil sie über einen anderen
Worktree-TYP sprach. Klasse: dieselbe Reichweiten-Frage wie beim
Vokabular-Cascade heute früh (0.10.20), anderer Träger.

**Beleg:** dieser Commit.

## 2026-08-15 — Worktree-Entfernung verbrennt den Resume-Kanal (statiker E-Lane-Batch)

**ANGEWANDT 2026-08-15 — Beleg: der `### ANGEWANDT`-Block DIREKT
DARÜBER** („Removal ist terminal; Reihenfolge und drei Heimaten"), der
diesen Eintrag disponiert. Bis zum Pass am 2026-08-17 trug er gar
keine eigene Disposition: sein einziges Ausgangs-Signal war die
POSITION im abgeflossenen Abschnitt — genau die Lesart, die dieser
Träger nicht mehr zulässt. Die Arbeit selbst war gelandet
(plugin/skills/worktree/SKILL.md, Cleanup-Klausel); die Lücke war der
RECORD, nachgetragen auf Befund der Frisch-Kontext-Runde.

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

### MERGE 2026-08-18 — VIERTER Slot derselben Wurzel: die geerbte WIRKUNGS-Behauptung, die als Begründung reist

**Vorfall + Basis:** Sprachpass-Bau (pbs-doc `93d576b`/`7eca7f2`,
opus-Lane, Planungsbüro-Desk). Der Bauer meldete im Abschluss-Bericht,
der Pass lese die ROHDATEI statt der kommentarfreien Zeilen — die
STRUKTURELLE Hälfte, belegt. Daran hing eine WIRKUNGS-Behauptung: „in
einem Repo mit großen LaTeX-Kommentarblöcken ersäuft der Pass in
Referenztext". Die war aus einem Docstring erschlossen, nie ausgeführt.
Der Dispatcher hat sie ungeprüft in einen Nachtrags-Bauauftrag
verwandelt („statt der Rohdatei die `code_zeilen` verwenden"). Beim Bau
hat der Bauer sie selbst widerlegt (`hunspell -t` entfernt
LaTeX-Kommentare, inklusive `\%`-Semantik; Abschalt-Probe über 20 .tex:
34 Kandidaten in beiden Varianten, 0 Dateien mit Unterschied) und
gestoppt, statt einen wirkungslosen Umbau zu bauen. Kosten: eine
Nachtrags-Runde plus eine Bau-Anweisung, die nicht rot herstellbar war.
Der Dispatcher hat die Widerlegung mit vier Zeilen in Sekunden
nachgefahren — dieselben Sekunden waren beim Brief-Schreiben verfügbar.

**Triage: loaded-but-inert, aber mit echter Verengung.** §1 bindet
Provenienz-Grade an „every line asserting the target repo's CURRENT
STATE" und nennt als Grenze „every audit finding turned into a build
step gets its cited line opened once". Eine WIRKUNGS-/Mechanismus-
Behauptung ist beides nicht: sie sagt nichts über den Ist-Zustand,
sondern über das Verhalten unter Bedingungen, die im Zielrepo gerade
nicht vorliegen — und sie reist als BEGRÜNDUNG der Anweisung, nicht als
Zitat. Damit trägt sie kein Grade-Etikett und niemand öffnet sie.

**Vorformulierter Regel-Text** (§1, an die Provenienz-Klausel): „Eine
geerbte Behauptung über WIRKUNG oder MECHANISMUS — was passieren
würde, warum ein Umbau nötig ist — wird beim Übergang in eine
Bau-Anweisung geöffnet wie eine Zustands-Behauptung: der Brief nennt
den ausgeführten Check oder trägt das Etikett „unverifiziert". Sie ist
die teuerste Klasse, weil sie als BEGRÜNDUNG reist statt als Zitat und
darum keinen Grade-Slot berührt; und weil ein Bauauftrag aus ihr
regelmäßig NICHT ROT HERSTELLBAR ist — der Bauer stößt erst am
Verifier darauf, eine Runde zu spät."

**Konsument + Abfluss-Naht:** nächste dispatch-guards-Maintenance-Runde
(§1-Provenienz-Klausel, gebündelt mit den drei Vorgänger-Slots). Die
Executor-Spiegelhälfte hat der Bauer selbst formuliert und sie ist
schärfer als die Dispatcher-Seite: ein Befund, der eine WIRKUNG
behauptet, nennt seinen ausgeführten Check oder trägt das Etikett —
Prosa-Befunde werden von nichts ausgeführt, anders als alles, was beim
Bauen ohnehin durchläuft. Sie gehört in den executor-Skill.

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

## Offen

Lebende Einträge — die Liste, an die angehängt wird. Was hier steht,
hat den Wartungs-Pass nicht verlassen, aus je am EINTRAG genanntem
Grund; diese Kopfzeile zählt sie nicht auf, damit sie nicht mit dem
Bestand veraltet (eine frühere Fassung sprach von „den drei unten",
während fünf hier standen — Etikett über eigenem Körper).

**RESIDUUM (Wartungs-Pass 2026-08-17) — Heimat außerhalb
dieser Arbeitskopie:** der vorformulierte Text amendiert das
guard-checker-bau-Devbook im dotfiles-Repo (dortiges CLAUDE.md,
§Registered procedure). Diese Session hält die dispatch-guards-Kopie,
nicht dotfiles (ein Schreiber pro Arbeitskopie), also ist der Eintrag
hier NICHT abgeflossen und wird auch nicht so gebucht. Naht: die
nächste Amendierung des Devbooks dort. Prüfung, wer sie am Abschluss
fährt: diese Session meldet die drei Texte an den dotfiles-Desk und
an den Operator; erledigt ist sie erst, wenn das Devbook sie trägt.
**Stand 2026-08-17, Abschluss dieses Passes:** die TEXTE sind im
besitzenden Repo gebucht (dotfiles b3571ca, READY-Eintrag mit
LEDGER-Zeile, am Quelltext geprüft); ANGEWANDT sind sie dort nicht.
Ein anderswo gebuchter Eintrag ist kein angewandter — die
Unterscheidung steht hier, weil eine Buchung sich beim Lesen wie
Erledigung anfühlt. Bleibt offen, Konsument unverändert.

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

**Positions-Nachtrag 2026-08-17 (Wartungs-Pass):** dieser Eintrag
wurde von einer dritten Session am Datei-ENDE angehängt und lag damit
im Abschnitt `## Abgeflossen` — ohne Disposition, also als abgeflossen
LESBAR, ohne es zu sein. Nur die Position ist geändert, der Wortlaut
steht unberührt. Der Auslöser ist strukturell, nicht persönlich: wer
anhängt, schreibt ans Datei-Ende — deshalb steht die lebende Liste
jetzt dort, und ein doc-drift-Check hält die Reihenfolge fest.

### MERGE 2026-08-18 — 2. Vorfall, neuer Mechanismus derselben Klasse: die Meldung hat ZWEI BLÖCKE, und `in stderr` unterscheidet sie nicht

1. **Vorfall + Basis:** YAML-Parse-Lane im globalen `pre-commit`
   (dotfiles `6c1ba7b`, opus-Lane aus dem Planungsbüro-Desk). Der
   Nachtrag gab der Lane eine ZWEITE Meldungs-Sektion („KONNTE NICHT
   GEPRÜFT WERDEN") neben der blockierenden. Der Biss dafür —
   ComposerError aus der Defekt-Menge entfernen — blieb GRÜN: die
   Zusicherung prüfte `"alias.yaml: ComposerError" in stderr`, und das
   ist in BEIDEN Welten wahr, weil dieselbe Zeile bei Fehl-Einordnung
   wortgleich in den anderen Block wandert; `rc==1` blieb ebenfalls
   wahr, weil ein zweiter Defekt weiter blockierte. Die Lane las das
   Grün als Befund über die eigene Zusicherung statt als Freispruch,
   verschärfte sie (Split am Blocker-Kopf + Abwesenheits-Prüfung im
   anderen Block) und bekam den Rot.
2. **Klasse:** identisch zum Stamm-Eintrag — ein Prädikat am AGGREGAT
   ist von jedem anderen Teil der Ausgabe erfüllbar. NEU ist der
   Auslöser: nicht ein FREMDER Check liefert die erfüllende Zeile,
   sondern der geprüfte Mechanismus SELBST, über seine zweite Sektion.
   Deshalb greift die Stamm-Formulierung („der Test isoliert den
   Eintrag des geprüften Schritts") hier nicht: der Eintrag IST
   isoliert, er steht nur im falschen Block.
3. **Vorformulierter Fix-Text** (Devbook guard-checker-bau, Schritt 4,
   an die Stamm-Ergänzung anzuhängen): „Emittiert ein Mechanismus mehr
   als EINE Meldungs-Sektion, nennt die Zusicherung die SEKTION, nie
   nur den Text: geprüft wird, dass die Zeile im erwarteten Block
   steht UND in keinem anderen. Eine Fehl-Einordnung zwischen zwei
   Sektionen erzeugt sonst dieselbe Zeichenfolge wie der korrekte
   Ausgang — der Biss ist dann in beiden Welten wahr."
4. **Konsument + Abfluss-Naht:** unverändert die nächste Amendierung
   des guard-checker-bau-Devbooks (dotfiles CLAUDE.md §Registered
   procedure), gebündelt mit den dort wartenden Schritt-4-Ergänzungen.

## 2026-08-18 — Die frisch gebaute MESSUNG ist selbst ein Instrument, und ihr Ergebnis liest sich fertig (2 Vorfälle, 2 Lanes, ein Tag)

1. **Vorfall + Basis:** (a) Sprachpass-Bau (pbs-doc `93d576b`,
   opus-Lane): Der Bestands-Lauf gab 209/185 statt der im Brief
   genannten 183/159. Ursache war die Zähl-Pipeline, nicht der
   Gegenstand — bei MEHREREN Dateiargumenten stellt `hunspell` jeder
   Ausgabezeile `<datei>: ` voran, `sort -u` zählte also
   Datei-Token-PAARE statt Tokens. Aufgedeckt allein durch den
   Abgleich mit einer unabhängig erhobenen zweiten Zahl (der des
   Dispatchers); ohne sie wäre 209 als Befund über den Bestand
   gebucht worden. (b) YAML-Lane (dotfiles `518a78d`, opus-Lane): die
   Bestands-BASELINE wurde aus einer Scratch-Kopie des Werkzeugs
   genommen — das Werkzeug warnt selbst, dass es den LIVE-Checkout
   misst. Eine „Baseline aus der Kopie" ist bei einem solchen
   Werkzeug keine.
2. **Klasse:** eine ad-hoc gebaute Messung (Zähl-Pipeline, Report-Diff,
   Baseline-Lauf) präsentiert sich als SCHAUEN, nicht als Messen —
   nichts fordert den Beweis an, und ihre Ausgabe kommt bereits in
   Antwort-Form. Der Korpus hat die Regel (Grounding, Instrument-Paar);
   was hier fehlt, ist ihre Kante im Brief: der Verifier-Slot
   kommissioniert die ZAHL, nie die Probe auf das Instrument, das sie
   erzeugt.
3. **Vorformulierter Regel-Text** (§1, Verifier-Klausel eines Briefs,
   der eine Bestands-ZAHL erwartet): „Nennt der Brief eine erwartete
   Bestands-Zahl, verlangt er die Zahl UND die Form ihrer Erhebung:
   welches Kommando, über welche Population, mit welchem
   bekannt-positiven Fall als Kontrolle. Weicht die gemessene Zahl ab,
   ist die erste Hypothese die MESSUNG, nicht der Bestand — und eine
   Baseline wird VOR der Installation genommen, nie aus einer Kopie
   danach, wenn das Werkzeug den Live-Zustand misst."
4. **Konsument + Abfluss-Naht:** nächste dispatch-guards-Maintenance-
   Runde (§1-Verifier-Klausel) und die nächste Amendierung des
   guard-checker-bau-Devbooks (dotfiles CLAUDE.md §Registered
   procedure, Schritt 2/5) — dort ist die Baseline-Hälfte zu Hause.
   Sofort-Konsument: jede Session, die eine Bestands-Zahl in einen
   Brief schreibt — per Hand bis zum Mint.

## 2026-08-18 — Der Devbook-Satz steht als VORFALLS-ERZÄHLUNG da, wo eine Anweisung gebraucht wird

1. **Vorfall + Basis:** YAML-Lane (dotfiles `518a78d`). Schritt 2 des
   guard-checker-bau-Devbooks verlangt, dass die ALTE Seite jede aus
   `__file__` abgeleitete Pfad-Prämisse erhält — der Text sagt das,
   aber als Erzählung zweier Vorfälle vom 2026-08-10 („zu eng in die
   eine Richtung … eine Ebene weiter draußen dasselbe"). Die Lane
   berichtet ausdrücklich: als Anweisung gelesen hätte sie zu eng
   kopiert; sie hat den ganzen Baum per `git archive` nur deshalb
   genommen, weil sie die Erzählung auf ihren eigenen Fall
   ÜBERTRAGEN hat. Das ist eine Leistung des Lesers, keine Eigenschaft
   des Texts.
2. **Klasse:** Devbook-Form. Eine Regel, die nur als Vorfalls-Bericht
   vorliegt, verlangt vom Ausführenden die Ableitung des Prädikats aus
   dem Beispiel — genau die Design-Arbeit, die das Devbook vor den
   Dispatch verschieben soll. Sie fällt nicht auf, weil ein guter
   Leser sie stillschweigend leistet.
3. **Vorformulierter Fix-Text** (Devbook guard-checker-bau, Schritt 2,
   Kopfsatz vor die Erzählung): „Die ALTE Seite ist eine Kopie des
   ganzen ARBEITSBAUMS (`git archive HEAD`), nicht des geänderten
   Verzeichnisses — jede aus `__file__` abgeleitete Pfad-Prämisse muss
   in ihr auflösen. Die Prüfung dafür ist der eigene Self-Check der
   Kopie GRÜN, bevor irgendein Rot aus ihr geglaubt wird. Die beiden
   Vorfälle unten zeigen, was zu eng aussieht." Der bestehende
   Erzähltext bleibt darunter stehen — er trägt die Belege.
4. **Konsument + Abfluss-Naht:** nächste Amendierung des
   guard-checker-bau-Devbooks (dotfiles CLAUDE.md §Registered
   procedure); Amendierung setzt den Fingerprint zurück (eval-open),
   also mit den anderen wartenden Schritt-2/4-Ergänzungen bündeln.

## 2026-08-17 — Ein Brief benennt eine Schema-Ableitungsquelle, die die abzuleitende LANE-KLASSE gar nicht führt (statiker P16-Lane)

1. **Vorfall + Basis:** Ein Build-Brief (statiker Stop-Hook-Lane,
   2026-08-17) wies den Executor an, das blockierende
   Stop-Hook-Schema "aus dem Referenz-Plugin dispatch-guards
   abzuleiten" — das Plugin führt aber KEINE blockierende
   Stop/SubagentStop-Lane (writer-reservation-gate warnt nur,
   report-enforcer injiziert nur additionalContext). Der Executor
   lief in die Sackgasse, wich korrekt auf die Harness-QUELLE aus
   (~/dev/reference/claude-code: processHookJSONOutput,
   stopHooks.ts) und meldete die Abweichung unter der
   vorautorisierten Reparaturklasse des Briefs. Kein Schaden —
   aber nur, weil die stärkere Quelle lokal vorlag und der
   Executor sie fand.
2. **Klasse:** Brief-Behauptung über eine QUELLE, deren bloße
   Existenz am Brief-Zeitpunkt geprüft wurde, deren INHALT aber
   nicht — die §1-Regel "Opening a REFERENCE is not opening its
   CONTENT", hier in der Ableitungs-Variante: die Quelle
   existiert, führt aber die Klasse nicht, die abgeleitet werden
   soll.
3. **Vorformulierter Regel-Text** (§1, an die
   Schema-bearing-external-facts-Klausel oder als eigener Punkt):
   „Ein Brief, der eine ABLEITUNGSQUELLE benennt (‚leite das
   Schema/Muster aus X ab'), prüft am Brief-Zeitpunkt, dass X die
   abzuleitende Klasse tatsächlich FÜHRT — ein Grep auf die
   Klassen-Signatur genügt; die Quelle nur zu öffnen genügt
   nicht. Führt X die Klasse nicht, benennt der Brief die echte
   Quelle oder kommissioniert die Suche ausdrücklich."
4. **Konsument + Abfluss-Naht:** nächste
   dispatch-guards-Maintenance-Runde (§1-Text); Quota-Drain nach
   OBSERVATIONS-Regel. Sofort-Konsument: jede Session, die heute
   Ableitungs-Briefe komponiert — per Hand bis zum Mint.

## 2026-08-17 — Das Signal ÜBER die Maschinerie, gelesen als Aussage über die ARBEIT (Spawn-Quittung; Wecker, der seine Lane überlebt)

1. **Vorfall + Basis (zwei Gesichter, je gemessen):** (a) Ein
   opus-Verifier-Dispatch quittierte "Spawned successfully … via
   mailbox" und starb Sekunden später am Wochenlimit — der
   Fehlschlag kam als SEPARATE Notification. Eine triviale
   sonnet-Lane eines Nachbar-Desks lieferte dieselbe Zeichenkette
   und lief durch. Ein Rückgabewert, entgegengesetzte Ausgänge: die
   Quittung unterscheidet nichts über den LAUF. (b) Zwei in
   derselben Session bewaffnete Horizont-Timer feuerten, NACHDEM
   ihre Lanes berichtet und geschlossen waren — n=2 am selben Tag,
   beide harmlos, beide aus demselben Loch: die frisch geschriebene
   §4-Klausel sagt, der Wartende BEWAFFNET den Horizont, und hört
   da auf.
2. **Klasse:** Ein Signal über die MASCHINERIE (Launcher-Quittung,
   Wecker, Scheduler-Exit) wird als Aussage über die ARBEIT
   gelesen. Der Korpus nennt die allgemeine Form — ein Launcher
   meldet, DASS gelaufen wurde, nie WAS er fand; diese beiden sind
   ihre Dispatch-Instanzen und beißen an entgegengesetzten Enden:
   eine Quittung, die zu viel behauptet, und ein Alarm, der seinen
   Gegenstand überlebt. Ein Fehlalarm auf dem Instrument, dessen
   ganze Aufgabe es ist, Schweigen lesbar zu machen, trainiert
   genau den Reflex, der das nächste echte Schweigen abtut.
3. **Vorformulierter Text** (§4, an die Horizont-Klausel, EIN Satz
   für beide Hälften — eine Nur-Bewaffnen-Regel ist ja das, was
   den Fehlalarm erzeugt hat): "Der Rückgabewert eines Spawns ist
   eine Launcher-Quittung: er belegt den START und sagt nichts
   über den Lauf — eine Lane, die Sekunden später stirbt,
   quittiert wie eine, die durchläuft, und ihr Fehlschlag kommt,
   wenn überhaupt, in eigener Meldung. Kapazitäts-,
   Lebendigkeits- und Zuschnitt-Schlüsse warten auf einen REPORT.
   Und der Wartende ENTSCHÄRFT seinen Horizont-Timer, sobald der
   Report landet: ein Wecker, der seine Lane überlebt, feuert auf
   eine geschlossene und macht das nächste echte Schweigen zu
   Rauschen."
4. **Konsument + Abfluss-Naht:** die nächste §4-Runde; hier
   gebucht und NICHT angewandt, weil der Release dieses Passes
   durch ist und ein weiterer Payload-Commit für einen Satz die
   Runde nicht wert ist — die Buchung ist der Ausgang, nicht der
   Aufschub.

## 2026-08-17 — Prädikat-WEITUNG entwertet Alt-Fixtures gleicher Form still; grün laufen genügt nicht (statiker Mint-Batch, P27)

1. **Vorfall + Basis:** Beim Weiten eines Verdikt-Prädikats
   (statiker P27: CLOSURE_ABSENT akzeptiert jetzt terminale
   [BIT]-Runden ohne design-ändernde Disposition als SATISFIED)
   änderten drei bestehende Suite-Stellen (2 Tests, 1
   Contract-Fixture) still ihre BEDEUTUNG — alle drei teilten
   eine Form (bare [BIT]-Runde, keine Findings, keine D-Zeile),
   die unter dem alten Prädikat must-fail war und unter dem
   neuen vakuum-grün lief. Die Lane fand sie per Form-SUCHE über
   die Suite, nicht über den Testlauf (der war grün); Executor-
   Report Lesson 3, Commit 522e8d2 (statiker).
2. **Klasse:** Accept-Set-Weitung macht Alt-Fixtures gleicher
   Form zu Vakuum-Pässen — die Fixture-hört-auf-zu-testen-Klasse
   (Korpus Fixing: Prädikat GEWINNT einen Wert) am Weitungs-Seam,
   wo der grüne Lauf das Loch exakt verdeckt.
3. **Vorformulierter Regel-Text** (§1, an die Verifier- oder
   Settled-Design-Klausel eines Build-Briefs, der ein Prädikat
   weitet): „Ein Brief, der ein Verdikt-/Gate-Prädikat WEITET,
   kommissioniert neben dem Testlauf eine FORM-SUCHE über die
   Suite: jede bestehende Assertion, deren Fixture die neu
   akzeptierte Form trägt, wird enumeriert und je als
   noch-testend oder vakuum-grün dispositioniert — ein grüner
   Lauf allein unterscheidet die beiden nicht."
4. **Konsument + Abfluss-Naht:** nächste
   dispatch-guards-Maintenance-Runde (§1-Text); Quota-Drain nach
   OBSERVATIONS-Regel. Sofort-Konsument: jede Session, die heute
   Prädikat-weitende Briefs komponiert — per Hand bis zum Mint.

### Ein Handoff, der EINEN Kanal nennt, hat einen Single Point of Failure — der Rückfall-Kanal rettet den Bericht, wenn der Absender vor ihm stirbt

**1. Vorfall + Basis.** 2026-08-18, unmittelbar nach dem
0.11.3-Pass. Ein Peer-Desk (pbs-office-Backlog) erteilte diesem
Desk drei Arbeitspunkte und nannte den Report-Kanal DOPPELT:
„SendMessage an diese Session — oder an den Betreiber im Terminal,
wenn dir das lieber ist; er hat den Auftrag erteilt und liest mit."
Der Zwischenbericht ging per SendMessage und LANDETE (success).
Der ABSCHLUSSBERICHT, keine Stunde später, scheiterte:
`No agent named 'planungsb-ro-schulz-96' is reachable`, und
ListAgents führte keine `planungsb-ro-*`-Session mehr. Der Absender
war zwischen den beiden Nachrichten verschwunden. Nebenbei im
Protokoll sichtbar: das Desk nannte sich in seiner eigenen
Kanal-Zeile `planungsb-ro-schulz-7f`, während die Harness es als
`-96` führte — zwei Kennungen für denselben Absender.

**2. Klasse.** Nicht der Horizont (der ist eine Stunde alt und
steht in §4), sondern seine SPIEGELUNG auf der Berichts-Seite: §4
verlangt heute `REPORT-CHANNEL: SendMessage <name|operator-terminal>`
— EINEN Kanal, als Entweder-oder. Der Kanal kann aber zwischen
Auftrag und Bericht sterben, und dann ist die genannte Heimat leer.
Hier ging nichts verloren, weil der Absender aus eigenem Antrieb
einen ZWEITEN nannte; die Regel verlangt das nicht. Das ist die
positive Probe: dieselbe Disziplin, die den Bericht rettete, ist
im Skill nicht vorgeschrieben.

**3. Vorformulierter Regel-/Fix-Text** (§4, an die Handoff-Klausel):

> Die Kanal-Zeile nennt einen RÜCKFALL, nicht nur ein Ziel:
> `REPORT-CHANNEL: SendMessage <name>, fallback <operator-terminal>`.
> Ein Peer-Kanal kann zwischen Auftrag und Bericht sterben — der
> Absender schließt, seine Kennung wechselt — und der Empfänger
> erfährt es erst beim Senden, also nachdem die Arbeit getan ist.
> Ohne benannten Rückfall ist der fertige Bericht dann heimatlos,
> und der Empfänger entscheidet ihn im Zweifel weg. Der Rückfall
> ist immer erreichbar: der Betreiber.

**4. Konsument + Abfluss-Naht.** Nächste dispatch-guards-Runde
(§4-Text). Nicht sofort gebaut, weil der Release dieses Passes
durch ist und ein Payload-Commit samt Bump für einen Satz die Runde
nicht wert ist — die Buchung ist der Ausgang, nicht der Aufschub.
Sofort-Konsument: jede Session, die heute einen Handoff annimmt —
den Rückfall per Hand erfragen, bis der Mint steht.

<!-- NEUE EINTRÄGE ANS DATEI-ENDE, UNTER "## Offen" — dies ist
     die lebende Liste. Abgeflossenes steht OBERHALB. Der
     doc-drift-Check erzwingt genau diese Reihenfolge, weil ein
     Anhängen am EOF sonst im abgeflossenen Abschnitt landet. -->

- 2026-08-18 **writer-reservation-gate benennt das FALSCHE Repo bei
  Cross-Repo-Commits** (n=2 am selben Abend, beide aus einer
  dotfiles-Session heraus: ein Subagent-Commit in
  `~/dev/Gunther-Schulz/claude-worktime` und ein Desk-Commit via
  `git -C .../claude-worktime` — beide WARNs nannten die
  dotfiles-Arbeitskopie samt fremdem Holder, obwohl kein benannter
  Pfad sie beruehrte; vom Subagenten korrekt als "misdirected/stale
  warning" gemeldet statt gehandelt). KLASSE: Ziel-Aufloesung eines
  Waechters aus dem Session-Kontext statt aus dem KOMMANDO — die
  Arbeitskopie wird aus der Session-cwd gelesen, nicht aus `-C
  <pfad>`/dem effektiven Ziel des git-Aufrufs; ein WARN ueber ein
  unbeteiligtes Repo ist die feuert-auf-Nicht-Defekt-Form und
  trainiert das Abtun genau der Warnung, die einmal echt sein wird.
  VORFORMULIERTER FIX-TEXT: der Gate loest VOR dem Vergleich die
  Ziel-Arbeitskopie des Kommandos auf (`-C`-Argument, sonst cwd des
  Bash-Aufrufs) und warnt nur, wenn DIESE Kopie reserviert ist;
  Selbstprobe ergaenzt ein Paar: Commit mit `-C` auf ein fremdes,
  unreserviertes Repo → still, Commit in der reservierten Kopie →
  WARN (beide Arme muessen differieren). KONSUMENT + ABFLUSS-NAHT:
  naechster Bau am `writer-reservation-gate` bzw. naechste
  dispatch-guards-Maintenance-Runde.
  **n=3 am 2026-08-19** (cache-fix-Desk, Lane `sonnet-backlog-close-home`,
  Commit `d2f9520` in `~/dev/Gunther-Schulz/dotfiles`): der WARN nannte
  `~/dev/vendor/claude-code-cache-fix` — die PRIMAERE cwd der
  dispatchenden Session — als umstrittene Arbeitskopie, waehrend der
  Commit korrekt per Pathspec in dotfiles lag. Dritte Instanz, dritte
  RICHTUNG derselben Wurzel: die beiden 08-18-Faelle liefen aus einer
  dotfiles-Session in ein Fremdrepo, dieser aus einer cache-fix-Session
  in dotfiles — die Ziel-Aufloesung folgt also der Session, nicht dem
  Kommando, unabhaengig davon, welches Repo welche Rolle hat. Der
  vorformulierte Fix oben deckt diesen Fall unveraendert ab; nichts
  daran zu aendern, nur der Zaehler und die Fundstelle.
  Was die Klasse hier zusaetzlich kostet, und es ist das Argument fuer
  den Bau statt fuer weiteres Zaehlen: der Agent hat den WARN korrekt
  als fehlgeleitet gemeldet und NICHT gehandelt — dreimal in Folge hat
  jetzt die Disziplin des Executors den Waechter aufgefangen, statt
  umgekehrt. Ein Waechter, der auf seine eigene Ignorierung angewiesen
  ist, um nicht zu schaden, ist die feuert-auf-Nicht-Defekt-Form im
  Endstadium.
  **n=4 am 2026-08-23** (Lane `opus-report-provenance`, drei Commits
  f6b7d94/554e36c/dbdd81a in `~/dev/Gunther-Schulz/dispatch-guards`):
  der WARN nannte `/home/g/wan2gp` — die cwd der DISPATCHENDEN
  Session, ein Repo, das dieser Commit gar nicht beruehrt. Vierte
  Instanz, vierte Konstellation: Session-cwd Repo A, Kommando-cwd
  Repo B, und weder das eine noch das andere ist dotfiles. Bestaetigt
  die 08-19-Diagnose ohne Zusatz — die Ziel-Aufloesung folgt der
  Session, nie dem Kommando —, und der Agent hat den WARN wieder
  gemeldet statt gehandelt: viermal in Folge faengt die
  Executor-Disziplin den Waechter auf. Am vorformulierten Fix oben
  ist nichts zu aendern, nur Zaehler und Fundstelle.

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
