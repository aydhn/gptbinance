from decimal import Decimal
import uuid

from app.performance_plane.models import (
    BenchmarkDefinition,
    ReturnSurface,
    BenchmarkRelativeReport,
    BenchmarkRef,
)


class BaselineEvaluator:
    @staticmethod
    def evaluate(
        return_surface: ReturnSurface,
        benchmark: BenchmarkDefinition,
        benchmark_value: Decimal,
    ) -> BenchmarkRelativeReport:
        mismatch_cautions = []

        # Simple alignment checks
        if (
            "base_currency_usd" in benchmark.comparability_requirements
            and return_surface.currency != "USD"
        ):
            mismatch_cautions.append(
                "Currency mismatch between return surface and benchmark."
            )

        relative_value = return_surface.value - benchmark_value

        return BenchmarkRelativeReport(
            report_id=str(uuid.uuid4()),
            surface_id=return_surface.surface_id,
            benchmark_ref=BenchmarkRef(
                benchmark_id=benchmark.benchmark_id, version="latest"
            ),
            relative_value=relative_value,
            mismatch_cautions=mismatch_cautions,
        )
