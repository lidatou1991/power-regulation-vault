#!/usr/bin/env python3
"""Report Obsidian Wiki Links that do not resolve to a Markdown note."""

from __future__ import annotations

import argparse
import re
import unicodedata
from pathlib import Path

LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")


def normalize(value: str) -> str:
    value = value.split("|", 1)[0].split("#", 1)[0].strip()
    value = unicodedata.normalize("NFKC", value).casefold()
    return re.sub(r"[\s_-]+", " ", value)


def note_names(path: Path) -> set[str]:
    names = {normalize(path.stem)}
    lines = path.read_text(encoding="utf-8").splitlines()
    if lines and lines[0].strip() == "---":
        for line in lines[1:]:
            if line.strip() == "---":
                break
            if line.startswith("title:"):
                title = line.split(":", 1)[1].strip().strip("\"'")
                if title:
                    names.add(normalize(title))
                break
    return names


def find_broken(root: Path) -> list[str]:
    markdown = [p for p in root.rglob("*.md") if ".git" not in p.parts and "09_Templates" not in p.parts]
    available: set[str] = set()
    for path in markdown:
        available.update(note_names(path))
    broken: list[str] = []
    for path in sorted(markdown):
        text = path.read_text(encoding="utf-8")
        for target in LINK_RE.findall(text):
            if normalize(target) not in available:
                broken.append(f"WARNING {path.relative_to(root)}: broken link [[{target}]]")
    return broken


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    broken = find_broken(args.root.resolve())
    for warning in broken:
        print(warning)
    print(f"Broken Wiki Links: {len(broken)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
