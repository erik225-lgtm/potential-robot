# potential-robot

## Crypto Tracker

A lightweight command-line cryptocurrency price tracker that uses the free [CoinGecko API](https://www.coingecko.com/en/api) — no API key required.

### Requirements

- Python 3.10+

### Usage

```bash
# Show prices for the default coins (bitcoin, ethereum, litecoin, dogecoin)
python crypto_tracker.py

# Show prices for specific coins (use CoinGecko IDs)
python crypto_tracker.py bitcoin solana cardano polkadot
```

### Example output

```
Fetching prices for: bitcoin, ethereum, litecoin, dogecoin

Coin            Price (USD)          24h Change   Last Updated
------------------------------------------------------------------------
bitcoin         67,123.45            +1.23%       2024-11-01 14:30 UTC
ethereum        3,456.78             -0.45%       2024-11-01 14:30 UTC
litecoin        78.90                +0.67%       2024-11-01 14:30 UTC
dogecoin        0.15                 +2.10%       2024-11-01 14:30 UTC
```
