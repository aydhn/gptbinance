# Repository Blueprint

This document defines the structural contract for the codebase. It dictates where code belongs, how modules interact, and the conventions that govern them.

## Folder Structure

```
├── app/                        # Core application code
│   ├── __init__.py
│   ├── main.py                 # Application entrypoint
│   ├── core/                   # Application-wide utilities, base classes, exceptions
│   ├── config/                 # Configuration management (Pydantic models, env loading)
│   ├── connectors/             # Exchange API adapters (Binance REST/WS, CCXT wrappers)
│   ├── data/                   # Data ingestion, processing, and local caching
│   ├── execution/              # Order routing, paper trading engine, fill reconciliation
│   ├── risk/                   # Account, strategy, and order-level risk limits
│   ├── portfolio/              # Position tracking, exposure management, PnL calculation
│   ├── strategies/             # Trading logic, signal generation
│   ├── research/               # Notebooks, exploration, benchmark definitions
│   ├── backtest/               # Core historical simulation engine
│   ├── ml/                     # (Optional) Model training, inference, feature engineering
│   ├── optimizer/              # Parameter search, walk-forward routines
│   ├── ops/                    # Operational scripts (DB migrations, cleanup, watchdogs)
│   └── telegram/               # Telegram bot interface, alert formatting
├── tests/                      # Automated test suite
│   ├── unit/                   # Fast, isolated tests
│   ├── integration/            # Tests covering module interactions
│   └── simulation/             # Dry-run execution and replay tests
├── scripts/                    # Utility scripts for operators (e.g., download_data.py)
├── docs/                       # Project documentation, architecture decisions
├── storage/                    # Local data persistence (IGNORED BY GIT)
│   ├── raw/                    # Raw tick/kline data
│   ├── processed/              # Cleaned, aggregated features (Parquet)
│   ├── state/                  # SQLite databases for execution state
│   └── artifacts/              # ML models, backtest reports, logs
├── pyproject.toml              # Dependency and build configuration
├── .env.example                # Template for environment variables
└── .gitignore                  # Git ignore rules
```

## Module Responsibilities & Import Boundaries

*   **`app/strategies/`**: Generates signals. **Cannot** import from `app/execution/`. Can only output standardized `Signal` or `OrderRequest` objects.
*   **`app/risk/`**: Validates `OrderRequest` objects against limits. **Cannot** generate signals. Must intercept all requests before execution.
*   **`app/execution/`**: Handles the physical or simulated routing of orders. Consumes validated requests from `app/risk/`.
*   **`app/connectors/`**: The *only* place where Binance-specific API logic resides. Other modules interact with connectors via standard internal interfaces.
*   **`app/portfolio/`**: Maintains the source of truth for current holdings. Updated by fill events from `app/execution/`.

## Dependency Rules
*   **No Circular Imports:** Strictly forbidden. Use dependency injection or refactor shared logic into `app/core/` if needed.
*   **Isolate Third-Party APIs:** Wrap exchange libraries (like `ccxt` or `binance-connector-python`) within `app/connectors/`. Do not bleed exchange-specific JSON structures into the rest of the app.

## Naming Conventions
*   **Python Code:** Follow PEP 8 strictly (snake_case for variables/functions, CamelCase for classes).
*   **Files:** snake_case.py
*   **Interfaces/Abstract Classes:** Prefix with `Base` or suffix with `Protocol` (e.g., `BaseConnector`, `RiskProtocol`).

## Coding Conventions
*   **Type Hinting:** Mandatory for all function signatures and class attributes. Use `typing` heavily.
*   **Docstrings:** Google-style docstrings required for all public classes and functions.
*   **Immutability:** Prefer immutable data structures (e.g., `dataclasses(frozen=True)`) for passing events (ticks, fills, signals) between modules.

## Documentation Conventions
*   Keep markdown files updated as architecture evolves.
*   Document *why* a decision was made, not just *how* it is implemented.
