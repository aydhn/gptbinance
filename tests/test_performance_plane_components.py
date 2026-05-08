from decimal import Decimal
from app.performance_plane.components import ComponentRegistry
from app.performance_plane.enums import DragClass


def test_component_lineage():
    component = ComponentRegistry.register_drag(
        drag_class=DragClass.SLIPPAGE,
        impact_value=Decimal("-10.0"),
        currency="USD",
        lineage_refs=["order_123_fill"],
    )

    assert component.drag_class == DragClass.SLIPPAGE
    assert component.impact_value == Decimal("-10.0")
    assert "order_123_fill" in component.lineage_refs
