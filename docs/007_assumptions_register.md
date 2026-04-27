# Assumptions Register

This document records major architectural assumptions made during Phase 01.

| ID | Description | Why Chosen | Risk if Wrong | Validation Strategy | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- |
| A-01 | **Binance-Only First** | Reduces scope complexity. Binance has the best liquidity and APIs for retail. | Missing out on arbitrage/better fees elsewhere. Architecture becomes too tightly coupled to Binance quirks. | Review exchange connector abstraction layer in Phase 10. | Low |
| A-02 | **SQLite for State** | Zero-setup, serverless, highly reliable for single-writer low-frequency workloads. | Database locking issues if concurrency increases significantly or multi-process architecture is needed. | Load test with simulated orders in Phase 20. | Medium |
| A-03 | **Parquet for Tick/Kline History** | Efficient columnar storage, native Pandas integration, free. | Slightly more complex to query manually than CSV/SQL. | Write helper scripts for reading artifacts. | Low |
| A-04 | **Low-Frequency Target** | Fits retail hardware, avoids colocation costs, reduces impact of Python's GIL. | Alpha may decay faster at lower frequencies in crypto. | Backtest execution frequency vs slippage models. | High |
| A-05 | **Telegram for UI/Ops** | Free, ubiquitous, provides push notifications, sufficient for bot commands. | Lack of visual charts/dashboards makes deep portfolio analysis harder on the fly. | Rely on local artifact generation (Jupyter notebooks) for deep analysis instead of a live dashboard. | Medium |
| A-06 | **Paper Trading Engine is Built Internally** | Testnet liquidity is often terrible and unrealistic. Internal simulation using live feeds is more accurate. | Building a realistic paper engine (modeling slippage, fees, queue position) is complex. | Compare Paper Trading results vs real-money micro-executions in later phases. | High |
| A-07 | **Pydantic for Config/Validation** | De facto standard in modern Python, excellent typing, self-documenting. | Slight performance overhead during validation (acceptable for low frequency). | Monitor startup and order validation latency. | Low |
| A-08 | **No Message Broker (Redis/RabbitMQ)** | Keeps architecture zero-budget and single-node simple. | Limits ability to easily scale out workers if ML inference becomes a bottleneck. | Implement in-memory Queues/Event loop (asyncio). Re-evaluate if ML needs dedicated processes. | Medium |
