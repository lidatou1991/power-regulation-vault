---
title: Source Intake Workflow
country: unknown
jurisdiction: unknown
regulator: unknown
topic: source intake governance
status: current
source_type: internal_governance
source: "[[AGENTS]]"
publication_date: 2026-08-14
effective_date: 2026-08-14
last_verified: 2026-08-14
verified_through: 2026-08-14
superseding_check: completed
confidence: high
---

# Source Intake Workflow

This workflow governs process, not regulatory substance. It keeps newly discovered material separate from verified knowledge.

```text
SOURCE DISCOVERY
       ↓
SOURCE INTAKE
       ↓
CHANGE CANDIDATE
       ↓
HUMAN REVIEW
       ↓
KNOWLEDGE UPDATE
```

## Lifecycle

```text
NEW
 ↓
TRIAGED
 ↓
SOURCE VERIFIED
 ↓
CHANGE IMPACT ASSESSED
 ↓
HUMAN REVIEW
 ↓
APPROVED / REJECTED
 ↓
KNOWLEDGE UPDATE (only for an approved, precisely scoped change)
```

1. **New:** Create a Source Intake record from `09_Templates/source_intake.md`. Preserve the discovered item in the appropriate inbox channel without treating it as knowledge.
2. **Triaged:** Check minimum metadata, duplicates, scope, and whether the item is plausibly authoritative or relevant.
3. **Source verified:** Verify document identity, provenance, authority, publication date, effective date, and completeness. Record unknowns; do not infer them.
4. **Change impact assessed:** Compare the source with existing claims. Set `potential_current_impact`; create a Change Candidate from `09_Templates/change_candidate.md` when a possible change needs review.
5. **Human review:** Apply the Human Review Gate in `[[AGENTS]]`, including later-authority, enactment-chain when relevant, transitional, and conflict checks.
6. **Approved or rejected:** Record the explicit human decision and rationale. Rejected records remain traceable and are not silently deleted.
7. **Knowledge update:** Only an explicitly approved Change Candidate may authorize a scoped edit. Preserve historical rules, update timelines when useful, and add the required change log.

## Non-Automation Rule

Approval of a source does not automatically mean that every statement in the source becomes `current` knowledge. Source approval establishes that the source may be used; claim-level conclusions still require evidence, temporal classification, conflict assessment, a Change Candidate, and explicit human approval.

No discovery or intake process may directly edit a `current` regulatory conclusion.

## Inbox Behavior

- `00_Inbox/pdf/`: manually supplied PDF documents awaiting intake.
- `00_Inbox/web/`: manually recorded web-source material awaiting intake; this is not authorization to fetch or scrape.
- `00_Inbox/manual/`: manually entered citations, observations, or source leads.
- `00_Inbox/processed/`: items whose intake disposition has been recorded. Moving an item here does not approve its content.
- `00_Inbox/rejected/`: items rejected during triage or review, retained for traceability with a rationale.

Do not move existing source files. `01_Sources/` remains separate from the inbox and stores original material or notes describing original material.
