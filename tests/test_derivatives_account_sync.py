import pytest
import time
from app.products.registry import ProductRegistry
from app.products.enums import ProductType, MarginMode
from app.execution.derivatives.leverage import LeverageManager
from app.execution.derivatives.margin_modes import MarginModeManager
from app.execution.derivatives.position_modes import PositionModeManager
from app.execution.derivatives.account_sync import DerivativeAccountSync

def test_derivative_account_sync():
    reg = ProductRegistry()
    lev = LeverageManager(reg)
    mar = MarginModeManager(reg)
    pos = PositionModeManager(reg)
    sync = DerivativeAccountSync(lev, mar, pos)

    mock_exchange_data = {
        "positions": [
            {"symbol": "BTCUSDT", "leverage": 4, "marginType": "isolated"}
        ]
    }

    sync.sync_from_exchange(ProductType.FUTURES_USDM, mock_exchange_data)

    assert lev.get_leverage(ProductType.FUTURES_USDM, "BTCUSDT") == 4
