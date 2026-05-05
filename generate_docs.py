import os

files = {
    "docs/216_order_lifecycle_orchestrator_ve_idempotent_submit_politikasi.md": """# Order Lifecycle Orchestrator and Idempotent Submit Policy

This document defines the lifecycle orchestration layer that securely translates compiled order plans into actual order attempts.

## Core Concepts
1. **Separation of Intent and Attempt:** A compiled plan is an intent. Submitting it creates an `OrderAttempt` which tracks its own state machine.
2. **Idempotency:** Every intent + leg + context produces a unique IdempotencyKey. Double submission of the exact same request is actively blocked by the `IdempotencyEngine`.
3. **State Machine:** Submissions must progress through strict states (e.g., `CREATED` -> `READY_TO_SUBMIT` -> `SUBMITTED_PENDING_ACK`).
4. **Client Order IDs:** Generated deterministically and tied to the attempt lineage.

This prevents the risk of duplicate execution.
""",
    "docs/217_ack_fill_cancel_replace_timeout_ve_orphan_order_politikasi.md": """# Ack, Fill, Cancel, Replace, Timeout and Orphan Order Policy

This document outlines the strict handling of venue execution events.

## Strict Rules
- **No Optimistic Success:** If we don't know the state (e.g. timeout on ack), the state is `TIMEOUT_UNKNOWN`.
- **Orphan Orders:** If a venue event arrives with no known local attempt, it is registered as an `ORPHANED` order and escalated.
- **Cancel/Replace Race Conditions:** We handle partial fills arriving after cancel intent without assuming optimistic cancel.
""",
    "docs/218_lifecycle_reconciliation_ledger_replay_ve_execution_truthfulness_politikasi.md": """# Lifecycle Reconciliation and Truthfulness Policy

This defines how the lifecycle orchestrator provides "execution truthfulness" to the Ledger, Replay, and Analytics layers.

## Reconciliation
We routinely reconcile:
1. Compiled Plan vs Order Attempts
2. Order Attempts vs Venue Events
3. Venue Fills vs Ledger Events

Unresolved states break the "truthfulness" assumption and are explicitly highlighted.
""",
    "docs/219_profile_aware_lifecycle_policies_ve_canary_live_caution_kurallari.md": """# Profile Aware Lifecycle Policies

Lifecycle policies adapt strictly based on the execution profile.

- `paper_default`: more relaxed timeout rules.
- `canary_live_caution`: incredibly strict threshold for `TIMEOUT_UNKNOWN` and orphan orders. Immediate halt on anomalies.
""",
    "docs/220_phase_42_definition_of_done.md": """# Phase 42 Definition of Done

## Criteria
- Order lifecycle framework works and is separated from compiled plans.
- State machine, idempotency, and clientOrderId lineage are enforced.
- Partial fill, cancel, replace, timeout, and orphan handling exist.
- Reconciliation hooks and CLI commands are integrated.
- Tests pass.

## Deliberately Postponed
- Actual connection to Binance API.
- Low-latency / HFT optimizations.
""",
}

for filepath, content in files.items():
    with open(filepath, "w") as f:
        f.write(content)
