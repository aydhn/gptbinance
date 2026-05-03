# Phase 32: Decision Path Reconstruction and Diff Engine Policy

## Strategy to Execution Decision Path
The decision reconstructor unrolls stage transitions: `Signal -> Regime -> ML Inference -> Risk Decision -> Portfolio Allocation -> Control Auth -> Execution`. At each stage, the system records input variables, the decision rule applied, and output outcomes.

## Replay Diff Interpretation
The Diff Engine contrasts the reconstructed path against the original path recorded in analytics/telemetry:
- **Original vs Replay Diff:** Assesses variance.
- **Benign vs Critical:** Tolerances manage numerical drift (e.g. non-deterministic floating math). Large deviations or different final verdicts (e.g. executed vs rejected) are marked as critical.

## Deterministic Mismatch Risks
A mismatch highlights environmental drift, code modifications (hotfixes since the run), or missing telemetry/state history.
