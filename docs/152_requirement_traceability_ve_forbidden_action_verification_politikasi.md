# Requirement Traceability and Forbidden Action Verification Policy

## Traceability
Every critical requirement must trace to a test scenario or an evidence piece. Uncovered requirements result in a degraded qualification score.

## Forbidden Actions
Testing what the system *should* do is not enough. We must test what it *must not* do.
- e.g., "Active runtime upgrade blocked"
- e.g., "Missing critical secret blocks live readiness"

If a forbidden action is allowed, the qualification fails immediately.
