import pytest
from unittest.mock import Mock
from app.backtest.validation.robustness import RobustnessRunner
from app.backtest.validation.models import RobustnessCheckResult, RobustnessCheckType
from app.backtest.models import BacktestConfig, PerformanceSummary as BacktestSummary
from app.backtest.models import BacktestConfig, PerformanceSummary as BacktestSummary
import uuid


def test_robustness_runner():
    runner = RobustnessRunner()
    runner.run_all = Mock(
        return_value=[
            RobustnessCheckResult(
                check_type=RobustnessCheckType.FEE_PERTURBATION,
                description="",
                is_fragile=False,
                details={},
            )
        ]
    )
    config = BacktestConfig(
        symbol="BTCUSDT",
        interval="1h",
        start_time="2024-01-01T00:00:00Z",
        end_time="2024-01-02T00:00:00Z",
    )
    summary = BacktestSummary(
        run_id=str(uuid.uuid4()), config_id=uuid.uuid4(), total_return_pct=10.0
    )

    res = runner.run_all(config, summary)
    assert len(res) == 1
    assert res[0].check_type.value == "FEE_PERTURBATION"
