# MVP Contract (First Pass)

This MVP intentionally focuses on trustworthy data handling before broad coverage.

## Scope

- Use official structured APIs first.
- Preserve raw responses exactly (or near-exactly).
- Keep parsed output deterministic and reproducible.
- Avoid nationwide crawling in v0.

## v0 Deliverables

1. A small CLI to fetch one source URL at a time and save:
   - raw payload
   - provenance metadata
   - checksum
2. A deterministic parser pass from one raw JSON file to JSONL records.
3. A concise reconnaissance checklist for manually sampling providers.

## Required Fields (Provenance)

Each retrieval record must include:

- `source_system` (for example `eperusteet`)
- `source_url`
- `retrieved_at_utc`
- `http_status`
- `content_sha256`
- `raw_path`
- `upstream_id` (nullable)
- `language` (nullable)
- `education_level` (nullable)
- `scope` (`national`, `local`, or nullable)

## Required Fields (Parsed JSONL)

Each parsed record must include:

- `record_id` (stable hash from source file + path + text)
- `source_raw_path`
- `source_system`
- `curriculum_id` (nullable)
- `language` (nullable)
- `education_level` (nullable)
- `scope` (nullable)
- `section_path` (list of keys/indexes)
- `text`

## Storage Layout (v0)

```text
data/
  raw/
    retrieval_log.jsonl
    <source_system>/
      <collection>/
        <deterministic filename>.json
  parsed/
    parsed_records.jsonl
```

## Non-Goals in v0

- Full nationwide downloader
- Municipality/provider canonicalization
- Advanced subject/topic normalization
- LLM-derived extraction
- Scheduling or continuous monitoring

## Acceptance Criteria

- Same input URL and metadata produce deterministic output paths.
- Raw file checksum in the provenance log matches file contents.
- Parsed output is deterministic across repeated runs.
- No derived claim is stored as raw source text.
