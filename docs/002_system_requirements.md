# System Requirements

## Functional Requirements
*   **Market Data Ingestion:** System must connect to Binance via WebSockets and REST to retrieve real-time and historical price, volume, and order book data for specified symbols.
*   **Order Execution:** System must create, route, monitor, and cancel orders (Market, Limit, Stop) across Spot, Margin, and Futures markets.
*   **State Management:** System must accurately track account balances, open positions, active orders, and historical trade fills.
*   **Strategy Execution:** System must provide an interface for custom trading strategies to consume data, generate signals, and request order placement.
*   **Paper Trading Engine:** System must provide a realistic internal simulation engine for forward-testing strategies using live data without risking capital.
*   **Risk Evaluation:** Every order request must pass through a strict risk evaluation layer before being routed to the exchange or paper engine.
*   **Telegram Integration:** System must send critical alerts, daily summaries, and heartbeat messages to a configured Telegram chat. Operator must be able to send emergency commands (e.g., "KILL") via Telegram.

## Non-Functional Requirements
*   **Language:** Python 3.10+ only.
*   **Dependencies:** Must use free, open-source libraries (e.g., `pandas`, `numpy`, `ccxt` or official binance connector, `python-telegram-bot`, `sqlalchemy`).
*   **Architecture:** Modular, decoupled design. Strategies must not directly access execution modules.
*   **Configuration:** All environment-specific variables and strategy parameters must be loaded from explicitly defined configuration files or environment variables.

## Reliability & Safety Requirements
*   **Idempotency:** Startup sequences must be idempotent, safely resuming from previous states without duplicating orders.
*   **Graceful Degradation:** If WebSocket data streams fail, the system must attempt reconnection. If reconnection fails, trading must halt safely.
*   **Orphan Order Prevention:** System must track and cancel orphaned orders upon restart or critical failure.
*   **Kill Switch:** A universal kill switch (triggerable locally or via Telegram) must immediately cancel all open orders and close all positions (or halt trading, depending on configuration).

## Observability Requirements
*   **Structured Logging:** All events must be logged in a structured format (e.g., JSON lines) to facilitate parsing and analysis.
*   **Log Levels:** Strict adherence to log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL).
*   **Audit Trail:** Every state change related to risk limits, order submission, and fills must be durably recorded.

## Portability & Hardware Expectations
*   **Hardware:** Must run smoothly on an average retail machine (e.g., 4 cores, 8GB RAM). GPU is strictly optional and not required for core operations.
*   **Network:** Assumes a standard, stable broadband connection (~100 Mbps). No colocation assumed.
*   **OS:** OS-agnostic, but primarily targeted for Linux/macOS environments for production deployment.

## Restart & Recovery Expectations
*   **State Persistence:** Critical state (fills, balances, active risk limits) must be persisted to local storage (e.g., SQLite) to survive process restarts.
*   **Reconciliation:** Upon restart, the system must reconcile internal state with the exchange state before resuming trading.

## Latency Assumptions
*   **Target Latency:** Milliseconds to seconds. The system is designed for low-to-medium frequency trading. Sub-millisecond latency is explicitly a non-goal.

## Storage Requirements
*   **Local Only:** No external databases (e.g., AWS RDS).
*   **Relational Data:** Use SQLite for transactional data (orders, fills, account state).
*   **Time-Series Data:** Use Parquet or CSV for historical market data and bulk analysis artifacts.

## Security Requirements
*   **Secrets Management:** API keys and Telegram tokens must be injected via environment variables or secure, non-version-controlled `.env` files.
*   **Least Privilege:** Exchange API keys must be configured with the minimum necessary permissions (e.g., restrict IP, disable withdrawals).
*   **No Hardcoded Secrets:** Absolutely no secrets committed to the repository.
