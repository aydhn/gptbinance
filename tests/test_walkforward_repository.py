import pytest
import tempfile
from app.backtest.walkforward.repository import WalkForwardRepository
from app.backtest.walkforward.storage import WalkForwardStorage
from app.backtest.walkforward.segment_runner import SegmentRunner
from app.backtest.walkforward.selection import CandidateSelector
from app.backtest.walkforward.freeze import FreezeManager
from app.backtest.walkforward.models import WalkForwardConfig
from app.backtest.walkforward.enums import WindowScheme
from app.strategies.models import StrategySpec
from app.strategies.enums import StrategyType

from tests.test_walkforward_segment_runner import _mock_run_backtest


def test_repository_run():
    with tempfile.TemporaryDirectory() as tmp:
        storage = WalkForwardStorage(base_dir=tmp)
        selector = CandidateSelector()
        freezer = FreezeManager()
        runner = SegmentRunner(selector, freezer, _mock_run_backtest)

        repo = WalkForwardRepository(storage, runner)

        config = WalkForwardConfig(
            symbol="BTCUSDT",
            interval="1h",
            start_ts=0,
            end_ts=1000000000,
            feature_set="core",
            strategy_set="core",
            window_scheme=WindowScheme.ROLLING,
            is_bars=50,
            oos_bars=20,
            step_bars=20,
        )
        specs = [
            StrategySpec(
                name="strat1",
                strategy_type=StrategyType.TREND_FOLLOW,
                required_features=[],
            )
        ]

        run = repo.run_workflow(config, specs)

        assert run is not None
        assert run.run_id is not None
        assert len(run.segments) > 0
        assert run.aggregate is not None

        loaded = repo.get_run(run.run_id)
        assert loaded.run_id == run.run_id
