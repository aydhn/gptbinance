from app.backtest.storage import BacktestStorage


class BacktestReporter:
    def __init__(self, storage: BacktestStorage):
        self.storage = storage

    def format_summary(self, run_id: str) -> str:
        summary = self.storage.load_summary(run_id)
        if not summary:
            return f"No summary found for run {run_id}"

        lines = [
            f"=== Backtest Summary ({run_id}) ===",
            f"Total Return: {summary['total_return_pct']:.2f}%",
            f"Final Equity: {summary['final_equity']:.2f}",
            f"Max Drawdown: {summary['max_drawdown_pct']:.2f}%",
            f"Total Trades: {summary['total_trades']}",
            f"Hit Rate:     {summary['hit_rate']:.2f}%",
            f"Expectancy:   {summary['expectancy']:.2f}",
            f"Profit Factor:{summary['profit_factor']:.2f}",
            f"Total Fees:   {summary['total_fees_paid']:.2f}",
        ]
        return "\n".join(lines)

    def format_trades(self, run_id: str, limit: int = 10) -> str:
        trades = self.storage.load_trades(run_id)
        if not trades:
            return f"No trades found for run {run_id}"

        lines = [f"=== Trade Log ({run_id}) ==="]
        for t in trades[:limit]:
            side = t["side"]
            qty = t["quantity"]
            ep = t["entry_price"]
            xp = t["exit_price"]
            pnl = t["realized_pnl"]
            lines.append(
                f"[{t['entry_timestamp']}] {side} {qty:.4f} @ {ep:.2f} -> {xp:.2f} | PnL: {pnl:.2f}"
            )

        if len(trades) > limit:
            lines.append(f"... and {len(trades) - limit} more trades.")

        return "\n".join(lines)

    def format_equity(self, run_id: str) -> str:
        equity = self.storage.load_equity(run_id)
        if not equity:
            return f"No equity data found for run {run_id}"

        lines = [f"=== Equity Curve Samples ({run_id}) ==="]
        step = max(1, len(equity) // 10)
        for i in range(0, len(equity), step):
            snap = equity[i]
            lines.append(
                f"[{snap['timestamp']}] Equity: {snap['equity']:.2f} | DD: {snap['drawdown_pct']:.2f}%"
            )

        return "\n".join(lines)
