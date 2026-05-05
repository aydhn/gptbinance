# Waiver Boundaries & Non-Waivable Invariants

## Waivers

Waivers allow specific rules to be temporarily bypassed for specific scopes. They require a TTL and rationale.
- Waivers do NOT mean safety is ignored; they are targeted exceptions.
- Expired (stale) waivers are ignored during evaluation.

## Non-Waivable Invariants

Invariants are core safety principles that can never be waived. They enforce boundary conditions such as preventing live trading without the correct workspace context or blocking the auto-application of venue-affecting remediations.
