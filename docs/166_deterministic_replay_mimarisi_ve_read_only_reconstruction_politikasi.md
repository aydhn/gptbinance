# Phase 32: Deterministic Replay Architecture and Read-Only Reconstruction Policy

## Replay Sources
The replay engine requires a set of artifact references to construct the initial state. Valid sources include paper session refs, live runtime refs, and execution order refs. The system enforces a strict minimum required artifact set and explicit scope boundaries (e.g., Trade, Session, Incident).

## Point-in-Time Snapshot
The system needs a view of the past reality:
- Bundle definitions
- Model versions
- Schema versions
- Risk profile
- Portfolio state
If elements are missing, the fidelity of the replay drops, generating caution metrics. The snapshot must not apply its state globally, staying confined to the replay instance.

## Timeline Reconstruction
A sequence builder reconstructs historical event streams, assembling them stably by timestamp, sequence id, and component. Detected gaps or suspicious overlaps lower the reproducibility score.

## Read-Only Guarantee
Under no circumstances should the deterministic replay layer alter historical records, submit actual exchange orders, or broadcast state updates into active execution contexts. It is purely reconstructive and read-only.
