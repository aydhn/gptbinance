from datetime import datetime
from pydantic import ValidationError
from app.backtest.models import BacktestConfig
from app.backtest.exceptions import InvalidBacktestConfigError


def validate_backtest_config(config_dict: dict) -> BacktestConfig:
    try:
        config = BacktestConfig(**config_dict)
    except ValidationError as e:
        raise InvalidBacktestConfigError(f"Invalid config: {e}")

    if config.start_time >= config.end_time:
        raise InvalidBacktestConfigError("start_time must be before end_time")

    if config.initial_capital <= 0:
        raise InvalidBacktestConfigError("initial_capital must be > 0")

    if not config.allow_long and not config.allow_short:
        raise InvalidBacktestConfigError(
            "At least one of allow_long or allow_short must be True"
        )

    return config
