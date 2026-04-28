import logging
from typing import Dict, Any

from app.backtest.validation.models import AblationSpec, AblationResult
from app.backtest.validation.enums import AblationType
from app.backtest.models import BacktestConfig, PerformanceSummary as BacktestSummary
from app.backtest.engine import BacktestEngine
from app.backtest.validation.comparisons import MetricComparisonEvaluator

logger = logging.getLogger(__name__)

# Predefined ablation specs
ABLATION_SCENARIOS = {
    AblationType.NO_REGIME: AblationSpec(
        ablation_type=AblationType.NO_REGIME,
        description="Disables market regime filtering.",
        toggled_features={"use_regime_filter": False},
    ),
    AblationType.NO_VOLATILITY: AblationSpec(
        ablation_type=AblationType.NO_VOLATILITY,
        description="Disables volatility gating.",
        toggled_features={"use_volatility_filter": False},
    ),
    AblationType.NO_STRUCTURE: AblationSpec(
        ablation_type=AblationType.NO_STRUCTURE,
        description="Disables market structure confirmation.",
        toggled_features={"use_structure_confirmation": False},
    ),
}


class AblationRunner:
    """Runs strategy variants with specific features toggled off."""

    def run_spec(
        self,
        spec: AblationSpec,
        base_config: BacktestConfig,
        base_summary: BacktestSummary,
    ) -> AblationResult:
        logger.info(f"Running ablation: {spec.ablation_type.value}")

        ablation_config = base_config.copy(deep=True)

        # Inject toggles into strategy params

        for feature, state in spec.toggled_features.items():
            setattr(ablation_config, feature, state)

        # Run backtest
        engine = BacktestEngine(config=ablation_config)
        engine.run()
        summary = engine.get_summary()

        # Compare to base
        # Note: in comparison, strategy is the base, benchmark is the ablated version
        # to see if base is better than ablated. Wait, usually we want to see if
        # ablated is worse. We'll use the metric evaluator but adapt the models.
        # Since MetricComparisonEvaluator takes a BenchmarkResult, we'll construct a dummy one
        # or rewrite a generic compare. For simplicity, we just use the evaluator.

        from app.backtest.validation.models import (
            BenchmarkResult,
            BenchmarkSpec,
            BaselineStrategyDescriptor,
        )
        from app.backtest.validation.enums import BenchmarkType
        import uuid

        dummy_bench_spec = BenchmarkSpec(
            run_id=base_summary.run_id,
            benchmark_type=BenchmarkType.FLAT,  # dummy
            baseline_descriptor=BaselineStrategyDescriptor(
                name=f"Ablated: {spec.ablation_type.value}",
                benchmark_type=BenchmarkType.FLAT,
                description="",
            ),
        )
        dummy_bench_res = BenchmarkResult(spec=dummy_bench_spec, summary=summary)

        evaluator = MetricComparisonEvaluator()
        comp_res = evaluator.compare(base_summary, dummy_bench_res)

        return AblationResult(spec=spec, summary=summary, comparison_to_base=comp_res)
