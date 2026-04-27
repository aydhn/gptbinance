# Research & Benchmarking Plan

This document outlines the evaluation doctrine for any strategy before it can be considered for paper or live trading.

## Baseline Benchmarks
Every proposed strategy must be compared against naive baselines to prove it possesses actual edge, not just market beta.
1.  **Buy and Hold (B&H):** The most fundamental benchmark.
2.  **Trend-Following Baseline:** A simple moving average crossover (e.g., 50/200 SMA).
3.  **Mean Reversion Baseline:** A simple Bollinger Band mean reversion strategy.

## Out-of-Sample (OOS) Discipline
*   Data must be strictly partitioned into In-Sample (IS) for development/tuning and Out-of-Sample (OOS) for validation.
*   "Peeking" at OOS data during development invalidates the research.

## Walk-Forward Analysis (WFA)
*   Static backtests over a single period are insufficient.
*   Strategies must undergo WFA (e.g., optimize on 1 year, test on next 3 months, roll forward) to evaluate parameter stability and robustness across changing market regimes.

## Regime Classification
*   The research layer should attempt to classify market regimes (e.g., Bull Volatile, Bear Quiet, Sideways).
*   Strategies should be evaluated based on which regimes they perform well in, enabling future meta-level switching.

## Ablation Studies
*   If a strategy has multiple rules or indicators, researchers must perform ablation studies (removing rules one by one) to prove that every piece of complexity adds measurable value.

## Promotion Criteria
Before promotion to `Paper` mode, a strategy must:
1.  Beat the relevant benchmark in Risk-Adjusted Return (e.g., Sharpe, Sortino, Calmar).
2.  Survive WFA without parameter collapse.
3.  Pass a code review ensuring it interfaces correctly with the standard `OrderRequest` mechanism and cannot bypass risk controls.
