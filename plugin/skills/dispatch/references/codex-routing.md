# §7 Codex routing (only when Codex CLI is installed)

Reference of the `dispatch` skill (operational corpus — see
SKILL.md's governance header). Applies only when
`command -v codex` succeeds. Bindings and certifications stamped
2026-09-12 (codex CLI 0.154.0; installed lineup gpt-5.5,
gpt-5.6-luna/sol/terra, gpt-6-astra — the configured default —
and gpt-reserve); re-check on a CLI or lineup change.

## Certified roles

Measured 2026-09-12 (mechanical read, attack, implementation,
reviewer) and 2026-09-13 (verify) in pre-registered, desk-graded
evals (evidence home: statiker `dev-notes/codex-pilot-2026-09-12.md`
and `dev-notes/codex-only-certification-2026-09-13.md`);
statiker-measured, so outside that repo the entries are
candidate-in-operation, graded by the fire-rate review.
Certification is per (role, model): a pass never infers down the
ladder, and a fail one tier down certifies nothing about the tier
above. UNMEASURED cells read as unmeasured, never as fine — luna
at attack/implementation, every codex tier at the desk role below.

- **Mechanical read** (lint/sweep comprehension, extraction):
  gpt-5.6-luna, gpt-5.6-terra and gpt-6-astra all PASS at sonnet
  parity; cheapest viable is luna.
- **Attack arm** (adversarial round against a locked design):
  gpt-6-astra for cross-vendor unique yield — it confirmed
  findings the opus arm missed while opus held more uniques, so
  the arm runs ALONGSIDE the site review tier, never instead of
  it; gpt-5.6-terra carries recovery-style attack (re-finding
  known-class defects) one price tier down.
- **Implementation** from a disposition-complete brief:
  gpt-5.6-terra (red-first replay PASS; the commit stays the
  dispatcher's — see bindings).
- **Reviewer: NOT codex.** Both tested tiers failed a checkpoint
  review replay outright (1/10 and 0/10 recovery of an
  adjudicated finding set): codex audits STRUCTURE (name parity,
  set equality, real executed probes) and does not read
  CONTRACT — page prose against tool behavior. Reviews stay on
  the site review tier. Second provenance: terra graded a verify
  requirement NOT-MET by grepping for its announcement text
  rather than reading that the page defines it as met by an
  R-line — the same structure-over-contract shape, at a new seam.
- **Verify (FP5)** (run the checks, paste output, return a
  per-requirement verdict): honesty floor HELD at every codex
  tier — zero fabricated "met" across luna/terra/astra,
  transcript-audited clean — but UNCOMPETITIVE on yield: of 9
  requirements terra resolved 6, astra 3, luna 2 (Claude
  comparison: sonnet 8, haiku 8 — both beat both codex tiers,
  cheapest Claude matching the strongest). Report SAFETY and
  YIELD as two figures, never one — only fabrication
  disqualifies, low yield is a cost. Where a codex verify leg is
  assigned, the tier is TERRA — not top, not cheapest: yield is
  INVERTED (terra 6 > astra 3 > luna 2) and cost runs the same
  way — luna spent the MOST tokens (69,525) for the FEWEST (2/9),
  breaking "volume roughly tier-invariant per role" (holds for
  attack/read-side, not verify).
- Desk role: uncertified — a verdict-battery probe saturated at
  1.00 across all three arms and two vendors and certifies
  nobody; certify only when a consuming run wants it and a probe
  that actually discriminates exists.

## Harness bindings (measured 2026-09-12)

- Invocation: `codex exec -s read-only|workspace-write -m
  <model> [--output-schema <file>]`, cwd = the workdir; a
  non-git workdir is refused without `--skip-git-repo-check`.
- **Exit 0 does not reflect API failures.** A 400 (for instance
  a schema error) empties the run and still exits 0; stderr is
  the verdict channel, and the `tokens used` figure prints
  there.
- Structured outputs run OpenAI strict mode: every declared
  property must appear in `required`.
- **The sandbox pins writes, never read reach.** A read-only arm
  hunted the whole disk and ran stale copies of the target
  repo's own tools (the oracle path). Any eval or score over a
  codex run counts only after a transcript audit for reads
  outside the workdir.
- **workspace-write denies `.git` writes even inside the
  workspace** — codex lanes cannot commit; the dispatcher
  commits. A git WORKTREE cannot serve as a codex workspace at
  all (its `.git` lives out-of-tree); isolate with an
  archive-init copy, or a clone with refs stripped and
  descendants pruned when history must resolve. Commit-bearing
  work needs `-s danger-full-access` (executed triple with a
  control) — state that loudly, a blast-radius fact, never a
  config footnote: it is NO sandbox. `read-only` cannot execute
  checks at all; a verify leg runs under `workspace-write` and
  pays the depression below.
- Suite runs inside the sandbox are depressed or blocked
  (pytest tmp-dir failures; failure counts that vanish outside
  the sandbox on the same tree). Grade suites outside the
  sandbox.
- A quota kill mid-run leaves an exit-0-shaped empty: a killed
  lane is a LOST lane, never a zero-findings result — read
  stderr before believing an empty output.
- Codex runs can exceed the Bash tool's default timeout: pass an
  explicit timeout or run in background.

## Conduct

- Prompt codex simply and self-contained — it is not Claude.
  Tell it to say clearly when it finds nothing, naming the
  target it inspected (prevents rerun loops in the parent).
- Inside workflows/agent fan-outs, wrap it: a thin Claude
  wrapper agent (model sonnet, effort low) writes the codex
  prompt, runs it via Bash, returns the report. Label such
  agents with the codex model as a name prefix so the real
  worker is visible.
- Cost model: run cost = tokens × the tier's per-token credit
  price. Measured volume is roughly tier-invariant per role
  (review-shaped objects excepted, where the cheaper tier spent
  more for less), so pick the tier by role fit and price, never
  by expected token volume.
