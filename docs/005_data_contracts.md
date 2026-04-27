# Data Contracts

This document defines the standardized data entities used for internal communication between modules. All entities should be implemented as immutable `dataclass` or `Pydantic` models.

## Market Data Entities

### `Tick`
*   **Purpose:** Represents a single trade or top-of-book update.
*   **Fields:** `symbol` (str), `timestamp` (int, ms), `price` (float), `quantity` (float), `side` (str: BUY/SELL), `is_trade` (bool).
*   **Source:** Binance WS.
*   **Update Frequency:** High (sub-second).
*   **Persistence:** Dropped in live mode; potentially aggregated to `Kline` for storage.

### `Kline` (Candle)
*   **Purpose:** Standard OHLCV data.
*   **Fields:** `symbol` (str), `interval` (str), `open_time` (int), `open` (float), `high` (float), `low` (float), `close` (float), `volume` (float), `close_time` (int).
*   **Source:** Binance REST/WS.
*   **Update Frequency:** Per interval (e.g., 1m, 1h).
*   **Persistence:** Parquet/SQLite.

## Execution Entities

### `OrderRequest`
*   **Purpose:** Request from a strategy to place an order.
*   **Fields:** `strategy_id` (str), `symbol` (str), `side` (str), `order_type` (str: MARKET/LIMIT), `quantity` (float), `price` (float, optional), `client_order_id` (str).
*   **Validation:** Checked by Risk module before routing.

### `OrderState`
*   **Purpose:** Represents the current status of an order on the exchange.
*   **Fields:** `internal_id` (str), `exchange_id` (str), `status` (str: NEW, PARTIALLY_FILLED, FILLED, CANCELED, REJECTED), `filled_qty` (float), `avg_fill_price` (float).
*   **Update Frequency:** On execution reports from WS/REST.
*   **Persistence:** SQLite.

### `FillEvent`
*   **Purpose:** Represents a specific execution (partial or full).
*   **Fields:** `order_id` (str), `symbol` (str), `fill_price` (float), `fill_qty` (float), `commission` (float), `commission_asset` (str), `timestamp` (int).
*   **Persistence:** SQLite (Critical for PnL).

## Account Entities

### `Position`
*   **Purpose:** Tracks current holdings for a specific asset/symbol.
*   **Fields:** `symbol` (str), `quantity` (float), `average_entry_price` (float), `unrealized_pnl` (float), `realized_pnl` (float).
*   **Update Frequency:** On `FillEvent`.
*   **Persistence:** SQLite.

### `PortfolioSnapshot`
*   **Purpose:** Point-in-time snapshot of account health.
*   **Fields:** `timestamp` (int), `total_equity` (float), `available_margin` (float), `used_margin` (float).
*   **Persistence:** SQLite (Recorded periodically, e.g., hourly/daily).

## Telemetry Entities

### `RiskEvent`
*   **Purpose:** Records when a risk limit is hit or an order is rejected.
*   **Fields:** `timestamp` (int), `level` (str), `module` (str), `message` (str), `context` (dict).

### `TelegramAlert`
*   **Purpose:** Formatted message intended for the operator.
*   **Fields:** `level` (str: INFO/WARN/CRITICAL), `message` (str), `requires_action` (bool).
