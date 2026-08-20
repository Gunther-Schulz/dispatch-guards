# dispatch-guards — working discipline

A Claude Code plugin: three skills (`dispatch`, `executor`,
`worktree`) plus the mechanical guards that enforce the computable
slice of the dispatch discipline. Prose rules are best-effort; hooks
are not — this repo carries both sides, and the split is the design.

## Discipline

- **Skill edits run skill-craft.** Any change under `plugin/skills/`
  invokes the `skill-craft` skill and works its
  `references/review-checklist.md`, findings stated per item with
  file:line. A pre-edit hook enforces the invocation per turn.
- **`plugin/skills/dispatch/` and `plugin/skills/executor/` are
  operational corpus** where this plugin is deployed as the
  operator's corpus half: their SKILL.md and `references/` are
  additionally governed by `~/.claude/CLAUDE-maintenance.md`
  (composition rule, Pareto, amendment-over-addition,
  provenance/de-particularization), and a structural restructure
  there lands first, then takes a fresh-context vet before push.
  They are the sending and receiving sides of one discipline and
  share its brief-facing forms, so a rule amended in either is
  audited across both. `worktree` is not corpus — portable git
  mechanics, governed by skill-craft alone.
- **Wrap corpus markdown at 69 columns.** Enforced by a hook on the
  operator's machine; the verify block below re-checks it anywhere.
- **Hook docstrings are canonical** for their own lanes, bindings,
  and accepted residue. The skills deliberately do not restate a
  lane list — a prose copy of a mechanical contract rots silently.
  Amending a lane means amending its docstring, and auditing every
  other home that states it (README table, skill prose).
- **New guard lanes ship default-warn** and earn `deny` through the
  fire-rate review against the fire log, never by assertion.
  Declared exception (operator decision 2026-08-08): the
  mandatory-name lane in agent-model-gate's check() blocks from day
  one — check()'s exit-2 path structurally precedes guard_mode(),
  and the lane's repair is compose-time and mechanical (add the
  `<model>-` name), the false-fire profile staging exists to
  protect against. A future lane wanting the same exemption earns
  it by its own operator decision, never by inheriting the
  structure.
- **Releases go through `skill-craft:release-plugin`** — version
  bump in `plugin/.claude-plugin/plugin.json`, marketplace pin,
  operator `/reload-plugins` handoff. Editing a skill and leaving it
  unreleased puts source and served version out of step.

## Role files

- `LEDGER.md` — the on-disk ledger: one entry per line, append-only,
  chronological; facts with basis, decisions with their why, open
  questions. Read its tail before re-deriving anything that may be
  settled; append there rather than leaving a rationale only in a
  commit message. Added 2026-08-06, reversing this file's former
  "no `LEDGER.md`" deviation — that deviation's own revisit condition
  ("if multi-session work here starts re-deriving settled ground")
  fired when multi-session corpus work began running in this repo.
- `BACKLOG.md` — parked items (each with its named missing evidence)
  and ready items (decision-complete, dispatchable).
- `dev-notes/` — the maintenance layer, never loaded by operational
  files: per-skill observation journals
  (`dispatch-OBSERVATIONS.md`, `executor-OBSERVATIONS.md`,
  `worktree-OBSERVATIONS.md`), harvest records, and evidence homes
  for claims the skills cite but do not rest on
  (`payload-cache-correlation.md`, `permission-request-seam.md`).
- `tools/` — repo-owned checks: `replay-bench.py` plus its curated
  payload corpus, `check-doc-drift.py`, and `lane-cost.py` (measures
  what a fan-out actually cost from its own transcripts, and the
  crossover call-count above which splitting a read-only lane pays
  on tokens alone — the sizing question §1's write-boundary join
  cannot answer for read lanes).
- `README.md` — humans deciding whether to install; the guard roster
  and the site-policy schema live there.

## Verify

These four commands are what make work in this repo trustworthy. Run
them before any commit that touches hooks, skills, or the corpus.

```bash
# 1. Guards, end-to-end through the real scripts (stdin → stdout JSON).
#    Fails on any missed catch or false fire, including the historical
#    false-fire regressions.
python3 tools/replay-bench.py

# 1a. The bench's OWN isolation — the environment premises it pins.
#     Its classification is TYPE-only, so a case's rendered CONTENT can
#     move with an unpinned environment file while the counts stay green:
#     measured 2026-08-20, every brief-reminder case was reading the
#     operator's real ~/.claude/readiness.json. Red-proven by removing the
#     pin (two failures: output identity, and a planted sentinel class
#     reaching the render).
python3 tools/replay-bench.py --test

# 2. Per-guard bite-tests — the function-arm net, and the only net for
#    the six guards the bench does not cover.
for h in plugin/hooks/*.py; do
  [ "$(basename $h)" = "_dispatch_common.py" ] && continue
  python3 "$h" --test || echo "FAILED: $h"
done

# 3. The devbook-form detector's own tests.
python3 plugin/skills/executor/scripts/check_devbook_form.py --test

# 3a. The worktree doctor's own tests — pure verdict aggregation plus a
#     real-git three-arm fixture (clean+owned / clean+undeclared / DIRTY).
#     Red-proven against the incident's own sweep loop, which destroys
#     all three arms including the dirty one.
python3 plugin/skills/worktree/scripts/worktree_doctor.py --test

# 3b. Doc-vs-mechanism drift: the guard roster, the shipped skills,
#     the §2 report slots and the policy schema are each stated in
#     both prose and a mechanism. Proven red on the two real
#     omissions the 2026-08-06 review found by reading.
python3 tools/check-doc-drift.py

# 4. Manifests parse, and corpus markdown stays inside 69 columns.
python3 -c "import json;[json.load(open(f)) for f in \
  ['plugin/.claude-plugin/plugin.json','.claude-plugin/marketplace.json']]"
python3 -c "
import subprocess,sys
d=subprocess.run(['git','diff','-U0','HEAD','--',
                  'plugin/skills/dispatch','plugin/skills/executor'],
                 capture_output=True,text=True).stdout
bad=[l[1:] for l in d.split(chr(10))
     if l.startswith('+') and not l.startswith('+++')
     and len(l)-1>69 and not l[1:].lstrip().startswith('description:')]
print(*bad,sep=chr(10)) if bad else print('wrap: clean')
sys.exit(1 if bad else 0)"
```

A guard change additionally extends `tools/corpus/guards.jsonl` — the
bench scores only the cases the corpus enumerates, so an unextended
corpus reports clean on an untested lane.
