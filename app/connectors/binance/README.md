# Binance Connector

This module provides the official connection layer to the Binance API.

## Phase 03: Public Read-Only Foundation
Currently, this connector is strictly in a **read-only, public data** mode. It does not handle authentication, secret key signing, order placement, or user-data streams.

### Architecture
- **Client Factory:** Resolves the appropriate base URLs depending on the `EnvironmentProfile` (e.g., testnet vs mainnet).
- **Services:** `TimeService`, `ExchangeInfoService`, `UniverseService`, and `HealthService` isolate specific Binance endpoints and normalize their output.
- **Domain Models:** Raw JSON responses are strictly mapped to normalized `pydantic` models before they touch the rest of the application.
- **Symbol Rules:** Enforces constraints like `tickSize`, `stepSize`, and `minNotional` safely using `Decimal` arithmetic.

### Purpose
To establish a robust, testable, and isolated boundary between the Binance API and our trading application, ensuring the rest of the application is never tightly coupled to Binance's raw JSON structures.

### Future Scope
In subsequent phases, this directory will expand to include:
- Account authentication and signature generation.
- Order execution and tracking (Spot/Margin/Futures).
- User data streams (WebSockets).
