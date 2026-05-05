# Experiment Governance & Hypothesis Registry

This document outlines the architecture for the controlled research loop. Findings from decision quality, remediation, and market truth layers are translated into formal hypotheses rather than immediate code changes.

The rationale for this separation is that direct ad-hoc tuning leads to overfitting and live optimizations. A disciplined research loop requires hypotheses to be explicitly stated and tested against frozen baselines.

## Flow
1. Findings are collected in the intake.
2. The finding is compiled into a `HypothesisRecord`.
3. An `ExperimentPack` is built containing the baseline and candidate configurations.
4. Offline evaluations produce evidence.
5. Fragility analysis ensures no overfit.
