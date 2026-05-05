# Blast Radius, Preflight, Dry-Run and Rollback Policy

## 1. Blast Radius
Every `RemediationPack` must undergo a Blast Radius Analysis before execution.
- **Low Severity**: Only affects local shadow/cache layers. Safe.
- **Medium Severity**: May affect local order routing or flag variables (e.g. symbol quarantine). Requires approval.
- **Critical/High Severity**: Modifies venue state. Must generate request instead of applying.

## 2. Preflight & Dry-Run
- **Preflight** checks system safety state (e.g., active incidents block remediation).
- **Dry-Run** checks logical state deltas (e.g., ensuring local recompute won't just yield identical results to avoid noise).

## 3. Rollback
Before applying any local remediation (even local recompute), a rollback plan is generated.
- Local Cache refresh -> Restore previous snapshot.
- Quarantine Flag -> Revert to Unquarantined.
- Venue action -> Rollback is NOT reliable, thus we do not support automated rollbacks of venue-affecting actions.
