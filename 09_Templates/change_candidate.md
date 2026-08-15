---
candidate_id:
source_id:
country:
detected_date:
affected_topics: []
existing_current_claim:
candidate_new_claim:
change_type: unknown
confidence:
evidence: []
conflicting_sources: []
superseding_check: incomplete
enactment_check: not_applicable
recommended_action:
review_status: new
---

# Change Candidate

> A Change Candidate is a review object. It does not modify a knowledge note or establish a `current` claim.

## Controlled Values

- `change_type`: `amendment`, `superseding_rule`, `new_rule`, `transitional_exception`, `repeal`, `implementation_detail`, `clarification`, `no_change`, or `unknown`
- `superseding_check`: `completed` or `incomplete`
- `enactment_check`: `completed`, `incomplete`, or `not_applicable`
- `review_status`: `new`, `triaged`, `requires_review`, `approved`, or `rejected`
- `confidence`: `high`, `medium`, `low`, or `unknown`
- `source_id`: the originating Source Intake identifier
- `evidence` and `conflicting_sources`: YAML lists of source IDs or precise source references

## Existing Current Claim

Quote or precisely identify the existing claim and link its knowledge note. Do not edit it here.

## Candidate New Claim

State the proposed change narrowly and preserve temporal qualifications.

## Evidence and Conflict Assessment

Document authoritative support, effective dates, later-authority searches, transitional provisions, and every conflicting source.

## Review Decision

Record reviewer, date, approval or rejection, rationale, and the exact authorized follow-up. Approval of this object is required before a `current` claim is changed, but does not make unrelated source statements current.
