import pytest
import tempfile
import os
from app.backtest.walkforward.storage import WalkForwardStorage
from app.backtest.walkforward.models import (
    WalkForwardRun,
    WalkForwardConfig,
    WalkForwardPlan,
    WalkForwardAggregateResult,
    PromotionGateResult,
)
from app.backtest.walkforward.enums import WindowScheme, AggregateVerdict


def test_storage():
    with tempfile.TemporaryDirectory() as tmp:
        storage = WalkForwardStorage(base_dir=tmp)

        config = WalkForwardConfig(
            symbol="BTCUSDT",
            interval="1h",
            start_ts=0,
            end_ts=1000,
            feature_set="core",
            strategy_set="core",
            window_scheme=WindowScheme.ROLLING,
            is_bars=50,
            oos_bars=20,
            step_bars=20,
        )
        plan = WalkForwardPlan(config=config, windows=[])
        agg = WalkForwardAggregateResult(
            total_segments=0,
            completed_segments=0,
            total_oos_trades=0,
            aggregate_oos_return=0,
            aggregate_oos_expectancy=0,
            aggregate_oos_max_drawdown=0,
            segment_summaries=[],
        )
        gates = PromotionGateResult(
            verdict=AggregateVerdict.PASS, checks=[], summary="ok"
        )

        run = WalkForwardRun(
            run_id="test-run",
            config=config,
            plan=plan,
            segments=[],
            aggregate=agg,
            gates=gates,
            created_at="2023-01-01T00:00:00Z",
        )

        storage.save_run(run)

        loaded = storage.load_run("test-run")
        assert loaded is not None
        assert loaded.run_id == "test-run"
