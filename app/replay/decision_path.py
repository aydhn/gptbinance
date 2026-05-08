from typing import Dict, Any, List
from app.performance_plane.models import PerformanceManifest, AttributionTree


class ReplayDecisionPath:
    @staticmethod
    def extract_path(
        replay_id: str,
        start_time: str,
        end_time: str,
        manifest: PerformanceManifest = None,
        attribution: AttributionTree = None,
    ) -> dict:
        path = {"replay_id": replay_id, "start": start_time, "end": end_time}
        if manifest:
            path["performance_manifest_id"] = manifest.manifest_id
        if attribution:
            path["attribution_tree_id"] = attribution.tree_id

        return path
