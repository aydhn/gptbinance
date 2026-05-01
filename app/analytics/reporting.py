from app.analytics.models import SessionAnalyticsSummary


class AnalyticsReporter:
    def format_strategy_attribution(self, rows: list) -> str:
        lines = ["Strategy Attribution:"]
        for r in rows:
            lines.append(
                f" - {r.strategy_family}: PnL={r.pnl:.2f}, Trades={r.trade_count}, HitRate={r.hit_rate*100:.1f}%"
            )
        return "\n".join(lines)

    def format_regime_attribution(self, rows: list) -> str:
        lines = ["Regime Attribution:"]
        for r in rows:
            lines.append(
                f" - {r.regime}: PnL={r.pnl:.2f}, Suitability={r.suitability_score:.2f}"
            )
        return "\n".join(lines)

    def format_execution_quality(self, report) -> str:
        if not report:
            return "No Execution Quality Data"
        return f"Execution Quality [{report.verdict.name}]: Submits={report.submit_count}, Fills={report.fill_count}, Rejects={report.reject_count}"

    def format_session_summary(self, summary: SessionAnalyticsSummary) -> str:
        lines = [
            f"=== Session Analytics Summary [{summary.run_id}] ===",
            f"Total PnL: {summary.total_pnl:.2f}",
            self.format_strategy_attribution(summary.strategy_attribution),
            self.format_regime_attribution(summary.regime_attribution),
            self.format_execution_quality(summary.execution_quality),
            f"Anomalies Detected: {len(summary.anomalies)}",
            f"Divergences Detected: {len(summary.divergence_warnings)}",
        ]
        return "\n".join(lines)
