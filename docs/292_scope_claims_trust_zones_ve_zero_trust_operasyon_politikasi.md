# Scope Claims, Trust Zones, and Zero-Trust Policy

## Scope Claims
Limits the blast radius. E.g., allowed on Workspace A but not Workspace B.
Evaluations require strict matching. Wildcards are virtually forbidden.

## Trust Zones
Enforces separation of access contexts.
- PUBLIC_READONLY
- OPERATIONAL_READONLY
- REVIEW_RESTRICTED
- RELEASE_CONTROLLED
- RUNTIME_SENSITIVE
- INCIDENT_SENSITIVE
- SECRET_ADJACENT
- BREAKGLASS_EMERGENCY

Crossing zones is strictly governed. An operator with `RUNTIME_SENSITIVE` rights shouldn't be implicitly trusted with `SECRET_ADJACENT` rights.
