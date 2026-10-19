"""Collect, replay and validate real source samples. No backtest is performed.

Python 3.10+, standard library only. Private price bytes never go in Git.
"""
import argparse
from collections import Counter, defaultdict
import csv
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal, InvalidOperation
import hashlib
import io
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
ANALYST_URL = "https://dalsnafin.com/analysts/data.csv"
PRICE_URL = ("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED"
             "&symbol=IBM&outputsize=full&apikey=demo")
MANIFESTS = ROOT / "data/manifests"
EVENT_PATH = ROOT / "data/processed/analyst_events.csv"
PRICE_PATH = ROOT / ".local-data/processed/prices_daily.csv"
EVENT_FIELDS = [
    "event_id", "ticker", "company", "analyst_firm", "analyst_name",
    "analyst_identity_level", "publication_date", "published_at_utc",
    "timing_precision", "availability_timestamp_known", "rating_raw",
    "rating_normalized", "rating_mapping_version", "price_target",
    "previous_price_target", "target_currency", "due_date", "horizon_note",
    "source_status", "source_name", "source_url", "dataset_source_url",
    "fetched_at_utc", "raw_snapshot_path", "raw_sha256", "data_license",
]
PRICE_FIELDS = [
    "provider", "ticker", "date", "currency", "exchange_timezone", "open",
    "high", "low", "close", "adjusted_close", "adjustment_factor", "volume",
    "dividend_amount", "split_coefficient", "adjustment_basis", "fetched_at_utc",
    "raw_snapshot_path", "raw_sha256",
]
RAW_FIELDS = {"firm", "ticker", "company", "rating_as_published", "target",
              "said_date", "due_date", "horizon_note", "source_name", "source_url", "status"}
# A research convention, NOT a claim that brokerage rating systems are equivalent.
RATING_MAP = {
    "buy": "Buy", "strong buy": "Buy", "outperform": "Buy",
    "overweight": "Buy", "market outperform": "Buy", "sector outperform": "Buy",
    "overweight / buy": "Buy", "hold": "Hold", "neutral": "Hold",
    "equal weight": "Hold", "equalweight": "Hold", "market perform": "Hold",
    "sector perform": "Hold", "in line": "Hold", "sell": "Sell",
    "strong sell": "Sell", "underweight": "Sell", "underperform": "Sell",
    "market underperform": "Sell", "sector underperform": "Sell", "reduce": "Sell",
}


def sha256(content):
    return hashlib.sha256(content).hexdigest()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def csv_bytes(rows, fields):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def write_csv(path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(csv_bytes(rows, fields))


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def download(url):
    request = Request(url, headers={"User-Agent": "stock-research-phase1/1.0 (public documented sample)"})
    with urlopen(request, timeout=45) as response:
        content = response.read()
        return content, {
            "http_status": response.status,
            "content_type": response.headers.get("Content-Type"),
            "etag": response.headers.get("ETag"),
            "last_modified": response.headers.get("Last-Modified"),
        }


def snapshot(url, content, headers, raw_path, license_name, public):
    if raw_path.exists() and raw_path.read_bytes() != content:
        raise ValueError(f"Refusing to overwrite a different snapshot: {raw_path}")
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    raw_path.write_bytes(content)
    return {
        "source_url": url, "fetched_at_utc": datetime.now(timezone.utc).isoformat(),
        "raw_path": raw_path.relative_to(ROOT).as_posix(), "sha256": sha256(content),
        "bytes": len(content), "license": license_name, "raw_committed": public,
        **headers,
    }


def fetch_analysts():
    content, headers = download(ANALYST_URL)
    rows = list(csv.DictReader(io.StringIO(content.decode("utf-8-sig"))))
    if not rows or set(rows[0]) != RAW_FIELDS:
        raise ValueError("Unexpected or empty Dalsna schema; nothing saved")
    day = datetime.now(timezone.utc).date().isoformat()
    path = ROOT / f"data/raw/dalsna/{day}-{sha256(content)[:12]}.csv"
    manifest = snapshot(ANALYST_URL, content, headers, path, "CC-BY-4.0", True)
    manifest.update({"provider": "Dalsna Finance", "rows": len(rows),
                     "license_url": "https://dalsnafin.com/analysts/methodology",
                     "attribution": "Dalsna Finance analyst price-target tracker, dalsnafin.com, CC BY 4.0",
                     "modifications": "CSV normalized; research rating mapping added; missing fields left empty."})
    write_json(MANIFESTS / "analysts_dalsna.json", manifest)
    print(f"Fetched {len(rows)} public analyst-firm target records")


def fetch_prices():
    content, headers = download(PRICE_URL)
    payload = json.loads(content)
    # HTTP 200 can carry an API entitlement/rate-limit message, not price data.
    series = payload.get("Time Series (Daily)")
    if not isinstance(series, dict) or not series:
        raise ValueError("Alpha Vantage returned no daily adjusted data; nothing saved")
    manifest = snapshot(PRICE_URL, content, headers,
                        ROOT / ".local-data/raw/alpha_vantage/IBM.json",
                        "Personal non-commercial research; no public redistribution grant verified", False)
    manifest.update({"provider": "Alpha Vantage", "ticker": "IBM", "rows": len(series),
                     "date_min": min(series), "date_max": max(series),
                     "terms_url": "https://www.alphavantage.co/terms_of_service/",
                     "documentation_url": "https://www.alphavantage.co/documentation/#dailyadj",
                     "metadata": payload.get("Meta Data", {}),
                     "public_price_rows_committed": 0})
    write_json(MANIFESTS / "prices_ibm.json", manifest)
    print(f"Fetched {len(series)} IBM adjusted daily records into ignored local storage")


def normalize_rating(value):
    key = re.sub(r"\s+", " ", (value or "").strip().lower().replace("-", " "))
    return RATING_MAP.get(key, "")


def normalize_events(raw_rows, manifest):
    result = []
    for raw in raw_rows:
        identity = [raw.get(k, "") for k in ("firm", "ticker", "said_date", "target", "source_url")]
        result.append({
            "event_id": "dalsna_" + sha256(json.dumps(identity, ensure_ascii=False).encode())[:24],
            "ticker": raw["ticker"], "company": raw["company"], "analyst_firm": raw["firm"],
            "analyst_name": "", "analyst_identity_level": "firm_only",
            "publication_date": raw["said_date"], "published_at_utc": "",
            "timing_precision": "date", "availability_timestamp_known": "false",
            "rating_raw": raw["rating_as_published"],
            "rating_normalized": normalize_rating(raw["rating_as_published"]),
            "rating_mapping_version": "research-v1", "price_target": raw["target"],
            "previous_price_target": "", "target_currency": "",
            "due_date": raw["due_date"], "horizon_note": raw["horizon_note"],
            "source_status": raw["status"], "source_name": raw["source_name"],
            "source_url": raw["source_url"], "dataset_source_url": ANALYST_URL,
            "fetched_at_utc": manifest["fetched_at_utc"],
            "raw_snapshot_path": manifest["raw_path"], "raw_sha256": manifest["sha256"],
            "data_license": "CC-BY-4.0",
        })
    return sorted(result, key=lambda x: (x["ticker"], x["publication_date"], x["event_id"]))


def parse_prices(payload, manifest):
    metadata = payload["Meta Data"]
    if metadata["2. Symbol"] != "IBM":
        raise ValueError("Only the documented IBM demo is supported")
    rows = []
    source_fields = {
        "open": "1. open", "high": "2. high", "low": "3. low", "close": "4. close",
        "adjusted_close": "5. adjusted close", "volume": "6. volume",
        "dividend_amount": "7. dividend amount", "split_coefficient": "8. split coefficient",
    }
    for day, record in sorted(payload["Time Series (Daily)"].items()):
        row = {field: str(record[key]) for field, key in source_fields.items()}
        row.update({
            "provider": "Alpha Vantage", "ticker": "IBM", "date": day, "currency": "USD",
            "exchange_timezone": metadata["5. Time Zone"],
            "adjustment_factor": str(Decimal(row["adjusted_close"]) / Decimal(row["close"])),
            "adjustment_basis": "provider_split_and_dividend_adjusted_close_as_of_fetch",
            "fetched_at_utc": manifest["fetched_at_utc"], "raw_snapshot_path": manifest["raw_path"],
            "raw_sha256": manifest["sha256"],
        })
        rows.append(row)
    return rows


def checked_raw(manifest):
    content = (ROOT / manifest["raw_path"]).read_bytes()
    if sha256(content) != manifest["sha256"]:
        raise ValueError("Raw snapshot hash mismatch")
    return content


def load_raw_events():
    manifest = read_json(MANIFESTS / "analysts_dalsna.json")
    raw = list(csv.DictReader(io.StringIO(checked_raw(manifest).decode("utf-8-sig"))))
    return raw, manifest


def build(with_private_prices=False):
    raw, manifest = load_raw_events()
    events = normalize_events(raw, manifest)
    errors = validate_events(events, raw)
    if errors:
        raise ValueError(errors)
    write_csv(EVENT_PATH, events, EVENT_FIELDS)
    if with_private_prices:
        price_manifest = read_json(MANIFESTS / "prices_ibm.json")
        prices = parse_prices(json.loads(checked_raw(price_manifest)), price_manifest)
        errors = validate_prices(prices)
        if errors:
            raise ValueError(errors)
        write_csv(PRICE_PATH, prices, PRICE_FIELDS)
    print(f"Built {len(events)} events" + (" and private prices" if with_private_prices else ""))


def iso_day(value):
    return bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", value)) and date.fromisoformat(value).isoformat() == value


def finite_number(value, positive=True):
    try:
        number = Decimal(value)
        return number.is_finite() and (number > 0 if positive else number >= 0)
    except (InvalidOperation, TypeError, ValueError):
        return False


def validate_events(events, raw_rows):
    errors = []
    if not events:
        errors.append("Empty event sample")
    if len(events) != len(raw_rows):
        errors.append("Input/output row counts do not reconcile")
    expected = {row["event_id"]: row for row in normalize_events(
        raw_rows, {"raw_path": "", "sha256": "", "fetched_at_utc": ""})}
    source_fields = ("ticker", "company", "analyst_firm", "publication_date", "rating_raw",
                     "price_target", "due_date", "horizon_note", "source_status", "source_name", "source_url")
    ids = [r["event_id"] for r in events]
    if len(set(ids)) != len(ids):
        errors.append("Duplicate event_id")
    for index, row in enumerate(events):
        prefix = f"event[{index}]"
        original = expected.get(row["event_id"])
        if original is None or any(row[field] != original[field] for field in source_fields):
            errors.append(f"{prefix}: normalized values differ from raw source")
        try:
            if not iso_day(row["publication_date"]) or not iso_day(row["due_date"]):
                errors.append(f"{prefix}: invalid date")
        except ValueError:
            errors.append(f"{prefix}: invalid date")
        if not finite_number(row["price_target"]):
            errors.append(f"{prefix}: invalid price target")
        if not row["ticker"] or not row["analyst_firm"]:
            errors.append(f"{prefix}: missing ticker or firm")
        if urlparse(row["source_url"]).scheme not in ("http", "https"):
            errors.append(f"{prefix}: invalid source URL")
        if row["rating_normalized"] != normalize_rating(row["rating_raw"]):
            errors.append(f"{prefix}: rating mapping mismatch")
        if (row["analyst_name"] or row["analyst_identity_level"] != "firm_only"
                or row["previous_price_target"] or row["published_at_utc"]
                or row["availability_timestamp_known"] != "false" or row["target_currency"]
                or row["timing_precision"] != "date"):
            errors.append(f"{prefix}: source-missing field was invented")
        if row["source_status"] not in ("open", "hit", "miss", "retracted"):
            errors.append(f"{prefix}: unknown status")
    return errors


def validate_prices(prices):
    errors, seen = [], set()
    if not prices:
        errors.append("Empty price sample")
    last_date = {}
    for index, row in enumerate(prices):
        prefix = f"price[{index}]"
        key = (row["provider"], row["ticker"], row["date"])
        if key in seen:
            errors.append(f"{prefix}: duplicate price key")
        seen.add(key)
        try:
            if not iso_day(row["date"]):
                errors.append(f"{prefix}: invalid date")
        except ValueError:
            errors.append(f"{prefix}: invalid date")
        group = key[:2]
        if row["date"] < last_date.get(group, ""):
            errors.append(f"{prefix}: dates not sorted")
        last_date[group] = row["date"]
        positive_fields = ("open", "high", "low", "close", "adjusted_close", "split_coefficient", "adjustment_factor")
        if not all(finite_number(row[k]) for k in positive_fields):
            errors.append(f"{prefix}: nonfinite or nonpositive price/adjustment")
            continue
        if not all(finite_number(row[k], positive=False) for k in ("volume", "dividend_amount")):
            errors.append(f"{prefix}: invalid volume/dividend")
        low, high = Decimal(row["low"]), Decimal(row["high"])
        if not low <= min(Decimal(row["open"]), Decimal(row["close"])) <= max(Decimal(row["open"]), Decimal(row["close"])) <= high:
            errors.append(f"{prefix}: OHLC bounds inconsistent")
        factor = Decimal(row["adjusted_close"]) / Decimal(row["close"])
        if abs(factor - Decimal(row["adjustment_factor"])) > Decimal("1e-20"):
            errors.append(f"{prefix}: adjustment factor mismatch")
        if row["currency"] != "USD" or not row["exchange_timezone"]:
            errors.append(f"{prefix}: missing/unsupported price units")
    return errors


def validate(with_private_prices=False):
    raw, manifest = load_raw_events()
    events = read_csv(EVENT_PATH)
    errors = validate_events(events, raw)
    replay = csv_bytes(normalize_events(raw, manifest), EVENT_FIELDS) == EVENT_PATH.read_bytes()
    if not replay:
        errors.append("Event snapshot replay differs from committed CSV")
    price_count = 0
    if with_private_prices:
        pm = read_json(MANIFESTS / "prices_ibm.json")
        prices = read_csv(PRICE_PATH)
        price_count = len(prices)
        errors.extend(validate_prices(prices))
        if csv_bytes(parse_prices(json.loads(checked_raw(pm)), pm), PRICE_FIELDS) != PRICE_PATH.read_bytes():
            errors.append("Price snapshot replay differs from local CSV")
    result = {"passed": not errors, "errors": errors, "event_rows": len(events),
              "input_rows": len(raw), "quarantined_rows": 0, "event_replay_identical": replay,
              "private_price_validation_run": with_private_prices, "private_price_rows": price_count,
              "public_price_rows": 0, "checked_at_utc": datetime.now(timezone.utc).isoformat()}
    write_json(ROOT / ("reports/validation_local.json" if with_private_prices else "reports/validation_public.json"), result)
    print(json.dumps(result, ensure_ascii=False))
    if errors:
        raise ValueError("Validation failed; see report")


def coverage(with_private_prices=False):
    events = read_csv(EVENT_PATH)
    groups = defaultdict(list)
    for row in events:
        groups[row["ticker"]].append(row)
    counts = Counter(r["rating_normalized"] or "Unmapped" for r in events)
    price_dates = defaultdict(list)
    if with_private_prices:
        for row in read_csv(PRICE_PATH):
            price_dates[row["ticker"]].append(date.fromisoformat(row["date"]))
    windows = []
    for row in events:
        available = price_dates[row["ticker"]]
        pub = date.fromisoformat(row["publication_date"])
        future = [day for day in available if day > pub]
        # Inventory only: exact session calendar and executable timing remain unresolved.
        entry = future[0] if future and (future[0] - pub).days <= 7 else None
        end = next((day for day in future if entry and day >= entry + timedelta(days=28)), None)
        windows.append({"event_id": row["event_id"], "ticker": row["ticker"],
                        "publication_date": row["publication_date"],
                        "has_next_session_within_7_calendar_days": bool(entry),
                        "has_28_calendar_day_followup_from_next_session": bool(end),
                        "individual_analyst_eligible": bool(row["analyst_name"])})
    semantic_keys = [(r["analyst_firm"], r["ticker"], r["publication_date"], r["price_target"]) for r in events]
    result = {
        "scope": "Observed downloaded sample only; not source-wide or US-market coverage",
        "event_rows": len(events), "tickers": len(groups),
        "firms": len({r["analyst_firm"] for r in events}),
        "publication_date_min": min(r["publication_date"] for r in events),
        "publication_date_max": max(r["publication_date"] for r in events),
        "ratings_normalized": dict(sorted(counts.items())),
        "ratings_unmapped_nonempty": dict(Counter(r["rating_raw"] for r in events if r["rating_raw"] and not r["rating_normalized"])),
        "missing_counts": {key: sum(not r[key] for r in events) for key in
                           ("analyst_name", "previous_price_target", "published_at_utc", "target_currency", "rating_raw", "price_target", "source_url")},
        "status_counts": dict(Counter(r["source_status"] for r in events)),
        "horizon_counts": dict(Counter(r["horizon_note"] for r in events)),
        "source_url_host_counts": dict(Counter(urlparse(r["source_url"]).netloc for r in events)),
        "duplicate_firm_ticker_date_target_rows": len(events) - len(set(semantic_keys)),
        "individual_analyst_eligible_rows": sum(bool(r["analyst_name"]) for r in events),
        "revision_chain_eligible_rows": 0,
        "price_scope": "IBM demo only; private local data" if with_private_prices else "No public price data; see separate local report",
        "price_tickers": sorted(k for k, v in price_dates.items() if v),
        "price_rows": sum(map(len, price_dates.values())), "public_price_rows": 0,
        "events_with_next_session": sum(w["has_next_session_within_7_calendar_days"] for w in windows),
        "events_with_28_day_followup": sum(w["has_28_calendar_day_followup_from_next_session"] for w in windows),
        "coverage_fractions": {
            "named_individual_events_over_all_events": sum(bool(r["analyst_name"]) for r in events) / len(events),
            "mapped_ratings_over_all_events": sum(bool(r["rating_normalized"]) for r in events) / len(events),
            "tickers_with_local_prices_over_observed_tickers": sum(bool(price_dates[k]) for k in groups) / len(groups),
            "events_with_next_session_over_all_events": sum(w["has_next_session_within_7_calendar_days"] for w in windows) / len(events),
            "events_with_28_day_followup_over_all_events": sum(w["has_28_calendar_day_followup_from_next_session"] for w in windows) / len(events),
        },
        "per_ticker": [{"ticker": key, "events": len(value),
                        "date_min": min(r["publication_date"] for r in value),
                        "date_max": max(r["publication_date"] for r in value),
                        "local_price_rows": len(price_dates[key])} for key, value in sorted(groups.items())],
        "backtest_run": False,
    }
    stem = "coverage_local" if with_private_prices else "coverage_public"
    write_json(ROOT / f"reports/{stem}.json", result)
    if with_private_prices:
        write_csv(ROOT / "reports/price_window_inventory.csv", windows, list(windows[0]))
    print(json.dumps({k: v for k, v in result.items() if k != "per_ticker"}, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["fetch-analysts", "fetch-prices", "build", "validate", "report"])
    parser.add_argument("--with-private-prices", action="store_true")
    args = parser.parse_args()
    if args.command == "fetch-analysts":
        fetch_analysts()
    elif args.command == "fetch-prices":
        fetch_prices()
    else:
        {"build": build, "validate": validate, "report": coverage}[args.command](args.with_private_prices)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
