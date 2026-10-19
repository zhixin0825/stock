"""Fetch and replay the documented, private-use EODHD AAPL demo.

OHLC is raw/as traded; adjusted_close includes splits and dividends. Volume
is already split adjusted. Separate corporate-action responses are preserved;
the daily endpoint does not supply daily dividend or split fields. All market
values stay under .local-data; the public manifest contains metadata only.
Python 3.10+, standard library only. This module performs no backtest.
"""

import argparse
from datetime import date, datetime, timezone
from decimal import Decimal, InvalidOperation
import json
from pathlib import Path

from scripts import phase1


START_DATE = "2025-01-01"
END_DATE = "2026-10-16"
TICKER = "AAPL"
PROVIDER = "EODHD"
MANIFEST_PATH = Path("data/manifests/prices_aapl_eodhd.json")
RAW_DIRECTORY = Path(".local-data/raw/eodhd")
TERMS_URL = "https://eodhd.com/financial-apis/terms-conditions"
DOCUMENTATION_URL = "https://eodhd.com/financial-apis/api-for-historical-data-and-volumes"
DEMO_DOCUMENTATION_URL = "https://eodhd.com/financial-apis/quick-start-with-our-financial-data-apis"
ACTION_DOCUMENTATION_URL = "https://eodhd.com/financial-apis/api-splits-dividends"
LICENSE_NOTE = (
    "Personal, private, non-commercial storage/manipulation/analysis permitted; "
    "redistribution, display and granting access prohibited without applicable rights."
)
URLS = {
    "eod": (
        "https://eodhd.com/api/eod/AAPL.US?api_token=demo"
        f"&from={START_DATE}&to={END_DATE}&period=d&fmt=json"
    ),
    "splits": (
        "https://eodhd.com/api/splits/AAPL.US?api_token=demo"
        f"&from={START_DATE}&to={END_DATE}&fmt=json"
    ),
    "dividends": (
        "https://eodhd.com/api/div/AAPL.US?api_token=demo"
        f"&from={START_DATE}&to={END_DATE}&fmt=json"
    ),
}
NUMERIC_FIELDS = ("open", "high", "low", "close", "adjusted_close", "volume")


def _valid_date(value):
    if not isinstance(value, str):
        return False
    try:
        return date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False


def _parse_records(content, kind, decimals=False):
    payload = json.loads(content, parse_float=Decimal) if decimals else json.loads(content)
    # Providers sometimes return entitlement/rate-limit messages with HTTP 200.
    if not isinstance(payload, list) or (kind == "eod" and not payload):
        raise ValueError(f"EODHD {kind} response is not the expected record list")
    if any(not isinstance(row, dict) for row in payload):
        raise ValueError(f"EODHD {kind} response contains a non-object record")
    for index, row in enumerate(payload):
        day = row.get("date")
        if not _valid_date(day) or not START_DATE <= day <= END_DATE:
            raise ValueError(f"EODHD {kind} record {index} has an invalid/out-of-window date")
        if kind == "eod" and any(field not in row for field in NUMERIC_FIELDS):
            raise ValueError(f"EODHD daily record {index} lacks required price fields")
    if kind in ("splits", "dividends"):
        _validate_actions(payload, kind)
    return payload


def _validate_actions(records, kind):
    seen = set()
    for index, row in enumerate(records):
        if kind == "splits":
            ratio = row.get("split")
            if not isinstance(ratio, str) or ratio.count("/") != 1:
                raise ValueError(f"EODHD split record {index} has no valid split ratio")
            try:
                parts = [Decimal(part) for part in ratio.split("/")]
            except (InvalidOperation, ValueError):
                raise ValueError(f"EODHD split record {index} has a nonnumeric ratio") from None
            if any(not part.is_finite() or part <= 0 for part in parts):
                raise ValueError(f"EODHD split record {index} has a nonpositive/nonfinite ratio")
            identity = (row["date"], ratio)
        else:
            try:
                value = Decimal(str(row["value"]))
            except (KeyError, InvalidOperation, ValueError):
                raise ValueError(f"EODHD dividend record {index} has no numeric value") from None
            if not value.is_finite() or value < 0:
                raise ValueError(f"EODHD dividend record {index} has a negative/nonfinite value")
            identity = (row["date"], str(row["value"]), row.get("currency", ""))
        if identity in seen:
            raise ValueError(f"EODHD {kind} response has duplicate action records")
        seen.add(identity)


def _metadata(url, content, headers, path, records):
    days = [row["date"] for row in records]
    return {
        "source_url": url,
        "fetched_at_utc": datetime.now(timezone.utc).isoformat(),
        "raw_path": path.as_posix(),
        "sha256": phase1.sha256(content),
        "bytes": len(content),
        "rows": len(records),
        "date_min": min(days) if days else "",
        "date_max": max(days) if days else "",
        "license": LICENSE_NOTE,
        "raw_committed": False,
        **headers,
    }


def _normalized_prices(records, snapshot):
    rows = []
    for record in records:
        row = {field: str(record[field]) for field in NUMERIC_FIELDS}
        try:
            close = Decimal(row["close"])
            adjusted = Decimal(row["adjusted_close"])
            if not close.is_finite() or not adjusted.is_finite() or close <= 0 or adjusted <= 0:
                raise ValueError("Daily close and adjusted_close must be finite and positive")
            factor = str(adjusted / close)
        except (InvalidOperation, ValueError, ZeroDivisionError):
            raise ValueError("Cannot derive EODHD adjustment factor from invalid prices") from None
        row.update({
            "ticker": TICKER,
            "date": record["date"],
            "provider": PROVIDER,
            "currency": "USD",
            "exchange_timezone": "America/New_York",
            "adjustment_factor": factor,
            "adjustment_basis": "provider_split_and_dividend_adjusted_close_as_of_fetch",
            "volume_basis": "split_adjusted",
            # Absence is not a reported zero/no-action observation.
            "dividend_amount": "",
            "split_coefficient": "",
            "fetched_at_utc": snapshot["fetched_at_utc"],
            "raw_snapshot_path": snapshot["raw_path"],
            "raw_sha256": snapshot["sha256"],
        })
        rows.append(row)
    return sorted(rows, key=lambda row: (row["ticker"], row["date"]))


def validate_prices(rows):
    """Return validation errors without assuming daily corporate-action fields."""
    errors = []
    seen = set()
    if not rows:
        return ["EODHD daily price sample is empty"]
    for index, row in enumerate(rows):
        label = f"EODHD daily row {index}"
        day = row.get("date")
        if not _valid_date(day):
            errors.append(f"{label}: invalid date")
        elif not START_DATE <= day <= END_DATE:
            errors.append(f"{label}: date outside requested window")
        key = (row.get("ticker"), day)
        if key in seen:
            errors.append(f"{label}: duplicate ticker/date")
        seen.add(key)
        for field, expected in (("ticker", TICKER), ("provider", PROVIDER),
                                ("currency", "USD"), ("volume_basis", "split_adjusted")):
            if row.get(field) != expected:
                errors.append(f"{label}: unexpected {field}")
        numbers = {}
        for field in (*NUMERIC_FIELDS, "adjustment_factor"):
            try:
                value = Decimal(str(row[field]))
                if not value.is_finite():
                    raise ValueError("not finite")
                numbers[field] = value
                if field == "volume":
                    if value < 0 or value != value.to_integral_value():
                        errors.append(f"{label}: volume must be a nonnegative integer")
                elif value <= 0:
                    errors.append(f"{label}: {field} must be positive")
            except (KeyError, InvalidOperation, ValueError):
                errors.append(f"{label}: {field} must be numeric and finite")
        if all(field in numbers for field in ("open", "high", "low", "close")):
            if not (numbers["low"] <= numbers["open"] <= numbers["high"]
                    and numbers["low"] <= numbers["close"] <= numbers["high"]):
                errors.append(f"{label}: inconsistent OHLC bounds")
        if all(field in numbers for field in ("close", "adjusted_close", "adjustment_factor")):
            if numbers["close"] > 0:
                expected = numbers["adjusted_close"] / numbers["close"]
                if abs(numbers["adjustment_factor"] - expected) > Decimal("1e-24"):
                    errors.append(f"{label}: inconsistent adjustment factor")
        if row.get("dividend_amount", "") != "" or row.get("split_coefficient", "") != "":
            errors.append(f"{label}: daily action fields must remain missing for this endpoint")
        for field in ("fetched_at_utc", "raw_snapshot_path", "raw_sha256"):
            if not row.get(field):
                errors.append(f"{label}: missing provenance {field}")
    return errors


def _checked_raw(root, snapshot):
    root = Path(root).resolve()
    raw_base = (root / RAW_DIRECTORY).resolve()
    raw_path = (root / snapshot["raw_path"]).resolve()
    if not raw_path.is_relative_to(raw_base):
        raise ValueError("EODHD raw snapshot must remain under ignored .local-data/raw/eodhd")
    content = raw_path.read_bytes()
    if phase1.sha256(content) != snapshot["sha256"]:
        raise ValueError("EODHD raw snapshot hash mismatch")
    if len(content) != snapshot["bytes"]:
        raise ValueError("EODHD raw snapshot byte count mismatch")
    return content


def _check_record_metadata(records, snapshot):
    days = [row["date"] for row in records]
    if len(records) != snapshot["rows"]:
        raise ValueError("EODHD raw record count disagrees with manifest")
    if (min(days) if days else "") != snapshot["date_min"]:
        raise ValueError("EODHD raw first date disagrees with manifest")
    if (max(days) if days else "") != snapshot["date_max"]:
        raise ValueError("EODHD raw last date disagrees with manifest")


def load_prices(root, manifest):
    """Replay local daily values, verifying the immutable snapshot hash first."""
    snapshot = manifest["snapshots"]["eod"]
    records = _parse_records(_checked_raw(root, snapshot), "eod", decimals=True)
    _check_record_metadata(records, snapshot)
    rows = _normalized_prices(records, snapshot)
    errors = validate_prices(rows)
    if errors:
        raise ValueError(errors)
    return rows


def load_actions(root, manifest):
    """Return reported action records only; an empty source list stays empty."""
    result = {}
    for kind in ("splits", "dividends"):
        snapshot = manifest["snapshots"][kind]
        records = _parse_records(_checked_raw(root, snapshot), kind)
        _check_record_metadata(records, snapshot)
        result[kind] = records
    return result


def fetch(root):
    """Fetch all three official samples; write private snapshots and metadata."""
    root = Path(root).resolve()
    pending = []
    snapshots = {}
    # Validate all responses before replacing the public manifest.
    for kind, url in URLS.items():
        content, headers = phase1.download(url)
        records = _parse_records(content, kind, decimals=(kind == "eod"))
        relative_path = RAW_DIRECTORY / f"AAPL-{kind}-{phase1.sha256(content)}.json"
        snapshot = _metadata(url, content, headers, relative_path, records)
        if kind == "eod":
            errors = validate_prices(_normalized_prices(records, snapshot))
            if errors:
                raise ValueError(errors)
        snapshots[kind] = snapshot
        pending.append((root / relative_path, content))
    for path, content in pending:
        if path.exists() and path.read_bytes() != content:
            raise ValueError("Refusing to overwrite a different EODHD raw snapshot")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    daily = snapshots["eod"]
    manifest = {
        "schema_version": 1,
        "provider": PROVIDER,
        "ticker": TICKER,
        "provider_symbol": "AAPL.US",
        "currency": "USD",
        "exchange_timezone": "America/New_York",
        "requested_date_from": START_DATE,
        "requested_date_to": END_DATE,
        "rows": daily["rows"],
        "date_min": daily["date_min"],
        "date_max": daily["date_max"],
        "source_url": daily["source_url"],
        "fetched_at_utc": daily["fetched_at_utc"],
        "raw_path": daily["raw_path"],
        "sha256": daily["sha256"],
        "license": LICENSE_NOTE,
        "terms_url": TERMS_URL,
        "documentation_url": DOCUMENTATION_URL,
        "demo_documentation_url": DEMO_DOCUMENTATION_URL,
        "action_documentation_url": ACTION_DOCUMENTATION_URL,
        "ohlc_basis": "raw_as_traded",
        "adjusted_close_basis": "splits_and_dividends_as_of_fetch",
        "volume_basis": "split_adjusted",
        "adjusted_history_may_be_revised": True,
        "daily_action_fields_available": False,
        "raw_committed": False,
        "public_price_rows_committed": 0,
        "public_action_rows_committed": 0,
        "snapshots": snapshots,
    }
    phase1.write_json(root / MANIFEST_PATH, manifest)
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("fetch",))
    parser.add_argument("--root", type=Path, default=phase1.ROOT)
    args = parser.parse_args()
    manifest = fetch(args.root)
    print(f"Fetched {manifest['rows']} AAPL daily records into ignored local storage")


if __name__ == "__main__":
    main()
