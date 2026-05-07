# Configuration Plane

The Configuration Plane provides unified, typed, and verifiable management of all system parameters.

## Core Concepts

1. **Schemas and Parameters**: All configuration parameters must be explicitly registered via `ConfigSchema`. No hidden defaults or unmanaged environment variables are allowed.
2. **Layers and Overrides**: Configuration values are layered (e.g., Base Defaults -> Profile Overrides -> degraded overlays).
3. **Effective Config Manifest**: At runtime, sources are resolved into a single, immutable `EffectiveConfigManifest`. The raw sources are never overwritten.
4. **Mutability and Governance**: Parameters are tagged with `MutabilityClass` (e.g., `RUNTIME_SAFE`, `REVIEW_ONLY`) to prevent unauthorized runtime patches.
5. **Diffs and Drift**: The plane supports semantic diffing between manifests and detects runtime drift.

## How to use
- `resolution_engine.resolve(...)` creates an effective config.
- `evaluate_equivalence(...)` checks if candidate config matches runtime config.
- Use `app.main` CLI commands to interact with this data.
