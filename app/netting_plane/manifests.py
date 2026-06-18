from typing import Dict, Any
from .models import NettingArtifactManifest

class ManifestBuilder:
    def __init__(self):
        self.manifests: Dict[str, NettingArtifactManifest] = {}

    def build_manifest(self, data: Dict[str, Any]) -> NettingArtifactManifest:
        manifest = NettingArtifactManifest(**data)
        self.manifests[manifest.manifest_id] = manifest
        return manifest
