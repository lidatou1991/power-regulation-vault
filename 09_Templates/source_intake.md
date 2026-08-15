---
source_id:
title:
country:
jurisdiction:
institution:
document_type:
document_number:
publication_date:
effective_date:
retrieval_date:
official_url:
local_file:
language:
status:
legal_status:
authority_level:
verified_through:
supersedes: []
amends: []
related_sources: []
related_topics: []
potential_current_impact: unknown
review_status: new
rights_class:
display_policy:
redistribution_allowed:
citation_required:
---

# Source Intake

> Intake metadata is a review record, not regulatory knowledge. Do not use it to modify a `current` claim directly.

## Controlled Values

- `status`: `current`, `historical`, `proposed`, `repealed`, `transitional`, or `unknown`
- `legal_status`: `enacted`, `effective`, `proposed`, `repealed`, `superseded`, `transitional`, or `unknown`
- `authority_level`: `legislation`, `regulation`, `regulator_decision`, `official_guidance`, `official_report`, `academic`, `industry`, or `media`
- `potential_current_impact`: `yes`, `no`, or `unknown`
- `review_status`: `new`, `triaged`, `requires_review`, `approved`, or `rejected`
- `rights_class`: `public_official`, `internal`, `licensed`, `copyrighted_reference`, or `unknown`
- `display_policy`: `full_text_allowed`, `excerpt_only`, `citation_only`, `internal_only`, or `unknown`
- `redistribution_allowed` and `citation_required`: record the reviewed value; use `unknown` rather than interpreting copyright
- Dates: ISO `YYYY-MM-DD`, or `unknown`
- Relationships: YAML lists of `source_id` values; topics should use Obsidian Wiki Links where possible

## Source ID Convention

Use an uppercase, hyphen-separated identifier:

`{COUNTRY}-{INSTITUTION}-{DOCUMENT_TYPE}-{DOCUMENT_NUMBER}-{PUBLICATION_YEAR}`

- `COUNTRY`: ISO 3166-1 alpha-3 code.
- `INSTITUTION`: stable official acronym or short code.
- `DOCUMENT_TYPE`: stable short code such as `LAW`, `DEC`, `RES`, `REG`, `PRORET`, or `REPORT`.
- `DOCUMENT_NUMBER`: normalized official identifier with spaces and punctuation replaced by hyphens. Omit only when the source has no official number; then use a short, stable title slug.
- `PUBLICATION_YEAR`: four-digit year from `publication_date`; use `UNKNOWN` when the date is unknown.

Examples of form only: `CHL-BCN-LAW-21833-2026`, `BRA-ANEEL-PRORET-M08-2025`. If two records would collide, add a deterministic distinguishing segment derived from the official document identifier; do not use a random UUID as the primary identifier. Once assigned, a `source_id` must not change merely because metadata or legal status changes.

## Discovery Context

Record how the source was found and why it may be relevant. Do not add unverified regulatory conclusions.

## Verification Notes

Record authority, identity, date, provenance, and completeness checks. Use `unknown` rather than guessing.

## Potential Impact

Describe only the issue requiring assessment. If impact may exist, create a separate Change Candidate before any knowledge update.

## Review Record

Record reviewer, review date, decision, and rationale when human review occurs.
