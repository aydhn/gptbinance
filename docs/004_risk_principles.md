# Risk Principles

Risk management is the foundational layer of this system. It operates on the principle of "guilty until proven innocent." Every action is blocked unless it explicitly passes all risk checks.

## Account-Level Risk Rules
*   **Global Kill Switch:** A hardware or software interrupt that instantly cancels all open orders and attempts to flatten all positions. Takes precedence over everything.
*   **Max Account Drawdown:** If the total account equity falls below a configured percentage (e.g., 20% from High Water Mark), trading is halted across all strategies globally.
*   **Daily Loss Limit:** Maximum allowable loss per 24-hour rolling period. Breach triggers an immediate halt until operator intervention.
*   **Total Exposure Cap:** The sum of all absolute position values (long + short) must not exceed a configured multiple of account equity (e.g., Max Gross Leverage = 2.0x).

## Strategy-Level Risk Rules
*   **Strategy Drawdown Cap:** If a specific strategy exceeds its allocated drawdown limit, only that strategy is halted.
*   **Allocation Limits:** Strategies can only risk their allocated portion of capital, preventing a rogue strategy from blowing up the entire account.
*   **Max Open Orders:** Hard cap on the number of simultaneous open orders a strategy can maintain.

## Trade-Level Risk Rules
*   **Max Order Size:** Hard limit on the notional value of a single order (e.g., "No order > $5,000").
*   **Fat Finger Protection:** Reject orders where the limit price deviates significantly (e.g., > 5%) from the current mark price.
*   **Min Notional Compliance:** Ensure orders meet Binance's minimum notional requirements to avoid API rejection loops.
*   **Step Size Compliance:** Quantize order quantities and prices to exactly match Binance's allowed step sizes and tick sizes.

## Circuit Breakers and Throttling
*   **Volatility Circuit Breaker:** If market volatility (e.g., 1-minute ATR) exceeds extreme thresholds, pause new entries; allow only exits.
*   **Order Rate Limiting:** Prevent the system from sending more than X orders per minute to avoid API bans and rapid cascading losses.

## Position Sizing Doctrine
*   Position sizing must be determined by a dedicated risk module, NOT hardcoded within the strategy logic. Strategies suggest a signal and conviction; Risk determines the size based on volatility, account equity, and current exposure.

## Execution Awareness
*   **Slippage Awareness:** Risk models must assume adverse slippage in simulations and live tracking.
*   **Fee Awareness:** All PnL and risk calculations must deduct estimated exchange fees.
*   **Margin/Funding Awareness:** Futures/Margin trading must actively track required margin, available collateral, and accrued funding rates.

## Liquidation Avoidance Doctrine
*   The system must never rely on the exchange's liquidation engine.
*   Internal margin calls must trigger position reduction well before the exchange's maintenance margin threshold is reached.

## Manual Override Doctrine
*   Operators can close positions or cancel orders manually via Telegram or CLI.
*   Manual interventions immediately sync state back to the portfolio manager. Strategies must adapt gracefully to positions disappearing due to manual override.
