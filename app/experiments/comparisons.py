from typing import Dict, Any, List
from app.performance_plane.models import PerformanceEquivalenceReport


class ExperimentComparisons:
    @staticmethod
    def compare_arms(
        experiment_id: str,
        baseline_manifest_id: str,
        candidate_manifest_id: str,
        equivalence_report: PerformanceEquivalenceReport,
    ) -> dict:
        return {
            "experiment_id": experiment_id,
            "baseline": baseline_manifest_id,
            "candidate": candidate_manifest_id,
            "equivalence_verdict": equivalence_report.verdict.value,
            "divergence_sources": equivalence_report.divergence_sources,
        }
