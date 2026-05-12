from datetime import datetime
from typing import Dict, List, Optional

from .models import ReliabilityArtifactManifest


class ManifestManager:
    def __init__(self):
        self._manifests: Dict[str, ReliabilityArtifactManifest] = {}

    def record_manifest(self, manifest: ReliabilityArtifactManifest) -> None:
        self._manifests[manifest.manifest_id] = manifest

    def get_manifest(self, manifest_id: str) -> Optional[ReliabilityArtifactManifest]:
        return self._manifests.get(manifest_id)

    def list_manifests(self) -> List[ReliabilityArtifactManifest]:
        return list(self._manifests.values())
