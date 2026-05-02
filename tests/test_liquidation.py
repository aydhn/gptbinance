import pytest
from app.execution.derivatives.liquidation import LiquidationApproxModel
from app.execution.derivatives.enums import LiquidationProximity


def test_liquidation_proximity():
    model = LiquidationApproxModel(maintenance_margin_rate=0.01)

    # Safe distance
    snap = model.calculate_liquidation_snapshot("BTC", 100, 100, 10, 1000, True)
    assert snap.proximity == LiquidationProximity.SAFE

    # Danger distance (balance is very low compared to maintenance req)
    snap = model.calculate_liquidation_snapshot("BTC", 100, 100, 10, 11, True)
    assert snap.proximity == LiquidationProximity.DANGER
