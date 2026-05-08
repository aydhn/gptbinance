from decimal import Decimal
from datetime import datetime, timezone
from app.performance_plane.quality import PerformanceQualityChecker
from app.performance_plane.attribution import AttributionTreeBuilder
from app.performance_plane.returns import ReturnSurfaceBuilder
from app.performance_plane.enums import PerformanceDomain, WindowClass, AttributionClass
from app.performance_plane.windows import WindowManager


def test_missing_attribution_component_warnings():
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

    builder = AttributionTreeBuilder(r)
    builder.add_node(AttributionClass.SIGNAL_SELECTION, Decimal("80.00"))
    tree = builder.build()

    warnings = PerformanceQualityChecker.check_quality(r, tree)
    assert len(warnings) > 0
    assert "High unexplained residual value" in warnings[0]
