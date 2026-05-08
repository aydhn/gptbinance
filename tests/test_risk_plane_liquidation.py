import math
from app.risk_plane.liquidation import calculate_liquidation_proximity
from app.risk_plane.enums import LiquidationClass


def test_calculate_liquidation_proximity():
    # Mark: 100, Liq: 95 -> dist: 0.05
    state = calculate_liquidation_proximity(
        mark_price=100.0, liquidation_price=95.0, stale_mark=False
    )
    assert math.isclose(state.proximity_ratio, 0.05)
    assert state.liquidation_class == LiquidationClass.WARNING
    assert math.isclose(state.conservative_buffer, 0.05)

    # Stale mark tightens buffer
    state2 = calculate_liquidation_proximity(
        mark_price=100.0, liquidation_price=95.0, stale_mark=True
    )
    assert math.isclose(state2.conservative_buffer, 0.04)  # 0.05 * 0.8
