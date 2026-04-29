import pytest
from app.execution.paper.position_book import PositionBookManager
from app.execution.paper.models import PaperPosition
from app.execution.paper.pnl import PnlTracker


def test_pnl_tracker():
    tracker = PnlTracker(10000.0)

    # Simulate fees and realized pnl
    tracker.add_fee(10.0)
    tracker.add_realized_pnl(500.0)

    assert tracker.current_equity == 10490.0

    # Add unrealized
    book = PositionBookManager()
    pos = book.get_position("BTC")
    pos.qty = 1.0
    pos.side = "LONG"
    pos.avg_entry_price = 50000.0

    snap = tracker.get_snapshot(book, {"BTC": 51000.0})
    assert snap.equity == 11490.0
    assert snap.drawdown_pct == 0.0

    # Market drop
    snap2 = tracker.get_snapshot(book, {"BTC": 49000.0})
    assert snap2.equity == 9490.0
    assert snap2.drawdown_pct > 0.0
