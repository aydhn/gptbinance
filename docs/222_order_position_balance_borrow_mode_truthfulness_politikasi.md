# Order, Position, Balance, Borrow, and Mode Truthfulness Policy

We evaluate truthfulness across 5 domains:
- **Open Orders**: Missing local vs Missing venue.
- **Positions**: Discrepancies in size or mode.
- **Balances**: Divergence in free, locked, or borrowed balances.
- **Borrow**: Undetected liabilities.
- **Mode**: Differences in Futures/Margin configuration.

Stale snapshots act as blockers to avoid making risky decisions on outdated evidence.
