# Staged Activation Controller & Rollout Governance

## Why is a Staged Activation Controller Needed?
A readiness board decision (go/no-go) is insufficient on its own to safely deploy a complex trading strategy or update. If an approved candidate is enabled across the entire platform instantly without monitoring, a single un-caught error can cause catastrophic loss.

The Activation Controller enforces:
- **Activation Intents:** Wrapping board decisions into a strict scope and bounded intent.
- **Rollout Plans:** Breaking the activation into observed stages (e.g., observe-only -> limited symbols -> restricted sessions -> wider tiers).
- **Active-set Registry:** Tracking exactly which configuration bundle is active at any given time, preventing conflicts and drift.
- **Probation:** Gating stage progression behind strict health checks (market truth, lifecycle, capital, cross-book stability).
- **Expansion/Halt/Revert:** Clear, explicit decision paths. No automatic expansions.

## Key Principles
- **No Automatic Live Switch:** A board approval does not mean an automated rollout. Activation plans must be generated and explicitly stepped through.
- **Scope Enforcement:** Conditonal-go bounds (e.g., "only BTC/USDT") survive as hard enforcement boundaries during activation.
- **Reversible:** An active-set must always have a prior lineage to allow for "revert-to-prior" planning.
