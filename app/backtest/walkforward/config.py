from app.backtest.walkforward.models import WalkForwardConfig
from app.backtest.walkforward.exceptions import InvalidWalkForwardConfigError


def validate_walkforward_config(config: WalkForwardConfig) -> WalkForwardConfig:
    if config.start_ts >= config.end_ts:
        raise InvalidWalkForwardConfigError("start_ts must be before end_ts")

    if config.is_bars <= 0:
        raise InvalidWalkForwardConfigError("is_bars must be > 0")

    if config.oos_bars <= 0:
        raise InvalidWalkForwardConfigError("oos_bars must be > 0")

    if config.step_bars <= 0:
        raise InvalidWalkForwardConfigError("step_bars must be > 0")

    # Minimum requirements for a meaningful test
    if config.is_bars < 50:
        raise InvalidWalkForwardConfigError("is_bars too small, minimum 50 recommended")

    return config
