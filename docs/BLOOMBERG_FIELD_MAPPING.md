# Bloomberg Field Mapping

## Access mode

LIVE - Bloomberg Terminal (remote session), function HP, daily, USD.

## Instruments

| Role | Canonical ticker | Bloomberg identifier |
|---|---|---|
| Instrument | AAPL | AAPL US Equity |
| Benchmark | SP500 | SPX Index |

Both were inspected with HP. Dates are shown as MM/DD/YY.

## Field mapping

| MarketPulse field | Source | Notes |
|---|---|---|
| date | Date | MM/DD/YY, convert to YYYY-MM-DD |
| ticker | application mapping | AAPL / SP500 |
| open | - | not observed |
| high | - | not observed |
| low | - | not observed |
| close | Last Price | observed |
| volume | - | not observed |

Field names are the HP screen labels. No field name was invented.

## TD10 handoff

- Access mode: LIVE
- AAPL US Equity -> AAPL, SPX Index -> SP500
- Date format: MM/DD/YY
- Input structure: HP price table, one row per trading day, most recent first
- Missing fields: open, high, low, volume
- Notes: remove thousands separator (7,182.78), skip empty days, keep analytics.py unchanged