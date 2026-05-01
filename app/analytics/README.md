# Analytics Layer

The analytics layer is strictly post-trade. It observes, aggregates, and attributes the results of actions taken by the rest of the system (strategy, risk, portfolio, execution).

It DOES NOT modify the live trading configuration or take actions automatically. Its purpose is to output actionable, human-readable data (via CLI and Telegram) so an operator can make informed decisions.
