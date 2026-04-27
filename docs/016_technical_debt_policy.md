# Technical Debt Policy

## Philosophy
Technical debt is a tool, not a sin. It is acceptable to incur technical debt to accelerate research or test a hypothesis in Paper mode. However, it is **unacceptable** to carry unmanaged technical debt into Live trading.

## Recording Tech Debt
*   All technical debt must be explicitly recorded in code using `TODO(TechDebt): [Description]`.
*   Major architectural shortcuts must be documented in a central `docs/tech_debt_register.md` (to be created when needed).

## Allowed Shortcuts (Paper/Research Only)
*   Hardcoding specific symbol parameters (temporarily) instead of dynamic config loading.
*   Inefficient Pandas operations in backtesting that don't scale well but work for small datasets.
*   Mocking API responses loosely in early integration tests.
*   Skipping edge-case error handling for rare API exceptions.

## Forbidden Shortcuts (Never Allowed)
*   Committing API keys or secrets to the repo.
*   Bypassing the Risk Module for *any* order.
*   Disabling the global Kill Switch.
*   Ignoring critical safety checks (like tickSize/stepSize validation) before routing to exchange.

## Labeling and Prioritization
*   **P0 (Critical):** Must be fixed before any Live trading. (e.g., Risk module hardcodes leverage limits instead of reading config).
*   **P1 (High):** Must be fixed before scaling strategy portfolio. (e.g., SQLite connection is single-threaded and locking frequently under load).
*   **P2 (Medium):** Refactoring needed for maintainability. (e.g., Duplicate API parsing logic in multiple connector files).
*   **P3 (Low):** Minor inefficiencies. (e.g., Unused imports, slow but functional backtest metric calculations).

## Repayment Rules
*   Before moving from Phase Stage 4 (Risk) to Stage 5 (Strategies), all P0 tech debt related to execution and risk must be resolved.
*   Before enabling the `live` configuration flag, an explicit audit of all `TODO(TechDebt)` items must be performed and signed off by the operator.
