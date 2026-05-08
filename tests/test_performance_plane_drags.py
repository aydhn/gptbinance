from decimal import Decimal
from app.performance_plane.drags import DragSurfaceAnalyzer
from app.performance_plane.components import ComponentRegistry
from app.performance_plane.enums import DragClass


def test_slippage_funding_fee_carry_drag_attribution():
    d1 = ComponentRegistry.register_drag(DragClass.SLIPPAGE, Decimal("-10.5"), "USD")
    d2 = ComponentRegistry.register_drag(DragClass.SLIPPAGE, Decimal("-5.0"), "USD")
    d3 = ComponentRegistry.register_drag(DragClass.FEE, Decimal("-2.5"), "USD")

    summary = DragSurfaceAnalyzer.summarize_drags([d1, d2, d3])

    assert summary[DragClass.SLIPPAGE.value] == -15.5
    assert summary[DragClass.FEE.value] == -2.5
    assert summary[DragClass.FUNDING.value] == 0.0
