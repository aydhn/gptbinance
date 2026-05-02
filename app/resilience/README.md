# Resilience & Chaos Laboratory

This module implements a safe, controlled environment for testing system resilience, chaos engineering, and stress profiles.

## Core Principles
1. **Safe Scopes Only**: By default, fault injection and chaos experiments are prohibited on the live mainnet. Experiments run in Simulation, Paper, Shadow, or Testnet modes.
2. **Assertion-Driven**: Every experiment must declare assertions (expected safe behaviors) and recovery checks.
3. **Reversible**: Faults must be automatically or manually reversible.
4. **Scoring**: Experiments generate a resilience score evaluating detection latency, containment, and recovery correctness.

## Workflow
1. Select a `Scenario` from the registry.
2. Define `ExperimentScope` (e.g., Paper mode).
3. The `SafetyGate` evaluates the request.
4. If allowed, `FaultInjector` and `StressGenerator` apply the conditions.
5. `AssertionEvaluator` checks if the system reacted properly.
6. Conditions are removed, and `RecoveryEvaluator` checks if the system healed.
7. `ResilienceScorer` generates a score and `Reporter` provides the summary.
