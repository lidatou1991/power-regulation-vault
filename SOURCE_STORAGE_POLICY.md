# Source Storage Policy

## Purpose

This repository keeps the reviewable knowledge layer in Git while keeping original source binaries in a separate local source archive. The separation prevents large or rights-restricted source files from entering repository history without sacrificing regulatory traceability.

## Stored in Git

- Markdown knowledge notes and entity/topic notes
- Source Notes, bibliographic records, filenames, citations, page/section references, provenance, and rights metadata
- Source Intake and Change Candidate records
- scripts, tests, public website files, reports, and changelog records

## Local Source Archive

Original PDFs, archives, office documents, ebooks, audio, video, and similar source binaries are local-only by default. Their original bytes and filenames must be preserved. The local archive may use paths under `01_Sources/` so Source Notes remain human-readable, but `.gitignore` prevents untracked binaries there from entering Git.

The local presence of a source binary does not make it public, publishable, approved, or cleared for redistribution. Publication remains subject to the human review gate, publication checklist, and recorded rights metadata.

## Repository Rules

1. Do not use Git LFS.
2. Do not commit an original source binary by default, regardless of size.
3. Never commit a file at or above GitHub's 100 MB per-file limit. Treat 50 MiB as the internal review threshold so growth and format changes cannot unexpectedly block a push.
4. Before staging a source binary below 50 MiB as a rare exception, document why Git storage is necessary, confirm redistribution rights, and obtain explicit human approval. Add a narrow `.gitignore` exception rather than weakening the archive-wide rules.
5. Preserve a Source Note with the source's identity, exact local filename or archive locator, bibliographic data, reviewed scope, and citation details.
6. Knowledge conclusions must cite Source Notes and authoritative sources even when the underlying binary is not in Git.
7. Removing a binary from Git tracking or unpublished history must not delete or modify the local archival copy.

## Pre-commit Checks

- Review staged files with `git diff --cached --stat` and `git diff --cached --numstat`.
- Check repository files and Git objects for unexpected large items.
- Confirm ignored archive files with `git check-ignore -v <path>`.
- Confirm the Source Note and knowledge links remain valid with the note, intake, and broken-link validators.
