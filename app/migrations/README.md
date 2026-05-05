# Migration Fabric

The Migration Fabric is a unified, deterministic framework designed to manage the evolution of stateful surfaces within the system—including configuration schemas, workspace manifests, policy rules, and ledger metadata.

## Why Do We Need This?
As the system evolves, ad-hoc scripts and silent updates introduce drift, stale evidence, and compatibility fractures. The Migration Fabric enforces safe, auditable state evolution by requiring:
- Explicit definitions
- Strict dependency resolution
- Matrix-based compatibility checks
- Mandatory preflight and dry-run phases before any application.

## Core Principles
1. **No Ad-Hoc Scripts:** Every change must be defined as a migration recipe.
2. **Compatibility Awareness:** Every migration declares its backward and forward compatibility.
3. **Scope Safety:** Migrations operate strictly within their allowed scopes (workspace/profile/domain).
4. **Rollforward-First:** Certain changes are non-reversible. The fabric explicitly supports "rollforward/quarantine" plans when rollback isn't possible.
5. **No Silent State Rewrite:** All updates are logged, verified, and tied to evidence bundles.

## Lifecycle
1. **Define:** `MigrationDefinition` explicitly models the change.
2. **Resolve:** Dependency graph determines execution order.
3. **Evaluate:** Compatibility checks block conflicting updates.
4. **Simulate:** Dry-runs reveal touched files and expectations.
5. **Apply:** Executed only if safe, generating before/after evidence.
6. **Verify:** Post-apply checks confirm integrity and version targets.
