# Decision Quality and Opportunity Forensics Layer

The true test of a trading system is not merely its PnL or executed trades, but the comprehensive understanding of its decision-making lifecycle. Why do some signals become trades while others are blocked? What is the impact of risk, capital, event, policy, and market truth constraints?

This layer establishes the Signal-to-Action Funnel, Block Reason Taxonomy, and Hindsight-Safe Opportunity Forensics.

## Why Decision Quality?
Most systems focus either entirely on executed trades or only on overall strategy returns. The Decision Quality layer breaks the process down:
- **Opportunities:** Every meaningful signal is captured as a candidate.
- **Funnel:** The candidate progresses through defined stages (risk, portfolio, policy, intent, lifecycle).
- **Outcomes:** A decision is reached: Executed, Blocked, Skipped, or Suppressed.
- **Friction:** Diagnostics reveal where drop-offs happen (e.g., market truth block vs. risk limit block).
- **Hindsight-Safe Diagnostics:** Future outcomes of decisions are measured but interpreted carefully. "Missed alpha" or "good blocks" are logged safely, without hindsight determinism or auto-optimization.

## Boundaries
- This layer **does not** automatically tune strategies.
- This layer **does not** loosen safety policies.
- This layer provides auditable evidence, friction attribution, and analytical visibility.
