from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.extract_math_7_9 import (  # noqa: E402
    SOURCES,
    SourceSpec,
    grade_number_from_code,
    normalized_subject,
    pick_math_subject,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "data" / "derived"
OUTPUT_JSONL = OUTPUT_DIR / "math_topic_candidates_7_9_pass2.jsonl"
OUTPUT_MD = OUTPUT_DIR / "math_topic_candidates_7_9_pass2.md"


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def flatten_text(value: Any) -> str | None:
    if isinstance(value, str):
        text = " ".join(value.replace("\n", " ").split())
        return text or None
    if isinstance(value, dict):
        # Prefer human-readable fields first.
        for key in ("fi", "sv", "teksti", "kuvaus", "otsikko", "nimi"):
            if key in value:
                out = flatten_text(value[key])
                if out:
                    return out
        for nested in value.values():
            out = flatten_text(nested)
            if out:
                return out
    if isinstance(value, list):
        for item in value:
            out = flatten_text(item)
            if out:
                return out
    return None


def lang_text(value: Any, lang: str) -> str | None:
    if isinstance(value, dict):
        candidate = value.get(lang)
        if isinstance(candidate, str):
            text = " ".join(candidate.replace("\n", " ").split())
            return text or None
    return None


def choose_topic_text(preferred_lang: str, fi: str | None, sv: str | None, fallback: str | None) -> str | None:
    if preferred_lang == "fi":
        return fi or sv or fallback
    if preferred_lang == "sv":
        return sv or fi or fallback
    return fi or sv or fallback


def stable_record_id(parts: list[str]) -> str:
    return hashlib.sha256("|".join(parts).encode("utf-8")).hexdigest()


def emit_row(
    spec: SourceSpec,
    math_subject: dict[str, Any],
    grade: int,
    band_index: int,
    node_level: str,
    evidence_type: str,
    evidence_item: dict[str, Any],
    section_path: list[str],
) -> dict[str, Any] | None:
    if evidence_type == "tavoite":
        fi = lang_text(evidence_item.get("tavoite"), "fi")
        sv = lang_text(evidence_item.get("tavoite"), "sv")
        fallback = flatten_text(evidence_item.get("tavoite"))
    else:
        fi = lang_text(evidence_item.get("nimi"), "fi") or lang_text(evidence_item.get("kuvaus"), "fi")
        sv = lang_text(evidence_item.get("nimi"), "sv") or lang_text(evidence_item.get("kuvaus"), "sv")
        fallback = flatten_text(evidence_item.get("nimi")) or flatten_text(evidence_item.get("kuvaus"))

    topic_text = choose_topic_text(spec.language, fi, sv, fallback)
    if not topic_text:
        return None

    evidence_id = str(evidence_item.get("id") or "")
    evidence_uuid = str(evidence_item.get("tunniste") or "")
    record_id = stable_record_id(
        [
            spec.raw_path,
            str(grade),
            evidence_type,
            evidence_id,
            evidence_uuid,
            topic_text,
        ]
    )

    return {
        "record_id": record_id,
        "source_system": spec.source_system,
        "scope": spec.scope,
        "language": spec.language,
        "curriculum_id": spec.curriculum_id,
        "label": spec.label,
        "source_raw_path": spec.raw_path,
        "subject_code": math_subject.get("koodiArvo"),
        "subject_name_fi": (math_subject.get("nimi") or {}).get("fi"),
        "subject_name_sv": (math_subject.get("nimi") or {}).get("sv"),
        "grade": grade,
        "band_index": band_index,
        "node_level": node_level,
        "evidence_type": evidence_type,
        "evidence_id": evidence_id or None,
        "evidence_tunniste": evidence_uuid or None,
        "section_path": section_path,
        "topic_candidate_text": topic_text,
        "topic_text_fi": fi,
        "topic_text_sv": sv,
    }


def extract_for_source(spec: SourceSpec) -> list[dict[str, Any]]:
    data = json.loads((ROOT / spec.raw_path).read_text(encoding="utf-8"))
    subjects = []
    if isinstance(data.get("oppiaineet"), list):
        subjects = data["oppiaineet"]
    elif isinstance((data.get("perusopetus") or {}).get("oppiaineet"), list):
        subjects = (data.get("perusopetus") or {}).get("oppiaineet") or []

    math_subject = pick_math_subject(subjects)
    if math_subject is None:
        return []

    rows: list[dict[str, Any]] = []
    for band_index, band in enumerate(math_subject.get("vuosiluokkakokonaisuudet") or []):
        raw_grade_nodes = band.get("vuosiluokat") or []
        for grade_node_index, grade_node in enumerate(raw_grade_nodes):
            if isinstance(grade_node, str):
                grade = grade_number_from_code(grade_node)
                if grade not in (7, 8, 9):
                    continue
                # In national data, tavoitteet/sisaltoalueet are often at band level.
                for idx, item in enumerate(band.get("tavoitteet") or []):
                    if not isinstance(item, dict):
                        continue
                    row = emit_row(
                        spec=spec,
                        math_subject=math_subject,
                        grade=grade,
                        band_index=band_index,
                        node_level="band",
                        evidence_type="tavoite",
                        evidence_item=item,
                        section_path=["vuosiluokkakokonaisuudet", str(band_index), "tavoitteet", str(idx)],
                    )
                    if row:
                        rows.append(row)
                for idx, item in enumerate(band.get("sisaltoalueet") or []):
                    if not isinstance(item, dict):
                        continue
                    row = emit_row(
                        spec=spec,
                        math_subject=math_subject,
                        grade=grade,
                        band_index=band_index,
                        node_level="band",
                        evidence_type="sisaltoalue",
                        evidence_item=item,
                        section_path=["vuosiluokkakokonaisuudet", str(band_index), "sisaltoalueet", str(idx)],
                    )
                    if row:
                        rows.append(row)
                continue

            if not isinstance(grade_node, dict):
                continue
            grade = grade_number_from_code(grade_node.get("vuosiluokka"))
            if grade not in (7, 8, 9):
                continue
            for idx, item in enumerate(grade_node.get("tavoitteet") or []):
                if not isinstance(item, dict):
                    continue
                row = emit_row(
                    spec=spec,
                    math_subject=math_subject,
                    grade=grade,
                    band_index=band_index,
                    node_level="grade",
                    evidence_type="tavoite",
                    evidence_item=item,
                    section_path=[
                        "vuosiluokkakokonaisuudet",
                        str(band_index),
                        "vuosiluokat",
                        str(grade_node_index),
                        "tavoitteet",
                        str(idx),
                    ],
                )
                if row:
                    rows.append(row)
            for idx, item in enumerate(grade_node.get("sisaltoalueet") or []):
                if not isinstance(item, dict):
                    continue
                row = emit_row(
                    spec=spec,
                    math_subject=math_subject,
                    grade=grade,
                    band_index=band_index,
                    node_level="grade",
                    evidence_type="sisaltoalue",
                    evidence_item=item,
                    section_path=[
                        "vuosiluokkakokonaisuudet",
                        str(band_index),
                        "vuosiluokat",
                        str(grade_node_index),
                        "sisaltoalueet",
                        str(idx),
                    ],
                )
                if row:
                    rows.append(row)

    rows.sort(key=lambda r: (r["label"], r["grade"], r["evidence_type"], r["topic_candidate_text"]))
    return rows


def render_summary(rows: list[dict[str, Any]]) -> str:
    counts: dict[tuple[str, int], dict[str, int]] = {}
    for row in rows:
        key = (row["label"], int(row["grade"]))
        if key not in counts:
            counts[key] = {"tavoite": 0, "sisaltoalue": 0}
        counts[key][row["evidence_type"]] += 1

    lines = [
        "# Math Topic Candidates 7-9 (Pass 2)",
        "",
        "Deterministic extraction of topic-candidate evidence from `tavoitteet` and `sisaltoalueet` in math grade nodes.",
        "",
        "| Curriculum | Grade | Tavoite rows | Sisaltoalue rows | Total |",
        "|---|---:|---:|---:|---:|",
    ]
    for (label, grade) in sorted(counts.keys(), key=lambda x: (x[0], x[1])):
        tavoite = counts[(label, grade)]["tavoite"]
        sisalto = counts[(label, grade)]["sisaltoalue"]
        lines.append(f"| {label} | {grade} | {tavoite} | {sisalto} | {tavoite + sisalto} |")

    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- One row = one auditable evidence item linked to source path + section path.",
            "- `topic_candidate_text` is language-preferred (`fi`/`sv`) with deterministic fallback.",
            "- No semantic clustering is done in this pass.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    rows: list[dict[str, Any]] = []
    for spec in SOURCES:
        rows.extend(extract_for_source(spec))
    rows.sort(key=lambda r: (r["label"], r["grade"], r["evidence_type"], r["topic_candidate_text"]))

    ensure_parent(OUTPUT_JSONL)
    with OUTPUT_JSONL.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True))
            handle.write("\n")

    ensure_parent(OUTPUT_MD)
    OUTPUT_MD.write_text(render_summary(rows), encoding="utf-8")

    print(f"Wrote {len(rows)} rows to {OUTPUT_JSONL}")
    print(f"Wrote summary markdown to {OUTPUT_MD}")


if __name__ == "__main__":
    main()
