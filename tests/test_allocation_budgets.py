from app.allocation.budgets import BudgetManager


def test_budget_manager():
    mgr = BudgetManager()
    b = mgr.get_budget("primary_alpha_01")
    assert b.headroom == 100000.0

    mgr.consume("primary_alpha_01", 10000.0)
    b2 = mgr.get_budget("primary_alpha_01")
    assert b2.headroom == 90000.0
    assert b2.consumed_notional == 10000.0
