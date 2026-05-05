# Order Lifecycle Orchestrator and Idempotent Submit Policy

This document defines the lifecycle orchestration layer that securely translates compiled order plans into actual order attempts.

## Core Concepts
1. **Separation of Intent and Attempt:** A compiled plan is an intent. Submitting it creates an `OrderAttempt` which tracks its own state machine.
2. **Idempotency:** Every intent + leg + context produces a unique IdempotencyKey. Double submission of the exact same request is actively blocked by the `IdempotencyEngine`.
3. **State Machine:** Submissions must progress through strict states (e.g., `CREATED` -> `READY_TO_SUBMIT` -> `SUBMITTED_PENDING_ACK`).
4. **Client Order IDs:** Generated deterministically and tied to the attempt lineage.

This prevents the risk of duplicate execution.
