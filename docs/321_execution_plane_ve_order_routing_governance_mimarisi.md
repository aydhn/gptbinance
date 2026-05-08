# Phase 63: Execution Plane & Order Routing Governance

## Execution Plane Necessity
An allocation intent is theoretical until executed. Direct execution without a translation layer creates massive operational risks including unchecked retries, uncontrolled slippage, untracked cancel/replace drift, and filter violations. The execution plane acts as a firewall between allocation intent and venue truth.

## Flow
Allocation Intent -> Execution Candidate -> Order Spec -> Routing Policy -> Send Attempt -> Fill.

## Principles
1. **No Direct HFT**: We do not implement a low-latency smart order router; we prioritize determinism, explainability, and governance.
2. **No Hidden Retries**: Duplicate order sends are deadly; idempotency records are strictly enforced.
3. **Execution Quality is a distinct layer**: Slippage, partial fills, and markouts are formally evaluated to inform future routing or allocation decisions.
