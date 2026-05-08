from decimal import Decimal
from datetime import datetime, timezone
from app.performance_plane.risk_adjusted import RiskAdjustedEvaluator
from app.performance_plane.returns import ReturnSurfaceBuilder
from app.performance_plane.enums import PerformanceDomain, WindowClass
from app.performance_plane.windows import WindowManager


def test_drawdown_aware_surfaces():
    w = WindowManager.create_window(
        WindowClass.SESSION,
        datetime(2024, 1, 1, tzinfo=timezone.utc),
        datetime(2024, 1, 2, tzinfo=timezone.utc),
    )
    r = ReturnSurfaceBuilder.build_pnl_linked(
        domain=PerformanceDomain.PORTFOLIO,
        target_id="MAIN",
        window=w,
        realized_pnl=Decimal("100.00"),
        currency="USD",
    )

    result = RiskAdjustedEvaluator.evaluate_drawdown_adjusted(r, Decimal("20.00"))
    assert result["return_on_max_drawdown"] == 5.0
    assert len(result["caveats"]) == 0

    result2 = RiskAdjustedEvaluator.evaluate_drawdown_adjusted(r, Decimal("0.00"))
    assert len(result2["caveats"]) == 1
    assert "meaningless" in result2["caveats"][0]
