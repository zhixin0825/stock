"""Offline unit tests with SYNTHETIC fixtures only, never research observations.

All example firms, recommendations and prices below are invented solely to test
validation. They are not collected data and must never enter data/ or reports/.
The tests make no network requests and do not write research output files.
"""
from copy import deepcopy
from decimal import Decimal
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts import phase1


SYNTHETIC_MANIFEST = {
    "raw_path": "tests/SYNTHETIC_UNIT_FIXTURE_ONLY",
    "sha256": "0" * 64,
    "fetched_at_utc": "2025-01-07T12:00:00+00:00",
}


def synthetic_events():
    """Return freshly allocated fake inputs, clearly separate from real data."""
    common = {
        "company": "SYNTHETIC UNIT FIXTURE — NOT RESEARCH DATA",
        "due_date": "2025-12-31",
        "horizon_note": "Synthetic validation fixture only",
        "source_name": "Synthetic unit fixture",
        "status": "open",
    }
    return [
        dict(common, firm="Synthetic Fixture Firm A", ticker="ZZFIXTURE",
             rating_as_published="Buy", target="130.00", said_date="2025-01-03",
             source_url="https://example.invalid/synthetic-fixture/1"),
        dict(common, firm="Synthetic Fixture Firm B", ticker="IBM",
             rating_as_published="Neutral", target="155", said_date="2025-01-02",
             source_url="https://example.invalid/synthetic-fixture/2"),
        dict(common, firm="Synthetic Fixture Firm A", ticker="IBM",
             rating_as_published="Forecast withheld", target="120.50", said_date="2025-01-06",
             source_url="https://example.invalid/synthetic-fixture/3"),
    ]


def synthetic_prices():
    """Fake Alpha Vantage-shaped payload; numbers are not market observations."""
    return {
        "Meta Data": {"2. Symbol": "IBM", "5. Time Zone": "US/Eastern"},
        "Time Series (Daily)": {
            # Deliberately newest first to exercise deterministic chronological output.
            "2025-01-06": {
                "1. open": "208.0000", "2. high": "212.0000", "3. low": "205.0000",
                "4. close": "210.0000", "5. adjusted close": "189.0000",
                "6. volume": "1000", "7. dividend amount": "0.0000",
                "8. split coefficient": "1.0",
            },
            "2025-01-03": {
                "1. open": "198.0000", "2. high": "205.0000", "3. low": "195.0000",
                "4. close": "200.0000", "5. adjusted close": "190.0000",
                "6. volume": "2000", "7. dividend amount": "0.0000",
                "8. split coefficient": "1.0",
            },
        },
    }


class RatingTests(unittest.TestCase):
    def test_explicit_mapping_and_whitespace(self):
        cases = {"  BUY  ": "Buy", "Strong-Buy": "Buy", "outperform": "Buy",
                 "Equal-Weight": "Hold", "Market Perform": "Hold",
                 "underperform": "Sell", "SELL": "Sell"}
        for raw, expected in cases.items():
            with self.subTest(raw=raw):
                self.assertEqual(phase1.normalize_rating(raw), expected)

    def test_unknown_text_never_defaults_to_hold_or_substring_match(self):
        for raw in ("", "Unrated", "Forecast withheld", "Not Buy", "Rebuy",
                    "Buy (review pending)", "Initiated"):
            with self.subTest(raw=raw):
                self.assertEqual(phase1.normalize_rating(raw), "")


class EventTests(unittest.TestCase):
    def setUp(self):
        self.raw = synthetic_events()
        self.events = phase1.normalize_events(self.raw, SYNTHETIC_MANIFEST)

    def test_no_drops_and_unknown_rating_is_retained(self):
        self.assertEqual(len(self.events), len(self.raw))
        by_url = {row["source_url"]: row for row in self.events}
        for raw in self.raw:
            event = by_url[raw["source_url"]]
            self.assertEqual(event["ticker"], raw["ticker"])
            self.assertEqual(event["publication_date"], raw["said_date"])
            self.assertEqual(event["price_target"], raw["target"])
        unknown = by_url["https://example.invalid/synthetic-fixture/3"]
        self.assertEqual(unknown["rating_raw"], "Forecast withheld")
        self.assertEqual(unknown["rating_normalized"], "")
        self.assertEqual(phase1.validate_events(self.events, self.raw), [])

    def test_source_missing_identities_and_timestamps_stay_missing(self):
        for event in self.events:
            for field in ("analyst_name", "previous_price_target", "published_at_utc", "target_currency"):
                self.assertEqual(event[field], "")
            self.assertEqual(event["analyst_identity_level"], "firm_only")
            self.assertEqual(event["availability_timestamp_known"], "false")
            self.assertEqual(event["timing_precision"], "date")

    def test_normalization_is_deterministic_under_shuffled_input(self):
        before = deepcopy(self.raw)
        for rows in (list(reversed(self.raw)), self.raw[1:] + self.raw[:1]):
            self.assertEqual(phase1.normalize_events(rows, SYNTHETIC_MANIFEST), self.events)
        self.assertEqual(self.raw, before)
        self.assertEqual(
            phase1.csv_bytes(self.events, phase1.EVENT_FIELDS),
            phase1.csv_bytes(phase1.normalize_events(self.raw, SYNTHETIC_MANIFEST), phase1.EVENT_FIELDS),
        )

    def test_dropped_row_and_duplicate_ids_fail(self):
        self.assertTrue(phase1.validate_events(self.events[:-1], self.raw))
        corrupted = deepcopy(self.events)
        corrupted[1] = deepcopy(corrupted[0])
        self.assertTrue(any("Duplicate event_id" in error
                            for error in phase1.validate_events(corrupted, self.raw)))

    def test_nonfinite_or_nonpositive_targets_fail(self):
        for value in ("0", "-1", "NaN", "Infinity", "-Infinity", ""):
            with self.subTest(value=value):
                corrupted = deepcopy(self.events)
                corrupted[0]["price_target"] = value
                self.assertTrue(any("price target" in error
                                    for error in phase1.validate_events(corrupted, self.raw)))

    def test_invalid_calendar_dates_fail(self):
        for value in ("2025-02-30", "2025-2-03", "not-a-date"):
            with self.subTest(value=value):
                corrupted = deepcopy(self.events)
                corrupted[0]["publication_date"] = value
                self.assertTrue(any("date" in error
                                    for error in phase1.validate_events(corrupted, self.raw)))

    def test_unsupported_source_fields_cannot_be_invented(self):
        cases = {
            "analyst_name": "Synthetic Named Analyst",
            "analyst_identity_level": "individual",
            "previous_price_target": "100",
            "published_at_utc": "2025-01-03T12:00:00Z",
            "availability_timestamp_known": "true",
            "target_currency": "USD",
            "timing_precision": "timestamp",
        }
        for field, value in cases.items():
            with self.subTest(field=field):
                corrupted = deepcopy(self.events)
                corrupted[0][field] = value
                self.assertTrue(phase1.validate_events(corrupted, self.raw))

    def test_valid_looking_values_must_match_raw_source(self):
        cases = {"publication_date": "2025-01-04", "price_target": "999",
                 "ticker": "OTHERFIXTURE", "source_url": "https://example.invalid/changed-source"}
        for field, value in cases.items():
            with self.subTest(field=field):
                corrupted = deepcopy(self.events)
                corrupted[0][field] = value
                self.assertTrue(phase1.validate_events(corrupted, self.raw))

    def test_normalized_rating_cannot_disagree_with_raw_rating(self):
        corrupted = deepcopy(self.events)
        corrupted[0]["rating_normalized"] = "Sell"
        self.assertTrue(any("rating mapping" in error
                            for error in phase1.validate_events(corrupted, self.raw)))


class PriceTests(unittest.TestCase):
    def setUp(self):
        self.payload = synthetic_prices()
        self.prices = phase1.parse_prices(self.payload, SYNTHETIC_MANIFEST)

    def test_preserves_raw_and_adjusted_close_with_exact_factor(self):
        self.assertEqual(phase1.validate_prices(self.prices), [])
        self.assertEqual([row["date"] for row in self.prices], ["2025-01-03", "2025-01-06"])
        self.assertEqual(self.prices[0]["close"], "200.0000")
        self.assertEqual(self.prices[0]["adjusted_close"], "190.0000")
        self.assertEqual(Decimal(self.prices[0]["adjustment_factor"]), Decimal("0.95"))
        for row in self.prices:
            self.assertEqual(row["currency"], "USD")
            self.assertEqual(row["exchange_timezone"], "US/Eastern")
            self.assertEqual(row["raw_sha256"], SYNTHETIC_MANIFEST["sha256"])

    def test_parser_is_deterministic_and_does_not_mutate_payload(self):
        before = deepcopy(self.payload)
        self.assertEqual(phase1.parse_prices(self.payload, SYNTHETIC_MANIFEST), self.prices)
        self.assertEqual(self.payload, before)

    def test_unsupported_symbol_is_not_silently_renamed(self):
        self.payload["Meta Data"]["2. Symbol"] = "OTHERFIXTURE"
        with self.assertRaises(ValueError):
            phase1.parse_prices(self.payload, SYNTHETIC_MANIFEST)

    def test_duplicate_price_keys_fail(self):
        corrupted = deepcopy(self.prices)
        corrupted.append(deepcopy(corrupted[-1]))
        self.assertTrue(any("duplicate price key" in error
                            for error in phase1.validate_prices(corrupted)))

    def test_dates_must_be_valid_and_sorted(self):
        self.assertTrue(any("dates not sorted" in error
                            for error in phase1.validate_prices(list(reversed(self.prices)))))
        corrupted = deepcopy(self.prices)
        corrupted[0]["date"] = "2025-02-30"
        self.assertTrue(any("invalid date" in error for error in phase1.validate_prices(corrupted)))

    def test_nonfinite_or_nonpositive_price_fields_fail(self):
        fields = ("open", "high", "low", "close", "adjusted_close",
                  "split_coefficient", "adjustment_factor")
        for field in fields:
            for value in ("NaN", "Infinity", "0", "-1"):
                with self.subTest(field=field, value=value):
                    corrupted = deepcopy(self.prices)
                    corrupted[0][field] = value
                    self.assertTrue(any("nonfinite or nonpositive" in error
                                        for error in phase1.validate_prices(corrupted)))

    def test_invalid_volume_or_dividend_fails(self):
        for field in ("volume", "dividend_amount"):
            for value in ("NaN", "-1"):
                with self.subTest(field=field, value=value):
                    corrupted = deepcopy(self.prices)
                    corrupted[0][field] = value
                    self.assertTrue(any("volume/dividend" in error
                                        for error in phase1.validate_prices(corrupted)))

    def test_inconsistent_ohlc_or_adjustment_factor_fails(self):
        for field, value, expected in (("high", "199", "OHLC bounds"),
                                       ("adjustment_factor", "0.8", "adjustment factor mismatch")):
            with self.subTest(field=field):
                corrupted = deepcopy(self.prices)
                corrupted[0][field] = value
                self.assertTrue(any(expected in error for error in phase1.validate_prices(corrupted)))

    def test_missing_currency_or_timezone_fails(self):
        for field in ("currency", "exchange_timezone"):
            with self.subTest(field=field):
                corrupted = deepcopy(self.prices)
                corrupted[0][field] = ""
                self.assertTrue(any("price units" in error for error in phase1.validate_prices(corrupted)))


if __name__ == "__main__":
    unittest.main()
