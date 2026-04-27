# Testing Strategy

The system relies on a multi-tiered testing strategy using standard, free Python tooling (`pytest`).

## 1. Unit Tests
*   **Scope:** Individual functions and classes (e.g., indicator calculations, config validation, risk calculations).
*   **Speed:** Must be extremely fast (<1s total).
*   **Rule:** No network calls allowed. Use `unittest.mock` for dependencies.

## 2. Integration Tests
*   **Scope:** Interaction between modules (e.g., Risk module validating a Strategy output and passing it to the Execution engine).
*   **Speed:** Moderate.
*   **Rule:** Can use local SQLite databases (in-memory or temp files), but no live exchange calls.

## 3. Connector Contract Tests
*   **Scope:** Verifying that the Binance API behaves as expected and our parsers are correct.
*   **Speed:** Slow (network dependent).
*   **Rule:** These tests hit the Binance Testnet (or public REST endpoints). They must be marked with `@pytest.mark.network` and are typically excluded from the fast CI loop.

## 4. Simulation / Replay Tests
*   **Scope:** Injecting historical tick/kline data into the event loop to verify the system (Strategy + Risk + Execution Simulation) behaves deterministically.
*   **Rule:** Given the same historical data and config, the resulting simulated fills must be identical across test runs.

## 5. Dry-Run Execution Tests
*   **Scope:** End-to-end tests that connect to Binance Testnet, place real (testnet) orders, and verify state changes.

## 6. Failure Injection Tests (Chaos)
*   **Scope:** Simulating network disconnects, invalid JSON responses, and API rate limit errors to ensure the system degrades gracefully or halts safely.

## CI Expectations
*   A basic GitHub Actions (or similar free CI) workflow should run Unit and Integration tests on every commit.
*   Formatting (`black`), linting (`flake8`/`ruff`), and type checking (`mypy`) must pass.
