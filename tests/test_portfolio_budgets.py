import pytest
from datetime import datetime, timezone
from app.portfolio.models import PortfolioConfig
from app.portfolio.budgets import BudgetManager


def test_calculate_snapshot():
    config = PortfolioConfig(total_budget=1000.0, reserve_cash_ratio=0.20)
    manager = BudgetManager(config)

    timestamp = datetime.now(timezone.utc)

    # scenario 1: current equity matches base budget
    snap = manager.calculate_snapshot(
        current_equity=1000.0, pending_allocations_notional=0.0, timestamp=timestamp
    )
    assert snap.total_capital == 1000.0
    assert snap.reserved_capital == 200.0
    assert snap.available_capital == 800.0

    # scenario 2: current equity is higher (e.g. profitable)
    snap2 = manager.calculate_snapshot(
        current_equity=2000.0, pending_allocations_notional=500.0, timestamp=timestamp
    )
    assert snap2.total_capital == 2000.0
    assert snap2.reserved_capital == 400.0
    assert snap2.available_capital == 1100.0  # 2000 - 400 - 500
