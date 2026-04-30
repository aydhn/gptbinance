# ML & Meta-Labeling Layer

## Architecture Overview
The ML layer is designed as an **auxiliary** component, meaning it supports but does not replace the rule-based strategy and risk engines. It operates with a strict time-aware discipline to prevent lookahead bias and data leakage.

The pipeline follows a rigid chain:
`Dataset Assembly -> Labeling -> Temporal Split -> Train -> Calibrate -> Register -> Infer -> Monitor Drift`

## Key Policies
1. **Auxiliary Role:** ML outputs act as quality scores, ranking helpers, or filters. They never act as sovereign decision-makers.
2. **Time Discipline:** Random shuffling during train/test splits is strictly prohibited. Data must be split chronologically (e.g., contiguous, anchored, expanding).
3. **Calibration:** Raw probabilities are not trusted. Calibration (e.g., Platt, Isotonic) must be evaluated and recorded.
4. **Registry & Lineage:** Every model must be registered with exact references to its dataset, features, labels, and training config.
5. **Drift Monitoring:** Production inference depends on drift visibility. If input distributions shift significantly, models must fallback safely to rule-based defaults.
