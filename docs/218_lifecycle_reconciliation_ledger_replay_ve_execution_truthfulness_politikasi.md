# Lifecycle Reconciliation and Truthfulness Policy

This defines how the lifecycle orchestrator provides "execution truthfulness" to the Ledger, Replay, and Analytics layers.

## Reconciliation
We routinely reconcile:
1. Compiled Plan vs Order Attempts
2. Order Attempts vs Venue Events
3. Venue Fills vs Ledger Events

Unresolved states break the "truthfulness" assumption and are explicitly highlighted.
