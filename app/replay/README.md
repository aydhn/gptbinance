# Deterministic Replay, Time-Travel Debugging & Incident Forensics

This module provides the deterministic replay, decision reconstruction, and counterfactual simulation layers for the platform.

## Why Deterministic Replay?
When an incident, anomaly, or execution difference occurs, analyzing static logs is often insufficient. This module allows the system to:
1. Identify the sources (e.g., paper session refs, bundle lineage).
2. Load a point-in-time snapshot.
3. Reconstruct the historical event timeline.
4. Execute a read-only replay of the components (signal -> risk -> portfolio -> execution).
5. Explain the decision path.
6. Compute diffs between the recorded history and the replay.
7. Run counterfactuals ("what-if" scenarios).
8. Generate forensic bundles for incident investigation.

## Read-Only Guarantee
**This layer never mutates the past.**
The replay engine operates strictly in a read-only context. It does not patch historical databases, and it absolutely never issues actual live orders or live restores.

## CLI Commands
- `--run-replay --replay-scope trade --replay-source-ref execution:<id>`: Run replay on a trade.
- `--run-counterfactual --run-id <id> --counterfactual-type ml_disabled`: Run a counterfactual simulation.
- `--show-replay-summary --run-id <id>`: Show verdict and fidelity summary.
- `--show-decision-path --run-id <id>`: Show decision sequence.
- `--build-forensic-bundle --run-id <id>`: Create a forensic artifact for investigations.
