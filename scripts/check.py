#!/usr/bin/env python3
"""Check skill metadata, local links, and the public file tree using only stdlib."""

import json
import os
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
WORDS = (
    "ad" + "itya", "sh" + "eth", "ez" + r" ?money", "itsez" + "money",
    "coo" + "kunity", "juice" + "box", "good" + "labs", "code" + "words",
    "age" + "mo", "screen" + r" ?print", r"\bs" + r"pi\b", "ba" + "bish",
    "de" + "vang", "rh" + "iz", "her" + "mes", "jar" + "vis",
    "open" + "claw", "com" + "posio", "wind" + "sor", "pipe" + "board",
    r"\bli" + r"near\b", "claw" + "mem", "va" + "ult",
    r"\bad" + r"v-?\d+\b", r"\be" + r"z-\d+\b",
    "/" + "Users/", "start" + "ups/", r"\.ag" + "ent/",
)
PRIVATE = re.compile("|".join(WORDS), re.IGNORECASE)
IDENTIFIERS = re.compile(
    r"\b\d{6,}\b|\b\d{3}-\d{3}-\d{4}\b|\b[CDGU](?=[A-Z0-9]*\d)[A-Z0-9]{8,}\b"
    r"|\b(?:GTM|G|AW|UA)-[A-Z0-9-]{6,}\b"
    r"|\b[0-9a-fA-F]{8}-(?:[0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}\b"
)
SECRETS = re.compile(
    r"\b(?:sk|ghp|gho|github_pat|xox[baprs])[-_][A-Za-z0-9_-]{16,}\b"
    r"|\bAK" + r"IA[0-9A-Z]{16}\b"
    r"|\bAI" + r"za[0-9A-Za-z_-]{35}\b"
    r"|\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\b"
    r"|-----BEGIN (?:[A-Z0-9 ]+ )?PRIVATE KEY-----"
)
INSTALL_URL = re.compile(
    r"https://(?:raw\.githubusercontent\.com|github\.com)/" + "ad" + "ityash8/"
    r"claude-seo-skills(?:\.git|/[^\s)`]+)?"
)


def public_files(errors):
    files = []
    for directory, dirs, names in os.walk(
        ROOT, followlinks=False, onerror=lambda error: errors.append(str(error))
    ):
        dirs[:] = [name for name in dirs if name != ".git"]
        names = [name for name in names if name != ".git"]
        for name in dirs[:] + names:
            path = Path(directory) / name
            relative = path.relative_to(ROOT)
            if PRIVATE.search(relative.as_posix()):
                errors.append(f"{relative}: private pattern in path")
            if path.is_symlink():
                errors.append(f"{relative}: symlinks are forbidden")
                if name in dirs:
                    dirs.remove(name)
            elif name in names:
                files.append(path)
    return sorted(files)


def scalar(value):
    value = value.strip()
    if not value or value[0] in ">|[{&*!":
        raise ValueError("must be a one-line string")
    if value.startswith('"'):
        value = json.loads(value)
    elif value.startswith("'"):
        if not re.fullmatch(r"'(?:[^']|'')*'", value):
            raise ValueError("invalid quoted string")
        value = value[1:-1].replace("''", "'")
    else:
        value = value.split(" #", 1)[0].strip()
        if value.lower() in {"null", "true", "false", "yes", "no", "on", "off", "~"} or re.match(r"[-+.]?\d|[+-]?\.?(?:inf|nan)$", value, re.I):
            raise ValueError("must be a string, not a YAML scalar type")
        if value.startswith("#") or ": " in value:
            raise ValueError("quote ambiguous YAML text")
    if not value or len(value.splitlines()) != 1 or any(ord(char) < 32 for char in value):
        raise ValueError("must be a nonempty one-line string")
    return value


def check_skill(path, content, errors):
    relative = path.relative_to(ROOT)
    lines = content.splitlines()
    if len(lines) > 250:
        errors.append(f"{relative}: exceeds 250 lines")
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        errors.append(f"{relative}: missing YAML frontmatter")
        return
    fields = {}
    header = lines[1:lines[1:].index("---") + 1]
    for index, line in enumerate(header):
        match = re.match(r"^(name|description):\s*(.*)$", line)
        if not match:
            continue
        key, value = match.groups()
        try:
            if key in fields:
                raise ValueError("duplicate field")
            fields[key] = scalar(value)
            following = next((item for item in header[index + 1:] if item.strip()), "")
            if following.startswith((" ", "\t")):
                raise ValueError("multiline field")
        except ValueError as error:
            errors.append(f"{relative}: {key}: {error}")
    if fields.get("name") != path.parent.name:
        errors.append(f"{relative}: name must match folder")
    description = fields.get("description", "")
    if not description or len(description) > 200:
        errors.append(f"{relative}: description must be 1 to 200 characters")


def main():
    errors = []
    files = public_files(errors)
    skills = 0
    for path in files:
        relative = path.relative_to(ROOT)
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            errors.append(f"{relative}: cannot scan as UTF-8: {error}")
            continue
        for number, line in enumerate(content.splitlines(), 1):
            candidate = line
            if relative == Path("README.md"):
                candidate = INSTALL_URL.sub(
                    lambda match: match.group().replace("ad" + "ityash8", "example-user", 1), line
                )
            if PRIVATE.search(candidate) or IDENTIFIERS.search(candidate) or SECRETS.search(candidate):
                errors.append(f"{relative}:{number}: private data or identifier pattern")
        if path.name == "SKILL.md" and relative.parts[:2] == (".claude", "skills") and len(relative.parts) == 4:
            skills += 1
            check_skill(path, content, errors)
        if path.suffix == ".md":
            definitions = dict(re.findall(r"(?m)^ {0,3}\[([^\]]+)\]:\s*<?([^\s>]+)>?", content))
            definitions = {key.casefold(): value for key, value in definitions.items()}
            for label, reference in re.findall(r"\[([^\]]+)\]\[([^\]]*)\]", content):
                if (reference or label).casefold() not in definitions:
                    errors.append(f"{relative}: undefined reference link: {reference or label}")
            targets = re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", content) + list(definitions.values())
            for target in targets:
                url = urlsplit(target)
                if url.scheme or url.netloc or not url.path or "{" in url.path:
                    continue
                destination = (path.parent / unquote(url.path)).resolve()
                if not destination.is_relative_to(ROOT) or not destination.exists():
                    errors.append(f"{relative}: broken or external local link: {target}")
    if not skills:
        errors.append("No skills found")
    if errors:
        print("FAIL")
        print("\n".join(errors))
        return 1
    print(f"PASS: {skills} skills; {len(files)} files; metadata, privacy, links, and symlinks checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
