# Strategies Framework (Phase 07)

This module is responsible for the **Strategy Framework**, which evaluates features, generates signal candidates, scores them, resolves conflicts, and outputs intent candidates.

## Signal vs. Execution Separation
A core principle of this architecture is the complete separation between strategy (what looks like a good idea) and execution (actually placing a trade).
*   **Signals & Intents:** This module produces `SignalCandidate` and `EntryIntentCandidate` objects. These are *requests* or *ideas*.
*   **No Risk:** This module does *not* check account balance, open positions, max drawdowns, or margin.
*   **No Orders:** This module does *not* create or route orders.

## Explainability
Every signal must come with a rationale (`StrategyRationale`). This allows operators to debug why a strategy fired or failed to fire. "Black box" signals are prohibited. The scoring mechanism also contributes to this explainability by showing exactly how the final score was built.

## Score, Conflict, and Cooldown
*   **Scoring:** Helps prioritize when multiple signals fire simultaneously. It is not a guarantee of trade success.
*   **Conflicts:** The `ConflictResolver` handles cases where multiple strategies fire at the same time (e.g., conflicting directions or multiple signals in the same direction).
*   **Cooldowns:** Prevent a strategy from spamming signals (churning) in sideways or choppy markets.

## Strategy Families
This directory contains the base classes and a set of reference implementations representing different core market hypotheses:
*   `trend_follow_core`
*   `mean_reversion_core`
*   `breakout_core`
*   `structure_divergence_core`
