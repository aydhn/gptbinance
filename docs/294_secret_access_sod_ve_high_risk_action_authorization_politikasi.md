# Secret Access, SoD, and High-Risk Action Authorization Policy

## Secret Adjacent
Distinguishes between accessing secret metadata and revealing secret material. Readonly zones cannot access secret-adjacent capabilities.

## Separation of Duties (SoD)
The `SeparationOfDutiesChecker` enforces:
- Producer != Reviewer
- Producer != Adjudicator
- Reviewer != Adjudicator

## High Risk Actions
Require specific high-risk capabilities, appropriate Trust Zones, and valid sessions. Proofs are logged and audited.
