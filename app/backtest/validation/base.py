import abc
from uuid import UUID
from typing import Dict, Any

from app.backtest.validation.models import (
    BenchmarkResult,
    ComparisonResult,
    ValidationSummary,
    AblationResult,
    RobustnessCheckResult,
    ResearchHonestyReport,
)
from app.backtest.models import BacktestConfig, PerformanceSummary as BacktestSummary


class BenchmarkEvaluatorBase(abc.ABC):
    @abc.abstractmethod
    def run(
        self, base_config: BacktestConfig, base_summary: BacktestSummary
    ) -> BenchmarkResult:
        pass


class ComparisonEvaluatorBase(abc.ABC):
    @abc.abstractmethod
    def compare(
        self, strategy_summary: BacktestSummary, benchmark_result: BenchmarkResult
    ) -> ComparisonResult:
        pass


class ValidationStepBase(abc.ABC):
    @abc.abstractmethod
    def execute(self, context: Dict[str, Any]) -> Any:
        pass
