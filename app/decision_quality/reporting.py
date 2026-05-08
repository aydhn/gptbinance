from typing import Dict, Any, List
from app.performance_plane.models import PerformanceManifest, AttributionTree


class DecisionQualityReporter:
    @staticmethod
    def generate_report(
        decision_id: str,
        context: Dict[str, Any],
        performance_manifest: PerformanceManifest = None,
        attribution_tree: AttributionTree = None,
    ) -> dict:
        report = {
            "decision_id": decision_id,
            "quality_score": 0.85,
        }
        if performance_manifest:
            report["performance_manifest_id"] = performance_manifest.manifest_id
        if attribution_tree:
            report["attribution_tree_id"] = attribution_tree.tree_id
            report["residual_unexplained"] = str(attribution_tree.residual_value)

        return report
