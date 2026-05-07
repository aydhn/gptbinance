# Mutability Classes & Governance

Parameters are not universally mutable.
- `IMMUTABLE`: Never changes post-release.
- `RELEASE_ONLY`: Changed via formal releases.
- `REVIEW_ONLY`: Changed via bundles needing human review.
- `RUNTIME_SAFE`: Can be hot-patched via `RUNTIME_SAFE_PATCH_INTENT` layer, but strictly bound by policy.

Runtime patch intents do not bypass the plane; they represent an intent that the configuration plane resolves if mutability allows.
