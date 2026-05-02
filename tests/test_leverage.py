import pytest
from app.products.registry import ProductRegistry
from app.products.enums import ProductType
from app.execution.derivatives.leverage import LeverageManager
from app.execution.derivatives.exceptions import InvalidLeverageChange


def test_leverage_cap_enforcement():
    reg = ProductRegistry()
    mgr = LeverageManager(reg)

    # Spot does not support leverage
    with pytest.raises(InvalidLeverageChange):
        mgr.set_leverage(ProductType.SPOT, "BTCUSDT", 2)

    # Futures has a cap (e.g. 5x)
    with pytest.raises(InvalidLeverageChange):
        mgr.set_leverage(ProductType.FUTURES_USDM, "BTCUSDT", 100)

    assert mgr.set_leverage(ProductType.FUTURES_USDM, "BTCUSDT", 3) == 3
