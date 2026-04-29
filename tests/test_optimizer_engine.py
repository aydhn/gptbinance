import pytest
from unittest.mock import MagicMock, patch
from app.optimizer.engine import OptimizerEngine
from app.optimizer.models import OptimizerConfig, SearchSpace, ParameterSpec
from app.optimizer.enums import SearchMode, ParameterType, OptimizerStatus


@patch("app.optimizer.engine.TrialRunner")
def test_optimizer_engine(mock_trial_runner_class):
    mock_runner = MagicMock()

    # Mock run_trial to return a dummy TrialResult
    mock_trial_result = MagicMock()
    mock_trial_result.error_message = None
    mock_trial_result.objective.total_score = 100.0
    mock_trial_result.metrics.expectancy = 1.0
    mock_trial_result.metrics.benchmark_relative_strength = 0.0
    mock_trial_result.metrics.max_drawdown_pct = 10.0
    mock_trial_result.metrics.total_trades = 50
    mock_trial_result.guard_report.pruning_verdict.value = "keep"

    mock_runner.run_trial.return_value = mock_trial_result
    mock_trial_runner_class.return_value = mock_runner

    config = OptimizerConfig(
        symbol="BTCUSDT",
        interval="1h",
        start_ts=0,
        end_ts=1000,
        feature_set="f1",
        strategy_family="s1",
        space_name="space1",
        max_trials=2,
    )
    space = SearchSpace(
        name="space1",
        strategy_family="s1",
        parameters=[
            ParameterSpec(
                name="p1",
                param_type=ParameterType.INT,
                bounds=[1, 2],
                step=1,
                default_value=1,
            )
        ],
    )

    engine = OptimizerEngine(config, space)
    run_result = engine.run()

    assert run_result.status == OptimizerStatus.COMPLETED
    assert len(run_result.trials) == 2
    assert run_result.summary.total_trials == 2
    assert run_result.summary.successful_trials == 2

    assert mock_runner.run_trial.call_count == 2
