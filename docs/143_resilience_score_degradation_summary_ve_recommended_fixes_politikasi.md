# Resilience Score and Degradation Summary Policy

## Resilience Score
The score (0-100) is a composite of:
- **Detection**: Did we notice the anomaly?
- **Containment**: Did we stop the bleeding (kill switch, pause)?
- **Recovery**: Did we heal after the anomaly passed?

## Degradation Summary
Documents how the system behaved under stress (e.g., degraded to `PAUSE` mode for 10 seconds).

## Recommended Fixes
If assertions fail, the system provides recommended fixes (e.g., "Add timeout to data stream connector", "Tune alert threshold for drift").
