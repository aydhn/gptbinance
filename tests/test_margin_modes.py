import pytest
from app.products.registry import ProductRegistry
from app.products.enums import ProductType, MarginMode
from app.execution.derivatives.margin_modes import MarginModeManager


def test_margin_mode_setting():
    reg = ProductRegistry()
    mgr = MarginModeManager(reg)

    mgr.set_mode(ProductType.FUTURES_USDM, "BTCUSDT", MarginMode.CROSS)
    assert mgr.get_mode(ProductType.FUTURES_USDM, "BTCUSDT") == MarginMode.CROSS
