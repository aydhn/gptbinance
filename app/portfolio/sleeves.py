from typing import Dict, Any
from app.portfolio.models import StrategySleeve, SymbolSleeve, PortfolioContext
from app.portfolio.base import BaseSleevePolicy


class SleeveManager(BaseSleevePolicy):
    def check_headroom(self, context: PortfolioContext) -> Dict[str, float]:
        headroom = {}
        for sf, slv in context.strategy_sleeves.items():
            headroom[f"strategy_{sf}"] = max(
                0.0, slv.budget_notional - slv.used_notional
            )

        for sym, slv in context.symbol_sleeves.items():
            headroom[f"symbol_{sym}"] = max(
                0.0, slv.budget_notional - slv.used_notional
            )

        return headroom

    def update_usage(
        self,
        context: PortfolioContext,
        strategy_family: str,
        symbol: str,
        notional: float,
    ):
        if strategy_family in context.strategy_sleeves:
            context.strategy_sleeves[strategy_family].used_notional += notional
        if symbol in context.symbol_sleeves:
            context.symbol_sleeves[symbol].used_notional += notional
