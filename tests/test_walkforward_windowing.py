import pytest
from app.backtest.walkforward.models import WalkForwardConfig
from app.backtest.walkforward.enums import WindowScheme
from app.backtest.walkforward.windowing import WindowGenerator, _interval_to_ms
from app.backtest.walkforward.exceptions import InvalidWindowPlanError


def test_rolling_windows():
    generator = WindowGenerator()
    start_ts = 0
    interval = "1h"
    ms = _interval_to_ms(interval)
    end_ts = 100 * ms  # 100 bars total

    config = WalkForwardConfig(
        symbol="BTCUSDT",
        interval=interval,
        start_ts=start_ts,
        end_ts=end_ts,
        feature_set="core",
        strategy_set="core",
        window_scheme=WindowScheme.ROLLING,
        is_bars=50,
        oos_bars=20,
        step_bars=20,
    )

    plan = generator.generate(config)
    assert len(plan.windows) == 3

    # Win 1: IS(0-50), OOS(50-70)
    assert plan.windows[0].is_start == 0
    assert plan.windows[0].is_end == 50 * ms
    assert plan.windows[0].oos_start == 50 * ms
    assert plan.windows[0].oos_end == 70 * ms
    assert plan.windows[0].is_valid is True

    # Win 2: IS(20-70), OOS(70-90)
    assert plan.windows[1].is_start == 20 * ms
    assert plan.windows[1].is_end == 70 * ms
    assert plan.windows[1].oos_start == 70 * ms
    assert plan.windows[1].oos_end == 90 * ms
    assert plan.windows[1].is_valid is True

    # Win 3: IS(40-90), OOS(90-100) -> Truncated
    assert plan.windows[2].is_start == 40 * ms
    assert plan.windows[2].is_end == 90 * ms
    assert plan.windows[2].oos_start == 90 * ms
    assert plan.windows[2].oos_end == 100 * ms
    assert "truncated" in plan.windows[2].reason


def test_anchored_windows():
    generator = WindowGenerator()
    start_ts = 0
    interval = "1h"
    ms = _interval_to_ms(interval)
    end_ts = 100 * ms

    config = WalkForwardConfig(
        symbol="BTCUSDT",
        interval=interval,
        start_ts=start_ts,
        end_ts=end_ts,
        feature_set="core",
        strategy_set="core",
        window_scheme=WindowScheme.ANCHORED,
        is_bars=50,
        oos_bars=20,
        step_bars=20,
    )

    plan = generator.generate(config)
    assert len(plan.windows) == 3

    # Win 1: IS(0-50), OOS(50-70)
    assert plan.windows[0].is_start == 0
    assert plan.windows[0].is_end == 50 * ms

    # Win 2: IS(0-70), OOS(70-90)
    assert plan.windows[1].is_start == 0
    assert plan.windows[1].is_end == 70 * ms

    # Win 3: IS(0-90), OOS(90-100)
    assert plan.windows[2].is_start == 0
    assert plan.windows[2].is_end == 90 * ms


def test_insufficient_data():
    generator = WindowGenerator()
    start_ts = 0
    interval = "1h"
    ms = _interval_to_ms(interval)
    end_ts = 10 * ms  # Too short

    config = WalkForwardConfig(
        symbol="BTCUSDT",
        interval=interval,
        start_ts=start_ts,
        end_ts=end_ts,
        feature_set="core",
        strategy_set="core",
        window_scheme=WindowScheme.ROLLING,
        is_bars=50,
        oos_bars=20,
        step_bars=20,
    )

    with pytest.raises(InvalidWindowPlanError):
        generator.generate(config)
