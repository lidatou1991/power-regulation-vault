#!/usr/bin/env python3
"""Validate formal knowledge notes and, optionally, Source Intake records."""

from __future__ import annotations

import argparse
from pathlib import Path

REQUIRED_FIELDS = ("title", "country", "status", "source_type", "last_verified", "confidence")
KNOWLEDGE_DIRS = ("02_Knowledge", "03_Entities", "04_Topics")
KNOWLEDGE_OPTIONAL_CONTROLLED_VALUES = {
    "publication_status": {"internal", "review", "approved", "published", "archived"},
    "audience": {"internal", "subscriber", "both"},
    "publishable": {"yes", "no", "conditional"},
}
INTAKE_REQUIRED_FIELDS = (
    "source_id", "title", "country", "jurisdiction", "institution",
    "document_type", "publication_date", "retrieval_date", "official_url",
    "local_file", "language", "status", "legal_status", "authority_level",
    "verified_through", "potential_current_impact", "review_status",
)
INTAKE_CONTROLLED_VALUES = {
    "legal_status": {"enacted", "effective", "proposed", "repealed", "superseded", "transitional", "unknown"},
    "authority_level": {"legislation", "regulation", "regulator_decision", "official_guidance", "official_report", "academic", "industry", "media"},
    "potential_current_impact": {"yes", "no", "unknown"},
    "review_status": {"new", "triaged", "requires_review", "approved", "rejected"},
    "rights_class": {"public_official", "internal", "licensed", "copyrighted_reference", "unknown"},
    "display_policy": {"full_text_allowed", "excerpt_only", "citation_only", "internal_only", "unknown"},
}


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
            value = value.strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
                value = value[1:-1]
            fields[key.strip()] = value
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
            for field, allowed in KNOWLEDGE_OPTIONAL_CONTROLLED_VALUES.items():
                value = fields.get(field)
                if value and value not in allowed:
                    warnings.append(
                        f"WARNING {path.relative_to(root)}: invalid {field}={value!r}"
                    )
    return warnings


def validate_intake(root: Path) -> list[str]:
    """Validate Markdown records beneath 00_Inbox that declare source_id."""
    warnings: list[str] = []
    directory = root / "00_Inbox"
    if not directory.exists():
        return warnings
    for path in sorted(directory.rglob("*.md")):
        fields = parse_frontmatter(path)
        if "source_id" not in fields:
            continue
        missing = [field for field in INTAKE_REQUIRED_FIELDS if not fields.get(field)]
        if missing:
            warnings.append(f"WARNING {path.relative_to(root)}: missing {', '.join(missing)}")
        for field, allowed in INTAKE_CONTROLLED_VALUES.items():
            value = fields.get(field)
            if value and value not in allowed:
                warnings.append(
                    f"WARNING {path.relative_to(root)}: invalid {field}={value!r}"
                )
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument(
        "--intake", action="store_true",
        help="also validate Source Intake records beneath 00_Inbox",
    )
    args = parser.parse_args()
    warnings = validate(args.root.resolve())
    intake_warnings = validate_intake(args.root.resolve()) if args.intake else []
    for warning in warnings:
        print(warning)
    for warning in intake_warnings:
        print(warning)
    print(f"Scanned formal knowledge notes: {len(warnings)} warning(s)")
    if args.intake:
        print(f"Scanned source intake records: {len(intake_warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
