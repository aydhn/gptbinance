# Binance Trading Platform - Core Infrastructure

This repository contains the foundational infrastructure for a zero-budget, Python-only, production-minded Binance trading platform.

## Mission
To provide a clean, realistic, extensible, research-to-execution architecture that can support the search for robust statistical edge on Binance. The system prioritizes survivability, auditability, extensibility, and disciplined risk-adjusted edge over guaranteed profitability or fantasy throughput.

## Major Modules
- `app/core`: Core application logic and utilities.
- `app/config`: Typed configuration management.
- `app/connectors`: Official Binance API integrations.
- `app/data`: Market and account data ingestion, processing, and persistence.
- `app/execution`: Order routing, tracking, and reconciliation.
- `app/risk`: Account, strategy, and trade-level risk controls.
- `app/portfolio`: Portfolio state management and exposure tracking.
- `app/strategies`: Signal generation and trading logic.
- `app/research`: Research, backtesting, and analysis tools.
- `app/backtest`: Core backtesting engine.
- `app/ml`: Optional ML model pipelines and inference.
- `app/optimizer`: Parameter optimization and walk-forward analysis.
- `app/ops`: Operational scripts and maintenance tools.
- `app/telegram`: Telegram integration for alerts and operator communication.

## Supported Operating Modes
- **Live Trading**: Real-money execution on Binance (Spot, Margin, Futures).
- **Paper Trading**: Simulated execution using real-time Binance data.
- **Testnet**: Execution on official Binance testnets (where available and reliable).
- **Backtesting**: Historical simulation of strategies.

## Non-Goals
- High-Frequency Trading (HFT) or sub-millisecond execution.
- Guaranteed profitability or "AI magic".
- Web dashboards or complex UI.
- Multi-exchange support (initially Binance only).
- Usage of paid APIs, premium SaaS, or proprietary backtesting services.
- HTML scraping or browser automation.

## Repository Organization
The repository is structured to separate concerns clearly, enforcing boundaries between data ingestion, signal generation, risk management, and execution.

## Safety Warning
**REAL TRADING IS RISKY.** This software is provided as-is, without any guarantees. Trading cryptocurrencies involves significant risk of loss. The operators must understand the risks and are fully responsible for any financial losses incurred while using this software.

## Phase 01: Foundation
Phase 01 establishes the program constitution, capability matrix, repository skeleton, configuration contract, risk governance baseline, data contract baseline, testing baseline, and a 100-phase milestone roadmap. It eliminates architectural ambiguity before implementation expands.
