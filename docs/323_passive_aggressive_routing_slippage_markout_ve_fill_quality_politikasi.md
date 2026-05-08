# Passive/Aggressive Routing, Slippage, Markout, and Fill Quality

## Routing Urgency
Execution orders carry routing policies (Passive, Aggressive, Staged Slice). The rationale for selecting the route is stored immutably to ensure explainability.

## Slippage & Markout
Realized slippage against the expected reference price is categorized explicitly (Mild, Elevated, Critical). Short-horizon markout evaluates passive vs. aggressive tradeoff quality post-fill.

## Fill Quality
We synthesize `FillQualityReport` based on fill completeness (partial fills) and maker/taker mix, which directly contributes to the overall `ExecutionQualityVerdict`.
