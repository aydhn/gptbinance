from app.capital.tiers import get_tier
from app.capital.budgets import budget_evaluator


def test_budget_evaluation():
    tier = get_tier("canary_micro")

    # Normal usage
    usage_ok = {"total_deployed": 10.0, "concurrent_positions": 1, "loss_intraday": 1.0}
    res_ok = budget_evaluator.evaluate_utilization(tier.budget, usage_ok)
    assert res_ok["ok"] is True

    # Breach
    usage_breach = {"total_deployed": 10.0, "loss_intraday": 10.0}
    res_breach = budget_evaluator.evaluate_utilization(tier.budget, usage_breach)
    assert res_breach["ok"] is False
    assert len(res_breach["breaches"]) > 0
