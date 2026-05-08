from decimal import Decimal
from datetime import datetime, timezone

from app.performance_plane.attribution import AttributionTreeBuilder
from app.performance_plane.returns import ReturnSurfaceBuilder
from app.performance_plane.enums import PerformanceDomain, WindowClass, AttributionClass
from app.performance_plane.windows import WindowManager


def test_attribution_tree_integrity():
    w = WindowManager.create_window(
        WindowClass.SESSION, datetime(2024, 1, 1, tzinfo=timezone.utc)
    )
    r = ReturnSurfaceBuilder.build_pnl_linked(
        domain=PerformanceDomain.PORTFOLIO,
        target_id="MAIN",
        window=w,
        realized_pnl=Decimal("100.00"),
        currency="USD",
    )

    builder = AttributionTreeBuilder(r)
    builder.add_node(
        AttributionClass.SIGNAL_SELECTION, Decimal("80.00"), ["Good signal"]
    )
    builder.add_node(AttributionClass.TIMING, Decimal("30.00"), ["Good timing"])
    builder.add_node(AttributionClass.EXECUTION, Decimal("-15.00"), ["Slippage drag"])

    tree = builder.build()

    assert len(tree.nodes) == 3
    # 80 + 30 - 15 = 95
    # residual should be 100 - 95 = 5
    assert tree.residual_value == Decimal("5.00")
