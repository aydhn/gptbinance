from typing import List, Dict


class FeatureLineageTracker:
    def __init__(self):
        self._lineage: Dict[str, List[str]] = {}

    def record_dependency(self, feature_id: str, depends_on: str):
        if feature_id not in self._lineage:
            self._lineage[feature_id] = []
        self._lineage[feature_id].append(depends_on)

    def get_lineage(self, feature_id: str) -> List[str]:
        return self._lineage.get(feature_id, [])
