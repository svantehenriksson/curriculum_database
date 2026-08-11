# Curriculum database

We are scraping, maintaining, analyzing and processing Finnish curricula.

The idea is to extract the best possible topics for school textbooks on various topics.

## MVP first pass

This repo now includes a minimal first-pass pipeline focused on provenance and reproducibility:

- `docs/mvp-contract.md`
- `docs/first-implementation-checklist.md`
- `docs/api-notes.md`
- `scripts/mvp_pipeline.py`
- `scripts/recon_openapi.py`

### Create and use local virtual environment

```bash
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install pytest
```

### Run tests

```bash
.\.venv\Scripts\python.exe -m pytest -q
```

### Fetch one JSON source URL into raw storage

```bash
python scripts/mvp_pipeline.py fetch-url \
  --source-url "https://example.org/source.json" \
  --source-system "eperusteet" \
  --collection "recon"
```

### Parse one raw JSON file to deterministic JSONL

```bash
python scripts/mvp_pipeline.py parse-json \
  --raw-file "data/raw/eperusteet/recon/url_<hash>.json" \
  --source-system "eperusteet"
```

### Probe likely OpenAPI endpoints

```bash
.\.venv\Scripts\python.exe scripts/recon_openapi.py
```

### Extract math topic candidates (grades 7-9, pass 2)

```bash
.\.venv\Scripts\python.exe scripts/extract_math_topic_candidates.py
```

### Cluster topics and build consensus matrix (pass 3)

```bash
.\.venv\Scripts\python.exe scripts/cluster_math_topics_pass3.py
```