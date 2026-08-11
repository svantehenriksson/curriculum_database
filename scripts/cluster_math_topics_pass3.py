from __future__ import annotations

import html
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
INPUT_JSONL = ROOT / "data" / "derived" / "math_topic_candidates_7_9_pass2.jsonl"
OUTPUT_DIR = ROOT / "data" / "derived"
OUTPUT_NORMALIZED_JSONL = OUTPUT_DIR / "math_topic_candidates_7_9_pass3_normalized.jsonl"
OUTPUT_MATRIX_JSONL = OUTPUT_DIR / "math_topic_consensus_matrix_7_9_pass3.jsonl"
OUTPUT_MD = OUTPUT_DIR / "math_topic_consensus_7_9_pass3.md"


RULES: list[tuple[str, str, str]] = [
    ("math.number.percent", "high", "prosent|percent|procentrak|procent"),
    ("math.number.real_numbers", "high", "reaalil|reella tal|rationaal|irrationaal"),
    ("math.number.negative_numbers", "high", "negatiiv|negativa tal"),
    ("math.algebra.expressions", "high", "lauseke|uttryck|polynom|monomi"),
    ("math.algebra.equations_linear", "high", "ensimmaisen asteen yhta|forstagradsekvation|lineaarinen yhta"),
    ("math.algebra.equations_quadratic_intro", "high", "toisen asteen yhta|andragradsekvation"),
    ("math.algebra.inequalities", "high", "epa[ae]yhta|olikhet|olikn"),
    ("math.algebra.proportionality", "high", "verrannoll|proportion|proportionalitet"),
    ("math.algebra.functions", "high", "funktio|funktion"),
    ("math.algebra.sequences", "high", "lukujono|talfoljd"),
    ("math.algebra.powers_roots", "high", "potens|juuri|kvadratrot|neli[oö]juuri"),
    ("math.geometry.angles_lines", "high", "kulma|vinkel|suora|raet linje|rat linje"),
    ("math.geometry.polygons", "high", "monikulm|polygon|nelikulm|kolmio|triangel"),
    ("math.geometry.congruence_similarity_scale", "high", "yhtenev|kongruens|samankalta|likformig|mittakaava|skala"),
    ("math.geometry.pythagoras", "high", "pythagora"),
    ("math.geometry.circle", "high", "ympyra|cirkel"),
    ("math.geometry.perimeter_area", "high", "piiri|omkrets|pinta-ala|area"),
    ("math.geometry.volume", "high", "tilavuus|volym"),
    ("math.geometry.transformations", "high", "kierto|peilaus|translaatio|rotation|spegling"),
    ("math.statistics_data", "high", "tilasto|mediaani|keskiarvo|frekvens|statistik"),
    ("math.probability", "high", "todennak|sannolikhet"),
    ("math.financial_math", "high", "korko|laina|alenn|rabatt|ranta"),
    ("math.digital_tools", "medium", "tieto- ja viestintatekni|informations- och kommunikationsteknik|digit"),
    ("math.reasoning_logic", "medium", "loog|logisk|perustel|motivera|paattely|slutsats"),
    ("math.problem_solving", "medium", "ongelmanratk|problemlos|soveltaa matemati|tillampa matematik"),
    ("math.identity_attitude", "low", "minakuva|sjalvbild|itseluottamus|lita pa sig"),
]


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def clean_text(text: str | None) -> str:
    if not text:
        return ""
    decoded = html.unescape(text)
    no_tags = re.sub(r"<[^>]+>", " ", decoded)
    squashed = " ".join(no_tags.split())
    return squashed


def normalize_for_match(text: str) -> str:
    # Remove diacritics and non-alnum to make FI/SV matching robust.
    normalized = unicodedata.normalize("NFKD", text.lower())
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    ascii_text = re.sub(r"[^a-z0-9]+", " ", ascii_text)
    return " ".join(ascii_text.split())


def map_topic(cleaned_text: str) -> tuple[str, str]:
    haystack = normalize_for_match(cleaned_text)
    for canonical_topic, confidence, pattern in RULES:
        if re.search(pattern, haystack):
            return canonical_topic, confidence
    return "math.unclassified", "low"


def load_rows(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def normalize_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for row in rows:
        cleaned = clean_text(row.get("topic_candidate_text"))
        canonical_topic, confidence = map_topic(cleaned)
        normalized = dict(row)
        normalized["topic_candidate_text_clean"] = cleaned
        normalized["canonical_topic"] = canonical_topic
        normalized["canonical_confidence"] = confidence
        out.append(normalized)
    out.sort(
        key=lambda r: (
            r["canonical_topic"],
            r["label"],
            int(r["grade"]),
            r["evidence_type"],
            r["topic_candidate_text_clean"],
        )
    )
    return out


def build_matrix(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    # Local curricula only for consensus percentages.
    local_rows = [r for r in rows if r.get("scope") == "local"]
    local_labels = sorted({str(r["label"]) for r in local_rows})
    total_local = len(local_labels)

    # topic -> grade -> labels
    coverage: dict[str, dict[int, set[str]]] = defaultdict(lambda: defaultdict(set))
    for row in local_rows:
        topic = str(row["canonical_topic"])
        grade = int(row["grade"])
        label = str(row["label"])
        coverage[topic][grade].add(label)

    matrix_rows: list[dict[str, Any]] = []
    for topic in sorted(coverage.keys()):
        row = {
            "canonical_topic": topic,
            "municipalities_observed": total_local,
            "grade_7_count": len(coverage[topic].get(7, set())),
            "grade_8_count": len(coverage[topic].get(8, set())),
            "grade_9_count": len(coverage[topic].get(9, set())),
        }
        for grade in (7, 8, 9):
            count = len(coverage[topic].get(grade, set()))
            pct = (count / total_local * 100.0) if total_local else 0.0
            row[f"grade_{grade}_pct"] = round(pct, 1)
        row["unclassified"] = topic == "math.unclassified"
        matrix_rows.append(row)
    matrix_rows.sort(
        key=lambda r: (
            r["unclassified"],
            -(r["grade_7_count"] + r["grade_8_count"] + r["grade_9_count"]),
            r["canonical_topic"],
        )
    )
    return matrix_rows


def render_md(matrix_rows: list[dict[str, Any]], normalized_rows: list[dict[str, Any]]) -> str:
    lines = [
        "# Math Topic Consensus 7-9 (Pass 3)",
        "",
        "Rule-based FI/SV lexical normalization from pass-2 topic evidence.",
        "",
        "## Coverage Matrix (Local Curricula)",
        "",
        "| Canonical topic | Grade 7 % | Grade 8 % | Grade 9 % |",
        "|---|---:|---:|---:|",
    ]
    for row in matrix_rows[:25]:
        lines.append(
            f"| {row['canonical_topic']} | {row['grade_7_pct']} | "
            f"{row['grade_8_pct']} | {row['grade_9_pct']} |"
        )

    by_topic: dict[str, int] = defaultdict(int)
    for row in normalized_rows:
        by_topic[str(row["canonical_topic"])] += 1

    lines.extend(
        [
            "",
            "## Distribution Notes",
            "",
            f"- Evidence rows normalized: {len(normalized_rows)}",
            f"- Canonical topics (including unclassified): {len(by_topic)}",
            f"- Unclassified rows: {by_topic.get('math.unclassified', 0)}",
            "- Percentages use local curricula only (national excluded from percentage denominator).",
        ]
    )
    return "\n".join(lines) + "\n"


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True))
            handle.write("\n")


def main() -> None:
    rows = load_rows(INPUT_JSONL)
    normalized_rows = normalize_rows(rows)
    matrix_rows = build_matrix(normalized_rows)

    write_jsonl(OUTPUT_NORMALIZED_JSONL, normalized_rows)
    write_jsonl(OUTPUT_MATRIX_JSONL, matrix_rows)

    ensure_parent(OUTPUT_MD)
    OUTPUT_MD.write_text(render_md(matrix_rows, normalized_rows), encoding="utf-8")

    print(f"Wrote {len(normalized_rows)} normalized rows to {OUTPUT_NORMALIZED_JSONL}")
    print(f"Wrote {len(matrix_rows)} matrix rows to {OUTPUT_MATRIX_JSONL}")
    print(f"Wrote summary markdown to {OUTPUT_MD}")


if __name__ == "__main__":
    main()
