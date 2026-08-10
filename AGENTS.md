# AGENTS.md

## Project purpose

This repository builds a machine-readable corpus of Finnish national and local curricula.

The initial business use case is educational publishing: determine what Finnish municipalities and education providers actually assign to different grades and subjects, especially where the national curriculum specifies broader grade bands such as grades 7–9.

The project should ultimately support questions such as:

* What mathematics topics are explicitly assigned to grade 7, 8, and 9 by different municipalities?
* How consistent are grade allocations across Finland?
* Which topics are usually taught in grade 8 even when the national curriculum only specifies grades 7–9?
* How do Finnish- and Swedish-language local curricula differ?
* Which municipalities leave national grade-band content unallocated to specific grades?
* How have curricula changed between versions?
* What would a de facto Finnish grade-by-grade curriculum look like when inferred from local curricula?
* Can the same underlying textbook structure serve a large majority of municipalities?

This is primarily a **data acquisition, preservation, provenance, and analysis project**, not a web application.

---

# Core principles

## 1. Prefer official structured sources

Use sources in this order:

1. Official ePerusteet / Opetushallitus public API
2. Other official Opetushallitus APIs or machine-readable sources
3. Official municipality / education-provider curriculum sources
4. Official PDFs or HTML pages
5. Third-party aggregators such as tavoitteet.fi only when they provide information unavailable from official sources

Do not scrape rendered HTML when equivalent structured JSON is available.

`tavoitteet.fi` is useful for reconnaissance and verification, but should not automatically become the canonical source.

---

## 2. Preserve raw source data

Never make normalized or AI-generated data the only surviving representation.

For every source retrieved, preserve the original response as closely as practical.

Examples:

* JSON → save original JSON
* HTML → save original HTML when needed
* PDF → retain original PDF when permitted/appropriate
* API metadata → retain IDs, status, version, language, timestamps, and links

Derived datasets must be reproducible from raw data.

---

## 3. Separate raw, parsed, and inferred information

Use three conceptual layers.

### Raw

Exact or near-exact source material retrieved from official sources.

No LLM rewriting.

No normalization beyond what is necessary to store the response.

### Parsed

Deterministically extracted structure such as:

* education provider
* municipality
* curriculum ID
* curriculum version
* language
* education level
* subject
* grade
* grade range
* section hierarchy
* national/local scope
* source identifiers
* text

Parsed output should be reproducible from raw source data.

### Derived

Interpretations such as:

* topic = "first-degree equations"
* probable grade = 8
* curriculum coverage
* topic equivalence across differently worded curricula
* inferred textbook chapter
* similarity between municipality curricula
* Finnish–Swedish equivalence
* confidence score

Derived information may use heuristics or LLMs.

Never silently present inferred information as source text.

---

# Licensing and copyright

## ePerusteet software

The upstream Opetushallitus `eperusteet` software repository is licensed under:

European Union Public Licence (EUPL), Version 1.1 or subsequent approved versions.

Commercial use is permitted.

However, avoid copying upstream application code unless there is a concrete reason to do so.

We primarily want to consume public APIs, not fork ePerusteet.

If upstream source code is copied or modified:

* retain copyright notices
* retain licence notices
* comply with the applicable EUPL obligations
* document copied files and their provenance
* do not silently relicense EUPL-covered code as proprietary code

## Curriculum content

IMPORTANT:

Do NOT assume that the EUPL licence covering the ePerusteet software automatically covers curriculum text or other API content.

Software licensing and content/data licensing are separate issues.

Until curriculum-content reuse rights have been verified:

* retrieval for analysis is allowed as a technical project requirement
* preserve source provenance
* do not claim that curriculum text is EUPL-licensed
* do not attach an open-content licence to downloaded curriculum text
* do not publish a bulk public mirror of curriculum text solely because the software is open source
* do not incorporate large verbatim blocks into commercial learning materials without checking the applicable rights

Maintain a document such as:

`docs/licensing.md`

recording what has actually been verified.

---

# Source provenance

Every retrieved curriculum should have enough metadata to trace it back to its source.

At minimum retain where available:

* source system
* source URL
* API endpoint
* upstream ID
* parent IDs
* provider / organization ID
* municipality
* education provider
* language
* curriculum type
* education level
* publication status
* version
* effective-from date
* effective-to date if present
* retrieval timestamp
* content checksum, preferably SHA-256

Never generate fake IDs when an upstream ID exists.

If we create an internal ID, retain the upstream ID separately.

---

# Languages

Finnish and Swedish must be treated as first-class source languages.

Do not assume the Swedish curriculum is merely a translation of the Finnish curriculum.

For example, represent:

* Kirkkonummi / Finnish
* Kyrkslätt / Swedish

as distinct curriculum records even if they belong to the same municipality.

Preserve original-language text.

Translation, if created, belongs in the derived layer.

Later we want to compare whether Finnish and Swedish curricula in the same municipality assign the same topics to the same grades.

---

# Educational hierarchy

Do not force all curricula into a simplistic grade 1–12 model.

Finnish basic education and upper-secondary education have different structures.

## Basic education

Grades 1–9.

National curriculum content may be specified for grade bands such as:

* 1–2
* 3–6
* 7–9

Local curricula may assign that content to individual grades.

Preserve BOTH:

* national grade-range information
* local grade-specific information

This difference is one of the central objects of study.

## Upper-secondary education

Do not pretend that national upper-secondary curricula consist simply of "grades 10, 11, 12".

Preserve the real structure:

* subject
* module
* study unit where local curricula define one
* credits
* compulsory / optional status where available
* dependencies or sequencing where available

A later derived layer may infer typical year-of-study sequencing.

---

# National versus local content

This distinction is critical.

Where possible, identify separately:

* national curriculum text
* local additions
* local refinements
* local grade allocations
* local omissions or references to national material

Preserve upstream relationships between local nodes and national parent nodes.

Do not flatten national and local text together if the API lets us distinguish them.

One major future analysis is:

`local curriculum = national basis + local refinements`

We should therefore preserve enough structure to calculate differences.

---

# Repository structure

Prefer a structure conceptually similar to:

```text
curricula/
  national/
    basic_education/
    upper_secondary/

  local/
    kirkkonummi/
      fi/
      sv/
    helsinki/
      fi/
      sv/
    ...

data/
  raw/
  parsed/
  derived/

docs/
  sources.md
  api-notes.md
  licensing.md
  data-model.md

scripts/
tests/
```

The exact structure may evolve after inspecting the APIs.

Do not prematurely create hundreds of empty directories.

---

# Raw-data storage

Prefer deterministic filenames based on upstream identifiers rather than human-readable titles alone.

Example:

```text
data/raw/eperusteet/perusteet/123456.json
```

or:

```text
data/raw/local/987654.json
```

Store metadata separately if necessary.

Raw API responses should not be manually edited.

---

# Parsed representation

JSONL is preferred for normalized analytical records unless another format provides a clear advantage.

A possible record:

```json
{
  "curriculum_id": "123456",
  "provider": "Kirkkonummen kunta",
  "municipality": "Kirkkonummi",
  "language": "fi",
  "education_level": "basic_education",
  "grade": 8,
  "grade_range": null,
  "subject": "matematiikka",
  "section_path": [
    "Vuosiluokka 8",
    "Matematiikka",
    "Keskeiset sisältöalueet",
    "S3 Algebra"
  ],
  "scope": "local",
  "text": "..."
}
```

This schema is illustrative, not fixed.

Inspect real API responses before finalizing it.

---

# API strategy

Before building a production downloader, perform API reconnaissance.

Determine:

1. How to enumerate national curriculum bases.
2. How to identify the current basic-education national curriculum.
3. How to identify the current upper-secondary national curriculum.
4. How to enumerate local curricula.
5. Whether all published local curricula can be discovered through one API.
6. How education-provider / organization IDs work.
7. How municipalities map to education providers.
8. How languages are represented.
9. How subjects are represented.
10. How grade and grade-range information is represented.
11. How local additions relate to national parent nodes.
12. How versioning and publication status work.
13. Whether pagination exists.
14. Whether rate limits are documented.
15. Whether some relevant endpoints require authentication.
16. Which external/public API endpoints are intended for third-party consumption.

Check the official generated OpenAPI / Swagger documentation first.

The upstream repository mentions generated external API documentation at:

`https://opetushallitus.github.io/eperusteet`

Use the public/external API where possible.

Do not rely on internal authenticated endpoints simply because they can be reverse engineered.

---

# Initial reconnaissance before large-scale downloading

Do not immediately crawl all Finland.

First test a deliberately varied sample of municipalities / providers, for example:

* Helsinki
* Espoo
* Vantaa
* Kirkkonummi / Kyrkslätt
* Turku / Åbo
* Tampere
* Oulu
* Vaasa / Vasa
* Porvoo / Borgå
* one or more small Finnish-speaking municipalities
* one or more strongly Swedish-speaking municipalities

For each determine:

* curriculum present in ePerusteet?
* current?
* Finnish?
* Swedish?
* subjects visible?
* individual-grade allocation present?
* national/local distinction recoverable?
* complete data obtainable through public API?

Write findings to `docs/api-notes.md`.

---

# Completeness audit

A central early task is determining how representative ePerusteet is.

We eventually want a table such as:

```text
provider
municipality
FI curriculum found
SV curriculum found
current curriculum found
source
API accessible
grade-specific allocation
notes
```

Do not assume that every Finnish municipality publishes its local curriculum through ePerusteet.

Measure coverage.

If substantial gaps exist, design fallback collection later.

---

# Fallback strategy

Only after evaluating ePerusteet coverage should we add alternative ingestion.

Possible fallbacks:

1. official municipality curriculum page
2. official municipality PDF
3. other official education-provider site
4. tavoitteet.fi
5. manual investigation

Each fallback source must retain provenance and source type.

Do not silently mix unofficial aggregator text with official API text.

---

# Rate limiting and respectful retrieval

This is a public-sector service, not infrastructure we control.

Downloader behaviour should be conservative.

Requirements:

* cache responses locally
* never repeatedly download unchanged data unnecessarily
* implement retry with exponential backoff
* respect HTTP status codes
* use bounded concurrency
* identify the client with a reasonable User-Agent if appropriate
* avoid hammering endpoints
* support resuming interrupted downloads
* permit targeted retrieval of one curriculum/provider
* avoid full recrawls when incremental retrieval suffices

Do not attempt to bypass access controls, authentication, throttling, or technical restrictions.

---

# Versioning and reproducibility

Curricula change.

A retrieval must not merely overwrite old content invisibly.

Where feasible preserve:

* upstream version
* publication status
* effective date
* retrieval date
* checksum

Git should make meaningful curriculum changes inspectable.

However, avoid creating enormous meaningless Git diffs solely because JSON key order or formatting changed.

Canonicalize derived output deterministically.

Raw source snapshots may be stored separately or managed with an appropriate strategy if volume becomes large.

Do not introduce Git LFS until there is an actual need.

---

# Change detection

Eventually support:

```text
fetch -> checksum -> compare -> store changed version -> derive diff
```

We want to answer questions such as:

* What changed in OPS?
* Which municipality changed grade allocations?
* Did a subject description change?
* Did Finnish and Swedish versions diverge?

Do not build scheduled monitoring before basic acquisition works.

---

# Analysis goals

Once sufficient data exists, priority analytical outputs include:

## Grade allocation matrix

For each subject/topic:

```text
topic
grade 7 %
grade 8 %
grade 9 %
not explicitly allocated %
municipalities observed
```

## Municipality matrix

For a chosen subject:

```text
municipality × topic -> grade
```

## Consensus curriculum

Infer what could reasonably be described as the de facto grade-specific Finnish curriculum based on local implementations.

This is DERIVED data and must never be confused with the official national curriculum.

## Outliers

Identify municipalities that assign topics substantially earlier/later than the modal allocation.

## Finnish–Swedish comparison

Compare local grade allocations by language.

---

# Topic normalization

Do not begin with a giant manually invented topic taxonomy.

First preserve source text and upstream structure.

Later, build normalization incrementally.

Example:

```text
"ensimmäisen asteen yhtälö"
"1. asteen yhtälö"
"lineaarinen yhtälö"
```

may map to a canonical analytical concept such as:

```text
math.algebra.linear_equation
```

But mappings must preserve evidence.

A normalized topic record should retain:

* source text
* source curriculum
* source section
* normalization rule/model
* confidence
* canonical topic

---

# LLM usage

LLMs may be useful for:

* topic classification
* terminology normalization
* comparing differently worded local requirements
* Finnish/Swedish semantic matching
* identifying likely grade allocations expressed in prose
* summarizing municipal differences

LLMs must NOT:

* alter raw source text
* invent missing curriculum requirements
* silently fill absent grade information
* replace deterministic parsing where structured fields already exist
* produce uncited facts that become canonical data

Any LLM-derived result belongs in `derived/`.

If LLM processing is introduced, make it reproducible where practical:

* store prompt version
* model identifier where available
* timestamp
* input identifiers
* output
* confidence / validation status

---

# Textbook-business separation

This corpus should describe curricula accurately regardless of our later publishing strategy.

Do not modify curriculum interpretations merely to fit a proposed textbook structure.

The direction must be:

```text
official evidence
    ↓
curriculum corpus
    ↓
derived consensus
    ↓
textbook structure
```

not:

```text
desired textbook structure
    ↓
reinterpret curriculum to fit it
```

---

# Testing

Prioritize tests for:

* deterministic parsing
* stable IDs
* language handling
* grade vs grade-range handling
* national/local distinction
* pagination
* version detection
* malformed or missing fields
* reproducible serialization

For API integration tests, avoid repeatedly hitting production endpoints where recorded fixtures will suffice.

Use small real API responses as fixtures where licensing and repository policy permit.

---

# Coding philosophy

Prefer:

* simple Python
* standard library where practical
* `requests` or `httpx`
* dataclasses / Pydantic only if they genuinely help
* explicit transformations
* small scripts
* JSON / JSONL
* pytest
* clear command-line interfaces

Avoid initially:

* databases unless volume/query requirements justify one
* Kubernetes
* microservices
* web frontends
* orchestration frameworks
* embedding/vector databases
* complex agent frameworks
* premature abstraction

A directory of trustworthy JSON plus a few good Python scripts is preferable to an elegant platform containing questionable data.

SQLite or DuckDB can be added later for analysis without changing the canonical source corpus.

---

# First milestone

The first meaningful milestone is NOT "scrape Finland."

It is:

1. Document the relevant official APIs.
2. Successfully retrieve the national basic-education curriculum.
3. Successfully retrieve the national upper-secondary curriculum.
4. Retrieve local curricula for Kirkkonummi/Kyrkslätt.
5. Demonstrate how national and local information relate.
6. Extract mathematics for grades 7–9.
7. Show whether Kirkkonummi's grade-specific additions can be identified automatically.
8. Repeat for approximately 10 diverse education providers.
9. Estimate nationwide ePerusteet coverage.
10. Only then design the full downloader.

---

# Definition of a good result

A good result is not the maximum number of downloaded documents.

A good result is a corpus where every claim can answer:

* Where did this come from?
* Was this national or local?
* Which version?
* Which language?
* Which grade or grade range?
* Is this original text or our inference?
* Can we reproduce the extraction?
* Can we detect when the source changes?

Accuracy and provenance are more important than collection speed.
