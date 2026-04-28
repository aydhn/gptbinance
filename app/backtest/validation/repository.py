import logging
from typing import List, Optional
from uuid import UUID

from app.backtest.validation.models import (
    ValidationSummary,
    ValidationSuiteConfig,
    BenchmarkSpec,
    ValidationArtifactManifest,
    ValidationStatus,
)
from app.backtest.validation.benchmarks import BENCHMARK_DESCRIPTORS
from app.backtest.validation.benchmark_runner import BenchmarkRunner
from app.backtest.validation.comparisons import MetricComparisonEvaluator
from app.backtest.validation.ablation import AblationRunner, ABLATION_SCENARIOS
from app.backtest.validation.robustness import RobustnessRunner
from app.backtest.validation.honesty_guards import HonestyGuardEvaluator
from app.backtest.validation.storage import ValidationStorage
from app.backtest.storage import BacktestStorage
from app.backtest.exceptions import BacktestError

logger = logging.getLogger(__name__)


class ValidationRepository:
    def __init__(
        self, backtest_storage: BacktestStorage, validation_storage: ValidationStorage
    ):
        self.b_storage = backtest_storage
        self.v_storage = validation_storage
        self.bench_runner = BenchmarkRunner()
        self.comp_evaluator = MetricComparisonEvaluator()
        self.ab_runner = AblationRunner()
        self.rob_runner = RobustnessRunner()
        self.honesty_evaluator = HonestyGuardEvaluator()

    def run_suite(
        self, strategy_run_id: UUID, config: ValidationSuiteConfig
    ) -> ValidationSummary:
        logger.info(f"Starting validation suite for run {strategy_run_id}")

        # Load base run
        base_record = self.b_storage.get_run_by_id(str(strategy_run_id))
        if not base_record:
            raise BacktestError(f"Base run {strategy_run_id} not found in storage.")

        base_summary = base_record.summary
        base_config = base_record.config

        bench_results = []
        comparisons = []
        ab_results = []
        rob_results = []

        # 1. Benchmarks
        for b_type in config.benchmark_types:
            spec = BenchmarkSpec(
                run_id=base_record.summary.run_id,
                benchmark_type=b_type,
                baseline_descriptor=BENCHMARK_DESCRIPTORS[b_type],
            )
            b_res = self.bench_runner.run_spec(spec, base_config)
            bench_results.append(b_res)

            # Comparison
            comp_res = self.comp_evaluator.compare(base_summary, b_res)
            comparisons.append(comp_res)

        # 2. Ablations
        for a_type in config.ablation_types:
            if a_type in ABLATION_SCENARIOS:
                a_res = self.ab_runner.run_spec(
                    ABLATION_SCENARIOS[a_type], base_config, base_summary
                )
                ab_results.append(a_res)

        # 3. Robustness
        if config.robustness_types:
            # Just run all for now
            rob_results = self.rob_runner.run_all(base_config, base_summary)

        # 4. Honesty
        honesty_report = None
        if config.enable_honesty_guards:
            honesty_report = self.honesty_evaluator.evaluate(base_summary)

        manifest = ValidationArtifactManifest(
            benchmark_run_ids=[b.spec.benchmark_id for b in bench_results],
            comparison_ids=[],  # Can generate UUIDs if stored separately
            ablation_run_ids=[],
            robustness_ids=[],
            honesty_report_id=None,
        )

        summary = ValidationSummary(
            strategy_run_id=strategy_run_id,
            status=ValidationStatus.COMPLETED,
            benchmarks=bench_results,
            comparisons=comparisons,
            ablations=ab_results,
            robustness_checks=rob_results,
            honesty_report=honesty_report,
            artifact_manifest=manifest,
        )

        self.v_storage.save_validation_summary(summary)
        return summary
