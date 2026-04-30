from typing import Dict, Any, List, Optional
from app.portfolio.models import PortfolioConfig, PortfolioContext, PortfolioCandidate


class PortfolioPolicyManager:
    def __init__(self, config: PortfolioConfig):
        self.config = config

    def check_max_symbol_weight(
        self, symbol: str, requested_notional: float, context: PortfolioContext
    ) -> Optional[str]:
        total_budget = context.budget.total_capital
        if total_budget <= 0:
            return "Zero total budget"

        current_exposure = context.symbol_sleeves.get(symbol, None)
        current_used = current_exposure.used_notional if current_exposure else 0.0

        projected_weight = (current_used + requested_notional) / total_budget
        if projected_weight > self.config.max_symbol_weight:
            return f"Max symbol weight exceeded for {symbol}: projected {projected_weight:.2f} > limit {self.config.max_symbol_weight:.2f}"
        return None

    def check_max_strategy_sleeve_weight(
        self, strategy_family: str, requested_notional: float, context: PortfolioContext
    ) -> Optional[str]:
        total_budget = context.budget.total_capital
        if total_budget <= 0:
            return "Zero total budget"

        current_exposure = context.strategy_sleeves.get(strategy_family, None)
        current_used = current_exposure.used_notional if current_exposure else 0.0

        projected_weight = (current_used + requested_notional) / total_budget
        if projected_weight > self.config.max_strategy_sleeve_weight:
            return f"Max strategy sleeve weight exceeded for {strategy_family}: projected {projected_weight:.2f} > limit {self.config.max_strategy_sleeve_weight:.2f}"
        return None

    def check_max_correlated_cluster_weight(
        self, symbol: str, requested_notional: float, context: PortfolioContext
    ) -> Optional[str]:
        # Identify if symbol is in a high correlation cluster
        cluster_id = None
        for c_id, symbols in context.correlation.clusters.items():
            if symbol in symbols:
                cluster_id = c_id
                break

        if not cluster_id:
            return None

        total_budget = context.budget.total_capital
        if total_budget <= 0:
            return "Zero total budget"

        # Sum exposure of all symbols in cluster
        cluster_exposure = 0.0
        for s in context.correlation.clusters[cluster_id]:
            slv = context.symbol_sleeves.get(s, None)
            if slv:
                cluster_exposure += slv.used_notional

        projected_weight = (cluster_exposure + requested_notional) / total_budget
        if projected_weight > self.config.max_correlated_cluster_weight:
            return f"Max correlated cluster weight exceeded for cluster {cluster_id}: projected {projected_weight:.2f} > limit {self.config.max_correlated_cluster_weight:.2f}"
        return None

    def check_max_new_allocations(
        self, current_allocations_count: int
    ) -> Optional[str]:
        if current_allocations_count >= self.config.max_new_allocations_per_cycle:
            return f"Max new allocations per cycle reached: {current_allocations_count} >= {self.config.max_new_allocations_per_cycle}"
        return None

    def check_reserve_cash(
        self, requested_notional: float, context: PortfolioContext
    ) -> Optional[str]:
        total_budget = context.budget.total_capital
        if total_budget <= 0:
            return "Zero total budget"

        projected_available = context.budget.available_capital - requested_notional
        required_reserve = total_budget * self.config.reserve_cash_ratio

        # If available capital after allocation drops below required reserve
        if projected_available < required_reserve:
            return f"Reserve cash ratio breached: projected available {projected_available:.2f} < required reserve {required_reserve:.2f}"
        return None
