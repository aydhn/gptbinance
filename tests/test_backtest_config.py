import pytest
from datetime import datetime
from app.backtest.config import validate_backtest_config
from app.backtest.exceptions import InvalidBacktestConfigError


def test_valid_config():
    config = validate_backtest_config(
        {
            "symbol": "BTCUSDT",
            "interval": "15m",
            "start_time": datetime(2023, 1, 1),
            "end_time": datetime(2023, 1, 2),
        }
    )
    assert config.symbol == "BTCUSDT"


def test_invalid_time_range():
    with pytest.raises(InvalidBacktestConfigError):
        validate_backtest_config(
            {
                "symbol": "BTCUSDT",
                "interval": "15m",
                "start_time": datetime(2023, 1, 2),
                "end_time": datetime(2023, 1, 1),
            }
        )


def test_invalid_capital():
    with pytest.raises(InvalidBacktestConfigError):
        validate_backtest_config(
            {
                "symbol": "BTCUSDT",
                "interval": "15m",
                "start_time": datetime(2023, 1, 1),
                "end_time": datetime(2023, 1, 2),
                "initial_capital": 0,
            }
        )
