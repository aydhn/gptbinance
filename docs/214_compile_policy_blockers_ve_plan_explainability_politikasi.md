# Compile Policy Blockers & Explainability

## Policy Blockers
The `PolicyEngine` can block intents based on:
- Event Risks (cannot open new positions during major data releases).
- Capital Posture (if the tier disables new exposure).
- Cross-book Fake Hedge (preventing isolated vs cross margin hedging conflicts).

## Explainability
Every plan includes a `PlanDiff` and `PlanExplanation`. This makes it clear *why* size was adjusted (due to rounding) or *why* the intent was blocked (e.g., "Event risk active").
