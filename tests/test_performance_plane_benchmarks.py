from app.performance_plane.models import BenchmarkDefinition
from app.performance_plane.enums import BenchmarkClass
from app.performance_plane.benchmarks import CanonicalBenchmarkRegistry


def test_benchmark_registry_integrity():
    registry = CanonicalBenchmarkRegistry()
    b1 = BenchmarkDefinition(
        benchmark_id="test_bench_1",
        benchmark_class=BenchmarkClass.NO_TRADE_BASELINE,
        description="No trade test.",
        comparability_requirements=["test_req"],
        freshness_ttl_seconds=3600,
    )
    registry.register(b1)

    assert registry.get("test_bench_1") is not None
    assert (
        registry.get("test_bench_1").benchmark_class == BenchmarkClass.NO_TRADE_BASELINE
    )
    assert len(registry.list_all()) == 1
