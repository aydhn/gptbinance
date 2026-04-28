# Backtest Engine

The Backtest Engine is an event-driven simulator designed to evaluate strategy and regime signals against historical data in a controlled, deterministic environment.

## Philosophy
*   **Separation of Concerns:** The simulator strictly separates the signal generation (Strategy Engine) from the execution simulation (Fill Model and Position State). Strategies do not magically grant themselves perfect fills.
*   **Honesty:** Assumes slippage, includes exchange fees, and forces realistic fill assumptions (e.g., executing on the next bar open following a signal).
*   **Auditability:** Every fill and trade is recorded in a ledger, and equity state is snapshotted to allow full transparency of the performance metrics.

## Components
*   `engine.py`: The orchestration core that ties everything together.
*   `replay_driver.py`: Iterates through historical data and yields `BacktestStepContext` bar by bar.
*   `fill_model.py`: Decides how and at what price a `SimulatedOrderIntent` is executed, outputting a `SimulatedFill`.
*   `position_state.py`: Manages current open positions, tracks entry prices, and calculates real-time unrealized PnL.
*   `ledger.py`: Records fills and closed trades.
*   `equity.py`: Tracks cash, total equity, and high-water marks for drawdown calculations.
*   `performance.py`: Summarizes ledger trades and equity into standard financial metrics.
*   `storage.py`: Persists backtest runs to disk for future analysis.
