# Human Review Fabric / Operator Workflow Governance

## Why
As the system evolves, many domains require explicit human review (e.g., readiness contradictions, incidents, non-reversible migrations). Managing these ad-hoc leads to lack of auditability, priority confusion, and bypassed checks. This fabric provides a unified, highly-structured queueing and adjudication engine.

## Core Tenets
1. **No Auto-Approval**: The system prepares evidence, but a human must adjudicate.
2. **Dual-Control / Separation of Duties**: The person requesting a critical review cannot be the same person adjudicating it.
3. **Checklist Driven**: Eligible reviews cannot be finalized without completing required checklist items.
4. **SLA and Escalation**: Reviews that sit too long are flagged and escalated, not silently ignored.
5. **Decision Records**: Every adjudication produces an immutable `ReviewDecisionRecord`.
