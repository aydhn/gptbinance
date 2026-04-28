from datetime import datetime, timedelta
from unittest.mock import MagicMock
from app.backtest.engine import BacktestEngine
from app.strategies.models import SignalBatch


def test_backtest_engine_run():
    config = {
        "symbol": "BTCUSDT",
        "interval": "15m",
        "start_time": datetime(2023, 1, 1),
        "end_time": datetime(2023, 1, 1, 1, 0),  # 1 hour = 4 bars
    }
    engine = BacktestEngine(config)

    # Mock the strategy engine so we don't depend on actual strategy logic
    engine.strategy_engine = MagicMock()
    empty_batch = SignalBatch(
        timestamp=datetime.now(),
        symbol="BTCUSDT",
        raw_signals=[],
        raw_entry_intents=[],
        raw_exit_intents=[],
    )
    engine.strategy_engine.evaluate.return_value = empty_batch

    result = engine.run_backtest()

    assert result.run.run_id is not None
    assert result.summary.initial_capital == 10000.0
