from datetime import datetime
from app.backtest.models import BacktestConfig
from app.backtest.enums import BacktestMode


def test_backtest_config():
    config = BacktestConfig(
        symbol="BTCUSDT",
        interval="15m",
        start_time=datetime(2023, 1, 1),
        end_time=datetime(2023, 1, 2),
    )
    assert config.symbol == "BTCUSDT"
    assert config.mode == BacktestMode.STANDARD
