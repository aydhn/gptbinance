from app.reliability.burn import BurnRateAnalytics
from app.reliability.models import ErrorBudget
from app.reliability.enums import BudgetClass, BurnSeverity


def test_short_long_window_burn():
    budget = ErrorBudget(
        budget_id="b1",
        slo_id="s1",
        budget_class=BudgetClass.SOFT,
        total_budget_value=100.0,
        remaining_budget=80.0,
    )

    # Fast burn: > 10% in short window
    report_fast = BurnRateAnalytics.calculate_burn_rate(budget, 15.0, 20.0, 1.0, 6.0)
    assert report_fast.severity == BurnSeverity.FAST_BURN
    assert report_fast.projected_exhaustion_hours is not None

    # Slow burn: > 5% in long window
    report_slow = BurnRateAnalytics.calculate_burn_rate(budget, 1.0, 6.0, 1.0, 6.0)
    assert report_slow.severity == BurnSeverity.SLOW_BURN
