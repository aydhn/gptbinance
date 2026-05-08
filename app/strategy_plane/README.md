# Strategy Plane and Thesis Lifecycle Governance

## Overview
This plane establishes a canonical strategy registry, hypothesis/thesis contracts, lifecycle governance, fit/overlap/decay/degradation analytics, equivalence, and a trusted strategy verdict.

## Key Principles
1. **Canonical Strategy Registry:** All strategies are typed and registered. No undocumented or hidden strategy logic.
2. **Hypothesis and Thesis Contracts:** Strategies are based on explicit behavioral claims and benchmarks.
3. **Lifecycle States:** Clear states (Research -> Replay -> Paper -> Probation -> Live) and promotion requirements.
4. **No Silent Mutation:** Code changes must be tracked; significant changes require new strategy versions.
5. **Replay/Live Equivalence:** We monitor for divergence between expected (replay) and actual (live) execution.
6. **Decay and Degradation:** We track when a strategy starts failing its thesis and explicitly manage its state (Degraded, Frozen, Retired).

## Why not just a backtest catalog?
Because a good backtest does not mean a good strategy in a specific regime or sleeve. This governance layer ensures strategies fit the current market environment and don't cannibalize each other, and requires explicit typed evidence for promotion.
