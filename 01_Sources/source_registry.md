---
title: Source Registry
registry_version: 1
last_updated: 2026-08-14
---

# Source Registry

The registry is an index of Source Intake records, not a substitute for original sources or verified knowledge. v0.4.1 defines its structure only; existing sources are not backfilled.

## Registry Fields

| Field | Purpose |
|---|---|
| `source_id` | Stable link to the intake record |
| `title` | Human-readable document title |
| `country` | Country scope |
| `institution` | Issuing or publishing institution |
| `document_type` / `document_number` | Document identity |
| `official_url` / `local_file` | Provenance and stored location |
| `publication_date` / `effective_date` | Temporal context |
| `retrieval_date` / `verified_through` | Retrieval and verification cutoff |
| `legal_status` / `authority_level` | Legal posture and source hierarchy |
| `related_topics` | Topics potentially affected |
| `review_status` | Human-review state |
| `change_candidates` | IDs or links to generated Change Candidates |
| `disposition` | Active, processed, rejected, or unknown |

## Entries

| Source ID | Title | Country | Institution | Type / Number | Publication / Effective | Location / Origin | Verified Through | Legal Status / Authority | Related Topics | Review Status | Change Candidates | Disposition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

Add entries only when a Source Intake record exists. Link the `source_id` to that record, preserve `unknown` values, and never treat registry presence as approval or as proof that a proposition is `current`.
