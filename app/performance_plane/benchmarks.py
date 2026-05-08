from typing import Dict, Optional, List
from app.performance_plane.models import BenchmarkDefinition
from app.performance_plane.enums import BenchmarkClass


class CanonicalBenchmarkRegistry:
    def __init__(self):
        self._registry: Dict[str, BenchmarkDefinition] = {}

    def register(self, definition: BenchmarkDefinition) -> None:
        self._registry[definition.benchmark_id] = definition

    def get(self, benchmark_id: str) -> Optional[BenchmarkDefinition]:
        return self._registry.get(benchmark_id)

    def list_all(self) -> List[BenchmarkDefinition]:
        return list(self._registry.values())


global_benchmark_registry = CanonicalBenchmarkRegistry()

# Standard Benchmark Families
global_benchmark_registry.register(
    BenchmarkDefinition(
        benchmark_id="cash_baseline_usd",
        benchmark_class=BenchmarkClass.CASH_BASELINE,
        description="Holding USD cash with 0% return.",
        comparability_requirements=["base_currency_usd"],
        freshness_ttl_seconds=86400,
    )
)
