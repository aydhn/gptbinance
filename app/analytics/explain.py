from typing import Dict, Any


class AnalyticsExplainer:
    def explain_strategy_performance(self, family: str, stats: Dict[str, Any]) -> str:
        return f"Strategy {family} generated {stats.get('pnl', 0.0)} PnL over {stats.get('trade_count', 0)} trades. Hit rate is {stats.get('hit_rate', 0.0)*100:.1f}%."

    def explain_regime_collapse(self, regime: str, suitability: float) -> str:
        if suitability < 0:
            return f"Regime {regime} showed negative suitability ({suitability}), suggesting a breakdown of assumptions."
        return f"Regime {regime} appears stable."

    def explain_divergence(self, diff: float) -> str:
        if abs(diff) > 5.0:
            return f"Significant divergence of {diff} detected between expected and realized outcomes. Check execution latency and slippage."
        return "Divergence is within acceptable bounds."

    def explain_concentration_effect(self, rejected: int) -> str:
        if rejected > 0:
            return f"Concentration limits rejected {rejected} trades, likely preventing overexposure."
        return "Concentration limits did not intervene significantly."
