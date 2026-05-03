import argparse
from typing import List

# This file contains the snippet to add to app/main.py

def add_universe_commands(parser: argparse.ArgumentParser):
    group = parser.add_argument_group("Universe & Instrument Management")
    group.add_argument("--refresh-instrument-registry", action="store_true", help="Fetch and update the instrument registry")
    group.add_argument("--show-instrument-registry", action="store_true", help="Display current active instrument registry")
    group.add_argument("--show-symbol-details", action="store_true", help="Display details for a specific symbol")
    group.add_argument("--show-exchange-filters", action="store_true", help="Display exchange filters for a specific symbol")
    group.add_argument("--run-tradability-check", action="store_true", help="Evaluate tradability for a symbol")
    group.add_argument("--show-liquidity-report", action="store_true", help="Display liquidity report for a symbol")
    group.add_argument("--show-spread-report", action="store_true", help="Display spread report for a symbol")
    group.add_argument("--build-universe-snapshot", action="store_true", help="Build a universe snapshot for a profile")
    group.add_argument("--show-universe-diff", action="store_true", help="Display differences between universe snapshots")
    group.add_argument("--show-lifecycle-events", action="store_true", help="Display lifecycle events history")
    group.add_argument("--show-universe-impact", action="store_true", help="Display impact of universe changes")
    group.add_argument("--show-profile-universe", action="store_true", help="Display the effective universe for a profile")

    # Arguments used by the commands above
    group.add_argument("--symbol", type=str, help="Symbol name (e.g., BTCUSDT)")
    group.add_argument("--product-type", type=str, choices=["spot", "margin", "futures"], help="Product type")
    group.add_argument("--profile", type=str, help="Profile context name")
    group.add_argument("--run-id", type=str, help="Run ID for diff/impact analysis")

# Note: The implementation of these command handlers would instantiate the components
# defined in the app/universe module and print the formatted outputs using UniverseReporter.
