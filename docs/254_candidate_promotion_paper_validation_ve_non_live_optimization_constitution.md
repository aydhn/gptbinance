# Promotion and Non-Live Optimization

A candidate that passes offline validation and fragility checks is **not** deployed live.
Instead, it is promoted to the next evaluation step: e.g., Paper or Shadow trading.

**Non-Live Optimization Constitution:**
- Experiments cannot bypass policy invariants.
- Experiments must not mutate live configuration silently.
- Candidates must pass through formal evidence bundling before promotion.
