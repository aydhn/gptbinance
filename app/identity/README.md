# Identity Plane & Least-Privilege Authorization Fabric

This module implements Phase 57: A dedicated Identity Plane that provides typing, capabilities, roles, trust zones, and a unified authorization engine.

## Core Philosophy

- **Typed Principals**: Actors are strictly identified and typed (Human, Service).
- **Separation of Role and Capability**: A Role describes a functional area; Capabilities grant specific permissions.
- **Trust Zones**: Operations are bounded by zones (e.g., ReadOnly, Restricted Review, Sensitive Runtime).
- **Least Privilege**: Explicit deny-by-default. Wildcards are discouraged.
- **Approval != Authorization**: Just because an action was approved in a workflow does not mean the executing principal is authorized to perform the underlying mutation.
- **No Secret Admin Bypass**: There are no hidden backdoor roles or superusers. All actions require capability proof.
- **Break-glass is Exception**: Breakglass is supported but heavily audited, scope-reduced, and requires post-event review.

## Main Components

- `principals.py`: Registry for principals.
- `roles.py`: Role definitions and bindings.
- `capabilities.py`: Granular capability grants.
- `zones.py`: Trust zone definitions and bindings.
- `sessions.py`: Session issuance and validation.
- `delegations.py`: Temporary transfer of capabilities.
- `elevations.py`: Temporary privilege increase.
- `breakglass.py`: Emergency overrides.
- `authorization.py` / `proofs.py`: The engine that evaluates requests against all the above and produces an auditable proof.
