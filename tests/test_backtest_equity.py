from datetime import datetime
from app.backtest.equity import EquityTracker


def test_equity_tracking():
    tracker = EquityTracker(1000.0)
    tracker.process_fill(fee=1.0, realized_pnl=50.0)  # Cash: 1049.0
    assert tracker.cash == 1049.0

    snap = tracker.snapshot(datetime.now(), unrealized_pnl=0.0)
    assert snap.equity == 1049.0
    assert tracker.high_water_mark == 1049.0

    # Drop in equity
    snap2 = tracker.snapshot(datetime.now(), unrealized_pnl=-100.0)  # Equity: 949.0
    assert snap2.equity == 949.0
    assert tracker.max_drawdown_pct > 0.0
