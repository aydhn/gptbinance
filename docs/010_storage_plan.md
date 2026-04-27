# Storage Plan

The system uses local storage exclusively to adhere to the zero-budget constraint.

## What Belongs Where

### 1. In-Memory (RAM)
*   Current order book snapshot (if needed).
*   Live tick streams before aggregation.
*   Active strategy state (e.g., rolling windows of indicators).
*   *Rule:* Anything in memory must be reconstructable from persistence upon restart, or considered ephemeral/non-critical.

### 2. SQLite (`storage/state/`)
*   **Purpose:** Transactional execution state.
*   **Tables:** `orders`, `fills`, `positions`, `portfolio_snapshots`, `risk_events`, `audit_log`.
*   **Performance:** Sufficient for low-frequency trading. Use WAL (Write-Ahead Logging) mode for better concurrent read/write performance if necessary.

### 3. Parquet / CSV (`storage/raw/`, `storage/processed/`)
*   **Purpose:** Bulk time-series data for research, backtesting, and model training.
*   **Format:** Parquet is strongly preferred over CSV for size and read speed.
*   **Partitioning:** By symbol and year/month (e.g., `storage/raw/BTCUSDT/2023_10.parquet`).

### 4. Artifacts (`storage/artifacts/`)
*   **Purpose:** Output from research and optimization runs.
*   **Contents:** HTML reports, JSON summary stats, serialized ML models (e.g., `.pkl` or `.onnx`).

## Backup & Export
*   SQLite DBs should be backed up periodically (e.g., daily cron job copying the file).
*   Logs should be rotated and archived.
*   *Note:* The repository itself should be version controlled on GitHub, but the `storage/` directory must be strictly in `.gitignore`.

## Data Hygiene
*   Raw data scripts must handle deduplication and gap-filling.
*   State databases should have scripts available to archive old orders/fills to Parquet to prevent SQLite from growing indefinitely over years.
