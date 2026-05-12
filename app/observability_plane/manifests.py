from typing import Dict, List, Optional
from .models import ObservabilityArtifactManifest

class ManifestBuilder:
    def __init__(self):
        self._manifests: Dict[str, ObservabilityArtifactManifest] = {}

    def register_manifest(self, manifest: ObservabilityArtifactManifest) -> None:
        self._manifests[manifest.manifest_id] = manifest

    def get_manifest(self, manifest_id: str) -> Optional[ObservabilityArtifactManifest]:
        return self._manifests.get(manifest_id)

    def list_manifests(self) -> List[ObservabilityArtifactManifest]:
        return list(self._manifests.values())
