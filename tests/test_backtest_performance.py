from app.backtest.performance import PerformanceCalculator
from app.backtest.models import TradeRecord, DrawdownSnapshot
from app.backtest.enums import PositionSide, TradeStatus
from datetime import datetime


def test_performance_calculation():
    trades = [
        TradeRecord(
            trade_id="1",
            symbol="BTC",
            side=PositionSide.LONG,
            entry_timestamp=datetime.now(),
            entry_price=100,
            exit_price=110,
            quantity=1,
            status=TradeStatus.CLOSED,
            realized_pnl=10.0,
        ),
        TradeRecord(
            trade_id="2",
            symbol="BTC",
            side=PositionSide.SHORT,
            entry_timestamp=datetime.now(),
            entry_price=100,
            exit_price=105,
            quantity=1,
            status=TradeStatus.CLOSED,
            realized_pnl=-5.0,
        ),
    ]

    dd = DrawdownSnapshot(max_drawdown_pct=5.0)

    summary = PerformanceCalculator.calculate(
        run_id="test",
        initial_capital=1000.0,
        trades=trades,
        final_equity=1005.0,
        drawdown_summary=dd,
        total_bars=10,
    )

    assert summary.total_trades == 2
    assert summary.winning_trades == 1
    assert summary.losing_trades == 1
    assert summary.hit_rate == 50.0
    assert summary.total_return_pct == 0.5
    assert summary.profit_factor == 2.0
