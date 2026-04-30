# Product Domain Layer

This layer defines the fundamental abstractions for different product types traded within the system (e.g., Spot, Margin, Futures).

## Motivation
Extending a Spot-centric system blindly to Margin or Futures introduces severe risks due to:
- Short positions
- Leverage
- Liquidation
- Funding and borrow costs
- Margin and position modes
- Reduce-only execution constraints

By clearly separating the `ProductType` and using descriptors/capabilities, the system explicitly acknowledges what is safe and supported for each product, ensuring that conservative, testnet-first defaults are respected.

## Core Components
- **ProductType**: SPOT, MARGIN, FUTURES_USDM, etc.
- **ProductDescriptor**: Immutable metadata defining what a product can do (Capabilities), its risks (RiskDescriptor), and its costs (CostModel).
- **ProductRegistry**: Centralized place to verify readiness (e.g. `TESTNET_ONLY`) and capabilities before execution.
