from datetime import datetime, timezone
from decimal import Decimal
from app.performance_plane.returns import ReturnSurfaceBuilder
from app.performance_plane.enums import PerformanceDomain, WindowClass
from app.performance_plane.windows import WindowManager


def test_return_surface_correctness():
    w = WindowManager.create_window(
        WindowClass.SESSION, datetime(2024, 1, 1, tzinfo=timezone.utc)
    )
    r = ReturnSurfaceBuilder.build_pnl_linked(
        domain=PerformanceDomain.PORTFOLIO,
        target_id="MAIN",
        window=w,
        realized_pnl=Decimal("150.50"),
        currency="USD",
    )

    assert r.value == Decimal("150.50")
    assert r.currency == "USD"
    assert r.domain == PerformanceDomain.PORTFOLIO
