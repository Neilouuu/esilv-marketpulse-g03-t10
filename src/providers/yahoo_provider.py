"""Yahoo Finance provider: returns canonical observation rows (TD08)."""

import yfinance as yf

CANONICAL_TO_YAHOO = {
    "AAPL": "AAPL",
    "SP500": "^GSPC",
}


def fetch_yahoo_prices(canonical_ticker, lookback="1mo", interval="1d"):
    yahoo_symbol = CANONICAL_TO_YAHOO[canonical_ticker]

    raw = yf.Ticker(yahoo_symbol).history(period=lookback, interval=interval)

    if raw.empty:
        raise ValueError(f"No Yahoo data returned for {yahoo_symbol}")

    rows = []
    for timestamp, values in raw.iterrows():
        rows.append(
            {
                "date": timestamp.strftime("%Y-%m-%d"),
                "ticker": canonical_ticker,
                "open": float(values["Open"]),
                "high": float(values["High"]),
                "low": float(values["Low"]),
                "close": float(values["Close"]),
                "volume": int(values["Volume"]),
            }
        )

    return sorted(rows, key=lambda row: row["date"])