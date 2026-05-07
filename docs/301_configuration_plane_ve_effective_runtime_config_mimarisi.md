# Configuration Plane Architecture

## Motivation
A robust trading platform requires absolute clarity on its configuration at any given time. Hiding defaults, implicitly mutating state, or resolving configs via undocumented cascades leads to uncontrollable risk.

## The Design
1. **Schemas & Parameter Registry**: The absolute truth of what parameters exist, what type they are, their default behavior, and mutability class.
2. **Layers & Sources**: Values are injected via known layers (Base, Profile, Candidate Bundle, etc.). Each payload applies via a determinist order.
3. **Effective Config Manifest**: A final, resolved, immutable snapshot of the configuration is built.
4. **Visibility**: Hidden defaults are disclosed. Overrides are tracked in a lineage chain.

## Rules
- No hidden defaults.
- No silent overrides without explicit layers.
- Strict scope checking prevents global bleeding.
