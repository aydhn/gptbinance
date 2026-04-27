# Capability Matrix

This matrix defines the support level and operational details for various execution modes and product types within the platform.

| Mode / Capability | Support Level | Execution Venue | Account Dependencies | Operational Risks | Simulation Fidelity | Implementation Priority | Comments |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Spot Live** | Native Official | Binance Spot | Real API Keys (Trading Enabled) | Real financial loss, rate limits, slippage | N/A (Real) | High (Core) | Foundational execution mode. |
| **Spot Paper** | Internally Simulated | Local Engine | None | Bugs in simulation logic leading to false confidence | High (must model fees, slippage, order book depth) | High | Critical for forward testing before live deployment. |
| **Spot Testnet** | Native Official | Binance Spot Testnet | Testnet API Keys | Testnet instability, unrealistic liquidity | Medium (liquidity differs from mainnet) | Medium | Useful for API contract testing, less so for strategy validation. |
| **Margin Live** | Native Official | Binance Margin (Cross/Isolated) | Real API Keys (Margin Enabled) | Liquidation, borrow interest, API complexity | N/A (Real) | Medium | Requires complex state management (borrowed assets, equity). |
| **Margin Paper** | Internally Simulated | Local Engine | None | Incorrectly modeling borrow costs or liquidation logic | High (must model interest, margin calls, collateral haircuts) | Low | Complex simulation; Spot and Futures paper are higher priority. |
| **Futures Live** | Native Official | Binance USDⓈ-M Futures | Real API Keys (Futures Enabled) | Rapid liquidation, funding rate impact | N/A (Real) | High | Essential for shorting and leverage. |
| **Futures Paper** | Internally Simulated | Local Engine | None | Inaccurate funding rate modeling, unrealistic slippage on high leverage | High (must model funding, mark price, liquidation) | High | Crucial for testing leveraged strategies safely. |
| **Futures Testnet**| Native Official | Binance Futures Testnet | Testnet API Keys | Testnet unreliability, unrealistic order book dynamics | Low/Medium | Medium | Good for basic API wiring, poor for performance testing. |
| **Long Capability**| Native Official | All Venues | Required asset balance | Standard directional risk | N/A | High | Fundamental requirement. |
| **Short Capability**| Native Official | Margin / Futures | Margin/Futures Account | Infinite theoretical loss (margin), Liquidation | N/A | High | Essential for market-neutral or bearish strategies. |
| **Leverage Support**| Native Official | Margin / Futures | Margin/Futures Account | Magnified losses, rapid liquidation | N/A | High (Futures) | Must be strictly controlled by risk modules. |
| **Borrow/Repay** | Native Official | Margin | Margin Account | Interest accumulation, failing to repay | N/A | Medium | Specific to Margin trading. |
| **Funding** | Wrapper-Supported | Futures | Futures Account | Drag on performance if ignored | Must track in Paper mode | High (Futures) | Must monitor and account for funding payments/receipts. |
| **Liquidation** | Native Official | Margin / Futures | Margin/Futures Account | Total loss of collateral | Must model accurately in Paper mode | High (Prevention) | System must actively avoid liquidation via risk controls. |
| **Order Types** | Native Official | All Venues | Varies by venue | Exchange rejection of complex orders | Must support Limit, Market, Stop-Loss | High | Start with Limit/Market, add advanced types later. |

## Mode Definitions
*   **Native Official:** Execution via the official Binance API against real or official testnet environments.
*   **Wrapper-Supported:** Handled via API wrappers but requiring specific internal state management (e.g., funding rates).
*   **Internally Simulated:** Execution handled by a local paper-trading engine that mimics exchange behavior using live market data.
*   **Deferred:** Planned for future phases; not part of the initial implementation.
