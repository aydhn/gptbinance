# Phase 32: Incident Forensics and Replayability Score Policy

## Forensic Bundle
For ad-hoc incident investigations, the system collects the timeline, decision path, diff findings, and telemetry logs into a single `ForensicBundle`.

## Replayability Score
To quantify trust in a replay:
- Source Completeness
- Lineage Completeness
- Snapshot Fidelity
- Schema Compatibility
The result is not just a single magic number, but a breakdown that issues a verdict: `TRUSTED`, `CAUTION`, or `UNTRUSTED`.
