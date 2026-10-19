"""Local-only named analyst sample; public outputs contain aggregate coverage only.

Run as python -m scripts.named_sample COMMAND. No performance study is run.
"""
import argparse
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict
import csv
from datetime import date, timedelta, datetime, timezone
from decimal import Decimal
import io
import json
from pathlib import Path
import subprocess
import sys

from scripts import phase1

ROOT = phase1.ROOT
SOURCE_URL = "https://anachart.store/wp-content/uploads/2026/09/AnaChart_AAPL_sample_100_rows.csv"
PERMISSION_URL = "https://anachart.store/free-sample/"
TERMS_URL = "https://anachart.store/terms-of-service/"
MANIFEST_PATH = ROOT / "data/manifests/analysts_anachart.json"
PRICE_MANIFEST_PATH = ROOT / "data/manifests/prices_aapl_eodhd.json"
LOCAL = ROOT / ".local-data/processed"
RAW_FIELDS = ["date", "analyst", "broker_number", "rating_before", "rating_after",
              "price_target_before", "price_target_after", "pt_after_nominal", "split_ratio",
              "close_price_adj", "close_nominal_on_date", "target_direction", "target_met",
              "date_met", "days_to_hit"]
OUTCOME_FIELDS = ["target_direction", "target_met", "date_met", "days_to_hit"]
FEATURE_FIELDS = [field for field in RAW_FIELDS if field not in OUTCOME_FIELDS]
EVENT_FIELDS = [
    "record_id", "event_key", "is_primary_record", "duplicate_of_record_id", "source_row_number",
    "ticker", "ticker_provenance", "publication_date", "published_at_utc", "timing_precision",
    "availability_timestamp_known", "analyst_name", "analyst_identity_level", "identity_verified_independently",
    "analyst_firm", "broker_id", "broker_id_raw", "rating_before", "rating_after", "rating_normalized",
    "rating_representation", "target_before_adjusted", "target_after_adjusted", "target_after_nominal",
    "split_ratio", "target_currency", "target_adjustment_basis", "source_close_adjusted", "source_close_nominal",
    "source_close_adjustment_basis", "source_url", "dataset_source_url", "fetched_at_utc",
    "raw_snapshot_path", "raw_sha256", "usage_scope",
]
PAIR_FIELDS = ["pair_id", "ticker", "analyst_name", "broker_id", "previous_record_ids", "next_record_ids",
               "previous_date", "next_date", "days_between", "status", "complete_revision_history_verified"]


def fetch_analysts():
    content, headers = phase1.download(SOURCE_URL)
    rows = list(csv.DictReader(io.StringIO(content.decode("utf-8-sig"))))
    if not rows or list(rows[0]) != RAW_FIELDS:
        raise ValueError("Unexpected or empty AnaChart schema; nothing saved")
    raw_path = ROOT / f".local-data/raw/anachart/{phase1.sha256(content)}.csv"
    manifest = phase1.snapshot(SOURCE_URL, content, headers, raw_path, "Internal research only; no raw publication", False)
    manifest.update({
        "provider": "AnaChart / VADJ Inc.", "ticker": "AAPL",
        "ticker_provenance": "Single-ticker download page and filename; CSV has no ticker column",
        "rows": len(rows), "date_min": min(r["date"] for r in rows), "date_max": max(r["date"] for r in rows),
        "columns": RAW_FIELDS, "permission_url": PERMISSION_URL, "terms_url": TERMS_URL,
        "permission_basis": "Sample explicitly allows internal testing; terms 4.1-4.3 permit aggregate derivative analyses, not public raw records",
        "attribution": "AnaChart AAPL 100-row preview; access time recorded in fetched_at_utc",
        "public_analyst_rows_committed": 0,
        "excluded_from_predictor_inputs": OUTCOME_FIELDS,
        "historical_availability_verified": False,
    })
    phase1.write_json(MANIFEST_PATH, manifest)
    print(f"Saved {len(rows)} AnaChart source rows to ignored local storage")


def load_raw():
    manifest = phase1.read_json(MANIFEST_PATH)
    content = phase1.checked_raw(manifest)
    rows = list(csv.DictReader(io.StringIO(content.decode("utf-8-sig"))))
    if not rows or list(rows[0]) != RAW_FIELDS:
        raise ValueError("Unexpected saved AnaChart schema")
    return rows, manifest


def broker_id(value):
    if not value:
        return ""
    parsed = Decimal(value)
    if not parsed.is_finite() or parsed <= 0 or parsed != parsed.to_integral_value():
        raise ValueError("Invalid source broker identifier")
    return str(int(parsed))


def normalize_events(raw_rows, manifest):
    events, seen = [], {}
    for index, raw in enumerate(raw_rows, start=2):
        key_values = [raw.get(field, "") for field in FEATURE_FIELDS]
        event_key = "anachart_" + phase1.sha256(json.dumps(key_values, ensure_ascii=False).encode())[:24]
        record_id = "record_" + phase1.sha256(f"{manifest['sha256']}:{index}".encode())[:24]
        previous_id = seen.get(event_key, "")
        seen.setdefault(event_key, record_id)
        events.append({
            "record_id": record_id, "event_key": event_key, "is_primary_record": "false" if previous_id else "true",
            "duplicate_of_record_id": previous_id, "source_row_number": str(index), "ticker": manifest["ticker"],
            "ticker_provenance": "provider_single_ticker_download_context", "publication_date": raw["date"],
            "published_at_utc": "", "timing_precision": "date", "availability_timestamp_known": "false",
            "analyst_name": raw["analyst"].strip(),
            "analyst_identity_level": "provider_named_individual" if raw["analyst"].strip() else "unknown",
            "identity_verified_independently": "false", "analyst_firm": "",
            "broker_id": broker_id(raw["broker_number"]), "broker_id_raw": raw["broker_number"],
            "rating_before": raw["rating_before"], "rating_after": raw["rating_after"],
            "rating_normalized": phase1.normalize_rating(raw["rating_after"]), "rating_representation": "vendor_simplified",
            "target_before_adjusted": raw["price_target_before"], "target_after_adjusted": raw["price_target_after"],
            "target_after_nominal": raw["pt_after_nominal"], "split_ratio": raw["split_ratio"], "target_currency": "",
            "target_adjustment_basis": "provider_split_adjusted", "source_close_adjusted": raw["close_price_adj"],
            "source_close_nominal": raw["close_nominal_on_date"], "source_close_adjustment_basis": "provider_adjustment_unspecified",
            "source_url": "", "dataset_source_url": manifest.get("source_url", SOURCE_URL),
            "fetched_at_utc": manifest["fetched_at_utc"], "raw_snapshot_path": manifest["raw_path"],
            "raw_sha256": manifest["sha256"], "usage_scope": "internal_research_only_no_public_records",
        })
    return events


def primary_events(events):
    return [row for row in events if row["is_primary_record"] == "true"]


def derive_revision_pairs(events):
    groups = defaultdict(lambda: defaultdict(list))
    for row in primary_events(events):
        if row["analyst_name"] and row["broker_id"]:
            groups[(row["ticker"], row["analyst_name"], row["broker_id"])][row["publication_date"]].append(row)
    pairs = []
    for (ticker, analyst, broker), dated in sorted(groups.items()):
        dates = sorted(dated)
        for previous_day, next_day in zip(dates, dates[1:]):
            previous, next_rows = dated[previous_day], dated[next_day]
            if len(previous) != 1 or len(next_rows) != 1:
                status = "ambiguous_same_day"
            else:
                before, after = next_rows[0]["target_before_adjusted"], previous[0]["target_after_adjusted"]
                if not before or not after:
                    status = "missing_target"
                elif abs(Decimal(before) - Decimal(after)) <= Decimal("0.000001"):
                    status = "linked_observed_pair"
                else:
                    status = "prior_target_mismatch"
            identity = [ticker, analyst, broker, previous_day, next_day]
            pairs.append({
                "pair_id": "pair_" + phase1.sha256(json.dumps(identity).encode())[:24],
                "ticker": ticker, "analyst_name": analyst, "broker_id": broker,
                "previous_record_ids": "|".join(sorted(r["record_id"] for r in previous)),
                "next_record_ids": "|".join(sorted(r["record_id"] for r in next_rows)),
                "previous_date": previous_day, "next_date": next_day,
                "days_between": str((date.fromisoformat(next_day) - date.fromisoformat(previous_day)).days),
                "status": status, "complete_revision_history_verified": "false",
            })
    return pairs


def validate_events(events, raw_rows, manifest):
    errors = []
    if not events or len(events) != len(raw_rows):
        errors.append("Raw/normalized rows do not reconcile or sample empty")
    if events != normalize_events(raw_rows, manifest):
        errors.append("Normalized event values differ from exact raw replay")
    if len({r["record_id"] for r in events}) != len(events):
        errors.append("Duplicate record_id")
    numeric = ["target_before_adjusted", "target_after_adjusted", "target_after_nominal", "split_ratio",
               "source_close_adjusted", "source_close_nominal"]
    for index, row in enumerate(events):
        try:
            if not phase1.iso_day(row["publication_date"]):
                errors.append(f"record[{index}]: invalid publication date")
        except ValueError:
            errors.append(f"record[{index}]: invalid publication date")
        if any(row[field] and not phase1.finite_number(row[field]) for field in numeric):
            errors.append(f"record[{index}]: invalid numeric source field")
        if any(field in row for field in OUTCOME_FIELDS):
            errors.append(f"record[{index}]: vendor outcome leaked into event inputs")
        if (row["published_at_utc"] or row["availability_timestamp_known"] != "false"
                or row["source_url"] or row["analyst_firm"] or row["target_currency"]):
            errors.append(f"record[{index}]: source-missing field invented")
    return errors


def load_price_data():
    from scripts import eodhd_prices
    manifest = phase1.read_json(PRICE_MANIFEST_PATH)
    prices = eodhd_prices.load_prices(ROOT, manifest)
    errors = eodhd_prices.validate_prices(prices)
    if errors:
        raise ValueError(errors)
    actions = eodhd_prices.load_actions(ROOT, manifest)
    return prices, actions, manifest


def price_windows(events, prices):
    groups = defaultdict(list)
    by_date = {}
    for row in prices:
        groups[row["ticker"]].append(date.fromisoformat(row["date"]))
        by_date[(row["ticker"], row["date"])] = row
    for days in groups.values():
        days.sort()
    result = []
    for event in events:
        pub = date.fromisoformat(event["publication_date"])
        days = groups[event["ticker"]]
        index = bisect_right(days, pub)
        entry = days[index] if index < len(days) and (days[index] - pub).days <= 7 else None
        end_index = bisect_left(days, entry + timedelta(days=28)) if entry else len(days)
        followup = days[end_index] if end_index < len(days) else None
        source_close = event["source_close_nominal"]
        quoted = by_date.get((event["ticker"], event["publication_date"]))
        comparable = bool(source_close and quoted)
        close_match = comparable and abs(Decimal(source_close) - Decimal(quoted["close"])) <= Decimal("0.02")
        result.append({
            "record_id": event["record_id"], "is_primary_record": event["is_primary_record"], "ticker": event["ticker"],
            "publication_date": event["publication_date"], "entry_date_inventory_only": entry.isoformat() if entry else "",
            "followup_date_inventory_only": followup.isoformat() if followup else "",
            "has_next_session": str(bool(entry)).lower(), "has_28_day_followup": str(bool(followup)).lower(),
            "nominal_event_close_comparable": str(comparable).lower(),
            "nominal_event_close_matches_within_0_02_usd": str(bool(close_match)).lower(),
        })
    return result


def build():
    raw, manifest = load_raw()
    events = normalize_events(raw, manifest)
    errors = validate_events(events, raw, manifest)
    if errors:
        raise ValueError(errors)
    pairs = derive_revision_pairs(events)
    prices, actions, pm = load_price_data()
    windows = price_windows(events, prices)
    phase1.write_csv(LOCAL / "named_events.csv", events, EVENT_FIELDS)
    phase1.write_csv(LOCAL / "named_revision_pairs.csv", pairs, PAIR_FIELDS)
    phase1.write_csv(LOCAL / "named_price_windows.csv", windows, list(windows[0]))
    # Outcomes do not enter event_key inputs, eligibility or matching criteria.
    # record_id and raw_sha256 identify the full source snapshot, not predictors.
    outcomes = [{"record_id": event["record_id"], **{field: row[field] for field in OUTCOME_FIELDS}}
                for row, event in zip(raw, events)]
    phase1.write_csv(LOCAL / "anachart_vendor_outcomes.csv", outcomes, ["record_id", *OUTCOME_FIELDS])
    phase1.write_csv(LOCAL / "eodhd_prices_daily.csv", prices, list(prices[0]))
    print(f"Built {len(events)} local records, {len(primary_events(events))} primary events, {len(prices)} private prices")


def validate():
    raw, manifest = load_raw()
    expected = normalize_events(raw, manifest)
    events = phase1.read_csv(LOCAL / "named_events.csv")
    errors = validate_events(events, raw, manifest)
    artifacts = [(LOCAL / "named_events.csv", expected, EVENT_FIELDS),
                 (LOCAL / "named_revision_pairs.csv", derive_revision_pairs(expected), PAIR_FIELDS)]
    prices, actions, price_manifest = load_price_data()
    windows = price_windows(expected, prices)
    outcomes = [{"record_id": event["record_id"], **{field: row[field] for field in OUTCOME_FIELDS}}
                for row, event in zip(raw, expected)]
    artifacts.extend([(LOCAL / "named_price_windows.csv", windows, list(windows[0])),
                      (LOCAL / "anachart_vendor_outcomes.csv", outcomes, ["record_id", *OUTCOME_FIELDS]),
                      (LOCAL / "eodhd_prices_daily.csv", prices, list(prices[0]))])
    for path, rows, fields in artifacts:
        if path.read_bytes() != phase1.csv_bytes(rows, fields):
            errors.append(f"Saved local artifact does not match snapshot replay: {path.name}")
    result = {"passed": not errors, "errors": errors, "raw_rows": len(raw), "normalized_rows": len(events),
              "primary_events": len(primary_events(events)), "price_rows": len(prices),
              "snapshot_replay_checks": len(artifacts), "public_raw_rows": 0, "backtest_run": False,
              "checked_at_utc": datetime.now(timezone.utc).isoformat(),
              "scope": "Structure and replay only; quality warnings remain in named_coverage.json"}
    phase1.write_json(ROOT / "reports/named_validation.json", result)
    print(json.dumps(result, ensure_ascii=False))
    if errors:
        raise ValueError("Named sample validation failed")


def report():
    raw, manifest = load_raw()
    events = normalize_events(raw, manifest)
    unique = primary_events(events)
    pairs = derive_revision_pairs(events)
    prices, actions, pm = load_price_data()
    windows = price_windows(events, prices)
    primary_windows = [r for r in windows if r["is_primary_record"] == "true"]
    dated_groups = defaultdict(set)
    for row in unique:
        if row["analyst_name"] and row["broker_id"]:
            dated_groups[(row["analyst_name"], row["broker_id"])].add(row["publication_date"])
    comparable = sum(r["nominal_event_close_comparable"] == "true" for r in primary_windows)
    matched = sum(r["nominal_event_close_matches_within_0_02_usd"] == "true" for r in primary_windows)
    primary_date_groups = Counter((r["ticker"], r["analyst_name"], r["broker_id"], r["publication_date"])
                                  for r in unique if r["analyst_name"] and r["broker_id"])
    revision_rows = lambda rows: sum(bool(r["target_before_adjusted"] and r["target_after_adjusted"])
                                   and Decimal(r["target_before_adjusted"]) != Decimal(r["target_after_adjusted"]) for r in rows)
    complete = lambda rows: sum(bool(r["analyst_name"] and r["rating_normalized"] and r["target_after_adjusted"]) for r in rows)
    result = {
        "scope": "AnaChart AAPL 100-row dated preview; aggregate inventory only; no market-wide coverage claim",
        "attribution": "AnaChart, https://anachart.store/free-sample/; EODHD price coverage metadata only",
        "raw_rows": len(raw), "primary_events": len(unique), "duplicate_rows_retained_and_flagged": len(events)-len(unique),
        "tickers": ["AAPL"], "publication_date_min": manifest["date_min"], "publication_date_max": manifest["date_max"],
        "named_analysts": len({r["analyst_name"] for r in unique if r["analyst_name"]}),
        "broker_ids": len({r["broker_id"] for r in unique if r["broker_id"]}),
        "raw_rows_with_name_rating_target": complete(events), "primary_events_with_name_rating_target": complete(unique),
        "raw_rows_with_reported_target_change": revision_rows(events), "primary_events_with_reported_target_change": revision_rows(unique),
        "primary_named_events_with_reported_target_change": revision_rows([r for r in unique if r["analyst_name"]]),
        "missing_primary_counts": {field: sum(not r[field] for r in unique) for field in
                                   ["analyst_name", "broker_id", "rating_before", "rating_after", "target_before_adjusted",
                                    "target_after_adjusted", "target_after_nominal", "split_ratio", "source_url", "published_at_utc", "analyst_firm", "target_currency"]},
        "primary_ratings_after_normalized": dict(Counter(r["rating_normalized"] or "Unmapped" for r in unique)),
        "analyst_broker_groups_on_multiple_dates": sum(len(days)>1 for days in dated_groups.values()),
        "ambiguous_same_day_identity_groups": sum(count > 1 for count in primary_date_groups.values()),
        "observed_adjacent_date_pair_status_counts": dict(Counter(r["status"] for r in pairs)),
        "complete_revision_histories_verified": 0,
        "price_tickers": ["AAPL"], "price_rows": len(prices),
        "price_date_min": min(r["date"] for r in prices), "price_date_max": max(r["date"] for r in prices),
        "corporate_action_rows": {key: len(value) for key, value in actions.items()},
        "primary_events_with_next_session": sum(r["has_next_session"] == "true" for r in primary_windows),
        "primary_events_with_28_day_followup": sum(r["has_28_day_followup"] == "true" for r in primary_windows),
        "primary_event_close_comparisons": comparable, "primary_event_closes_matching_within_0_02_usd": matched,
        "primary_event_close_mismatches": comparable-matched,
        "distinct_event_dates_compared": len({r["publication_date"] for r in primary_windows if r["nominal_event_close_comparable"] == "true"}),
        "coverage_fractions": {"named_over_primary_events": sum(bool(r["analyst_name"]) for r in unique)/len(unique),
                               "name_rating_target_over_primary_events": complete(unique)/len(unique),
                               "priced_tickers_over_sample_tickers": 1.0,
                               "next_session_over_primary_events": sum(r["has_next_session"] == "true" for r in primary_windows)/len(unique),
                               "28_day_followup_over_primary_events": sum(r["has_28_day_followup"] == "true" for r in primary_windows)/len(unique)},
        "outcome_columns_quarantined": OUTCOME_FIELDS, "public_analyst_rows": 0, "public_price_rows": 0,
        "historical_availability_verified": False, "backtest_run": False,
        "limitations": ["No row-level article links or original brokerage wording", "Names are vendor canonical identities, not independently verified",
                        "Same-day conflicts have no recoverable ordering", "Observed target matches do not establish complete revision history",
                        "Date-only publication; current snapshot is not verified point-in-time", "Only AAPL recent preview; selection bias",
                        "Vendor outcomes excluded from event inputs; no hit rate or returns computed", "Calendar-window inventory does not prove every expected session is present"],
    }
    phase1.write_json(ROOT / "reports/named_coverage.json", result)
    # Overall inventory keeps these datasets separate; no unsupported event-level merging.
    dalsna = phase1.read_csv(phase1.EVENT_PATH)
    ibm = phase1.read_json(phase1.MANIFESTS / "prices_ibm.json")
    phase1.write_json(ROOT / "reports/dataset_inventory.json", {
        "datasets": [
            {"name": "Dalsna", "public_event_rows": len(dalsna), "named_person_rows": sum(bool(r["analyst_name"]) for r in dalsna), "coverage_report": "coverage_public.json"},
            {"name": "AnaChart AAPL preview", "local_source_rows": len(events), "local_primary_events": len(unique),
             "public_event_rows": 0, "coverage_report": "named_coverage.json"}],
        "price_datasets": [{"name": "Alpha Vantage IBM", "local_rows_as_recorded_in_manifest": ibm["rows"], "public_rows": 0},
                           {"name": "EODHD AAPL", "local_rows": len(prices), "public_rows": 0}],
        "datasets_deduplicated_against_each_other": False, "backtest_run": False})
    print(json.dumps(result, ensure_ascii=False, indent=2))


def check_public():
    tracked = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode().split("\0")
    forbidden_names = {"named_events.csv", "named_revision_pairs.csv", "named_price_windows.csv",
                       "anachart_vendor_outcomes.csv", "eodhd_prices_daily.csv", "AnaChart_AAPL_sample_100_rows.csv"}
    errors = [f"Restricted file is tracked: {p}" for p in tracked if p and
              (p.startswith(".local-data/") or Path(p).name in forbidden_names)]
    local_scan = False
    if MANIFEST_PATH.exists() and (ROOT / phase1.read_json(MANIFEST_PATH)["raw_path"]).exists():
        raw, manifest = load_raw()
        names = {r["analyst"].strip() for r in raw if r["analyst"].strip()}
        local_scan = True
        for relative in tracked:
            path = ROOT / relative
            if relative and path.is_file():
                text = path.read_text(encoding="utf-8-sig", errors="replace")
                if any(name in text for name in names):
                    errors.append(f"Private sample analyst name appears in tracked text: {relative}")
    result = {"passed": not errors, "errors": errors, "tracked_restricted_files": len(errors),
              "local_private_name_scan_performed": local_scan, "raw_rows_published": 0}
    phase1.write_json(ROOT / "reports/named_public_boundary.json", result)
    print(json.dumps(result))
    if errors:
        raise ValueError("Private/public data boundary check failed")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["fetch-analysts", "build", "validate", "report", "check-public"])
    args = parser.parse_args()
    {"fetch-analysts": fetch_analysts, "build": build, "validate": validate, "report": report,
     "check-public": check_public}[args.command]()


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
