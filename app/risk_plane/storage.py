
from typing import Dict
from .models import RiskArtifactManifest


class RiskStorage:
    def __init__(self):
        self._manifests: Dict[str, RiskArtifactManifest] = {}

    def store_manifest(self, manifest: RiskArtifactManifest):
        self._manifests[manifest.manifest_id] = manifest

    def get_manifest(self, manifest_id: str) -> RiskArtifactManifest:
        return self._manifests.get(manifest_id)


global_risk_storage = RiskStorage()
