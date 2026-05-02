# Alert Correlation and Runbook Enrichment

## Alert Correlation
We use an `AlertCorrelator` to group alerts based on component overlap and time windows.
- Example: If `stream_stale` and `live_execution_rejects` spike simultaneously, they are likely related to network/exchange issues.

## Runbook Enrichment
When an alert triggers, the `IncidentEnricher` attempts to attach a `RunbookRef`.
- **Purpose**: Gives human operators immediate, static next steps.
- **Rule**: Runbooks do *not* execute code automatically; they guide the human.

## Suppression Rules
Alerts can be suppressed during maintenance windows using the `SuppressionEngine`. Critical alerts bypass standard suppression bounds to avoid hiding catastrophic failures.
