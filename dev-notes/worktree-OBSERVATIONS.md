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

## Abgeflossen

Angewandte oder verworfene Einträge mit Beleg — der Eintrag WANDERT
hierher (Form: `dev-notes/OBSERVATIONS-FORM.md`).

### ABGEFLOSSEN 2026-08-17 (Wartungs-Pass, mit dem dispatch-Carrier
### mitgezogen — dieser Träger schuldete nach Quote nichts)

Vorschläge 1–3 sind gebaut, 5 verworfen, 4 bleibt geparkt — der
Eintrag verlässt damit die lebende Liste, ohne dass die offene Frage
verschwindet:

1. **Ownership** — realisiert als DEKLARATION statt Markierung:
   `worktree_doctor.py` behandelt nur per `--owned PATH` erklärte
   Worktrees als eigene, leitet Besitz nie aus Pfad-Form, Namens-
   Präfix oder Branch ab (genau die Muster-Blindheit, die der
   Vorschlag ausschloss); alles andere ist UNKNOWN und nie entfernbar.
2. **Kein Force über schmutzige Worktrees** — das Werkzeug hat
   überhaupt keinen Entfernungs-Pfad: es druckt das unforcierte
   `git worktree remove <path>` als TEXT, DIRTY schlägt jede andere
   Klassifikation.
3. **Melden vor Handeln** — die drei Verdikte (clean / stale-found /
   could-not-verify) sind die Ausgangs-Codes; UNREADABLE wird nie zu
   etwas anderem gemacht.
4. **Retirement-Trigger** — bleibt OFFEN mit unveränderter genannter
   fehlender Evidenz (Fehlfeuer-Rate eines Kandidaten-Prädikats);
   Heimat ist der BACKLOG-Eintrag PARKED 2026-08-08, nicht dieser
   Träger.
5. **Lane meldet ihren Worktree-Pfad** — VERWORFEN: der Dispatcher
   legt den Worktree an und hält den Pfad per Konstruktion; die
   Entfernung selbst ist im dispatch-Skill §1 als terminaler Akt
   sequenziert.

**Fund desselben Passes, hier vermerkt, weil er diesen Träger
betrifft:** die Cleanup-Sektion des Skills wies noch an, Reader-/
Probe-Worktrees „at the booking of their findings" zu entfernen —
die Reihenfolge, die die 0.10.25-Amendierung als verlierend
identifiziert und in dispatch §1 korrigiert hatte, ohne diese vierte
Heimat zu erreichen (geprüft: `git log -L` zeigt die Zeile seit
38e9ae7 unverändert, `git show --stat 7a23673` nennt drei Dateien,
diese nicht dabei). Jetzt: buchen, befragen, DANN entfernen. Beleg:
dieser Commit.

## 2026-08-08 — LIFECYCLE: nobody removes worktrees, and the sweep that does has no ownership predicate

Two halves of one system, both measured the same afternoon in
`Gunther-Schulz/claude-code-cache-fix`. Neither is a binding to git
semantics — this is the first CAPABILITY-PATCH-shaped entry here, so it
is fire-checked rather than staleness-checked, and the fire rate is the
whole argument.

**Half 1 — removal is prose, so it does not happen.** The repo held
**16 extra registered worktrees**, accumulated over roughly a week by
several different sessions, every one of which had committed its work
and left. Both the dispatch skill's worktree recipe and that repo's
`docs/dev-loop.md` say the dispatcher removes the worktree after
integration. A rule stated in two places, followed by nobody, for a
week. A stale worktree is silent — it costs disk, makes `git worktree
list` unreadable, pins branches against pruning, and presents a large
undifferentiated cleanup target. The harness-cut `.claude/worktrees/
agent-*` ones behaved as documented (auto-clean only when UNCHANGED;
both carried commits, so both stayed) — the 15 hand-cut ones had no
owner at all.

**Half 2 — the cleanup that happens is unsafe.** A dispatcher session
intending to remove its OWN four lanes' worktrees ran

    for w in $(git worktree list --porcelain | awk '/^worktree/{print $2}' \
              | grep -v "^$(pwd)$"); do git worktree remove --force "$w"; done

and destroyed all 16, including one in a different session's scratchpad.
Committed work survived (branches are untouched by worktree removal; all
28 remained). **Uncommitted work in those directories is unrecoverable**,
and the path→branch mapping died with `git worktree prune` — nothing in
`.git` retains it afterwards.

**The two facts a fix has to hold together.** `--force` is the entire
difference between this and a no-op: plain `git worktree remove` already
refuses a dirty worktree, and that refusal is a feature. And the loop had
no OWNERSHIP predicate — it could not tell this session's lanes from a
week of other people's, because nothing marks ownership at create time.

**Why they are one problem:** accumulation creates the mess, the mess
invites a blunt sweep, and the sweep is destructive because ownership is
unmarked. Fixing either half alone leaves the other running.

**Evidence limit, stated because it is load-bearing:** the population
that would have shown whether this generalises was destroyed by the
incident. A scan of every repo under `~/dev` immediately afterwards
returned ZERO extra worktrees anywhere — which proves nothing, since the
only known population had just been deleted. Treat "16 in one repo over a
week" as the single datapoint it is; whether other repos accumulate is
UNMEASURED and has to be established prospectively. Equally: nobody knows
whether any of the 16 held uncommitted work and nobody can now find out,
so the honest statement is "all committed work survived; uncommitted work,
if any, is unrecoverable and its existence is unknown" — never "no work
was lost".

**Proposed rule changes (design NOT settled — the open questions are the
deliverable):**
1. Ownership is MARKED at create time by the creator, in a form that
   survives the creating session's death. Any predicate keyed on a NAMING
   convention re-creates the pattern-blind-spot class and is rejected on
   that ground alone.
2. Nothing force-removes a dirty worktree without an explicit
   per-worktree decision; the plain-remove refusal is preserved, not
   worked around.
3. A sweep REPORTS before it acts — dry-run default, each target named
   with why it qualifies. A reporting doctor verdict (three answers:
   clean / stale-found / could-not-verify) is the safe first ship; the
   automatic remover is the tempting version and is the one that just
   went wrong.
4. The retirement TRIGGER is open. Age alone is wrong (long-lived PR-slice
   worktrees are legitimate, and their branches are deliberately unmerged
   upstream slices, so "merged into main" fails too). Any candidate needs
   a measured false-fire rate before it removes anything.
5. Consider whether the dispatcher's integration step can carry removal
   mechanically, and whether a lane's closing report must state its
   worktree path so the dispatcher has the target in hand.

**Red-first verifier for whatever ships**, in a throwaway clone: three
worktrees — one clean+owned, one clean+foreign, one DIRTY. The mechanism
must name all three in its report, act on only the owned clean one, refuse
the dirty one loudly even when owned, and leave the foreign one untouched
with a stated reason. **Arm three is the one this incident would have
failed.**

Do not delete branches as part of any worktree cleanup — branches are why
the committed work survived; their retirement is a separate question.

## Offen

Lebende Einträge: keine. Neue Beobachtungen ans
Datei-Ende, unter diese Überschrift.

<!-- NEUE EINTRÄGE ANS DATEI-ENDE, UNTER "## Offen" — dies ist
     die lebende Liste. Abgeflossenes steht OBERHALB. Der
     doc-drift-Check erzwingt genau diese Reihenfolge, weil ein
     Anhängen am EOF sonst im abgeflossenen Abschnitt landet. -->
