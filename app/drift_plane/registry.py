from app.drift_plane.base import DriftRegistryBase
from app.drift_plane.enums import DriftClass
from typing import List, Dict

class CanonicalDriftRegistry(DriftRegistryBase):
    def __init__(self):
        self.drifts: Dict[str, Dict] = {}

    def register_drift(self, drift_id: str, class_type: DriftClass, is_mandatory: bool = True):
        self.drifts[drift_id] = {
            "class_type": class_type,
            "mandatory": is_mandatory,
            "marker": "production-grade" if is_mandatory else "advisory"
        }

    def get_drift(self, drift_id: str):
        return self.drifts.get(drift_id)

    def list_drifts(self):
        return self.drifts
