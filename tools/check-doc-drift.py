#!/usr/bin/env python3
"""Doc-vs-mechanism drift check for this repo.

Every fact below is stated twice by design — once in a mechanism
(hooks.json, a skill directory, a hook constant) and once in prose a
human reads (README, plugin.json, the §2 report form). Duplication
that cannot be removed has to be checked, or it drifts silently: the
2026-08-06 review found the README missing a shipped guard and
plugin.json missing a shipped skill, both undetectable by any test in
the repo and both found only by reading.

This script is that reading, mechanized. It is the deliverable of
that manual pass — the pass finds the drift once, this finds it at
every run, without the reasoning that produced it.

Run: python3 tools/check-doc-drift.py   (exit 1 on any drift)
Consumers: the repo CLAUDE.md verify block, and any release.

NOT covered, deliberately: whether the prose is CORRECT, only whether
both sides name the same things. A row describing a guard wrongly
passes here and is a review question, not a computable one.
"""
from __future__ import annotations

import ast
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def _read(*parts: str) -> str:
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as fh:
        return fh.read()


def check_guards() -> list:
    """Every guard on disk is wired, and every wired guard is in the
    README table — the drift that shipped push-claim-reminder
    undocumented."""
    out = []
    wired = set()
    for event in json.loads(_read("plugin", "hooks", "hooks.json"))["hooks"].values():
        for matcher in event:
            for hook in matcher["hooks"]:
                wired.add(os.path.basename(hook["command"])[:-3])

    on_disk = {os.path.basename(p)[:-3]
               for p in glob.glob(os.path.join(ROOT, "plugin/hooks/*.py"))
               if not os.path.basename(p).startswith("_")}
    documented = set(re.findall(r"^\| `([a-z-]+)` \|",
                                _read("README.md"), re.M))

    for name in sorted(on_disk - wired):
        out.append(f"guard `{name}` exists but is not wired in hooks.json")
    for name in sorted(wired - on_disk):
        out.append(f"hooks.json wires `{name}` but no such file exists")
    for name in sorted(wired - documented):
        out.append(f"guard `{name}` is wired but missing from the README table")
    for name in sorted(documented - wired):
        out.append(f"README documents `{name}` but nothing wires it")
    return out


def check_skills() -> list:
    """Every shipped skill is named in plugin.json's description and in
    the README — the drift that shipped `executor` undocumented in
    both for three versions."""
    out = []
    skills = {os.path.basename(os.path.dirname(p))
              for p in glob.glob(os.path.join(ROOT, "plugin/skills/*/SKILL.md"))}
    description = json.loads(
        _read("plugin", ".claude-plugin", "plugin.json"))["description"]
    readme = _read("README.md")
    for name in sorted(skills):
        if name not in description:
            out.append(f"skill `{name}` ships but plugin.json's description omits it")
        if f"`{name}`" not in readme:
            out.append(f"skill `{name}` ships but the README omits it")
    return out


def check_report_slots() -> list:
    """The §2 report form and the gate that validates it must agree:
    every REQUIRED_SLOTS letter is listed in the form, and the form
    lists nothing beyond the required set except the documented
    execution-tail extra."""
    out = []
    forms = _read("plugin", "skills", "dispatch", "references", "forms.md")
    section2 = forms.split("## 3.")[0]
    listed = set(re.findall(r"^  \(([a-h])\)", section2, re.M))

    gate = _read("plugin", "hooks", "report-form-gate.py")
    required = set(re.search(r'REQUIRED_SLOTS = set\("([a-z]+)"\)',
                             gate).group(1))
    tail_only = {"h"}   # documented in forms.md as execution-tail only

    for slot in sorted(required - listed):
        out.append(f"report-form-gate requires slot ({slot}) but forms.md §2 "
                   f"does not list it")
    for slot in sorted(listed - required - tail_only):
        out.append(f"forms.md §2 lists slot ({slot}) that the gate neither "
                   f"requires nor documents as tail-only")
    return out


def check_config_schema() -> list:
    """Every policy key the guards actually read is documented in the
    README, and vice versa."""
    out = []
    common = _read("plugin", "hooks", "_dispatch_common.py")
    block = common.split("_DEFAULTS: dict = ", 1)[1]
    depth = 0
    for i, ch in enumerate(block):
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                block = block[:i + 1]
                break
    keys = set(ast.literal_eval(block))
    if not keys:                      # instrument sanity: a pattern that
        out.append("check_config_schema found NO keys — parser broken, "
                   "not a clean result")
        return out
    documented = set(re.findall(r"^- `([a-z_]+)`", _read("README.md"), re.M))
    for key in sorted(keys - documented):
        out.append(f"policy key `{key}` is read by the guards but undocumented "
                   f"in the README")
    for key in sorted(documented - keys):
        out.append(f"README documents policy key `{key}` that no guard reads")
    return out


CHECKS = (
    ("guard roster", check_guards),
    ("skills", check_skills),
    ("report-form slots", check_report_slots),
    ("config schema", check_config_schema),
)


def main() -> int:
    failures = 0
    for label, fn in CHECKS:
        findings = fn()
        if findings:
            failures += len(findings)
            print(f"[DRIFT] {label}:")
            for f in findings:
                print(f"   - {f}")
        else:
            print(f"[ok]    {label}")
    if failures:
        print(f"\n{failures} drift(s). Doc and mechanism disagree; fix the "
              f"side that is wrong — both are shipped.")
        return 1
    print("\nno drift: prose and mechanism name the same things.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
