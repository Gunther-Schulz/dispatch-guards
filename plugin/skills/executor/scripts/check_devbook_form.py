#!/usr/bin/env python3
"""Devbook form check (executor skill §3): per-element presence detector.

Usage: check_devbook_form.py <devbook.md> [...]
Exit 0 when every file carries all five form elements, 1 otherwise.

DETECTOR, NOT DEFINITION: the normative list is executor SKILL.md §3;
this script finds the loud absences cheaply (the under-report principle
applied to devbooks themselves — a missing section is a visible FAIL
line, not a silent pass). Patterns are bilingual (the graded corpus is
German and English) and deliberately generous per element: a devbook
that PASSES here can still fail human grading; one that FAILS here is
missing the element in any recognizable form. Red-proven at build time
(2026-08-05) against a probe devbook without a box; green against the
two source devbooks the form was lifted from.

Element criteria (each: first matching line is the evidence):
  1 head       addressee/consumer or named normative sources
  2 verify     numbered steps AND a verification naming its command
  3 box        an explicit limits section (closed never-do list)
  4 stop       halt conditions with return-the-question behavior
  5 report     a named report form incl. its §2-pointer variant
"""
from __future__ import annotations

import re
import sys

ELEMENTS: list[tuple[str, str, re.Pattern]] = [
    ("head", "addressee/consumer + normative sources named", re.compile(
        r"Consumer:|Adressat|written for a fresh (?:context|session)"
        r"|Quelle:|Companion facts|Grounding|GROUNDING|Zweck:", re.I)),
    ("verify", "per-case verification naming its command", re.compile(
        r"Verifikation|Verification|\bVerify\b|VERIFIKATION", re.I)),
    ("box", "explicit limits section (the box)", re.compile(
        r"\bLimits\b|the box|SCHREIB-GRENZEN|Verbots|NIE ohne"
        r"|never without|must not|darfst? nie|R10\b", re.I)),
    ("stop", "halt conditions, return-the-question", re.compile(
        r"STOPP|\bSTOP\b|stop and surface|returns? as a question"
        r"|Eskalation|escalat|Befund", re.I)),
    ("report", "named report form, empty-valid-absent-not", re.compile(
        r"report form|Report\b|Bericht|Abschluss-Bericht|§2\b", re.I)),
]
NUMBERED_STEP = re.compile(r"^\s{0,3}\d+\.\s", re.M)


def check(text: str) -> list[tuple[str, str, str | None]]:
    """[(element, description, evidence-line-or-None)] — None = ABSENT."""
    lines = text.splitlines()
    out = []
    for name, desc, pat in ELEMENTS:
        hit = next((ln.strip() for ln in lines if pat.search(ln)), None)
        if name == "verify" and hit and not NUMBERED_STEP.search(text):
            hit = None  # verification without numbered steps is not the form
        out.append((name, desc, hit))
    return out


def main(paths: list[str]) -> int:
    rc = 0
    for path in paths:
        try:
            with open(path, "r", encoding="utf-8", errors="replace") as f:
                text = f.read()
        except OSError as exc:
            print(f"{path}: UNREADABLE ({exc}) — could not verify")
            rc = 1
            continue
        results = check(text)
        missing = [name for name, _, ev in results if ev is None]
        verdict = "PASS" if not missing else f"FAIL (missing: {', '.join(missing)})"
        print(f"{path}: {verdict}")
        for name, desc, ev in results:
            print(f"  [{name}] " + (f"{ev[:90]}" if ev else f"ABSENT — {desc}"))
        if missing:
            rc = 1
    return rc


if __name__ == "__main__":
    if "--test" in sys.argv:
        conforming = (
            "# Devbook\nConsumer: any dev session, written for a fresh "
            "context.\n\n1. Do the thing.\n2. **Verify.** Run `x --test`, "
            "paste its output.\n\n## Limits (the box)\n- No pushes.\n\nA "
            "finding needing an unsettled decision returns as a question "
            "in the report.\n\n## Report\nClose with the §2 report form; "
            "empty is valid, absent is not.\n")
        r = check(conforming)
        assert all(ev for _, _, ev in r), r

        # RED bite: the probe shape the form check was built for — a
        # devbook with steps, verification, and report but NO box.
        boxless = (
            "# Devbook\nConsumer: any dev session.\n\n1. Do the thing.\n"
            "2. Verification: run `x --test`.\n\n## Report\nUse the "
            "report form.\n")
        r = {name: ev for name, _, ev in check(boxless)}
        assert r["box"] is None, r
        assert r["stop"] is None, r

        # Verification prose without numbered steps is not the form.
        proseonly = "Consumer: x.\nVerification exists.\nLimits: none may "\
            "push.\nSTOP on doubt.\nReport form named.\n"
        r = {name: ev for name, _, ev in check(proseonly)}
        assert r["verify"] is None, r

        print("check_devbook_form: all tests passed")
        sys.exit(0)
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1:]))
