import pytest
from unittest.mock import MagicMock
from app.execution.live_runtime.flatten import LiveFlattenController
from app.execution.live_runtime.models import LiveFlattenRequest
from app.execution.live_runtime.enums import FlattenMode


def test_live_flatten():
    mock_gateway = MagicMock()
    mock_pos_book = MagicMock()

    # Mock open orders
    o1 = MagicMock()
    o1.symbol = "BTCUSDT"
    o1.order_id = "o1"
    mock_gateway.get_open_orders.return_value = [o1]

    # Mock positions
    pos1 = MagicMock()
    pos1.qty = 1.0
    pb = MagicMock()
    pb.positions = {"BTCUSDT": pos1}
    mock_pos_book.get_book.return_value = pb

    controller = LiveFlattenController(mock_gateway, mock_pos_book)

    req = LiveFlattenRequest(
        run_id="r1", mode=FlattenMode.CANCEL_AND_CLOSE, reason="Test"
    )
    res = controller.execute_flatten(req)

    assert res.success
    assert res.orders_cancelled == 1
    assert res.positions_closed == 1
    mock_gateway.cancel_order.assert_called_once_with("BTCUSDT", "o1")
    mock_gateway.submit_market_order.assert_called_once_with(
        symbol="BTCUSDT", side="SELL", qty=1.0
    )
