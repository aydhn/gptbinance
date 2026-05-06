# Phase 56: Human Review Fabric & Operator Workflow Governance

## Review Request Lifecycle
- Request -> Queue -> Assignment -> Checklist -> Adjudication -> (Escalation/Handoff)
- No auto-approvals. Human-in-the-loop is mandatory for specific tasks.
- Separation of duties (SoD) requires producer and adjudicator to be different.

## Dual Control
Certain high-risk actions (e.g. non-reversible migrations, production board overrides) mandate a formal "four eyes" check, enforcing a secondary approver.
