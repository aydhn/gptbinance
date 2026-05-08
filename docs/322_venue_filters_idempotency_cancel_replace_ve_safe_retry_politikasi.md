# Venue Filters, Idempotency, Cancel/Replace, and Safe Retry

## Venue Filters
All venues must be explicitly registered. Orders must pass minimum notional, tick size, step size, and product constraints before they are eligible to be compiled into execution plans. Stale venue definitions block execution.

## Idempotency & Safe Retry
Duplicate submissions are forbidden. `IdempotencyRecord` tracking guarantees safe retries. Only specific explicit rejection errors can trigger retries; if the error is unrecoverable (e.g., insufficient margin), it terminates immediately.

## Cancel / Replace Chains
Modifying an order is treated as a chain. If the state of the original order is ambiguous (e.g., network disconnect before cancellation confirms), replace requests are blocked to prevent duplicate risk exposure.
