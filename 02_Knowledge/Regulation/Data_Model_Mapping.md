---
title: Data Model Mapping
country: global
jurisdiction: project
regulator: unknown
topic: knowledge data model
status: current
source_type: internal_project_document
source: "[[Data Model Mapping]]"
publication_date: 2026-08-14
effective_date: 2026-08-14
last_verified: 2026-08-14
confidence: high
knowledge_id: GLOBAL-KM-DATA-MODEL-MAPPING
publication_status: internal
audience: internal
publishable: "no"
knowledge_version: 1
review_status: internal
---

# Data Model Mapping

This is a migration map, not a database design or implementation. Markdown files and Git remain canonical.

| Future entity | Current Markdown representation | Major fields |
|---|---|---|
| `KnowledgeNote` | `02_Knowledge/`, `03_Entities/`, `04_Topics/` | `knowledge_id`, title, country, jurisdiction, regulator, topic, legal `status`, source references, effective dates, verification fields, confidence, summary/body, `knowledge_version` |
| `Source` | `01_Sources/` and Source Intake records | `source_id`, title, institution, document type/number, dates, URL/local file, language, authority/legal status, relationships, rights and display fields |
| `Entity` | `03_Entities/` | stable ID, name, country, entity type, aliases, relationships, source references |
| `Topic` | `04_Topics/` and Wiki Links | stable ID, name, domain, country, related topics and knowledge notes |
| `ChangeCandidate` | `09_Templates/change_candidate.md` instances | `candidate_id`, `source_id`, affected topics, old/new claim, change type, evidence, conflicts, verification checks, recommendation, review status |
| `RegulatoryChange` | `07_ChangeLog/` | date, topic, country, old rule, new rule, reason, source, impact, linked knowledge/change candidate |
| `Review` | review fields and checklist | reviewed object ID/type, reviewer, reviewed date, decision/status, rationale, checklist results |
| `Publication` | optional knowledge frontmatter | `knowledge_id`, publication status, audience, publishable flag, valid interval, publication date, version, rights decision |

## Relationship Expectations

- A `KnowledgeNote` cites one or more `Source` records.
- A `Source` may support many knowledge notes and Change Candidates.
- A `ChangeCandidate` must precede a human-approved change to a `current` claim.
- A `RegulatoryChange` preserves the audit record after an approved material change.
- A `Review` applies only to the identified object and version.
- A `Publication` can exist only for reviewed knowledge and must retain sources and verification dates.
- Entities and Topics connect through stable IDs or current Obsidian Wiki Links until export.

Blank optional fields map to null/unset values. YAML lists map to relationships. Markdown section bodies map to structured content fields only when an exporter can preserve their meaning and provenance. Git history remains the editorial audit trail even after a future export.

## Related Topics

- [[Publishing Model]]
- [[Source Intake Workflow]]
