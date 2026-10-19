"""Offline EODHD validation checks using SYNTHETIC prices, never market data.

Temporary snapshots are test fixtures only and never enter research outputs.
"""
from decimal import Decimal
import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts import eodhd_prices, phase1


def synthetic_prices():
    return [{"date": "2025-01-02", "open": "99", "high": "102", "low": "98",
             "close": "100", "adjusted_close": "95", "volume": "1000"}]


def synthetic_snapshot(content):
    return {
        "raw_path": ".local-data/raw/eodhd/SYNTHETIC_TEST_ONLY.json",
        "sha256": phase1.sha256(content), "bytes": len(content), "rows": 1,
        "date_min": "2025-01-02", "date_max": "2025-01-02",
        "fetched_at_utc": "2026-10-19T00:00:00+00:00",
    }


class EodhdTests(unittest.TestCase):
    def test_api_error_object_or_empty_daily_response_is_rejected(self):
        for payload in (b'{"error":"synthetic rate-limit response"}', b'[]', b'["invalid record"]'):
            with self.subTest(payload=payload):
                with self.assertRaises(ValueError):
                    eodhd_prices._parse_records(payload, "eod")

    def test_nonfinite_and_nonpositive_prices_are_rejected(self):
        for field in ("open", "high", "low", "close", "adjusted_close"):
            for value in ("NaN", "Infinity", "0", "-1"):
                with self.subTest(field=field, value=value):
                    records = synthetic_prices()
                    records[0][field] = value
                    content = json.dumps(records).encode()
                    try:
                        rows = eodhd_prices._normalized_prices(records, synthetic_snapshot(content))
                    except ValueError:
                        continue
                    self.assertTrue(eodhd_prices.validate_prices(rows))

    def test_snapshot_replay_checks_hash_bytes_and_metadata(self):
        content = json.dumps(synthetic_prices()).encode()
        snapshot = synthetic_snapshot(content)
        with TemporaryDirectory(prefix="stock_SYNTHETIC_test_") as directory:
            root = Path(directory)
            path = root / snapshot["raw_path"]
            path.parent.mkdir(parents=True)
            path.write_bytes(content)
            rows = eodhd_prices.load_prices(root, {"snapshots": {"eod": snapshot}})
            self.assertEqual(len(rows), 1)
            self.assertEqual(Decimal(rows[0]["adjustment_factor"]), Decimal("0.95"))
            self.assertEqual(rows[0]["volume_basis"], "split_adjusted")
            self.assertEqual(rows[0]["dividend_amount"], "")
            self.assertEqual(rows[0]["split_coefficient"], "")
            for field, value in (("sha256", "0" * 64), ("bytes", len(content) + 1),
                                 ("rows", 2), ("date_max", "2025-01-03")):
                with self.subTest(field=field):
                    corrupted = dict(snapshot, **{field: value})
                    with self.assertRaises(ValueError):
                        eodhd_prices.load_prices(root, {"snapshots": {"eod": corrupted}})
            path.write_bytes(content + b" ")
            with self.assertRaises(ValueError):
                eodhd_prices.load_prices(root, {"snapshots": {"eod": snapshot}})

    def test_raw_snapshot_cannot_escape_private_directory(self):
        with TemporaryDirectory(prefix="stock_SYNTHETIC_test_") as directory:
            content = json.dumps(synthetic_prices()).encode()
            snapshot = dict(synthetic_snapshot(content), raw_path="outside-private-directory.json")
            (Path(directory) / snapshot["raw_path"]).write_bytes(content)
            with self.assertRaises(ValueError):
                eodhd_prices._checked_raw(directory, snapshot)

    def test_empty_action_lists_stay_empty_and_invalid_actions_fail(self):
        self.assertEqual(eodhd_prices._parse_records(b"[]", "splits"), [])
        self.assertEqual(eodhd_prices._parse_records(b"[]", "dividends"), [])
        cases = (("splits", {"date": "2025-01-02", "split": "0/1"}),
                 ("splits", {"date": "2025-01-02", "split": "NaN/1"}),
                 ("dividends", {"date": "2025-01-02", "value": "NaN"}),
                 ("dividends", {"date": "2025-01-02", "value": "-1"}))
        for kind, record in cases:
            with self.subTest(kind=kind, record=record):
                with self.assertRaises(ValueError):
                    eodhd_prices._parse_records(json.dumps([record]).encode(), kind)


if __name__ == "__main__":
    unittest.main()
