# Ledger Plane & Balance Truth Architecture

## Why Ledger Plane?
Position truth and PnL truth alone are not sufficient for a highly mature trading platform. Operational errors frequently occur in cashflow and balance truth: available balance may be misrepresented, funding can be missed, internal transfers forgotten, or locked collateral assumed as free capital. Furthermore, wallet states can diverge from the venue's view.

This plane strictly governs the flow:
`fills -> cashflows -> ledger entries -> balances -> collateral truth`

## Core Concepts
- **Balance != Available != Collateral**: These buckets represent entirely different accounting states and cannot be used interchangeably.
- **No Opaque Treasury Truth**: The system rejects any single magical "equity" number without a full breakdown. Account-level equity is always derived from specific typed values.
- **Boundaries**: This phase builds the accounting/governance structure for balances. It **does not** create a custody/withdrawal automation engine, general accounting ERP, or silent synthetic adjustments.

## Features
- Cashflow Lineage
- Typed Balance and Collateral Truth
- Divergence detection (Runtime vs Venue)
- Trust verdicts and Evidence graph integration
