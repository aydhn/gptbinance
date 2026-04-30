# Derivatives Execution Base

This module contains the models and rules required for managing Futures and Margin specific execution mechanics, heavily isolating them from the traditional Spot engine.

## Components
- **Leverage & Margin Modes**: Explicitly manages requested vs accepted states for each symbol to prevent unintended high leverage.
- **Reduce Only**: A strict safety valve to prevent closing orders from accidentally opening new positions on the reverse side.
- **Liquidation**: Approximate distance/proximity modeling to warn the system *before* submitting orders that could push the account near margin calls.
- **Carry Costs**: Accounting layer to ensure funding and borrow costs are visible in backtests and live sessions.
- **Pretrade Validation**: Gates derivative orders, enforcing max caps and reduce-only consistency.

## Design Philosophy
Do not mix this with Spot. These files are conservative safety guardrails explicitly designed for testnet-first and paper trading before live enablement.
