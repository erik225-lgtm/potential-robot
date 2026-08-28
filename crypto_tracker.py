#!/usr/bin/env python3
"""
Crypto Tracker - Fetch and display current cryptocurrency prices.

Uses the public CoinGecko API (no API key required).
"""

import json
import sys
import urllib.request
from datetime import datetime, timezone


COINGECKO_API = "https://api.coingecko.com/api/v3"

DEFAULT_COINS = ["bitcoin", "ethereum", "litecoin", "dogecoin"]
DEFAULT_CURRENCY = "usd"


def fetch_prices(coin_ids: list[str], vs_currency: str = DEFAULT_CURRENCY) -> dict:
    """Fetch current prices for the given coin IDs from CoinGecko."""
    ids_param = ",".join(coin_ids)
    url = (
        f"{COINGECKO_API}/simple/price"
        f"?ids={ids_param}"
        f"&vs_currencies={vs_currency}"
        f"&include_24hr_change=true"
        f"&include_last_updated_at=true"
    )
    with urllib.request.urlopen(url, timeout=10) as response:
        return json.loads(response.read())


def format_change(change: float | None) -> str:
    """Format a 24-hour percentage change with colour indicators."""
    if change is None:
        return "  n/a  "
    sign = "+" if change >= 0 else ""
    return f"{sign}{change:.2f}%"


def display_prices(data: dict, vs_currency: str = DEFAULT_CURRENCY) -> None:
    """Print a table of cryptocurrency prices."""
    currency_symbol = vs_currency.upper()
    col_coin = 15
    col_price = 20
    col_change = 12
    header_parts = [
        f"{'Coin':<{col_coin}}",
        f"{'Price (' + currency_symbol + ')':<{col_price}}",
        f"{'24h Change':<{col_change}}",
        "Last Updated",
    ]
    header = " ".join(header_parts)
    print(header)
    print("-" * len(header))
    for coin_id, info in data.items():
        price = info.get(vs_currency)
        change = info.get(f"{vs_currency}_24h_change")
        last_updated = info.get("last_updated_at")
        updated_str = (
            datetime.fromtimestamp(last_updated, tz=timezone.utc).strftime(
                "%Y-%m-%d %H:%M UTC"
            )
            if last_updated
            else "unknown"
        )
        price_str = f"{price:,.2f}" if price is not None else "n/a"
        print(
            f"{coin_id:<{col_coin}} {price_str:<{col_price}} {format_change(change):<{col_change}} {updated_str}"
        )


def main(argv: list[str] | None = None) -> int:
    """Entry point for the crypto tracker CLI."""
    args = argv if argv is not None else sys.argv[1:]

    # Allow the user to pass coin IDs as CLI arguments, e.g.:
    #   python crypto_tracker.py bitcoin ethereum solana
    coins = args if args else DEFAULT_COINS
    currency = DEFAULT_CURRENCY

    print(f"Fetching prices for: {', '.join(coins)}\n")
    try:
        data = fetch_prices(coins, currency)
    except Exception as exc:  # noqa: BLE001
        print(f"Error fetching data: {exc}", file=sys.stderr)
        return 1

    if not data:
        print("No data returned. Check that the coin IDs are valid.", file=sys.stderr)
        return 1

    display_prices(data, currency)
    return 0


if __name__ == "__main__":
    sys.exit(main())
