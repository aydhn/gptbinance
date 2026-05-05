# Phase 51: Staged Activation Controller & Active Set Governance

## Goal
Establish a disciplined, audit-friendly, and reproducible governance layer to manage the transition from "Board Approved" to "Active in Production". This replaces manual silent switches and unmonitored feature flags.

## Definition of Done
1. **Activation Intents Framework:** Board decisions can be securely converted to Activation Intents with well-defined, strict scopes and TTLs.
2. **Rollout Plans:** Configurable, staged rollout plans (e.g. observe -> limited symbol -> limited session) exist with built in probation windows.
3. **Active Set Registry:** A clear registry records which intent/candidate is currently active for which scopes, maintaining prior state lineage.
4. **Probation Tracking:** Activation stages enforce mandatory probation loops requiring explicit health signals (Market truth, lifecycle, capital, shadow).
5. **No Automatic Expansion:** No automatic transitions to larger scopes. Only advisory expansions or approvals are supported.
6. **Revert Capability:** An explicit revert planner allows reverting to a verified prior Active Set in case of failure.
7. **CLI Integration:** Commands exist to build intents, show plans, view probation states, and check active sets.
8. **Tests Passed:** Comprehensive test suite for scopes, intents, active sets, and probation limits.

## Explicitly Deferred
- Implementation of the detailed integrations with the Runtime Engine (which actually reads Active Sets to gate execution paths in real-time); this is planned for Phase 52.
- The actual GUI/Dashboard for Activation workflows, sticking to CLI & Telegram only.

## Next Phase (Phase 52)
**Runtime Activation Enforcer:** Wiring the actual live runtime components (Strategy runners, order routers) to strictly respect the currently enforced `ActiveSetRegistry` instead of static configs.
