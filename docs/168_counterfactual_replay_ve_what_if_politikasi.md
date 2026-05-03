# Phase 32: Counterfactual Replay and What-If Policy

## Historical vs Counterfactual
Historical replay verifies "what happened", matching recorded execution. Counterfactual replay asks "what if" by selectively injecting state variations (e.g., lower portfolio budget, ML module disabled, varying network slippage).

## Supported What-Ifs
- `ml_disabled`: Removes AI inputs from risk.
- `lower_budget`: Adjusts portfolio cap constraint.
- `stricter_concentration`: Tighter risk rules.

## The Rule of Reality
Counterfactual runs are permanently tagged to separate them from historic logs. They never replace canonical records. Governance uses them for decay analysis and regime sensitivity testing.
