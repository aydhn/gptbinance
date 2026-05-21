# Phase 109 - Objectives, Benefits, Burdens, Externalities, Sacrifices, and Non-Compensable Constraints Policy

## 1. Objectives
An objective is a typed intent (e.g., Speed, Safety, Reliability, Compliance, Value). All tradeoff decisions must bind to an explicit Objective Set. Optimization claims made without a defined objective set are treated as invalid.

## 2. Benefits vs. Value Gain
Value gain is the positive outcome of a decision, but it must be recorded alongside its scope. A localized benefit (e.g., faster execution on one node) is not treated as a global improvement until its federated impact is proven.

## 3. Burdens and Externalities
A burden is a cost or risk assumed by the decision.
- **Direct Burden**: Borne immediately by the executing team.
- **Transferred Burden**: Pushed to another team (e.g., human toil for operations).
- **Externality**: A burden placed on downstream consumers, cross-tenants, or future maintainers.
*Rule*: Burden burial is explicitly prohibited.

## 4. Sacrifices
A sacrifice is an explicit acknowledgment of a foregone benefit or an accepted degradation. It must be logged. A tradeoff object claiming improvements across the board without sacrifices is flagged as suspicious ("Sacrifice Burial Warning").

## 5. Non-Compensable Constraints
Some boundaries (e.g., core security postures, legal compliance, constitutional rules) are non-compensable. No amount of utility or speed can override these boundaries. Attempting to trade them away results in an immediate `BLOCKED` verdict.
