# Fair Comparison, Exposure Allocation, and Hidden Baseline Drift Policy

## Exposure Allocation
Arms must receive explicit allocations. A 90/10 split inherently causes different capacity constraint impacts. This must be tracked.

## Fairness Criteria
- Exposure imbalance
- Window imbalance
- Regime imbalance
- Missingness imbalance
- Risk block imbalance
- Execution friction imbalance

## Baseline/Control Drift
If the baseline's configuration or code changes during an experiment, this hidden drift must be caught and logged.

## Incomparable Arm Risks
Using pseudo controls that don't match the candidate's core universe or capacity structure leads to invalid promotion decisions.

## Why Hidden Traffic Shift is Forbidden
A strategy automatically grabbing more exposure mid-experiment because it's doing well compromises the stopping rules and fair comparison window.
