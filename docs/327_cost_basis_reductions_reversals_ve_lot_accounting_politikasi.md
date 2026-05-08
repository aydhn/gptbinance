# Lot Accounting, Cost Basis, Reductions ve Reversals Politikası

## Lot Accounting
Every fill generates a lot. Lots are immutable regarding their entry price and initial quantity, but their remaining quantity is consumed.

## Partial Close (Reductions)
Reductions consume open lots based on the chosen cost basis strategy (e.g., FIFO). They trigger realized PnL.

## Reverse / Flip
Reversing a position first acts as a full close on existing lots, generating realized PnL, and then opens new lots for the remaining amount in the new direction.

## Dust Residuals
Dust is explicitly tracked as a LifecycleState.DUST_RESIDUAL to prevent "almost closed" positions from cluttering normal logic while still maintaining accounting integrity.

## Why lot lineage matters
Realized PnL and fee attribution are only trusted if they can be traced back to the exact lots and fills that generated them.
