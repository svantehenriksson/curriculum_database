# API Notes (Recon)

This file records early reconnaissance findings for official curriculum APIs.

## MVP Recon Goal

Before broad downloading, verify:

- Where official public OpenAPI/Swagger docs live.
- Which external endpoints are intended for third-party use.
- Whether key curriculum discovery tasks are possible via public API.

## Tiny Recon Flow

1. Run OpenAPI candidate probe:

```bash
.\.venv\Scripts\python.exe scripts/recon_openapi.py
```

2. Inspect machine-readable captures (if found):

- `data/raw/eperusteet/openapi/*.json`
- `data/raw/eperusteet/openapi/recon_results.jsonl`

3. Choose the canonical public docs endpoint and note it below.

## Initial Candidate Endpoints

- `https://opetushallitus.github.io/eperusteet`
- `https://opetushallitus.github.io/eperusteet/swagger.json`
- `https://opetushallitus.github.io/eperusteet/openapi.json`
- `https://eperusteet.opintopolku.fi/api/external/docs`
- `https://eperusteet.opintopolku.fi/api/external/swagger.json`
- `https://eperusteet.opintopolku.fi/api/external/openapi.json`

## Findings Log

### Run 1

- Date: 2026-08-10 (UTC+3 local session)
- Command: `.\.venv\Scripts\python.exe scripts/recon_openapi.py`
- Canonical docs endpoint selected: `https://opetushallitus.github.io/eperusteet` (landing page only, for now)
- Notes:
  - `https://opetushallitus.github.io/eperusteet` returned HTTP 200.
  - Landing-page HTML was preserved under `data/raw/eperusteet/openapi/`.
  - The tested direct `swagger.json` and `openapi.json` candidates returned HTTP 404.
  - The tested `eperusteet.opintopolku.fi/api/external/*` docs candidates returned HTTP 404.
  - Recon log saved to `data/raw/eperusteet/openapi/recon_results.jsonl`.
  - Next step: discover actual schema/document URLs linked from the landing page and probe those directly.

## Questions to Answer Next

- How to enumerate national curriculum bases?
- How to identify current basic-education national curriculum?
- How to identify current upper-secondary national curriculum?
- How to enumerate local curricula and provider mappings?
