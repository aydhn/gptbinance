# Phase 64: Position Plane ve Inventory Truth Mimarisi

## fills -> lots -> states -> exposures -> pnl attribution akışı
The position plane is designed to create a deterministic path from execution fills to the final recognized position state and its corresponding PnL. This avoids any magical summarization and traces every lot.

## Why no approximate inventory
Approximations lead to risk, capital, and compliance failures. We must have strict definitions of our actual position or flag it explicitly as degraded.

## Why realized != unrealized
Realized PnL is cash that has settled based on closed lots. Unrealized PnL is a mark-to-market estimation based on current prices, which may be stale.

## Position governance mantığı
Governance is the core here. The system must explicitly know what it owns, what it costs, and what caveats apply to those valuations.
