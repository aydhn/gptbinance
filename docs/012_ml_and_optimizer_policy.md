# ML & Optimizer Policy

The emphasis here is discipline, not hype. Machine Learning is treated as a highly suspicious, optional toolset that must prove its worth.

## What ML IS Allowed To Do
*   Generate predictive signals (e.g., probability of upward movement in next N periods).
*   Classify market regimes to adjust strategy weights.
*   Act as a meta-labeler (e.g., predicting whether a standard indicator's signal will be profitable).

## What ML is NOT Allowed To Do
*   Directly manage portfolio sizing.
*   Bypass hard risk limits.
*   Execute orders directly.
*   Operate as a "black box" where feature importance cannot be somewhat understood (prefer interpretable models initially).

## Candidate Model Categories
*   Tree-based ensembles (XGBoost, LightGBM, Random Forest) are preferred over Deep Learning for tabular time-series data due to speed, interpretability, and lower risk of silent overfitting.
*   Linear/Logistic regression for baseline comparisons.

## Defenses Against Overfitting
*   **Purging and Embargoing:** When using cross-validation on time-series, overlapping data points must be purged, and an embargo period applied to prevent future leakage.
*   **Feature Importance Stability:** Features must show consistent importance across different folds.

## Optimizer Constraints
*   Hyperparameter search spaces must be constrained. (e.g., don't search SMA lengths from 1 to 1000; search sensible ranges).
*   Avoid maximizing for a single metric (like raw return). Optimize for stability and risk-adjusted metrics.

## Retraining Governance
*   Models do not "learn online" in real-time. This is too dangerous.
*   Models are retrained offline periodically (e.g., weekly/monthly) using newly collected data.
*   A new model version must be benchmarked against the currently running version (Champion vs. Challenger) before promotion.
