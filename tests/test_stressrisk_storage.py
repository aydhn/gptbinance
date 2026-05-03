from app.stressrisk.enums import LossSeverity, BudgetVerdict, StressOverlayVerdict
from app.stressrisk.models import StressRun, PortfolioStressSnapshot, StressBudgetResult, CorrelationStressSnapshot, LiquidityStressSnapshot, StressOverlayDecision
from app.stressrisk.storage import StressStorage
from app.stressrisk.repository import StressRepository


def test_storage():
    storage = StressStorage()
    repo = StressRepository(storage)
    run = StressRun(
        run_id="run1",
        timestamp="2023-01-01T00:00:00Z",
        scenario_set_id="set1",
        profile="live",
        portfolio_snapshot=PortfolioStressSnapshot(
            run_id="run1",
            timestamp="2023-01-01T00:00:00Z",
            total_base_value=1000.0,
            total_estimated_loss=100.0,
            overall_severity=LossSeverity.LOW,
            scenario_losses=[],
            reserve_cash_sensitivity=0.0,
        ),
        budget_result=StressBudgetResult(
            profile="live",
            verdict=BudgetVerdict.PASS,
            utilized_daily_budget_pct=10.0,
            utilized_scenario_budget_pct=10.0,
            reasons=[],
        ),
        vulnerabilities=[],
        correlation_snapshot=CorrelationStressSnapshot(
            average_correlation_jump=0.1,
            diversification_erosion_pct=0.1,
            highly_correlated_clusters=[],
        ),
        liquidity_snapshot=LiquidityStressSnapshot(
            average_spread_widening_pct=0.1,
            average_turnover_drop_pct=0.1,
            illiquid_symbols_warning=[],
        ),
        overlay_decision=StressOverlayDecision(
            run_id="run1",
            profile="live",
            verdict=StressOverlayVerdict.ALLOW,
            reasons=[],
            evidence_refs=[],
        ),
        findings=[],
        recommendations=[],
    )
    repo.store_run(run)
    assert repo.fetch_run("run1") is not None
