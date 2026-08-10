# First Implementation Checklist

This checklist is intentionally strict and small to keep the first milestone realistic.

## 1) Foundation

- [x] Define MVP contract in `docs/mvp-contract.md`.
- [ ] Confirm Python version available locally.
- [x] Create minimal folder layout (`data/raw`, `data/parsed`, `scripts`, `tests`, `docs`).

## 2) Retrieval (Raw + Provenance)

- [x] Implement CLI command to fetch one URL and store raw JSON deterministically.
- [x] Compute and store SHA-256 checksum.
- [x] Append retrieval metadata to `data/raw/retrieval_log.jsonl`.
- [x] Keep retrieval logic conservative (single request, explicit timeout, no aggressive retry loops in v0).

## 3) Parsing (Deterministic)

- [x] Implement deterministic extraction of text-bearing nodes from one raw JSON file.
- [x] Write normalized JSONL records to `data/parsed/parsed_records.jsonl`.
- [x] Generate stable record IDs based on source path + section path + text.

## 4) Tests

- [x] Add unit tests for deterministic path generation.
- [x] Add unit tests for checksum and stable record IDs.
- [x] Add unit tests for deterministic parsed ordering.

## 5) Manual Recon Workflow (v0)

- [ ] Fetch official OpenAPI/Swagger documents and preserve raw files.
- [ ] Identify candidate endpoints for:
  - national basic education curricula
  - national upper-secondary curricula
  - local curricula listing
- [ ] Fetch a small sample (Kirkkonummi/Kyrkslatt FI/SV when discoverable).
- [ ] Document findings in `docs/api-notes.md`.

## 6) Exit Criteria for “Simple First Pass”

- [ ] You can run one command to fetch a raw source payload with provenance logging.
- [ ] You can run one command to parse that raw payload into reproducible JSONL.
- [ ] Tests pass.
- [ ] No assumptions are made that FI/SV are mere translations.
