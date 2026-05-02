import pytest
from app.products.registry import ProductRegistry
from app.products.enums import ProductType, PositionMode
from app.execution.derivatives.position_modes import PositionModeManager
from app.execution.derivatives.exceptions import InvalidMarginModeTransition


def test_position_mode_setting():
    reg = ProductRegistry()
    mgr = PositionModeManager(reg)

    mgr.set_mode(ProductType.FUTURES_USDM, PositionMode.HEDGE)
    assert mgr.get_mode(ProductType.FUTURES_USDM) == PositionMode.HEDGE
