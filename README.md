# potential-robot

A simple cryptocurrency price tracker.

## Usage

Run the tracker to display current USD prices for Bitcoin, Ethereum, and Litecoin:

```bash
python crypto_tracker.py
```

You can also import and call the functions directly:

```python
from crypto_tracker import get_crypto_price, display_prices

price = get_crypto_price("bitcoin")
print(price)  # {'symbol': 'bitcoin', 'price_usd': ...}

display_prices(["bitcoin", "ethereum"])
```
