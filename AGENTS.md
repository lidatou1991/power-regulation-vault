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

