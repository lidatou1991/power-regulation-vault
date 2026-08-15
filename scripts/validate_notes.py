#!/usr/bin/env python3
"""Warn when formal knowledge notes omit required frontmatter fields."""

from __future__ import annotations

import argparse
from pathlib import Path

REQUIRED_FIELDS = ("title", "country", "status", "source_type", "last_verified", "confidence")
KNOWLEDGE_DIRS = ("02_Knowledge", "03_Entities", "04_Topics")


def parse_frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields


def validate(root: Path) -> list[str]:
    warnings: list[str] = []
    for dirname in KNOWLEDGE_DIRS:
        directory = root / dirname
        if not directory.exists():
            continue
        for path in sorted(directory.rglob("*.md")):
            fields = parse_frontmatter(path)
            missing = [field for field in REQUIRED_FIELDS if not fields.get(field)]
            if missing:
                warnings.append(f"WARNING {path.relative_to(root)}: missing {', '.join(missing)}")
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    warnings = validate(args.root.resolve())
    for warning in warnings:
        print(warning)
    print(f"Scanned formal knowledge notes: {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

