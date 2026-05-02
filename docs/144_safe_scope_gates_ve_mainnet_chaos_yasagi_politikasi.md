# Safe Scope Gates and Mainnet Chaos Ban Policy

## Mainnet Ban
Injecting faults into the live mainnet execution path is strictly banned by default. The `SafetyGate` explicitly checks `is_live_mainnet` and blocks execution.

## Allowed Scopes
- **Simulation**: Safe, pure math/logic testing.
- **Paper**: Safe, real market data but fake execution.
- **Shadow**: Safe, runs alongside live but doesn't send orders.
- **Testnet**: Safe, real network but fake funds.

Even with a force token, any bypass must generate a severe audit trail and alert.
