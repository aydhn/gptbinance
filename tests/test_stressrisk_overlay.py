from app.stressrisk.enums import StressOverlayVerdict, BudgetVerdict
from app.stressrisk.models import StressBudgetResult
from app.stressrisk.overlay import StressOverlayEngine


def test_overlay_engine():
    engine = StressOverlayEngine()
    budget_result = StressBudgetResult(
        profile="live",
        verdict=BudgetVerdict.BREACH,
        utilized_daily_budget_pct=150.0,
        utilized_scenario_budget_pct=150.0,
        reasons=["Exceeded"],
    )
    decision = engine.generate_overlay("live", budget_result)
    assert decision.verdict == StressOverlayVerdict.BLOCK
