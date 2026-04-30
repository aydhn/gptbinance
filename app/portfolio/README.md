# Portfolio Orchestration Module

The Portfolio Engine is responsible for capital allocation, position sizing, concentration control, and risk overlap management across multiple simultaneous opportunities (intents).

It acts as an orchestration layer sitting between the **Risk Engine** and the **Execution Engine**.

## Why not just Risk Engine?
The Risk Engine looks at a single intent and asks: "Is this transaction safe to execute based on predefined risk caps and account limits?"

The Portfolio Engine looks at a *batch* of risk-approved intents and asks: "Given our limited capital, which of these opportunities are the best? Are we getting too concentrated in one symbol or strategy? Do these opportunities overlap and compound risk?"

## Core Components
- **BudgetManager**: Ensures total reserved and available capital limits are respected.
- **PortfolioPolicyManager**: Enforces limits on symbol weight, strategy weight, and cluster weight.
- **SleeveManager**: Tracks strategy-specific and symbol-specific capital "sleeves" to prevent over-allocation.
- **CorrelationEstimator & OverlapEstimator**: Prevents "crowded" trades by penalizing intents that correlate strongly with existing exposure.
- **SimpleRankingModel**: Orders multiple valid intents based on score, overlap penalties, and utilization penalties.
- **ConservativeAllocator**: Processes ranked intents one by one, issuing APPROVE, REDUCE, DEFER, or REJECT verdicts based on budgets and policies.

## Deterministic and Conservative
We explicitly avoid black-box Convex Optimizers (like Mean-Variance or Black-Litterman). Allocation decisions must be completely transparent, explainable (`ExplainabilityEngine`), and conservative by default to ensure operational safety during live trading.
