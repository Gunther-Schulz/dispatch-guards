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

Run: python3 tools/check-doc-drift.py
Exit codes: 0 clean, 1 drift found, 2 a check COULD NOT VERIFY (its
input was missing, unreadable, or carried no anchor to compare — the
third answer; a check that compared nothing never prints `[ok]`).
Consumers: the repo CLAUDE.md verify block, and any release.

NOT covered, deliberately: whether the prose is CORRECT, only whether
both sides name the same things. A row describing a guard wrongly
passes here and is a review question, not a computable one.
"""
from __future__ import annotations

import ast
import glob
import importlib.util
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class CouldNotVerify(Exception):
    """A check could not READ what it compares.

    Distinct from a finding: a finding says the two sides disagree, this
    says nothing was compared. Both are non-zero exits, because "0
    compared" printed as `[ok]` is the could-not-verify lie the
    three-answers rule forbids — the check has to NAME what is missing.
    """


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


_HOOK_REL = ("plugin", "hooks", "brief-reminder.py")
_FORMS_REL = ("plugin", "skills", "dispatch", "references", "forms.md")
_EXEC_TAIL_HEADING = "EXECUTION tail (any dispatch that writes):"
_CHANNEL_PLACEHOLDER = "<channel line>"
_BG_CHANNEL_RE = re.compile(r"^- named \(mailbox teammate\): `([^`]+)`",
                            re.M)
_UNNAMED_CHANNEL_RE = re.compile(
    r"^- unnamed \(background task\): `([^`]+)`", re.M | re.S)


def _brief_reminder() -> object:
    """brief-reminder.py imported by path (the hyphen rules out a plain
    import). The check borrows the hook's OWN `_norm` rather than
    copying it: a second copy of the normalization is precisely the
    duplication this tool exists to catch."""
    path = os.path.join(ROOT, *_HOOK_REL)
    spec = importlib.util.spec_from_file_location("_brief_reminder", path)
    if spec is None or spec.loader is None:
        raise CouldNotVerify(f"{os.path.join(*_HOOK_REL)} is not importable")
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except Exception as exc:                       # noqa: BLE001
        raise CouldNotVerify(
            f"{os.path.join(*_HOOK_REL)} failed to import: {exc}") from exc
    if not hasattr(module, "_norm"):
        raise CouldNotVerify(
            f"{os.path.join(*_HOOK_REL)} no longer defines `_norm`, the "
            f"normalization this comparison is defined in terms of")
    return module


def _string_literal(source: str, name: str, where: str) -> str:
    """The value of a module-level-or-nested `<name> = "…"` assignment,
    read with ast — the fixture lives inside `if __name__ ==
    "__main__"`, so it cannot be reached by importing."""
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        raise CouldNotVerify(f"{where} does not parse: {exc}") from exc
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        if not any(isinstance(t, ast.Name) and t.id == name
                   for t in node.targets):
            continue
        try:
            value = ast.literal_eval(node.value)
        except (ValueError, SyntaxError) as exc:
            raise CouldNotVerify(
                f"`{name}` in {where} is not a literal string: {exc}"
            ) from exc
        if not isinstance(value, str):
            raise CouldNotVerify(f"`{name}` in {where} is not a string")
        return value
    raise CouldNotVerify(f"{where} contains no `{name}` assignment")


def _forms_execution_tail(forms: str) -> str:
    """The indented EXECUTION tail block from forms.md §2, dedented."""
    if _EXEC_TAIL_HEADING not in forms:
        raise CouldNotVerify(
            f"forms.md carries no \"{_EXEC_TAIL_HEADING}\" heading — "
            f"nothing was compared")
    after = forms.split(_EXEC_TAIL_HEADING, 1)[1]
    block: list[str] = []
    for line in after.splitlines():
        if not line.strip():
            if block:
                break
            continue
        if not line.startswith("    "):
            break
        block.append(line[4:])
    if not block:
        raise CouldNotVerify(
            "the EXECUTION tail heading in forms.md is followed by no "
            "indented block — nothing was compared")
    return "\n".join(block)


def check_execution_tail_fixture() -> list:
    """brief-reminder's EXECUTION_TAIL_BG fixture still says what the §2
    EXECUTION tail says.

    The fixture is a deliberate INDEPENDENT COPY (so the hook's bites do
    not share parentage with the constants they test), and an
    independent copy of a moving text is a frozen fixture: on
    2026-08-10 it had drifted four ways — it still promised a report
    FILE the harness has blocked since 2026-08-01, lacked the
    await-a-backgrounded-check and never-amend clauses, and taught
    `git add <paths>`, the very form §2 now prohibits. Green bites
    against a shape the real form no longer produces catch no tail
    regression at all.

    The grain is NORMALIZED TEXT — brief-reminder's own `_norm`, i.e.
    whitespace-insensitive. Not a line comparison: the two copies are
    independently wrapped (5 literal lines vs 33 in forms.md), so a
    line-sequence check could never go green whatever either file
    said, and the same normalization is what the hook itself matches
    with (its 2026-07-30 hard-wrap false fire).
    """
    out = []
    forms = _read(*_FORMS_REL)
    tail = _forms_execution_tail(forms)
    if _CHANNEL_PLACEHOLDER not in tail:
        raise CouldNotVerify(
            f"the EXECUTION tail in forms.md carries no "
            f"`{_CHANNEL_PLACEHOLDER}` placeholder — the fixture's "
            f"channel line has nothing to be compared against")
    channel = _BG_CHANNEL_RE.search(forms)
    if channel is None:
        raise CouldNotVerify(
            "forms.md §2 names no `- named (mailbox teammate):` "
            "channel line — the substitution has no source")
    expected = tail.replace(_CHANNEL_PLACEHOLDER, channel.group(1))
    fixture = _string_literal(_read(*_HOOK_REL), "EXECUTION_TAIL_BG",
                              os.path.join(*_HOOK_REL))
    norm = _brief_reminder()._norm
    want, got = norm(expected), norm(fixture)
    if want != got:
        i = len(os.path.commonprefix([want, got]))
        out.append(
            "brief-reminder's EXECUTION_TAIL_BG fixture no longer "
            "matches the §2 EXECUTION tail in forms.md (background "
            "channel line substituted); first divergence at "
            f"normalized char {i}:\n"
            f"       forms.md: …{want[max(0, i - 40):i + 60]!r}\n"
            f"       fixture:  …{got[max(0, i - 40):i + 60]!r}")
    return out



def check_channel_line_markers() -> list:
    """Each §2 channel line must contain the marker the hook matches it
    by — otherwise the guard classifies a correctly-pasted tail as the
    wrong lane, or fails to classify it at all.

    This is the consistency question a fresh-context reviewer would
    ask, made mechanical: forms.md and brief-reminder are two homes of
    ONE rule, and the marker constants are the only place they touch.
    Both sides are read from their OWN home — the lines from forms.md,
    the markers from the hook's module — so the comparison is not
    vacuous the way deriving one from the other would be.
    """
    out = []
    forms = _read(*_FORMS_REL)
    hook = _brief_reminder()
    named = _BG_CHANNEL_RE.search(forms)
    unnamed = _UNNAMED_CHANNEL_RE.search(forms)
    if named is None or unnamed is None:
        raise CouldNotVerify(
            "forms.md §2 does not name both channel lines "
            "(`- named (mailbox teammate):` / `- unnamed (background "
            "task):`) — there is nothing to compare the hook's "
            "markers against")
    norm = hook._norm
    pairs = (("named/mailbox", named.group(1), hook._MAILBOX_TAIL_MARKER),
             ("unnamed/background task", unnamed.group(1),
              hook._DELIVERED_TAIL_MARKER))
    for lane, line, marker in pairs:
        if marker not in norm(line):
            out.append(
                f"forms.md's {lane} channel line does not contain the "
                f"marker brief-reminder matches it by: line is "
                f"{norm(line)!r}, marker is {marker!r} — a tail pasted "
                f"verbatim from §2 would be read as the wrong lane")
    # the markers must also tell the two lanes APART: a marker that
    # matches both lines classifies nothing.
    if hook._MAILBOX_TAIL_MARKER in norm(unnamed.group(1)):
        out.append("the mailbox marker also matches the unnamed lane's "
                   "channel line — the two lanes are indistinguishable")
    if hook._DELIVERED_TAIL_MARKER in norm(named.group(1)):
        out.append("the background-task marker also matches the named "
                   "lane's channel line — the two lanes are "
                   "indistinguishable")
    return out


CHECKS = (
    ("guard roster", check_guards),
    ("skills", check_skills),
    ("report-form slots", check_report_slots),
    ("config schema", check_config_schema),
    ("EXECUTION tail fixture", check_execution_tail_fixture),
    ("channel-line markers", check_channel_line_markers),
)


def main() -> int:
    failures = 0
    unverified = 0
    for label, fn in CHECKS:
        # A check whose input is missing, unreadable, or anchorless
        # compared NOTHING. That is neither a pass nor a drift, and it
        # must never print like a clean run: it reports could-not-verify
        # and names what is missing (exit 2).
        try:
            findings = fn()
        except CouldNotVerify as exc:
            unverified += 1
            print(f"[?????] {label}: COULD NOT VERIFY — {exc}")
            continue
        except OSError as exc:
            unverified += 1
            print(f"[?????] {label}: COULD NOT VERIFY — unreadable input: "
                  f"{exc}")
            continue
        if findings:
            failures += len(findings)
            print(f"[DRIFT] {label}:")
            for f in findings:
                print(f"   - {f}")
        else:
            print(f"[ok]    {label}")
    if unverified:
        print(f"\n{unverified} check(s) COULD NOT VERIFY — named above. A "
              f"check that compared nothing is not a clean run; restore "
              f"the missing input or repair the check.")
    if failures:
        print(f"\n{failures} drift(s). Doc and mechanism disagree; fix the "
              f"side that is wrong — both are shipped.")
        return 1
    if unverified:
        return 2
    print("\nno drift: prose and mechanism name the same things.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
