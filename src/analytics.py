"""MarketPulse analytics: pure functions for comparison"""


def index_by_date(prices):
    raise NotImplementedError  # Student 2 (timeo-b)


def align_series(instrument_prices, benchmark_prices):
    raise NotImplementedError  # Lead (kharishan)


def calculate_period_return(prices):
    raise NotImplementedError  # Student 2 (timeo-b)


def calculate_base_100(prices):
    if not prices:
        raise ValueError("Cannot compute base 100 on an empty series")
    first_close = float(prices[0]["close"])
    if first_close == 0:
        raise ValueError("First close is zero: base 100 is undefined")
    return [
        {
            "date": row["date"],
            "ticker": row["ticker"],
            "value": (float(row["close"]) / first_close) * 100.0,
        }
        for row in prices
    ]


def calculate_relative_performance(instrument_return, benchmark_return):
    return instrument_return - benchmark_return