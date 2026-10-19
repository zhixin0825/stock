"""Offline checks using SYNTHETIC fixtures, never actual analyst observations.

The names, ratings, targets and prices here are invented for validation only.
These fixtures are not research data, make no network requests, and must not be
copied into data/, reports/, or the private research sample.
"""
from copy import deepcopy
from decimal import Decimal
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts import named_sample


SYNTHETIC_MANIFEST = {
    "raw_path": "tests/SYNTHETIC_NAMED_UNIT_FIXTURE_ONLY",
    "sha256": "0" * 64,
    "fetched_at_utc": "2026-10-19T00:00:00+00:00",
    "ticker": "AAPL",
}


def synthetic_event(day="2026-01-02", analyst="SYNTHETIC FIXTURE ANALYST A",
                    broker="99001", before="90", after="100"):
    """Return one fake source-shaped row, separate from collected observations."""
    return {
        "date": day,
        "analyst": analyst,
        "broker_number": broker,
        "rating_before": "hold",
        "rating_after": "buy",
        "price_target_before": before,
        "price_target_after": after,
        "pt_after_nominal": after,
        "split_ratio": "1",
        "close_price_adj": "95",
        "close_nominal_on_date": "95",
        "target_direction": "up",
        "target_met": "yes",
        "date_met": "2026-12-31",
        "days_to_hit": "363",
    }


def normalize(rows):
    return named_sample.normalize_events(rows, SYNTHETIC_MANIFEST)


class NamedNormalizationTests(unittest.TestCase):
    def setUp(self):
        first = synthetic_event()
        self.raw = [first, deepcopy(first), synthetic_event("2026-01-05", before="100", after="110")]
        self.events = normalize(self.raw)

    def test_all_rows_retained_and_exact_duplicates_have_one_primary(self):
        self.assertEqual(len(self.events), len(self.raw))
        self.assertEqual(len({row["record_id"] for row in self.events}), len(self.raw))
        primaries = [row for row in self.events if row["is_primary_record"] == "true"]
        duplicates = [row for row in self.events if row["is_primary_record"] == "false"]
        self.assertEqual(len(primaries), 2)
        self.assertEqual(len(duplicates), 1)
        primary_ids = {row["record_id"]: row for row in primaries}
        for row in duplicates:
            primary = primary_ids[row["duplicate_of_record_id"]]
            self.assertEqual(row["event_key"], primary["event_key"])
        self.assertEqual(named_sample.validate_events(self.events, self.raw, SYNTHETIC_MANIFEST), [])

    def test_outcome_labels_do_not_enter_predictor_records(self):
        outcomes = {"target_met", "date_met", "days_to_hit"}
        for row in self.events:
            self.assertTrue(outcomes.isdisjoint(row))
            self.assertEqual(row["source_url"], "")
            self.assertEqual(row.get("published_at_utc", ""), "")
        self.assertEqual(self.events[0]["rating_normalized"], "Buy")

    def test_missing_identity_or_rating_is_not_invented_or_dropped(self):
        raw = [synthetic_event(analyst="", broker="")]
        raw[0]["rating_after"] = "unrecognized fixture rating"
        events = normalize(raw)
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0]["analyst_name"], "")
        self.assertEqual(events[0]["broker_id"], "")
        self.assertEqual(events[0]["rating_normalized"], "")

    def test_split_adjusted_and_nominal_values_stay_separate(self):
        raw = [synthetic_event(before="90", after="100")]
        raw[0].update(pt_after_nominal="200", split_ratio="2",
                      close_price_adj="95", close_nominal_on_date="190")
        row = normalize(raw)[0]
        self.assertEqual(Decimal(row["target_after_adjusted"]), Decimal("100"))
        self.assertEqual(Decimal(row["target_after_nominal"]), Decimal("200"))
        self.assertEqual(Decimal(row["split_ratio"]), Decimal("2"))
        self.assertEqual(Decimal(row["source_close_adjusted"]), Decimal("95"))
        self.assertEqual(Decimal(row["source_close_nominal"]), Decimal("190"))
        self.assertEqual(named_sample.validate_events([row], raw, SYNTHETIC_MANIFEST), [])

    def test_normalization_replays_without_mutating_input(self):
        before = deepcopy(self.raw)
        self.assertEqual(normalize(self.raw), self.events)
        self.assertEqual(self.raw, before)

    def test_normalized_fields_must_match_source(self):
        cases = {"publication_date": "2026-01-03", "analyst_name": "INVENTED FIXTURE PERSON",
                 "broker_id": "99099", "target_after_adjusted": "999",
                 "source_url": "https://example.invalid/invented-article"}
        for field, value in cases.items():
            with self.subTest(field=field):
                corrupted = deepcopy(self.events)
                corrupted[0][field] = value
                self.assertTrue(named_sample.validate_events(corrupted, self.raw, SYNTHETIC_MANIFEST))

    def test_invalid_dates_and_numeric_source_values_fail(self):
        cases = {"date": ("2026-02-30", "2026-1-2"),
                 "price_target_after": ("NaN", "Infinity", "0", "-1"),
                 "price_target_before": ("NaN", "-1"),
                 "pt_after_nominal": ("NaN", "-1"),
                 "split_ratio": ("NaN", "0", "-1"),
                 "close_price_adj": ("NaN", "-1"),
                 "close_nominal_on_date": ("NaN", "-1")}
        for field, values in cases.items():
            for value in values:
                with self.subTest(field=field, value=value):
                    raw = [synthetic_event()]
                    raw[0][field] = value
                    self.assertTrue(named_sample.validate_events(normalize(raw), raw, SYNTHETIC_MANIFEST))

    def test_missing_targets_remain_valid_missing_values(self):
        raw = [synthetic_event(before="", after="")]
        events = normalize(raw)
        self.assertEqual(events[0]["target_before_adjusted"], "")
        self.assertEqual(events[0]["target_after_adjusted"], "")
        self.assertEqual(named_sample.validate_events(events, raw, SYNTHETIC_MANIFEST), [])

    def test_missing_row_and_duplicate_record_ids_fail(self):
        self.assertTrue(named_sample.validate_events(self.events[:-1], self.raw, SYNTHETIC_MANIFEST))
        corrupted = deepcopy(self.events)
        corrupted[1]["record_id"] = corrupted[0]["record_id"]
        self.assertTrue(named_sample.validate_events(corrupted, self.raw, SYNTHETIC_MANIFEST))


class ObservedPairTests(unittest.TestCase):
    def pairs(self, raw):
        return named_sample.derive_revision_pairs(normalize(raw))

    def test_adjacent_observations_link_when_prior_target_matches(self):
        raw = [synthetic_event("2026-01-06", before="110", after="120"),
               synthetic_event("2026-01-02", before="90", after="100"),
               synthetic_event("2026-01-05", before="100", after="110")]
        pairs = self.pairs(raw)
        self.assertEqual(len(pairs), 2)
        self.assertEqual([row["status"] for row in pairs],
                         ["linked_observed_pair", "linked_observed_pair"])

    def test_exact_duplicate_does_not_create_same_day_ambiguity(self):
        first = synthetic_event()
        pairs = self.pairs([first, deepcopy(first), synthetic_event("2026-01-05", before="100", after="110")])
        self.assertEqual(len(pairs), 1)
        self.assertEqual(pairs[0]["status"], "linked_observed_pair")

    def test_mismatching_reported_prior_target_is_not_a_link(self):
        pairs = self.pairs([synthetic_event(), synthetic_event("2026-01-05", before="99", after="110")])
        self.assertEqual([row["status"] for row in pairs], ["prior_target_mismatch"])

    def test_missing_targets_cannot_create_a_link(self):
        for previous_after, successor_before in (("", "100"), ("100", "")):
            with self.subTest(previous_after=previous_after, successor_before=successor_before):
                pairs = self.pairs([synthetic_event(after=previous_after),
                                    synthetic_event("2026-01-05", before=successor_before, after="110")])
                self.assertEqual([row["status"] for row in pairs], ["missing_target"])

    def test_distinct_same_day_events_have_no_inferred_order(self):
        raw = [synthetic_event(), synthetic_event(after="105"),
               synthetic_event("2026-01-05", before="105", after="110"),
               synthetic_event("2026-01-06", before="110", after="120")]
        pairs = self.pairs(raw)
        self.assertEqual(len(pairs), 2)
        self.assertEqual([row["status"] for row in pairs],
                         ["ambiguous_same_day", "linked_observed_pair"])

    def test_same_name_at_another_broker_is_a_separate_group(self):
        pairs = self.pairs([synthetic_event(),
                            synthetic_event("2026-01-05", broker="99002", before="100", after="110")])
        self.assertEqual(pairs, [])

    def test_different_analysts_at_one_broker_are_separate_groups(self):
        pairs = self.pairs([synthetic_event(),
                            synthetic_event("2026-01-05", analyst="SYNTHETIC FIXTURE ANALYST B", before="100", after="110")])
        self.assertEqual(pairs, [])

    def test_missing_name_or_broker_does_not_form_identity_group(self):
        for field in ("analyst", "broker_number"):
            with self.subTest(field=field):
                raw = [synthetic_event(), synthetic_event("2026-01-05", before="100", after="110")]
                for row in raw:
                    row[field] = ""
                self.assertEqual(self.pairs(raw), [])

    def test_matching_names_and_brokers_on_other_tickers_are_separate(self):
        first = normalize([synthetic_event()])
        other_manifest = dict(SYNTHETIC_MANIFEST, ticker="OTHERFIXTURE")
        second = named_sample.normalize_events(
            [synthetic_event("2026-01-05", before="100", after="110")], other_manifest)
        self.assertEqual(named_sample.derive_revision_pairs(first + second), [])


if __name__ == "__main__":
    unittest.main()
