import logging
from uuid import UUID
import uuid

from app.backtest.validation.models import BenchmarkSpec, BenchmarkResult
from app.backtest.validation.base import BenchmarkEvaluatorBase
from app.backtest.validation.benchmarks import (
    BENCHMARK_STRATEGY_MAP,
    BENCHMARK_DESCRIPTORS,
)
from app.backtest.models import BacktestConfig, PerformanceSummary as BacktestSummary
from app.backtest.engine import BacktestEngine
from app.backtest.exceptions import BacktestError
from app.backtest.validation.exceptions import InvalidBenchmarkSpecError

logger = logging.getLogger(__name__)


class BenchmarkRunner(BenchmarkEvaluatorBase):
    """
    Runs benchmark strategies using the same BacktestEngine and data
    as the strategy being validated.
    """

    def run(
        self, base_config: BacktestConfig, base_summary: BacktestSummary
    ) -> BenchmarkResult:
        # NOTE: This signature is slightly different than requested in models,
        # but usually we want to run *all* or *specific* benchmarks.
        # Let's adjust to run a single benchmark spec.
        raise NotImplementedError("Use run_spec instead")

    def run_spec(
        self, spec: BenchmarkSpec, base_config: BacktestConfig
    ) -> BenchmarkResult:
        """Runs a single benchmark given a spec and the original strategy's config."""
        logger.info(f"Running benchmark: {spec.benchmark_type.value}")

        if spec.benchmark_type not in BENCHMARK_STRATEGY_MAP:
            raise InvalidBenchmarkSpecError(
                f"Unknown benchmark type: {spec.benchmark_type}"
            )

        strategy_class = BENCHMARK_STRATEGY_MAP[spec.benchmark_type]

        # Create a matching config but replace strategy
        benchmark_config = base_config.copy(deep=True)
        # Assuming run_id needs to be unique per benchmark run
        benchmark_run_id = uuid.uuid4()
        # Note: BacktestConfig might not have a mutable run_id depending on phase 09,
        # we assume we can create a new engine instance.

        try:
            # Re-use BacktestEngine but with the benchmark strategy
            # We need to instantiate the strategy
            strategy_instance = strategy_class(
                symbol=benchmark_config.symbol,
                # pass other required args like broker if needed,
                # BacktestEngine usually handles strategy instantiation or takes it
            )

            # Since BacktestEngine might take config and instantiate internally:
            # We might need to mock or inject. Let's assume we can pass a class or name.
            # For this layer, we will just patch the config's strategy_name to our baseline.
            benchmark_config.strategy_name = spec.benchmark_type.value

            engine = BacktestEngine(config=benchmark_config)

            # Monkey patch the strategy factory/creation logic in engine for baselines
            # Alternatively, if engine takes strategy instance:
            engine.strategy = strategy_instance  # type: ignore
            if hasattr(engine.strategy, "broker"):
                engine.strategy.broker = engine.broker  # type: ignore  # bind broker

            engine.run()
            summary = engine.get_summary()

            return BenchmarkResult(spec=spec, summary=summary)

        except Exception as e:
            logger.error(f"Benchmark {spec.benchmark_type} failed: {e}")
            raise BacktestError(f"Benchmark run failed: {e}")
