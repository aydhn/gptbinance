# 100-Phase Milestone Roadmap

## Stage 1: Foundations (1-10)
1. **Constitution & Skeleton**: Establish program charter, repo structure, docs. (Phase 01)
2. **Config Engine**: Implement typed Pydantic settings and env loading.
3. **Core Logging**: Implement structured JSON logging and log rotation.
4. **Local DB Scaffold**: Setup SQLite schemas for state, orders, fills.
5. **Data Contracts Implementation**: Code the `Tick`, `Kline`, `OrderRequest` dataclasses.
6. **Error Handling Core**: Define custom exceptions and global catchers.
7. **Basic Telemetry**: Implement heartbeat script that logs to file.
8. **Telegram Bot Base**: Implement basic Telegram messaging (send-only).
9. **Telegram Commands**: Implement `/status`, `/ping` commands via Telegram.
10. **State Persistence Base**: Write CRUD operations for basic state in SQLite.

## Stage 2: Connectors & Data (11-20)
11. **Binance REST Base**: Implement basic authenticated REST wrapper.
12. **Exchange Info Sync**: Fetch and parse exchange filters (tickSize, minNotional).
13. **Data Downloader**: Script to download historical Klines via REST.
14. **Historical Parquet Storage**: Convert downloaded CSVs to partitioned Parquet.
15. **Binance WS Base**: Implement async Websocket connection manager.
16. **Live Tick Stream**: Subscribe to trades/bookTicker and parse to `Tick` objects.
17. **Live Kline Stream**: Subscribe to klines and parse to `Kline` objects.
18. **WS Auto-Reconnect**: Implement exponential backoff reconnect logic for WS.
19. **Stream Health Monitor**: Detect stale streams and trigger alerts.
20. **Data Feed Aggregator**: Multiplex multiple WS streams into a single async queue.

## Stage 3: Paper Trading Core (21-30)
21. **Paper Engine Skeleton**: Create the internal matching engine class.
22. **Paper Order Routing**: Route `OrderRequest` to the paper engine.
23. **Paper Market Fills**: Implement realistic market order fill logic against ticks.
24. **Paper Limit Fills**: Implement queue-aware limit order fill logic.
25. **Paper Commission**: Deduct realistic Binance fees from paper fills.
26. **Portfolio State Update**: Update `Position` objects based on `FillEvent`s.
27. **Local PnL Calculation**: Calculate un/realized PnL based on mark price.
28. **Paper Engine Tests**: Unit tests proving fill realism and PnL math.
29. **Paper Session Manager**: Script to run paper engine against live WS feeds.
30. **Daily Paper Summary**: Generate EOD report on paper performance via Telegram.

## Stage 4: Risk Layer (31-40)
31. **Risk Engine Skeleton**: Implement base risk validation pipeline.
32. **Max Notional Filter**: Reject orders exceeding USD limits.
33. **Precision Filter**: Enforce tickSize and stepSize rounding before execution.
34. **Fat Finger Filter**: Reject orders too far from mark price.
35. **Max Drawdown Limit**: Halt trading if account equity drops X%.
36. **Global Kill Switch**: Implement `/kill` command via Telegram to halt system.
37. **Rate Limiter**: Track order submissions and throttle if exceeding limits.
38. **Exposure Tracker**: Calculate total gross/net exposure across portfolio.
39. **Leverage Cap**: Prevent order placement that pushes leverage past limit.
40. **Risk Integration Test**: End-to-end tests proving risk intercepts bad orders.

## Stage 5: Strategy Skeleton (41-50)
41. **Strategy Base Class**: Define the standard interface (`on_tick`, `on_kline`).
42. **Signal Generator Interface**: Standardize how strategies emit conviction.
43. **Simple SMA Strategy**: Implement a basic moving average crossover for testing.
44. **Position Sizer Module**: Convert abstract signals into concrete order sizes.
45. **Strategy Registry**: Dynamic loading of strategies from config.
46. **Strategy Context**: Provide strategies safe access to historical data buffer.
47. **Cooldown Logic**: Prevent strategies from over-trading after a stop-out.
48. **Basic Indicator Library**: Implement fast SMA, EMA, RSI using NumPy/Pandas.
49. **Mock Strategy Test**: Unit test the SMA strategy against mocked data.
50. **Strategy to Paper E2E**: Run the SMA strategy live in Paper mode.

## Stage 6: Backtesting (51-60)
51. **Backtest Engine Base**: Create offline event loop for historical data.
52. **Vectorized vs Event-Driven**: Implement both paths (fast vectorized for screening, event-driven for accurate fill simulation).
53. **Backtest Data Loader**: Efficiently load Parquet files into the engine.
54. **Slippage Modeling**: Implement statistical slippage models for backtesting.
55. **Metrics Calculator**: Calculate Sharpe, Sortino, Max DD, Win Rate.
56. **Tear Sheet Generation**: Output basic HTML/Markdown reports of backtest.
57. **Baseline Benchmarks**: Implement B&H and naive SMA benchmarks.
58. **Benchmark Comparison**: Code to overlay strategy performance vs benchmark.
59. **Backtest Validation**: Verify backtest results match paper trading results (sanity check).
60. **Batch Backtesting**: Script to run multiple strategies/params across history.

## Stage 7: Optimizer & Robustness (61-70)
61. **Optimizer Base**: Define interface for hyperparameter search.
62. **Grid Search Implementation**: Basic exhaustive search.
63. **Walk-Forward Core**: Implement rolling train/test window logic.
64. **WFA Metrics**: Track parameter stability across walk-forward windows.
65. **Overfitting Detection**: Scripts to identify strategies whose OOS performance diverges wildly from IS.
66. **Ablation Toolkit**: Helper functions to turn strategy rules on/off to measure impact.
67. **Randomized Data Testing**: Test strategy against shuffled/bootstrapped price data.
68. **Parameter Heatmaps**: Generate visual heatmaps of parameter landscapes.
69. **Optuna Integration**: (Optional) Integrate Optuna for smarter parameter search.
70. **Optimizer Policy Enforcement**: Hardcode rules preventing excessive parameter counts.

## Stage 8: Margin & Futures Extension (71-80)
71. **Margin/Futures Architecture**: Extend Data Contracts for Margin/Futures specifics.
72. **Futures Rest Connectors**: Implement USDⓈ-M API wrappers.
73. **Funding Rate Sync**: Fetch and store historical/live funding rates.
74. **Paper Funding Simulation**: Apply funding rate payments/receipts to paper positions.
75. **Liquidation Modeling**: Calculate margin ratios and simulate margin calls locally.
76. **Shorting Support**: Ensure risk and portfolio modules handle negative quantities correctly.
77. **Futures Order Types**: Support Post-Only and Time-In-Force constraints.
78. **Cross vs Isolated Support**: Differentiate accounting for margin types.
79. **Futures Strategy Adapters**: Create strategies specifically aware of funding costs.
80. **Futures Paper E2E**: Run a short-selling strategy live in Paper mode.

## Stage 9: ML Integration (81-90)
81. **ML Feature Pipeline**: Scripts to convert raw Klines into standard ML features.
82. **Dataset Creation**: Standardize train/val/test splits, applying purging/embargoing.
83. **Baseline Models**: Implement simple Logistic Regression labeler.
84. **Model Serialization**: Save/load models using ONNX or Joblib.
85. **Inference Engine**: Load model in live/paper mode for real-time predictions.
86. **Regime Classifier**: Train a model to classify market volatility/trend state.
87. **Meta-Labeling**: Train model to predict whether base strategy signal will win.
88. **Feature Importance Logging**: Track which features drive predictions over time.
89. **Champion/Challenger System**: Logic to run old/new models side-by-side.
90. **ML Safety Bounds**: Ensure ML outputs cannot override hard risk rules.

## Stage 10: Live Readiness & Ops (91-100)
91. **Live Execution Routing**: Connect Risk-validated orders to actual Binance REST endpoints.
92. **ClientOrderId Management**: Ensure robust duplicate-order prevention.
93. **Live Fill Reconciliation**: Sync local state with Binance `executionReport` WS events.
94. **Orphan Order Sweeper**: Script to cancel unrecorded orders on startup.
95. **Operator Runbook**: Finalize docs/018_operator_runbook_outline.md into actionable guides.
96. **Dry-Run Mode**: Final test connecting to live API but with `TEST` flag set on order payloads.
97. **Alert Hardening**: Ensure critical alerts bypass silent modes and require operator ack.
98. **Database Compaction**: Ops scripts to clean old state and maintain SQLite performance.
99. **Final Security Audit**: Review secrets handling, file permissions, and API key limits.
100. **Live Production Launch**: Enable `live` mode flag with minimal capital.
