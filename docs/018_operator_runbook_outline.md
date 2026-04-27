# Operator Runbook Outline

This outline defines the expected standard operating procedures (SOPs) for managing the platform.

## 1. Startup Sequence
*   Verify `.env` configuration (API keys, target environment).
*   Ensure SQLite databases are accessible and permissions are correct.
*   Start the main process (e.g., `python -m app.main`).
*   Observe startup logs for config validation success, DB connection, and WebSocket stream establishment.
*   Verify initial Telegram heartbeat is received.

## 2. Shutdown Sequence
*   Graceful shutdown via SIGINT (Ctrl+C) or Telegram `/stop` command.
*   System must cancel all pending open orders (configurable behavior).
*   System flushes pending writes to SQLite.
*   Verify process terminates cleanly in logs.

## 3. Paper Session Monitoring
*   Check Telegram daily summary for PnL and trade counts.
*   Periodically review `storage/artifacts/` for strategy tear sheets or backtest vs. paper divergence.
*   Look for `WARNING` logs regarding simulated slippage anomalies.

## 4. Live Session Monitoring (Future)
*   Check Telegram twice daily for exact equity matches between internal state and Binance.
*   Verify no orphaned orders exist via Binance UI vs. Internal SQLite state.
*   Monitor server resource usage (CPU/RAM).

## 5. Critical Alert Response
*   **Action:** If a `CRITICAL` alert fires (e.g., Risk Breach), the system should automatically halt.
*   **Operator Steps:**
    1. Check Telegram for exact error context.
    2. Log into Binance UI to manually verify no rogue open orders exist. Flatten positions if necessary.
    3. Review `logs/app.log` leading up to the event.
    4. Fix the underlying issue before restarting.

## 6. Strategy Disable / Enable
*   Modify the dynamic strategy config file or database.
*   System should pick up the change without a full restart (or via a quick restart if dynamic reload isn't implemented).
*   Ensure disabling a strategy triggers a graceful exit of its current positions (or hands them off to a manual liquidation module).

## 7. Emergency Kill Switch
*   Send `/kill` via Telegram.
*   System immediately cancels all orders and attempts market-close of all positions.
*   System shuts down event loop and exits.

## 8. Daily & Weekly Review
*   **Daily:** Check PnL, ensure log rotation is working, verify backup of SQLite DB.
*   **Weekly:** Review strategy metrics, run database compaction scripts if needed, archive old Parquet files to cold storage if space is tight.
