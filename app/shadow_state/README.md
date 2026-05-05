# Venue Shadow State & Account Digital Twin Architecture

## Purpose
This layer acts as the convergence governance backbone. It is strictly responsible for comparing the **Venue Truth** (Binance reality) against the **Local Derived Truth** (ledger, crossbook, order lifecycle) and evaluating drift.

## Core Rules
1. **No Auto-Repair:** This phase explicitly forbids silent auto-healing or forcing the local state to mimic the venue state without an audit trail.
2. **Review Only Remediation:** Any remediation planning leads to review requests. It does not overwrite the database blindly.
3. **Eventual Consistency:** We model timing delays safely via Consistency Windows, separating real accounting drift from transient network jitter.
4. **Isolated Twin Assembly:** Convergence is determined via a `ShadowTwinSnapshot` object which immutable preserves the moment of evaluation.

## Workflow
`Snapshots -> Twin -> Convergence Engine -> Drift Taxonomy -> Remediation Planning -> Reporting`
