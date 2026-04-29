# Live Runtime

The `live_runtime` module is the strict, highly-controlled operational boundary between the abstract Trading Logic (Strategy & Risk Engine) and the physical Execution Gateway interacting with Mainnet.

## Purpose
While the `risk` module approves trade intents mathematically, the `live_runtime` approves them operationally. It enforces strict **Capital Caps** (max exposure, max daily loss, daily session limits) independent of the strategy. It manages **Rollout Modes** (`shadow_only`, `canary_live`, `capped_live`, `full_live_locked`) ensuring that real money trades are never enabled by default.

## Boundaries
- It **does not** decide what to trade (Strategy).
- It **does not** handle REST/WS API requests (Execution Gateway).
- It **does not** manage system deployments or global incident lifecycles (Ops Control Plane).
- It **does** orchestrate a safe, isolated live trading session, maintaining its own Live Position Book and Live PnL, enforcing limits, flattening positions on panic, and writing an exact Post-Trade Audit Trail.
