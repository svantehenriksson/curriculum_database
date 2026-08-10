from pathlib import Path
import json
import tempfile

from scripts.mvp_pipeline import (
    canonical_json_bytes,
    deterministic_raw_path,
    sha256_hex,
    stable_record_id,
    walk_text_nodes,
)


def test_canonical_json_bytes_deterministic_key_order() -> None:
    payload_a = {"b": 2, "a": 1}
    payload_b = {"a": 1, "b": 2}
    assert canonical_json_bytes(payload_a) == canonical_json_bytes(payload_b)


def test_deterministic_raw_path_same_inputs_same_path() -> None:
    first = deterministic_raw_path("eperusteet", "perusteet", "123456", "https://example.org/a")
    second = deterministic_raw_path("eperusteet", "perusteet", "123456", "https://example.org/a")
    assert first == second


def test_stable_record_id_same_inputs_same_output() -> None:
    rid_1 = stable_record_id("data/raw/eperusteet/x.json", ["root", "node"], "hello")
    rid_2 = stable_record_id("data/raw/eperusteet/x.json", ["root", "node"], "hello")
    assert rid_1 == rid_2
    assert len(rid_1) == 64


def test_walk_text_nodes_is_deterministic_and_complete() -> None:
    payload = {
        "z": "final",
        "a": {"nested": "value"},
        "list": ["x", {"m": "y"}],
    }
    first = list(walk_text_nodes(payload, []))
    second = list(walk_text_nodes(payload, []))
    assert first == second
    texts = [text for _, text in first]
    assert sorted(texts) == ["final", "value", "x", "y"]


def test_sha256_matches_written_canonical_json() -> None:
    payload = {"k": "v", "n": 1}
    data = canonical_json_bytes(payload)
    digest = sha256_hex(data)
    with tempfile.TemporaryDirectory() as tmp_dir:
        path = Path(tmp_dir) / "sample.json"
        path.write_bytes(data)
        reloaded = path.read_bytes()
    assert sha256_hex(reloaded) == digest
