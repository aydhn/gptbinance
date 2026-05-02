# Health, Alert, and SLO Boundaries

## Health Severity
- `HEALTHY`: Component operating within normal parameters.
- `DEGRADED`: Partial failure (e.g., minor lag, few rejected orders) but still functioning.
- `CRITICAL`: Severe issue (e.g., stream dead, max drawdown breached). Requires immediate operator attention.
- `HALTED`: The component has safely suspended operations.

## Alert Lifecycle
Alerts transition from `OPEN` to `CLEARED`. If they repeat rapidly, their `occurrence_count` increments rather than spamming the event bus.

## SLO Philosophy
We measure standard reliability indicators (SLIs) like stream freshness or readiness success rates. However, we avoid aggressive enterprise guarantees. The SLO system provides honest, local-first measurements of system quality.
