# Project Instructions

These rules govern every contribution to the Power Regulation Living Knowledge Base.

## 1. Source First

Every regulatory conclusion must cite a source. Never write a regulatory conclusion from model memory alone. Prefer sources in this order:

1. Laws and formally enacted regulations
2. Official documents from governments, regulators, and system operators
3. Official technical reports
4. Official consultation documents
5. Academic books and papers
6. Industry research reports
7. News media

News may identify a policy change, but it must not be the sole authority for a legal conclusion when a formal regulation or official document exists.

## 2. Temporal Awareness

Classify regulatory conclusions as `current`, `historical`, `proposed`, `repealed`, `transitional`, or `unknown`. Never overwrite an old conclusion when a rule changes. Preserve it with `status: historical`, add the replacement with `status: current`, and create a timeline when useful.

## 3. No Silent Correction

When sources conflict, preserve both sources. Create a conflict note that describes the disagreement and marks it for further verification. Never silently choose one source and delete the other.

## 4. Traceability

Every formal knowledge note must record at least:

```yaml
country:
jurisdiction:
regulator:
topic:
status:
source_type:
source:
publication_date:
effective_date:
last_verified:
confidence:
```

Use `unknown` for unknown values. Do not infer or guess them.

## 5. Atomic Knowledge

Prefer focused, atomic notes over a single long summary of an entire source. Examples include `VAD.md`, `Empresa_Modelo.md`, `Parcela_A.md`, `RTP.md`, and `PRORET.md`. Connect notes with Obsidian Wiki Links such as `[[VAD]]`, `[[Empresa Modelo]]`, and `[[ANEEL]]`.

## 6. Separate Sources from Knowledge

`01_Sources/` stores original material and notes describing original material. `02_Knowledge/` and `04_Topics/` store analyzed and verified knowledge cards. Entity knowledge lives in `03_Entities/`. Never present an AI-generated summary as an original source.

## 7. Change Log

For every material change to a regulatory knowledge node, add a record under `07_ChangeLog/` containing `date`, `topic`, `country`, `old_rule`, `new_rule`, `reason`, `source`, and `impact`.

## 8. Research Gaps

Never fabricate missing knowledge. Add unresolved questions as checkboxes in `08_Research_Gaps/Research_Gaps.md`. When new material arrives, check whether it closes an existing gap.

## 9. v0.1 Boundaries

Do not install Obsidian, call external APIs, create embeddings or vector databases, build RAG or chatbots, scrape websites, download PDFs automatically, or generate unsourced regulatory claims. v0.1 is only a reliable, extensible, traceable, time-aware Markdown scaffold.

## 10. Mandatory CURRENT-Claim Verification

Before marking a regulatory conclusion `current`, complete this pipeline:

```text
Source Authority Check
↓
Effective Date Check
↓
Latest Amendment Check
↓
Superseding Law Check
↓
Transitional Provision Check
↓
Cross-source Conflict Check
↓
CURRENT conclusion
```

A statement must not be marked `current` merely because it comes from an official source, is the latest source stored in the vault, remains displayed on a regulator webpage, or encountered no contradiction during the first search. Search actively and reverse chronologically for later authority through the stated verification cutoff. Distinguish enactment, publication, and effective date from parliamentary approval or official announcements about a bill.

## 11. Negative Verification

Important CURRENT conclusions must record the date through which later amendments and superseding or transitional rules were checked. Use:

```yaml
verified_through: YYYY-MM-DD
superseding_check: completed
```

Use `superseding_check: incomplete` when the later-authority search is unfinished, and do not present the conclusion as definitively current. Preserve the searched sources and any conflict between a legacy administrative label and later legal effect.

## 12. Enactment-Chain Verification

For regulatory propositions based on pending or recently approved legislation, do not assign `current` status solely from a parliamentary or project-status page. Where relevant, verify the complete chain:

```text
Bill / Boletín
↓
Congressional approval
↓
Presidential promulgation
↓
Diario Oficial publication
↓
Assigned law number
↓
Effective date
↓
Final enacted text
```

If a parliamentary workflow page remains stale after the Diario Oficial has published the law, the published law controls. Record the stale workflow metadata and the published enactment as a source conflict; never silently ignore or delete the stale official record. Use `enactment_check: completed` for a CURRENT conclusion when this chain is relevant and has been verified. The field is optional where no legislative enactment chain is relevant.

## 13. Human Review Gate

No source intake or automated discovery process may directly alter a `current` regulatory claim. Source discovery, source intake, Change Candidate creation, human review, and knowledge updates are separate stages.

A `current` claim may be changed only after all of the following have been completed:

1. authoritative source verification;
2. effective-date verification;
3. superseding-law check;
4. enactment-chain verification when relevant;
5. conflict assessment;
6. creation of a Change Candidate; and
7. explicit human approval.

Approval applies to the reviewed source or Change Candidate only. It does not automatically make every statement in a source `current` knowledge.

## 14. Publication Trust Boundary

Personal/internal knowledge and published subscriber knowledge are different trust levels. `status: current` describes the assessed legal or regulatory state; it does not make a note publishable. Publication requires explicit human approval and the publication checklist.

Published knowledge must retain source traceability and its verification cutoff. Commercial or public display must follow the source's recorded rights metadata; missing or `unknown` rights metadata requires review, not a legal assumption. Future product interfaces must never expose unpublished internal notes, drafts, Source Intake records, or Change Candidates as verified subscriber knowledge.
