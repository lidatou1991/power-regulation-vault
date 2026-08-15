---
title: Publishing Model
country: global
jurisdiction: project
regulator: unknown
topic: knowledge publishing
status: current
source_type: internal_project_document
source: "[[Publishing Model]]"
publication_date: 2026-08-14
effective_date: 2026-08-14
last_verified: 2026-08-14
confidence: high
knowledge_id: GLOBAL-KM-PUBLISHING-MODEL
publication_status: internal
audience: internal
publishable: "no"
knowledge_version: 1
review_status: internal
---

# Publishing Model

Markdown and Git remain the canonical, human-readable editorial and audit layer. Publication metadata describes a possible downstream use; it does not replace files, Git history, manual review, source traceability, temporal status, research gaps, or change logs.

## Publishable Knowledge

```text
Raw Source
↓
Source Intake
↓
Knowledge Analysis
↓
Change Candidate
↓
Human Review
↓
Approved Knowledge
↓
Published Knowledge
↓
Subscriber Product
```

The product must never expose draft or Change Candidate content as verified `current` knowledge. Human approval is an explicit gate between analysis and approved knowledge. Publication is a later decision governed by audience, rights, quality, and publication status.

## Legal Status and Editorial Status

`status` records legal or regulatory status: `current`, `historical`, `transitional`, `proposed`, `repealed`, or `unknown`. `publication_status` records editorial workflow: `internal`, `review`, `approved`, `published`, or `archived`.

These axes are independent. For example:

```yaml
status: current
publication_status: internal
```

This means the regulatory conclusion is believed current under the required verification process, but has not been approved for subscriber publication. Neither `approved` nor `published` changes the legal status.

## Optional Publishing Metadata

- `knowledge_id`: stable human-readable identifier.
- `publication_status`: editorial workflow state.
- `audience`: `internal`, `subscriber`, or `both`.
- `publishable`: `yes`, `no`, or `conditional`.
- `valid_from` / `valid_to`: applicability interval when supported by evidence.
- `published_at`: publication timestamp or date.
- `knowledge_version`: editorial version of the knowledge object.
- `review_status`, `reviewed_by`, `reviewed_at`: human-review record.

These fields are optional for backward compatibility. Unknown facts must not be guessed. A future exporter may treat missing values as unset, not approved.

## Stable Knowledge ID Convention

Use uppercase hyphen-separated identifiers:

`{COUNTRY}-{DOMAIN}-{SUBJECT}`

- `COUNTRY`: ISO 3166-1 alpha-3 code, or `GLOBAL` for project-wide concepts.
- `DOMAIN`: stable short code such as `DIST`, `GEN`, `TRANS`, `MARKET`, `REG`, or `KM`.
- `SUBJECT`: concise stable topic or entity slug; add a regulator segment where it prevents ambiguity.

Examples: `CHL-DIST-VAD`, `CHL-DIST-EMPRESA-MODELO`, `BRA-DIST-PARCELA-A`, and `BRA-REG-ANEEL-PRORET`.

Assign one ID to one knowledge concept. Keep it unchanged when a title, filename, legal status, or publication state changes. Do not reuse retired IDs or use a random UUID as the primary public identifier. If concepts split, retain the original for the continuing concept and assign new documented IDs to newly distinct concepts.

## Product-Facing Sections

New notes may use `Executive Summary`, `Current Rule`, `Why It Matters`, `Regulatory Timeline`, `Sources`, `Related Topics`, and `Open Questions`. The executive summary should be publication-ready in tone but remains internal until approved. Business impact must be evidence-based and must not overstate legal or commercial implications.

## Source Rights

Source records may use `rights_class` (`public_official`, `internal`, `licensed`, `copyrighted_reference`, `unknown`) and `display_policy` (`full_text_allowed`, `excerpt_only`, `citation_only`, `internal_only`, `unknown`), plus `redistribution_allowed` and `citation_required`. These fields record a later review; they do not constitute copyright analysis. `unknown` blocks an assumption that public display is allowed.

## Personal-Use Compatibility

Personal use continues without a product layer: open the repository, browse and search Markdown, use Obsidian later, add sources manually, read conclusions, and inspect timelines. Publishing fields are optional annotations and must not become prerequisites for ordinary internal editing.

## Related Topics

- [[Source Intake Workflow]]
- [[Data Model Mapping]]
