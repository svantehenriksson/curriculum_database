from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

if __package__ in (None, ""):
    # Allow `python scripts/recon_openapi.py` from repository root.
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.mvp_pipeline import ensure_parent, sanitize_piece, sha256_hex


ROOT = Path(__file__).resolve().parents[1]
OPENAPI_RAW_ROOT = ROOT / "data" / "raw" / "eperusteet" / "openapi"
OPENAPI_RECON_LOG = OPENAPI_RAW_ROOT / "recon_results.jsonl"


DEFAULT_CANDIDATES = [
    "https://opetushallitus.github.io/eperusteet",
    "https://opetushallitus.github.io/eperusteet/swagger.json",
    "https://opetushallitus.github.io/eperusteet/openapi.json",
    "https://eperusteet.opintopolku.fi/api/external/docs",
    "https://eperusteet.opintopolku.fi/api/external/swagger.json",
    "https://eperusteet.opintopolku.fi/api/external/openapi.json",
]


@dataclass
class ProbeResult:
    url: str
    retrieved_at_utc: str
    ok: bool
    http_status: int | None
    content_type: str | None
    bytes_received: int | None
    error: str | None
    saved_raw_path: str | None
    content_sha256: str | None


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def probe_url(url: str, timeout_seconds: int) -> tuple[ProbeResult, bytes | None]:
    request = Request(
        url,
        headers={
            "Accept": "application/json, text/html;q=0.9, */*;q=0.1",
            "User-Agent": "curriculum-database-recon/0.1 (+local research use)",
        },
    )
    try:
        with urlopen(request, timeout=timeout_seconds) as response:
            status = int(getattr(response, "status", 200))
            content_type = str(response.headers.get("Content-Type", ""))
            body = response.read()
            return (
                ProbeResult(
                    url=url,
                    retrieved_at_utc=utc_now_iso(),
                    ok=True,
                    http_status=status,
                    content_type=content_type,
                    bytes_received=len(body),
                    error=None,
                    saved_raw_path=None,
                    content_sha256=None,
                ),
                body,
            )
    except HTTPError as exc:
        return (
            ProbeResult(
                url=url,
                retrieved_at_utc=utc_now_iso(),
                ok=False,
                http_status=exc.code,
                content_type=None,
                bytes_received=None,
                error=f"HTTPError: {exc.code}",
                saved_raw_path=None,
                content_sha256=None,
            ),
            None,
        )
    except URLError as exc:
        return (
            ProbeResult(
                url=url,
                retrieved_at_utc=utc_now_iso(),
                ok=False,
                http_status=None,
                content_type=None,
                bytes_received=None,
                error=f"URLError: {exc.reason}",
                saved_raw_path=None,
                content_sha256=None,
            ),
            None,
        )


def raw_filename_for_url(url: str, suffix: str) -> str:
    parsed = urlparse(url)
    host = sanitize_piece(parsed.netloc)
    path = sanitize_piece(parsed.path or "root")
    tag = sha256_hex(url.encode("utf-8"))[:10]
    return f"{host}__{path}__{tag}.{suffix}"


def save_raw_payload(url: str, body: bytes, content_type: str) -> tuple[str | None, str | None]:
    content_type_lower = content_type.lower()
    if "json" in content_type_lower:
        suffix = "json"
    elif "html" in content_type_lower:
        suffix = "html"
    else:
        return None, None

    digest = sha256_hex(body)
    raw_path = OPENAPI_RAW_ROOT / raw_filename_for_url(url, suffix)
    ensure_parent(raw_path)
    raw_path.write_bytes(body)
    rel = str(raw_path.relative_to(ROOT)).replace("\\", "/")
    return rel, digest


def append_jsonl(path: Path, record: dict[str, Any]) -> None:
    ensure_parent(path)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True))
        handle.write("\n")


def run_recon(candidates: list[str], timeout_seconds: int) -> None:
    print(f"Probing {len(candidates)} candidate URLs...")
    for url in candidates:
        result, body = probe_url(url, timeout_seconds=timeout_seconds)

        if result.ok and body is not None and result.content_type is not None:
            saved_path, digest = save_raw_payload(url, body, result.content_type)
            result.saved_raw_path = saved_path
            result.content_sha256 = digest

        record = {
            "url": result.url,
            "retrieved_at_utc": result.retrieved_at_utc,
            "ok": result.ok,
            "http_status": result.http_status,
            "content_type": result.content_type,
            "bytes_received": result.bytes_received,
            "error": result.error,
            "saved_raw_path": result.saved_raw_path,
            "content_sha256": result.content_sha256,
        }
        append_jsonl(OPENAPI_RECON_LOG, record)

        status_text = result.http_status if result.http_status is not None else "n/a"
        saved = result.saved_raw_path if result.saved_raw_path else "-"
        print(f"- {url} -> status={status_text}, json_saved={saved}")

    print(f"Wrote recon log to: {OPENAPI_RECON_LOG}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Tiny ePerusteet OpenAPI endpoint recon.")
    parser.add_argument("--timeout-seconds", type=int, default=20)
    parser.add_argument("--url", action="append", help="Custom candidate URL. Repeat for multiple.")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    candidates = args.url if args.url else DEFAULT_CANDIDATES
    run_recon(candidates=candidates, timeout_seconds=args.timeout_seconds)


if __name__ == "__main__":
    main()
