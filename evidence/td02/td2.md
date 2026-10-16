# TD02 - Python + CSV / JSON

Équipe G03 / T10 : Neil GHARBI TORCHOUNA (@Neilouuu), Timéo BOLLOMEY (@timeo-b), Harishan KONESWARAN (@kharishan)
But du TD : charger les deux fichiers de `data/sample`, séparer AAPL et SP500, et afficher un résumé avec une seule fonction réutilisable.

## Code de `src/main.py`

```python
from pathlib import Path
import csv
import json


# dossier où sont rangés instruments.json et prices.csv
DATA_DIR = Path("data/sample")

# valeurs reprises de config/settings.yml (on ne lit pas le YAML pour l'instant)
LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"


# lit le JSON -> renvoie un dict avec 2 clés : "instrument" et "benchmark"
def load_instruments():
    with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
        return json.load(file)


# lit le CSV -> renvoie une liste de dicts (1 ligne du csv = 1 dict)
# attention : toutes les valeurs sont des str
def load_prices():
    with open(DATA_DIR / "prices.csv", encoding="utf-8") as file:
        return list(csv.DictReader(file))


# garde seulement les lignes du ticker demandé (AAPL ou SP500)
# boucle + condition, écrit en list comprehension
def filter_prices(prices, ticker):
    return [row for row in prices if row["ticker"] == ticker]


# prices[0] = premier jour de la période
# float() obligatoire sinon on a "250.00" en texte
def get_first_close(prices):
    return float(prices[0]["close"])


# prices[-1] = dernier jour
def get_last_close(prices):
    return float(prices[-1]["close"])


# même affichage pour l'instrument et le benchmark
# show_currency=False pour le S&P 500 car c'est un indice (en points, pas en USD)
def display_market_summary(asset, prices, show_currency=True):
    currency = f" {asset['currency']}" if show_currency else ""
    print(f"{asset['ticker']} - {asset['name']}")
    print(f"Observations : {len(prices)}")
    print(f"First close  : {get_first_close(prices):.2f}{currency}")
    print(f"Last close   : {get_last_close(prices):.2f}{currency}")


def main():
    # 1. charger
    instruments = load_instruments()
    prices = load_prices()

    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    # 2. filtrer (les 2 séries sont dans le même csv)
    instrument_prices = filter_prices(prices, instrument["ticker"])
    benchmark_prices = filter_prices(prices, benchmark["ticker"])

    # 3. afficher
    print("=== MarketPulse ===")
    print()
    print("Market configuration")
    print(f"Period   : {LOOKBACK_LABEL}")
    print(f"Interval : {INTERVAL_LABEL}")
    print()
    print("Instrument")
    display_market_summary(instrument, instrument_prices)
    print()
    print("Benchmark")
    display_market_summary(benchmark, benchmark_prices, show_currency=False)


if __name__ == "__main__":
    main()
```

## Résultat

```
=== MarketPulse ===

Market configuration
Period   : 1 month
Interval : Daily

Instrument
AAPL - Apple Inc.
Observations : 21
First close  : 250.00 USD
Last close   : 266.20 USD

Benchmark
SP500 - S&P 500
Observations : 21
First close  : 6600.00
Last close   : 6742.00
```

## Ce que j'ai retenu

- JSON -> dict, CSV -> liste de dicts
- les valeurs du CSV sont du texte, il faut `float()` avant de faire des calculs
- `prices[0]` / `prices[-1]` pour le premier et le dernier jour
- une fonction réutilisée 2 fois au lieu de copier-coller le même code
- `main()` reste simple : charger -> filtrer -> afficher
