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

### Run 2

- Date: 2026-08-10 (UTC+3 local session)
- Command:
  - `.\.venv\Scripts\python.exe scripts/recon_openapi.py --url ...`
  - `.\.venv\Scripts\python.exe scripts/mvp_pipeline.py fetch-url --source-url "https://virkailija.opintopolku.fi/.../api-docs/external" ...`
- Canonical docs endpoints selected:
  - `https://virkailija.opintopolku.fi/eperusteet-service/api-docs/external`
  - `https://virkailija.opintopolku.fi/eperusteet-ylops-service/api-docs/external`
  - `https://virkailija.opintopolku.fi/eperusteet-amosaa-service/api-docs/external`
- Notes:
  - The GitHub docs subpages (`/api/eperusteet`, `/api/ylops`, `/api/amosaa`) returned HTTP 200 and exposed the real OpenAPI URLs in embedded Swagger config.
  - Raw OpenAPI JSON specs were saved via the MVP pipeline:
    - `data/raw/eperusteet/openapi/eperusteet-service-external.json`
    - `data/raw/eperusteet/openapi/ylops-service-external.json`
    - `data/raw/eperusteet/openapi/amosaa-service-external.json`
  - Key discovered external listing endpoints:
    - National bases: `/api/external/perusteet` (eperusteet-service)
    - National detail: `/api/external/peruste/{perusteId}` (eperusteet-service)
    - Local OPS listing: `/api/external/opetussuunnitelmat` (ylops-service)
    - Local OPS detail: `/api/external/opetussuunnitelma/{opetussuunnitelmaId}` (ylops-service)

### Run 3 (First Real Retrieval Pass)

- Date: 2026-08-10 (UTC+3 local session)
- Command: `.\.venv\Scripts\python.exe scripts/mvp_pipeline.py fetch-url --source-url ...`
- National IDs retrieved:
  - `419550` (`Perusopetuksen opetussuunnitelman perusteet 2014`)
  - `6828810` (`Lukion opetussuunnitelman perusteet 2019`)
- Local IDs retrieved (Kirkkonummi/Kyrkslatt basic education):
  - `28444489` (`Kirkkonummen suomenkielisen perusopetuksen opetussuunnitelma 2025`)
  - `32965859` (`Läroplan för den grundläggande utbildningen i Kyrkslätt 2026`)
- Files saved:
  - `data/raw/eperusteet/national/419550.json`
  - `data/raw/eperusteet/national/6828810.json`
  - `data/raw/eperusteet-ylops/local/28444489.json`
  - `data/raw/eperusteet-ylops/local/32965859.json`
- Parser smoke test:
  - Parsed `28444489.json` into `data/parsed/parsed_records.jsonl` (`20789` records).

## Questions to Answer Next

- How to robustly identify "current" national bases (selection rule by status/effective date)?
- How to map municipalities to organization/provider IDs deterministically?
- How to extract mathematics grade 7–9 (and grade-band relations) from local and national nodes?
- How to paginate local listings for a representative 10-provider sample?
