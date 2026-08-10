from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
RAW_ROOT = ROOT / "data" / "raw"
PARSED_ROOT = ROOT / "data" / "parsed"
RETRIEVAL_LOG_PATH = RAW_ROOT / "retrieval_log.jsonl"
PARSED_OUTPUT_PATH = PARSED_ROOT / "parsed_records.jsonl"


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def canonical_json_bytes(payload: Any) -> bytes:
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sanitize_piece(value: str | None) -> str:
    if not value:
        return "unknown"
    cleaned = "".join(ch if ch.isalnum() or ch in ("-", "_") else "_" for ch in value.strip().lower())
    cleaned = cleaned.strip("_")
    return cleaned or "unknown"


def deterministic_raw_filename(upstream_id: str | None, source_url: str) -> str:
    if upstream_id:
        return f"{sanitize_piece(upstream_id)}.json"
    return f"url_{sha256_hex(source_url.encode('utf-8'))[:16]}.json"


def deterministic_raw_path(source_system: str, collection: str, upstream_id: str | None, source_url: str) -> Path:
    return (
        RAW_ROOT
        / sanitize_piece(source_system)
        / sanitize_piece(collection)
        / deterministic_raw_filename(upstream_id, source_url)
    )


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def append_jsonl(path: Path, record: dict[str, Any]) -> None:
    ensure_parent(path)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True))
        handle.write("\n")


@dataclass
class FetchResult:
    payload: Any
    status: int
    final_url: str


def fetch_json(source_url: str, timeout_seconds: int = 30) -> FetchResult:
    request = Request(
        source_url,
        headers={
            "Accept": "application/json",
            "User-Agent": "curriculum-database-mvp/0.1 (+local research use)",
        },
    )
    try:
        with urlopen(request, timeout=timeout_seconds) as response:
            status = int(getattr(response, "status", 200))
            final_url = str(getattr(response, "url", source_url))
            raw = response.read()
    except HTTPError as exc:
        raise RuntimeError(f"HTTP error {exc.code} for {source_url}") from exc
    except URLError as exc:
        raise RuntimeError(f"Network error for {source_url}: {exc.reason}") from exc

    try:
        payload = json.loads(raw.decode("utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Response from {source_url} was not valid JSON.") from exc
    return FetchResult(payload=payload, status=status, final_url=final_url)


def persist_raw_json(raw_path: Path, payload: Any) -> str:
    ensure_parent(raw_path)
    bytes_out = canonical_json_bytes(payload)
    raw_path.write_bytes(bytes_out)
    return sha256_hex(bytes_out)


def fetch_url_command(args: argparse.Namespace) -> None:
    result = fetch_json(args.source_url, timeout_seconds=args.timeout_seconds)
    raw_path = deterministic_raw_path(
        source_system=args.source_system,
        collection=args.collection,
        upstream_id=args.upstream_id,
        source_url=result.final_url,
    )
    digest = persist_raw_json(raw_path, result.payload)

    log_record = {
        "source_system": args.source_system,
        "source_url": result.final_url,
        "retrieved_at_utc": utc_now_iso(),
        "http_status": result.status,
        "content_sha256": digest,
        "raw_path": str(raw_path.relative_to(ROOT)).replace("\\", "/"),
        "upstream_id": args.upstream_id,
        "language": args.language,
        "education_level": args.education_level,
        "scope": args.scope,
    }
    append_jsonl(RETRIEVAL_LOG_PATH, log_record)

    print(f"Saved raw JSON to: {raw_path}")
    print(f"Logged provenance to: {RETRIEVAL_LOG_PATH}")


def walk_text_nodes(node: Any, section_path: list[str]) -> Iterable[tuple[list[str], str]]:
    if isinstance(node, dict):
        for key in sorted(node.keys()):
            value = node[key]
            next_path = section_path + [str(key)]
            if isinstance(value, str) and value.strip():
                yield (next_path, value.strip())
            else:
                yield from walk_text_nodes(value, next_path)
    elif isinstance(node, list):
        for idx, value in enumerate(node):
            next_path = section_path + [f"[{idx}]"]
            if isinstance(value, str) and value.strip():
                yield (next_path, value.strip())
            else:
                yield from walk_text_nodes(value, next_path)


def stable_record_id(source_raw_path: str, section_path: list[str], text: str) -> str:
    base = "|".join([source_raw_path, "/".join(section_path), text])
    return sha256_hex(base.encode("utf-8"))


def parse_json_command(args: argparse.Namespace) -> None:
    raw_path = Path(args.raw_file)
    if not raw_path.is_absolute():
        raw_path = ROOT / raw_path
    if not raw_path.exists():
        raise RuntimeError(f"Raw file does not exist: {raw_path}")

    payload = json.loads(raw_path.read_text(encoding="utf-8"))
    source_raw_path = str(raw_path.relative_to(ROOT)).replace("\\", "/")

    records: list[dict[str, Any]] = []
    for section_path, text in walk_text_nodes(payload, []):
        record = {
            "record_id": stable_record_id(source_raw_path, section_path, text),
            "source_raw_path": source_raw_path,
            "source_system": args.source_system,
            "curriculum_id": args.curriculum_id,
            "language": args.language,
            "education_level": args.education_level,
            "scope": args.scope,
            "section_path": section_path,
            "text": text,
        }
        records.append(record)

    records.sort(key=lambda r: (r["section_path"], r["record_id"]))

    ensure_parent(PARSED_OUTPUT_PATH)
    with PARSED_OUTPUT_PATH.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True))
            handle.write("\n")

    print(f"Wrote {len(records)} parsed records to: {PARSED_OUTPUT_PATH}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="First-pass curriculum MVP pipeline.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    fetch_parser = subparsers.add_parser("fetch-url", help="Fetch one JSON URL to raw storage with provenance.")
    fetch_parser.add_argument("--source-url", required=True)
    fetch_parser.add_argument("--source-system", default="eperusteet")
    fetch_parser.add_argument("--collection", default="manual")
    fetch_parser.add_argument("--upstream-id")
    fetch_parser.add_argument("--language")
    fetch_parser.add_argument("--education-level")
    fetch_parser.add_argument("--scope", choices=["national", "local"])
    fetch_parser.add_argument("--timeout-seconds", type=int, default=30)
    fetch_parser.set_defaults(func=fetch_url_command)

    parse_parser = subparsers.add_parser("parse-json", help="Parse one raw JSON file into deterministic JSONL.")
    parse_parser.add_argument("--raw-file", required=True)
    parse_parser.add_argument("--source-system", default="eperusteet")
    parse_parser.add_argument("--curriculum-id")
    parse_parser.add_argument("--language")
    parse_parser.add_argument("--education-level")
    parse_parser.add_argument("--scope", choices=["national", "local"])
    parse_parser.set_defaults(func=parse_json_command)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
