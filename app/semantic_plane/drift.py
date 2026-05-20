from typing import Dict, List
from app.semantic_plane.models import SemanticDriftRecord

class DriftManager:
    def __init__(self, registry):
        self.registry = registry
        self.drifts: Dict[str, SemanticDriftRecord] = {}

    def register_drift(self, drift: SemanticDriftRecord):
        self.drifts[drift.drift_id] = drift

    def get_critical_drifts(self) -> List[SemanticDriftRecord]:
        return [d for d in self.drifts.values() if d.severity.lower() == "critical"]
