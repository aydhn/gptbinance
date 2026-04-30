from datetime import datetime
from typing import Dict, List
from app.portfolio.models import (
    PortfolioConfig,
    PortfolioBudgetSnapshot,
    PortfolioContext,
)


class BudgetManager:
    def __init__(self, config: PortfolioConfig):
        self.config = config

    def calculate_snapshot(
        self,
        current_equity: float,
        pending_allocations_notional: float,
        timestamp: datetime,
    ) -> PortfolioBudgetSnapshot:
        total_capital = max(current_equity, self.config.total_budget)
        reserved_capital = total_capital * self.config.reserve_cash_ratio

        # Available capital is total minus reserved and pending. It can go negative if over-allocated
        available_capital = (
            total_capital - reserved_capital - pending_allocations_notional
        )

        return PortfolioBudgetSnapshot(
            timestamp=timestamp,
            total_capital=total_capital,
            reserved_capital=reserved_capital,
            available_capital=max(0.0, available_capital),  # Clamp to 0
            pending_allocations_notional=pending_allocations_notional,
        )

    def can_allocate(
        self, requested_notional: float, context: PortfolioContext
    ) -> bool:
        """Quick check if there's enough available budget"""
        return context.budget.available_capital >= requested_notional
