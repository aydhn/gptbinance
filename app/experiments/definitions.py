from typing import Dict, Any, List
from app.performance_plane.models import BenchmarkRef, PerformanceManifest


class ExperimentDefinitions:
    @staticmethod
    def define_experiment(
        experiment_id: str, arms: List[Dict[str, Any]], benchmark_ref: BenchmarkRef
    ) -> dict:
        return {
            "experiment_id": experiment_id,
            "arms": arms,
            "benchmark": benchmark_ref.dict(),
        }
