from datetime import datetime, timezone
from decimal import Decimal
from app.performance_plane.baselines import BaselineEvaluator
from app.performance_plane.models import BenchmarkDefinition
from app.performance_plane.enums import BenchmarkClass, PerformanceDomain, WindowClass
from app.performance_plane.returns import ReturnSurfaceBuilder
from app.performance_plane.windows import WindowManager


def test_baseline_suitability():
    w = WindowManager.create_window(
        WindowClass.SESSION, datetime(2024, 1, 1, tzinfo=timezone.utc)
    )
    r = ReturnSurfaceBuilder.build_pnl_linked(
        domain=PerformanceDomain.PORTFOLIO,
        target_id="MAIN",
        window=w,
        realized_pnl=Decimal("100.00"),
        currency="EUR",  # Mismatch with baseline expectation
    )

    b = BenchmarkDefinition(
        benchmark_id="cash_usd",
        benchmark_class=BenchmarkClass.CASH_BASELINE,
        description="USD Cash",
        comparability_requirements=["base_currency_usd"],
        freshness_ttl_seconds=3600,
    )

    report = BaselineEvaluator.evaluate(r, b, Decimal("0.0"))

    assert report.relative_value == Decimal("100.00")
    assert len(report.mismatch_cautions) > 0
    assert "Currency mismatch" in report.mismatch_cautions[0]
