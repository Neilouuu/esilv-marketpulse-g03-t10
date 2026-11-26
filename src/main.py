from pathlib import Path
import csv
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.analytics import (
    align_series,
    calculate_period_return,
    calculate_base_100,
    calculate_relative_performance,
)
from src.providers.yahoo_provider import fetch_yahoo_prices
from src.providers.bloomberg_provider import ACCESS_MODE, fetch_bloomberg_prices


DATA_DIR = Path("data/sample")

LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"

PROVIDER = "bloomberg"  # "bloomberg", "yahoo" or "csv"
YAHOO_LOOKBACK = "1mo"
YAHOO_INTERVAL = "1d"


def load_instruments():
    with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
        return json.load(file)


def load_prices():
    with open(DATA_DIR / "prices.csv", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def filter_prices(prices, ticker):
    return [row for row in prices if row["ticker"] == ticker]


def display_market_summary(asset, prices, show_currency=True):
    currency = f" {asset['currency']}" if show_currency else ""
    print(f"{asset['ticker']} - {asset['name']}")
    print(f"Market       : {asset['market']}")
    print(f"Observations : {len(prices)}")
    print(f"First date   : {prices[0]['date']}")
    print(f"Last date    : {prices[-1]['date']}")
    print(f"First close  : {float(prices[0]['close']):.2f}{currency}")
    print(f"Last close   : {float(prices[-1]['close']):.2f}{currency}")


def build_market_snapshot():
    instruments = load_instruments()
    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    if PROVIDER == "bloomberg":
        instrument_prices = fetch_bloomberg_prices(instrument["ticker"])
        benchmark_prices = fetch_bloomberg_prices(benchmark["ticker"])
    elif PROVIDER == "yahoo":
        instrument_prices = fetch_yahoo_prices(instrument["ticker"], YAHOO_LOOKBACK, YAHOO_INTERVAL)
        benchmark_prices = fetch_yahoo_prices(benchmark["ticker"], YAHOO_LOOKBACK, YAHOO_INTERVAL)
    else:
        prices = load_prices()
        instrument_prices = filter_prices(prices, instrument["ticker"])
        benchmark_prices = filter_prices(prices, benchmark["ticker"])

    aligned_instrument, aligned_benchmark = align_series(instrument_prices, benchmark_prices)
    instrument_return = calculate_period_return(aligned_instrument)
    benchmark_return = calculate_period_return(aligned_benchmark)

    return {
        "provider": PROVIDER,
        "access_mode": ACCESS_MODE if PROVIDER == "bloomberg" else "-",
        "lookback": LOOKBACK_LABEL,
        "interval": INTERVAL_LABEL,
        "instrument": instrument,
        "benchmark": benchmark,
        "instrument_prices": instrument_prices,
        "benchmark_prices": benchmark_prices,
        "aligned_sessions": len(aligned_instrument),
        "instrument_return": instrument_return,
        "benchmark_return": benchmark_return,
        "relative_performance": calculate_relative_performance(instrument_return, benchmark_return),
        "instrument_base_100": calculate_base_100(aligned_instrument),
        "benchmark_base_100": calculate_base_100(aligned_benchmark),
    }


def main():
    s = build_market_snapshot()
    inst = s["instrument"]["ticker"]
    bench = s["benchmark"]["ticker"]

    print("=== MarketPulse - Instrument vs Benchmark ===")
    print()
    print(f"Provider    : {s['provider']}")
    print(f"Access mode : {s['access_mode']}")
    print(f"Period      : {s['lookback']}")
    print(f"Interval    : {s['interval']}")
    print()
    print("Instrument")
    display_market_summary(s["instrument"], s["instrument_prices"])
    print()
    print("Benchmark")
    display_market_summary(s["benchmark"], s["benchmark_prices"], show_currency=False)
    print()
    print(f"Aligned sessions     : {s['aligned_sessions']}")
    print(f"{inst} return          : {s['instrument_return']:+.2f}%")
    print(f"{bench} return         : {s['benchmark_return']:+.2f}%")
    print(f"Relative performance : {s['relative_performance']:+.2f} pts")
    print(f"Base 100 {inst}        : 100.00 -> {s['instrument_base_100'][-1]['value']:.2f}")
    print(f"Base 100 {bench}       : 100.00 -> {s['benchmark_base_100'][-1]['value']:.2f}")


if __name__ == "__main__":
    main()