# Fee, Funding, Carry, Mark-to-Market ve PnL Attribution Politikası

## Realized vs Unrealized
Clear segregation between settled cash flows and mark-to-market estimations.

## Fee/Funding/Carry Ayrımı
Fees, funding, and carry costs are separated from the pure price-move PnL to allow accurate performance analysis.

## Mark Freshness and Stale Mark Caveats
Unrealized PnL heavily depends on mark freshness. If a mark is stale (e.g., > 60s), the unrealized PnL is flagged with a caveat and its confidence score drops.

## Attribution Discipline
No blended opaque totals. Every dollar of PnL must be attributed to a specific component.
