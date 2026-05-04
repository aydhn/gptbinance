# Reduce-Only, Borrow/Repay, and Multi-Leg Policy

## Safety Guards
- **Reduce-Only**: Ensure compilation fails if a reduce-only intent is on the same side as the existing exposure (e.g., trying to BUY when already LONG).
- **Close-Only**: Uses `closePosition` strictly to flatten.

## Margin Borrow/Repay
Intent like `margin_borrow_backed_buy` compiles into a Multi-Leg Plan:
1. `MARGIN_BORROW` (leg 1)
2. `MARGIN_TRADE` (leg 2, depends on leg 1).

## Multi-Leg Plans
They define explicit dependencies. If Leg 1 fails, Leg 2 must not execute. This logic is handled by execution, but defined clearly in the Compiled Plan.
