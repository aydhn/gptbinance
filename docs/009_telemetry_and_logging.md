# Telemetry & Logging

## Principles
*   **Structured Logging:** Prefer JSON lines for application logs to allow easy parsing via `jq` or local log viewers.
*   **Verbosity:** `INFO` should describe the high-level state (e.g., "Order placed", "Position closed"). `DEBUG` should contain the raw API payloads and granular state changes.

## Log Levels
*   `DEBUG`: Raw WS messages, REST payloads, intermediate calculation steps.
*   `INFO`: Startup sequence, normal state transitions, order placements, fills.
*   `WARNING`: Network retries, minor data gaps, unexpected but recoverable API responses.
*   `ERROR`: Unhandled exceptions in strategy logic, failed order routing, DB write errors.
*   `CRITICAL`: Risk limit breaches, global kill switch activation, irrecoverable state corruption.

## Telegram Escalation Rules
Telegram is for human operators, not machines. Do not spam.
*   **Heartbeat:** A daily or twice-daily message summarizing portfolio equity, open positions, and 24h PnL.
*   **INFO:** (Optional, configurable) Significant fills or strategy entries/exits.
*   **WARNING:** Connection drops lasting longer than X minutes.
*   **ERROR/CRITICAL:** Sent immediately. E.g., "RISK LIMIT BREACH: Halting trading."

## Rotation and Retention
*   Use Python's built-in `logging.handlers.TimedRotatingFileHandler` or `RotatingFileHandler`.
*   Retain `INFO`+ logs for 30 days.
*   Retain `DEBUG` logs for 3 days (due to size).

## Pre-Live Requirements
Before any real money trading is enabled, the system MUST log:
1.  The exact configuration profile loaded.
2.  The explicit boolean flag `DRY_RUN_SAFETY_FLAG=False`.
3.  Confirmation that the DB connection is writable.
4.  Confirmation that Telegram is reachable.
