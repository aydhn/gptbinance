# Workflow Plane & Orchestration Governance

The workflow plane orchestrates the end-to-end execution of operational domains: Data, Feature, Model, Allocation, Execution, Position, Ledger, and Risk.

## Design Tenets
1. **Canonical Workflows:** No undocumented or implicit operations.
2. **Explicit Reruns/Retries:** Re-executions require explicit supersede records instead of silently overwriting historical data.
3. **Strict Gate Keeping:** Downstream jobs must wait for verifiable gate clearance and output presence. No exceptions without an audit.
4. **Duplicate Safeguard:** Prevent identical window+workflow combination runs unless explicitly flagged as a rerun.

## Scope of Phase 73
Implemented the orchestration modeling, state machines, duplicate run protections, rerun superseding records, and dependency mapping.
