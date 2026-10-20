## Quick start

1. Open a terminal at the **root of the repository** (in Codespaces: `/workspaces/esilv-marketpulse-g03-t10`).

2. Run:

```bash
   python src/main.py
```

3. Check the output. At the current stage, it should be:

```text
   === MarketPulse ===

   Market configuration
   Period   : 1 month
   Interval : Daily

   Instrument
   AAPL - Apple Inc.
   Observations : 21
   First date   : 2026-09-01
   Last date    : 2026-09-30
   First close  : 250.00 USD
   Last close   : 266.20 USD

   Benchmark
   SP500 - S&P 500
   Observations : 21
   First date   : 2026-09-01
   Last date    : 2026-09-30
   First close  : 6600.00
   Last close   : 6742.00
```

**Common error:** `can't open file '.../src/main.py'` means the command was not run from the repository root. Run `pwd` to check where you are, then go back with:

```bash
cd /workspaces/esilv-marketpulse-g03-t10
```