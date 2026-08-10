from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "data" / "derived"
OUTPUT_JSONL = OUTPUT_DIR / "math_grade_7_9_first_pass.jsonl"
OUTPUT_MD = OUTPUT_DIR / "math_grade_7_9_first_pass.md"


@dataclass(frozen=True)
class SourceSpec:
    raw_path: str
    source_system: str
    scope: str
    language: str
    curriculum_id: str
    label: str


SOURCES: list[SourceSpec] = [
    SourceSpec(
        raw_path="data/raw/eperusteet/national/419550.json",
        source_system="eperusteet",
        scope="national",
        language="fi",
        curriculum_id="419550",
        label="National basic education 2014 (FI)",
    ),
    SourceSpec(
        raw_path="data/raw/eperusteet-ylops/local/28444489.json",
        source_system="eperusteet-ylops",
        scope="local",
        language="fi",
        curriculum_id="28444489",
        label="Kirkkonummi local 2025 (FI)",
    ),
    SourceSpec(
        raw_path="data/raw/eperusteet-ylops/local/32965859.json",
        source_system="eperusteet-ylops",
        scope="local",
        language="sv",
        curriculum_id="32965859",
        label="Kyrkslatt local 2026 (SV)",
    ),
    SourceSpec(
        raw_path="data/raw/eperusteet-ylops/local/22890002.json",
        source_system="eperusteet-ylops",
        scope="local",
        language="fi",
        curriculum_id="22890002",
        label="Helsinki local 2016 (FI)",
    ),
    SourceSpec(
        raw_path="data/raw/eperusteet-ylops/local/22890003.json",
        source_system="eperusteet-ylops",
        scope="local",
        language="sv",
        curriculum_id="22890003",
        label="Helsingfors local 2016 (SV)",
    ),
    SourceSpec(
        raw_path="data/raw/eperusteet-ylops/local/35439754.json",
        source_system="eperusteet-ylops",
        scope="local",
        language="fi",
        curriculum_id="35439754",
        label="Turku local 2026 (FI)",
    ),
    SourceSpec(
        raw_path="data/raw/eperusteet-ylops/local/22617371.json",
        source_system="eperusteet-ylops",
        scope="local",
        language="sv",
        curriculum_id="22617371",
        label="Abo local 2026 (SV)",
    ),
    SourceSpec(
        raw_path="data/raw/eperusteet-ylops/local/1283735.json",
        source_system="eperusteet-ylops",
        scope="local",
        language="fi",
        curriculum_id="1283735",
        label="Vaasa local (FI)",
    ),
    SourceSpec(
        raw_path="data/raw/eperusteet-ylops/local/27446734.json",
        source_system="eperusteet-ylops",
        scope="local",
        language="sv",
        curriculum_id="27446734",
        label="Vasa local (SV)",
    ),
]


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def normalized_subject(item: dict[str, Any]) -> dict[str, Any]:
    # Local ylops payloads wrap subject data under `oppiaine`.
    wrapped = item.get("oppiaine")
    if isinstance(wrapped, dict):
        return wrapped
    return item


def is_math_subject(subject: dict[str, Any]) -> bool:
    code = str(subject.get("koodiArvo") or "").upper()
    if code == "MA":
        return True
    name = subject.get("nimi") or {}
    for lang in ("fi", "sv"):
        text = str(name.get(lang) or "").lower()
        if "matematiikka" in text or "matematik" in text:
            return True
    return False


def pick_math_subject(subjects: list[dict[str, Any]]) -> dict[str, Any] | None:
    normalized = [normalized_subject(item) for item in subjects]
    for subject in normalized:
        if str(subject.get("koodiArvo") or "").upper() == "MA":
            return subject
    for subject in normalized:
        if is_math_subject(subject):
            return subject
    return None


def grade_number_from_code(code: str | None) -> int | None:
    if not code:
        return None
    code = str(code)
    if code.startswith("vuosiluokka_"):
        try:
            return int(code.split("_", 1)[1])
        except ValueError:
            return None
    return None


def extract_text_snippet(node: Any, max_len: int = 180) -> str | None:
    if isinstance(node, str):
        text = " ".join(node.replace("\n", " ").split())
        if not text:
            return None
        return text[:max_len]
    if isinstance(node, dict):
        for key in ("teksti", "kuvaus", "otsikko", "fi", "sv"):
            if key in node:
                snippet = extract_text_snippet(node[key], max_len=max_len)
                if snippet:
                    return snippet
        for value in node.values():
            snippet = extract_text_snippet(value, max_len=max_len)
            if snippet:
                return snippet
    if isinstance(node, list):
        for item in node:
            snippet = extract_text_snippet(item, max_len=max_len)
            if snippet:
                return snippet
    return None


def extract_records_for_source(spec: SourceSpec) -> list[dict[str, Any]]:
    raw_file = ROOT / spec.raw_path
    data = json.loads(raw_file.read_text(encoding="utf-8"))

    subjects = []
    if isinstance(data.get("oppiaineet"), list):
        subjects = data["oppiaineet"]
    elif isinstance((data.get("perusopetus") or {}).get("oppiaineet"), list):
        subjects = (data.get("perusopetus") or {}).get("oppiaineet") or []

    math_subject = pick_math_subject(subjects)
    if math_subject is None:
        return []

    out: list[dict[str, Any]] = []
    bands = math_subject.get("vuosiluokkakokonaisuudet") or []
    for band_index, band in enumerate(bands):
        grade_nodes = band.get("vuosiluokat") or []
        for node in grade_nodes:
            if isinstance(node, dict):
                grade = grade_number_from_code(node.get("vuosiluokka"))
                if grade not in (7, 8, 9):
                    continue
                tavoitteet = node.get("tavoitteet") or []
                sisaltoalueet = node.get("sisaltoalueet") or []
            elif isinstance(node, str):
                grade = grade_number_from_code(node)
                if grade not in (7, 8, 9):
                    continue
                # National data may keep objectives/content at band level.
                tavoitteet = band.get("tavoitteet") or []
                sisaltoalueet = band.get("sisaltoalueet") or []
            else:
                continue

            tavoitteet_sample = extract_text_snippet(tavoitteet)
            sisalto_sample = extract_text_snippet(sisaltoalueet)

            out.append(
                {
                    "source_system": spec.source_system,
                    "scope": spec.scope,
                    "language": spec.language,
                    "curriculum_id": spec.curriculum_id,
                    "label": spec.label,
                    "source_raw_path": spec.raw_path,
                    "subject_code": math_subject.get("koodiArvo"),
                    "subject_name_fi": (math_subject.get("nimi") or {}).get("fi"),
                    "subject_name_sv": (math_subject.get("nimi") or {}).get("sv"),
                    "band_index": band_index,
                    "grade": grade,
                    "tavoitteet_count": len(tavoitteet),
                    "sisaltoalueet_count": len(sisaltoalueet),
                    "sample_tavoite_text": tavoitteet_sample,
                    "sample_sisalto_text": sisalto_sample,
                }
            )
    out.sort(key=lambda r: (r["label"], r["grade"]))
    return out


def render_markdown(records: list[dict[str, Any]]) -> str:
    lines = [
        "# Math Grade 7-9 First Pass",
        "",
        "Deterministic extraction from raw JSON using explicit `vuosiluokka_*` nodes under mathematics (`koodiArvo=MA`).",
        "",
        "| Curriculum | Scope | Lang | Grade | Tavoitteet | Sisaltoalueet |",
        "|---|---|---|---:|---:|---:|",
    ]
    for record in records:
        lines.append(
            f"| {record['label']} | {record['scope']} | {record['language']} | "
            f"{record['grade']} | {record['tavoitteet_count']} | {record['sisaltoalueet_count']} |"
        )
    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append("- Counts reflect explicit per-grade entries in the source structures.")
    lines.append("- This first pass does not yet normalize topic equivalence across municipalities.")
    lines.append("- Sample evidence text is retained in JSONL fields for auditing.")
    return "\n".join(lines) + "\n"


def main() -> None:
    all_records: list[dict[str, Any]] = []
    for spec in SOURCES:
        all_records.extend(extract_records_for_source(spec))
    all_records.sort(key=lambda r: (r["label"], r["grade"]))

    ensure_parent(OUTPUT_JSONL)
    with OUTPUT_JSONL.open("w", encoding="utf-8") as handle:
        for record in all_records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True))
            handle.write("\n")

    md = render_markdown(all_records)
    ensure_parent(OUTPUT_MD)
    OUTPUT_MD.write_text(md, encoding="utf-8")

    print(f"Wrote {len(all_records)} rows to {OUTPUT_JSONL}")
    print(f"Wrote summary markdown to {OUTPUT_MD}")


if __name__ == "__main__":
    main()
