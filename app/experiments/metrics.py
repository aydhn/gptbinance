class MetricsCollector:
    def collect(self, run_results: dict) -> dict:
        return {
            "pnl": run_results.get("pnl_delta", 0),
            "trade_count": run_results.get("trade_count_delta", 0),
            "friction": run_results.get("friction_reduction", 0),
        }
