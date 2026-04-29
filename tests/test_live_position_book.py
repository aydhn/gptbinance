import pytest
from app.execution.live_runtime.position_book import LivePositionManager
from app.execution.live_runtime.models import LiveFillRecord


def test_position_book_long_entry_and_close():
    pm = LivePositionManager()

    # Buy 1 BTC @ 50k
    fill1 = LiveFillRecord(
        fill_id="f1",
        order_id="o1",
        client_order_id="c1",
        symbol="BTCUSDT",
        side="BUY",
        qty=1.0,
        price=50000.0,
        fee=10.0,
        fee_asset="USDT",
    )
    pm.process_fill(fill1)

    book = pm.get_book()
    pos = book.positions["BTCUSDT"]
    assert pos.qty == 1.0
    assert pos.avg_entry_price == 50000.0

    # Sell 0.5 BTC @ 60k -> realized PnL +5k
    fill2 = LiveFillRecord(
        fill_id="f2",
        order_id="o2",
        client_order_id="c2",
        symbol="BTCUSDT",
        side="SELL",
        qty=0.5,
        price=60000.0,
        fee=10.0,
        fee_asset="USDT",
    )
    pm.process_fill(fill2)

    pos = book.positions["BTCUSDT"]
    assert pos.qty == 0.5
    assert pos.avg_entry_price == 50000.0
    # Expected Realized PnL: 5000 - 20 (fees) = 4980
    assert pos.realized_pnl == 4980.0
