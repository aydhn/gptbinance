# Spot, Margin, Futures Venue Semantics & Account Mode Policy

## Venue Semantics
- **Spot**: Simple asset trading. No leverage, no reduceOnly, no closePosition.
- **Margin (Cross/Isolated)**: Allows borrowing. Does not use standard `reduceOnly` flags (uses repay mechanisms).
- **Futures (USDM/COINM)**: Supports `reduceOnly`, `closePosition`. Highly sensitive to `positionMode` (One-Way vs Hedge).

## Account Mode Checks
The system must resolve the current `AccountModeSnapshot` before compiling. Trying to open a Hedge Mode futures order while the account is in One-Way mode will be blocked at compile-time.
