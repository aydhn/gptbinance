from app.stressrisk.enums import BudgetVerdict
from app.stressrisk.budgets import BudgetManager


def test_budget_manager():
    mgr = BudgetManager()
    res = mgr.evaluate("canary_live_caution", 300.0)  # max is 200.0
    assert res.verdict == BudgetVerdict.BREACH

    res = mgr.evaluate("canary_live_caution", 100.0)
    assert res.verdict == BudgetVerdict.PASS
