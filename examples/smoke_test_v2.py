"""Minimal J-Quants API v2 smoke test.

Reads the API key only from the JQUANTS_API_KEY environment variable.
Fetches one historical daily bar for Toyota Motor (7203) using the user's plan.
No orders, account access, file writes, or external destinations are used.
"""

import os
import sys

import jquantsapi


def main() -> int:
    if not os.getenv("JQUANTS_API_KEY"):
        print("ERROR: JQUANTS_API_KEY is not set.")
        return 2

    client = jquantsapi.ClientV2()

    # Free-plan-friendly historical date: well outside the 12-week delay window.
    df = client.get_eq_bars_daily(
        code="7203",
        date_yyyymmdd="2026-07-01",
    )

    if df.empty:
        print("Connected to J-Quants, but no row was returned for 7203 on 2026-07-01.")
        return 1

    print(df.to_string(index=False))
    print(f"\nSUCCESS: fetched {len(df)} row(s) from J-Quants API v2.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
