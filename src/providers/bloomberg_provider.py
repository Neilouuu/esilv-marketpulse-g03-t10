import json

BLOOMBERG_IDENTIFIERS = {
    "AAPL": "AAPL US Equity",
    "SP500": "SPX Index",
}

ACCESS_MODE = "APPROVED_SAMPLE"
SAMPLE_FILE = "data/sample/bloomberg_reference_sample.json"


def fetch_raw_bloomberg_history(identifier):
    with open(SAMPLE_FILE, encoding="utf-8") as file:
        sample = json.load(file)
    for series in sample["series"]:
        if series["provider_identifier"] == identifier:
            return series["observations"]
    raise ValueError(f"No data for {identifier}")


def normalize_bloomberg_history(raw_data, canonical_ticker):
    rows = [
        {
            "date": obs["observation_date"],
            "ticker": canonical_ticker,
            "open": float(obs["open_value"]),
            "high": float(obs["high_value"]),
            "low": float(obs["low_value"]),
            "close": float(obs["close_value"]),
            "volume": int(obs["volume_value"]),
        }
        for obs in raw_data
    ]
    return sorted(rows, key=lambda row: row["date"])


def fetch_bloomberg_prices(canonical_ticker):
    identifier = BLOOMBERG_IDENTIFIERS[canonical_ticker]
    return normalize_bloomberg_history(fetch_raw_bloomberg_history(identifier), canonical_ticker)