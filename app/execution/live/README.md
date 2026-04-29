# Execution Gateway (Live)

The Execution Gateway is the final layer before orders hit the exchange.

## Why Testnet-First?
Paper trading is an internal simulation. To cross the gap to production, we must test actual exchange mechanics: rate limits, filter enforcement (min-notional, tick size), latency, REST vs Stream discrepancies, and partial fills. Testnet provides a safe, free environment to validate the execution infrastructure before touching real funds.

## Mainnet Safety Gates
Mainnet execution is explicitly disabled by default. It requires multiple levels of "arming" (e.g., config flag, profile flag, CLI confirmation) to unlock. If any gate fails, the system safely falls back or blocks execution.

## Key Components
- **Pretrade Validator**: Enforces symbol rules *before* network requests.
- **Client Order IDs**: Ensures idempotency and trace lineage.
- **User Stream & Reconciliation**: Listens for exact exchange state and reconciles it with local state.
- **Cancel/Replace Engine**: Safely manages in-flight modifications.
