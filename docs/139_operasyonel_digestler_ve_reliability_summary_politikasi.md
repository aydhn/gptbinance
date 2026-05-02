# Operational Digests and Reliability Summary

## Digest Generation
The `DigestBuilder` constructs periodic summaries representing system health over a `SESSION`, `DAILY`, or `WEEKLY` scope.

## Digest Contents
1. **Top Alerts**: The most frequent or severe alerts in the time window.
2. **Health Highlights**: High-level text summarizing major transitions or stable periods.
3. **SLO Summary**: Number of breached vs. evaluated Service Level Objectives.

## Objective
Provide governance and ops layers with a high-level overview of system reliability without forcing operators to dig through individual metric samples.
