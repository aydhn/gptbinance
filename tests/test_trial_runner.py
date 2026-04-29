import pytest
from unittest.mock import MagicMock, patch
from app.optimizer.trial_runner import TrialRunner
from app.optimizer.models import (
    TrialConfig,
    ParameterCandidate,
    SearchSpace,
    ParameterSpec,
)
from app.optimizer.enums import ParameterType
from app.backtest.config import BacktestConfig
from app.strategies.specs import get_core_strategy_specs
from app.backtest.models import PerformanceSummary


@patch("app.optimizer.trial_runner.StrategyRegistry")
@patch("app.optimizer.trial_runner.BacktestEngine")
@patch("app.optimizer.trial_runner.BenchmarkRunner")
def test_trial_runner(mock_bm_runner, mock_bt_engine, mock_registry_class):
    # Mocking
    mock_engine_instance = MagicMock()

    summary = PerformanceSummary(
        run_id="12345678-1234-5678-1234-567812345678",
        start_time="2023-01-01T00:00:00Z",
        end_time="2023-01-02T00:00:00Z",
        total_trades=50,
        hit_rate=50.0,
        profit_factor=1.5,
        expectancy=1.0,
        total_return_pct=20.0,
        max_drawdown_pct=10.0,
        max_win=0.0,
    )

    mock_bt_result = MagicMock()
    mock_bt_result.summary = summary
    mock_bt_result.run_id = "12345678-1234-5678-1234-567812345678"

    mock_engine_instance.get_results.return_value = [mock_bt_result]
    mock_bt_engine.return_value = mock_engine_instance

    mock_bm_instance = MagicMock()
    mock_bm_result = MagicMock()
    mock_bm_result.run.config.strategy_set = "buy_and_hold"

    bm_summary = PerformanceSummary(
        run_id="12345678-1234-5678-1234-567812345678",
        start_time="2023-01-01T00:00:00Z",
        end_time="2023-01-02T00:00:00Z",
        total_trades=1,
        hit_rate=100.0,
        profit_factor=0.0,
        expectancy=10.0,
        total_return_pct=10.0,
        max_drawdown_pct=0.0,
        max_win=10.0,
    )
    mock_bm_result.summary = bm_summary
    mock_bm_instance.run_benchmarks.return_value = [mock_bm_result]
    mock_bm_runner.return_value = mock_bm_instance

    mock_registry = MagicMock()
    mock_registry.get_spec.return_value = get_core_strategy_specs()[0]
    mock_registry_class.return_value = mock_registry

    # Setup
    scorer = MagicMock()
    from app.optimizer.models import ObjectiveScore

    scorer.score.return_value = ObjectiveScore(
        total_score=100.0, component_scores={}, penalties={}, rationale=""
    )

    guard = MagicMock()
    from app.optimizer.models import OptimizationGuardReport, PruningVerdict

    guard_report = OptimizationGuardReport(
        trial_id="t1", warnings=[], passed_all=True, pruning_verdict=PruningVerdict.KEEP
    )
    guard.evaluate.return_value = guard_report

    runner = TrialRunner(scorer=scorer, guard_evaluator=guard)

    config = TrialConfig(
        trial_id="t1",
        run_id="r1",
        candidate=ParameterCandidate(
            candidate_id="c1", values={"trend_threshold": 0.5}
        ),
    )
    space = SearchSpace(
        name="test",
        strategy_family="trend_follow_core",
        parameters=[
            ParameterSpec(
                name="trend_threshold",
                param_type=ParameterType.FLOAT,
                default_value=0.0,
            )
        ],
    )
    bt_config = BacktestConfig(
        symbol="BTCUSDT",
        interval="1h",
        start_time="2023-01-01T00:00:00Z",
        end_time="2023-01-02T00:00:00Z",
        feature_set="core_trend_vol",
        strategy_set="trend_follow_core",
    )

    result = runner.run_trial(config, space, bt_config)

    assert result.error_message is None
    assert result.metrics is not None
    assert result.metrics.expectancy == 1.0
    assert result.metrics.benchmark_relative_strength == 1.0

    mock_engine_instance.run.assert_called_once()
    scorer.score.assert_called_once()
    guard.evaluate.assert_called_once()
