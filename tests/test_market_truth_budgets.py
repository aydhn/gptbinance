from app.market_truth.budgets import BudgetRegistry


def test_budget_registry():
    b = BudgetRegistry.get_budget("canary_live_caution")
    assert b.max_lag_ms == 500.0
