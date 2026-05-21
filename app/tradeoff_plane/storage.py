from typing import Dict, List, Optional
from .models import TradeoffObject, TradeoffArtifactManifest, TradeoffTrustVerdict

class TradeoffStorage:
    def __init__(self):
        self._objects: Dict[str, TradeoffObject] = {}
        self._manifests: Dict[str, List[TradeoffArtifactManifest]] = {}
        self._verdicts: Dict[str, List[TradeoffTrustVerdict]] = {}

    def save_object(self, obj: TradeoffObject) -> None:
        self._objects[obj.tradeoff_id] = obj

    def get_object(self, tradeoff_id: str) -> Optional[TradeoffObject]:
        return self._objects.get(tradeoff_id)

    def save_manifest(self, manifest: TradeoffArtifactManifest) -> None:
        if manifest.tradeoff_id not in self._manifests:
            self._manifests[manifest.tradeoff_id] = []
        self._manifests[manifest.tradeoff_id].append(manifest)

    def save_verdict(self, verdict: TradeoffTrustVerdict) -> None:
        if verdict.tradeoff_id not in self._verdicts:
            self._verdicts[verdict.tradeoff_id] = []
        self._verdicts[verdict.tradeoff_id].append(verdict)

tradeoff_storage = TradeoffStorage()
