import pytest
from app.execution.paper.models import PaperFill
from app.execution.paper.position_book import PositionBookManager


def test_position_book_open_long():
    book = PositionBookManager()
    fill = PaperFill(
        fill_id="f1",
        order_id="o1",
        symbol="BTCUSDT",
        side="BUY",
        qty=1.0,
        price=50000.0,
        fees=0.0,
        slippage=0.0,
    )
    pnl = book.process_fill(fill)
    assert pnl == 0.0
    pos = book.get_position("BTCUSDT")
    assert pos.qty == 1.0
    assert pos.avg_entry_price == 50000.0
    assert pos.side == "LONG"


def test_position_book_close_long_profit():
    book = PositionBookManager()
    fill1 = PaperFill(
        fill_id="f1",
        order_id="o1",
        symbol="BTCUSDT",
        side="BUY",
        qty=1.0,
        price=50000.0,
        fees=0.0,
        slippage=0.0,
    )
    book.process_fill(fill1)

    fill2 = PaperFill(
        fill_id="f2",
        order_id="o2",
        symbol="BTCUSDT",
        side="SELL",
        qty=1.0,
        price=55000.0,
        fees=0.0,
        slippage=0.0,
    )
    pnl = book.process_fill(fill2)
    assert pnl == 5000.0
    pos = book.get_position("BTCUSDT")
    assert pos.qty == 0.0
    assert pos.side == "FLAT"


def test_position_book_reverse_short_to_long():
    book = PositionBookManager()
    fill1 = PaperFill(
        fill_id="f1",
        order_id="o1",
        symbol="BTCUSDT",
        side="SELL",
        qty=1.0,
        price=50000.0,
        fees=0.0,
        slippage=0.0,
    )
    book.process_fill(fill1)

    # Reverse position
    fill2 = PaperFill(
        fill_id="f2",
        order_id="o2",
        symbol="BTCUSDT",
        side="BUY",
        qty=2.0,
        price=45000.0,
        fees=0.0,
        slippage=0.0,
    )
    pnl = book.process_fill(fill2)

    # Made 5000 on short, now long 1 @ 45000
    assert pnl == 5000.0
    pos = book.get_position("BTCUSDT")
    assert pos.qty == 1.0
    assert pos.avg_entry_price == 45000.0
    assert pos.side == "LONG"
