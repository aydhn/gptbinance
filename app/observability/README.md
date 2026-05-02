# Observability and Operational Telemetry

This package implements Phase 26 requirements. It is a strictly structured, dashboard-less telemetry layer designed for a zero-budget, high-reliability Python trading platform.

## Key Subsystems:
- **`metrics.py`**: Typed metric registry.
- **`telemetry.py`**: Structured event ingestion.
- **`health.py`**: Component and System health aggregation.
- **`alerts.py`**: Alert lifecycle and rule evaluation.
- **`correlation.py`**: Alert deduplication and grouping.
- **`suppression.py`**: Alert noise reduction.
- **`slo.py`**: Internal SLI/SLO compliance engine.
- **`enrichment.py`**: Context and runbook attachment to incidents.
- **`digests.py`**: Periodic summary generation.
- **`storage.py`**: SQLite persistence layer.

## Philosophy
- **No Dashboards**: Operations are driven by CLI commands and Telegram notifications.
- **Read-Only**: Observability measures and correlates, it does NOT automatically heal or modify the runtime configuration.
- **Typed**: Everything uses Pydantic models to ensure auditability and predictability.
