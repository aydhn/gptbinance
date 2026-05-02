# Failure Injection and Recovery Assertion Policy

## Fault Injection Rules
1. **Bounded Duration**: Faults must have a strict timeout (`duration_ms`).
2. **Reversible**: The system must be able to return to its previous state.
3. **No Silent State Corruption**: Faults should mimic external failures (latency, malformed data), not corrupt internal critical DB state without a recovery path.

## Assertion Policy
1. **Defense Verification**: We assert that the system *detected* the fault (e.g., opened an alert, engaged a kill switch). We don't just assert that the fault happened.
2. **Recovery Verification**: After the fault is removed, the system must prove it can recover (e.g., queues drain, alerts clear).
3. **Pass/Fail Interpretation**: If a fault happens but the system doesn't alert/defend, the assertion fails, and the resilience score drops.
