# Observability Architecture and Typed Telemetry Policy

## Purpose
This document outlines the architecture for Phase 26, focusing on a structured, code-first observability layer without relying on external SaaS dashboards.

## Core Pillars
1. **Typed Metrics and Events**: We strictly use typed telemetry (`MetricSample`, `TelemetryEvent`) instead of unstructured logs to prevent parsing errors and ensure queryability.
2. **Component Health**: Each module (`DATA_STREAM`, `EXECUTION`, etc.) computes its own health (`HEALTHY`, `DEGRADED`, `CRITICAL`), aggregating into a `SystemHealthSnapshot`.
3. **Alert Correlation**: To prevent alert fatigue, occurrences are deduplicated, and overlapping alerts are grouped into `AlertCorrelationGroup`s.

## Why No Dashboard?
Trading operations demand speed and absolute clarity. Web dashboards often hide the root cause behind abstract scores. By using a CLI-first approach (e.g., `--show-system-health`), operators get instant, reproducible, and verifiable snapshots.
