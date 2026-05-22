from typing import Dict, List
from app.finality_plane.models import FinalityObject, ClosureRecord, FinalityTrustVerdict, FinalityManifest

class FinalityStorage:
    def __init__(self):
        self.objects: Dict[str, FinalityObject] = {}
        self.closures: Dict[str, List[ClosureRecord]] = {}
        self.manifests: Dict[str, FinalityManifest] = {}

    def save_object(self, obj: FinalityObject):
        self.objects[obj.finality_id] = obj

    def get_object(self, finality_id: str) -> FinalityObject:
        return self.objects.get(finality_id)

    def save_manifest(self, manifest: FinalityManifest):
        self.manifests[manifest.finality_id] = manifest

storage = FinalityStorage()
