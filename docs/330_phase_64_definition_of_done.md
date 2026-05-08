# Phase 64: Definition of Done

## Tamamlanma Ölçütleri
- Position Plane framework is built (lots, states, exposures).
- Realized/unrealized/fee/funding/carry logic is isolated.
- Hedge-aware exposure, reconciliation, and divergence are implemented.
- Equivalence and trust verdicts are working.
- Integration points are established.
- CLI commands are available.
- Tests cover core logic.

## Bilerek Ertelenenler
- Real-time stream processing for position states (deferred to infrastructure phase).
- Complex cross-margin collateral calculations (deferred to advanced capital phase).

## Sonraki Faza Geçiş Şartları
All tests must pass and the CLI must accurately return the desired position summaries. Phase 65 will focus on advanced automated hedging and execution routing overlay.
