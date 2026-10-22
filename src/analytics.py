"""MarketPulse analytics: pure functions for comparison"""


def index_by_date(prices):
    return {row["date"]: row for row in prices}

def align_series(inst_prices, benchmark_prices):
    inst_by_date = index_by_date(inst_prices)
    benchmark_by_date = index_by_date(benchmark_prices)

    common_dates = sorted(set(inst_by_date) & set(benchmark_by_date))

    aligned_inst = [inst_by_date[date] for date in common_dates]
    aligned_benchmark = [benchmark_by_date[date] for date in common_dates]

    return aligned_inst, aligned_benchmark # Lead (kharishan)


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