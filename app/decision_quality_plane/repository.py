from typing import Dict, List
from app.decision_quality_plane.models import DecisionManifest
from app.decision_quality_plane.exceptions import DecisionStorageError

class DecisionRepository:
    def __init__(self):
        self._manifests: Dict[str, DecisionManifest] = {}

    def save(self, manifest: DecisionManifest):
        self._manifests[manifest.decision.decision_id] = manifest

    def get(self, decision_id: str) -> DecisionManifest:
        return self._manifests.get(decision_id)

    def list_all(self) -> List[DecisionManifest]:
        return list(self._manifests.values())
