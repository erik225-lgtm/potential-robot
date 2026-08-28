"""Simple cryptocurrency price tracker."""

import json
import urllib.error
import urllib.request


def get_crypto_price(symbol: str) -> dict:
    """Fetch the current price of a cryptocurrency by symbol (e.g. 'bitcoin')."""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read())
            if symbol in data:
                return {"symbol": symbol, "price_usd": data[symbol]["usd"]}
            return {"error": f"Symbol '{symbol}' not found"}
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError, ValueError) as exc:
        return {"error": str(exc)}


def display_prices(symbols: list[str]) -> None:
    """Print prices for a list of cryptocurrency symbols."""
    print(f"{'Cryptocurrency':<20} {'Price (USD)':>15}")
    print("-" * 36)
    for symbol in symbols:
        result = get_crypto_price(symbol)
        if "error" in result:
            print(f"{symbol:<20} {'N/A':>15}  ({result['error']})")
        else:
            print(f"{result['symbol']:<20} ${result['price_usd']:>14,.2f}")


if __name__ == "__main__":
    tracked = ["bitcoin", "ethereum", "litecoin"]
    display_prices(tracked)
