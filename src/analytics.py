"""MarketPulse analytics: pure functions for comparison"""


def index_by_date(prices):
    return {row["date"]: row for row in prices}

def align_series(instrument_prices, benchmark_prices):
    raise NotImplementedError  # Lead (kharishan)


def calculate_period_return(prices):
    if not prices:
        raise ValueError("Cannot compute a return on an empty series")

    first_close = float(prices[0]["close"])
    last_close = float(prices[-1]["close"])

    if first_close == 0:
        raise ValueError("First close is zero: return is undefined")

    return ((last_close / first_close) - 1.0) * 100.0


def calculate_base_100(prices):
    raise NotImplementedError  # Student 3 (Neilouuu)


def calculate_relative_performance(instrument_return, benchmark_return):
    raise NotImplementedError  # Student 3 (Neilouuu)