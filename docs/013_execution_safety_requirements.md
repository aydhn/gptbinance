# Execution Safety Requirements

The execution engine is the most dangerous part of the system. It must be heavily armored.

## Exchange Filter Handling
Binance enforces strict filters (e.g., `PRICE_FILTER`, `LOT_SIZE`, `MIN_NOTIONAL`).
*   The system must fetch and cache exchange filters periodically.
*   Before any order is sent, the execution module MUST locally validate the order against these filters. If it fails, the order is rejected internally without hitting the API.

## Precision and Step-Size
*   Float math is dangerous. The system must quantize prices to `tickSize` and quantities to `stepSize` using appropriate rounding rules (e.g., round down for quantity to avoid insufficient balance errors).

## Partial Fill Handling
*   Strategies must be written to handle `PARTIALLY_FILLED` states. An order might sit partially filled for a long time.
*   The Portfolio module must accurately reflect partial additions to inventory.

## Duplicate Order Protection (Client Order ID)
*   Every order sent to Binance MUST include a unique, locally generated `newClientOrderId`.
*   If a network timeout occurs during submission, the system can query the order status using this ID to determine if it was actually placed, preventing duplicate submissions on retry.

## Retry and Reconnect Policy
*   **Data Websockets:** Aggressive automatic reconnects with exponential backoff.
*   **Order Placement:** NO automatic retries for timeouts on Market orders (too dangerous if it actually filled). Limit orders may be retried cautiously if the `clientOrderId` confirms it was not placed.

## Stale Data Handling
*   If the system detects that the last websocket tick is older than a threshold (e.g., > 10 seconds), it must pause trading and assume the connection is dead/stale.

## Paper-Fill Realism
*   The paper trading engine must NOT assume instant fills at the mid-price.
*   Market orders must be filled against the actual order book (simulated slippage).
*   Limit orders must only fill when the actual market price trades *through* the limit price.
