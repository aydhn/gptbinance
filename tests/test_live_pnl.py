import pytest
from app.execution.live_runtime.pnl import LivePnlCalculator
from app.execution.live_runtime.models import (
    LivePositionBook,
    LivePosition,
    LiveAccountSnapshot,
    LiveBalanceSnapshot,
)


def test_live_pnl_calculator():
    calc = LivePnlCalculator("run_id_1")

    pb = LivePositionBook()
    pb.positions["BTCUSDT"] = LivePosition(
        symbol="BTCUSDT", qty=1.0, avg_entry_price=50000.0, realized_pnl=500.0
    )

    prices = {"BTCUSDT": 51000.0}
    pnl_snaps = calc.compute_pnl(pb, prices)

    assert len(pnl_snaps) == 1
    assert pnl_snaps[0].unrealized_pnl == 1000.0
    assert pnl_snaps[0].realized_pnl == 500.0

    account = LiveAccountSnapshot(
        run_id="run_id_1",
        balances=[LiveBalanceSnapshot(asset="USDT", free=10000.0, locked=0.0)],
    )

    eq_snap = calc.generate_equity_snapshot(account, pnl_snaps)
    # Equity = 10000 (base) + 500 (realized) + 1000 (unrealized) = 11500
    assert eq_snap.total_equity_usd == 11500.0
    assert eq_snap.max_drawdown_pct == 0.0
