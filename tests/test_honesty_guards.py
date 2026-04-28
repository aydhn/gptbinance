import pytest
import uuid
from app.backtest.validation.honesty_guards import HonestyGuardEvaluator
from app.backtest.models import PerformanceSummary as BacktestSummary


def test_honesty_guards():
    evaluator = HonestyGuardEvaluator()
    summary = BacktestSummary(
        run_id=str(uuid.uuid4()),
        config_id=uuid.uuid4(),
        total_return_pct=20.0,
        max_drawdown_pct=10.0,
        total_trades=5,
        win_rate_pct=90.0,
        profit_factor=1.05,
    )
    report = evaluator.evaluate(summary)
    assert not report.passed_all
    assert len(report.warnings) > 0
