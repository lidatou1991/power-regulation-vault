# Power Regulation Living Knowledge Base

An Obsidian-compatible, source-first knowledge base designed to continuously absorb power-sector laws, regulatory documents, research, and policy changes while preserving history, traceability, and relationships between concepts.

## Version

Current version: **v0.4.2 — Product-Ready Knowledge Model**.

## Principles

- Every regulatory conclusion must be traceable to a source.
- Current, historical, proposed, repealed, transitional, and unknown rules remain explicitly distinguishable.
- Conflicting sources are preserved and documented rather than silently reconciled.
- Knowledge is stored as small, linked, reusable Markdown notes.
- Original sources remain separate from analyzed knowledge.
- Unknown facts are recorded as research gaps, never guessed.

## Scope

- Supported countries: **Chile** and **Brazil**
- Current focus: **Distribution Regulation**
- Planned domains: Transmission, Generation, Market, Reliability, Tariff, and broader Regulation topics

The repository now includes verified Chile VAD knowledge. Version v0.3.4 corrects the v0.3.2 enactment error: Ley No. 21.833 makes 2024-2030 a transitional six-year VAD period while preserving the normal four-year rule and identifying 2030-2034 as the next period. The CNE's **VAD 2024-2028** title is retained as a legacy process name, not current legal effect.

Version v0.4.1 adds a standardized, human-gated Source Intake and Change Candidate workflow. Intake records cannot directly alter `current` regulatory conclusions.

Version v0.4.2 keeps Markdown and Git as the canonical personal editorial layer while adding optional publication metadata, stable knowledge IDs, source-rights metadata, and a future database mapping. These additions do not require existing notes to be backfilled and do not create a product runtime.

## Personal Use

The repository remains directly browsable as Markdown and compatible with Git and future Obsidian use. A user can search notes, add sources manually, read regulatory conclusions, and inspect timelines without any database, account, API, or publishing service. Product-facing metadata is optional and must not complicate this workflow.

## Knowledge Maturity

- **Level 0 — Inbox:** material has been captured but not verified.
- **Level 1 — Source verified:** provenance and authority have been checked.
- **Level 2 — Knowledge extracted:** focused knowledge has been derived with citations.
- **Level 3 — Current status verified:** required current-claim and negative-verification checks are complete.
- **Level 4 — Human approved:** an identified human reviewer has approved the knowledge.
- **Level 5 — Publishable:** publication, audience, rights, and quality checks are complete.

Maturity is a quality indicator, not legal status. A `current` conclusion can remain internal and below Level 5.

## Public Prototype Website

`docs/` contains the static, Chinese-language public prototype intended for future GitHub Pages use. It presents approved informational content only and does not automatically publish internal Markdown, source files, research gaps, or Change Candidates. Open `docs/index.html` directly or serve `docs/` with any simple local static-file server; no build system is required.
