# Diff, Drift, and Equivalence

- **Diff**: The semantic difference between two manifests (e.g., candidate vs. runtime).
- **Drift**: When the actual running state of the platform diverges from the `EffectiveConfigManifest`. Detected via runtime monitoring.
- **Equivalence**: Evaluation if a candidate deployment aligns with the expected baseline. Divergences can block activations if the verict is `DEGRADED` or `BLOCKED`.
