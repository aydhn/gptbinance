# Identity Plane & Least Privilege Authorization Architecture

This document describes the identity plane established in Phase 57.

## Principals, Roles, Capabilities, Zones
We decouple "who you are" from "what you do", "what you can actually mutate", and "where you operate".

- **Principal**: Typed identity (Human, Service, System).
- **Role**: Functional family grouping (e.g., REVIEW_OPERATOR). Roles DO NOT grant permissions.
- **Capability**: Explicit granular permission (e.g., ADJUDICATE_REVIEW). Required for actions.
- **Trust Zone**: Bounding context (e.g., REVIEW_RESTRICTED, RUNTIME_SENSITIVE). Prevents capabilities from bleeding across operational boundaries.

## Approval != Authorization
A workflow may be marked 'approved', but if the user attempting to actuate the transition lacks the specific capability, or is in the wrong trust zone, or violates SoD constraints, the action is Denied. Authorization is runtime-evaluated and produces an immutable proof.

## No Superuser
There is no `ADMIN` role. No wildcard capabilities exist.
