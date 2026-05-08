# Execution Plane Governance Layer

## Necessity
An allocation intent defines *what* should happen to the portfolio. It does not define *how* it should safely interact with real-world venues. The Execution Plane solves the translation gap by converting intents into typed, venue-aware, and idempotency-protected `OrderSpec` definitions.

## Scope
- Allocation to Execution Candidate translation.
- Venue Filters (Notional, Qty, Tick Size) enforcement.
- Passive vs Aggressive routing evaluation.
- Idempotency checks to block duplicate sends.
- Safe Cancel/Replace chains blocking ambiguous original states.
- Short-horizon markout and realized slippage analysis.

## Boundaries
- No HFT router capabilities.
- No direct exchange connection/execution within this layer (handled by Venue adapters).
- Execution Quality is kept distinct from Portfolio Attribution.
