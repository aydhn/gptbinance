# Phase 109 - Dominance, Frontier, Local vs Global Optimum, and Metric Gaming Policy

## 1. Dominance Evaluation
An option is **dominated** if another option exists that is better in at least one objective and no worse in all others. The tradeoff plane actively evaluates options to detect dominance. Selecting a dominated option is a severe governance failure and triggers immediate alerts.

## 2. Tradeoff Frontiers
The tradeoff frontier represents the set of non-dominated options (Pareto-like efficiency). Decisions must explicitly declare their position on this frontier.

## 3. Local vs. Global Optima
Optimizing a single component (Local Optimum) often degrades the overall system (Global Optimum). The tradeoff plane requires options to specify their evaluation scope. A local optimum that creates negative externalities globally will have its trust degraded.

## 4. Preventing Metric Gaming
- **Single-Metric Theater**: Optimizing exclusively for one objective while ignoring all others (e.g., achieving ultra-low latency at the cost of zero resilience) is flagged.
- **Top Metric != Best Choice**: A metric improvement does not authorize an action if the resultant burden shift is unacceptable.
