# Control and Approval Layer

This module provides a human-in-the-loop control plane for sensitive operations. It enforces policies like four-eyes approval, TTL for stale requests, and mandatory journaling for full accountability.

## Architecture
- **Requests**: Represents an operator's intent to perform an action.
- **Approvals**: Contains decisions from approvers.
- **Authorization**: Execution-time validation that approvals are valid, sufficient, and not stale.
- **Journal**: Immutable record of all commands and decisions.

This layer does NOT bypass safety gates; it is a prerequisite for executing sensitive actions.
