from app.compliance_plane.models import ComplianceArtifactManifest
from typing import Dict, List


class ManifestManager:
    def __init__(self):
        self._manifests: Dict[str, ComplianceArtifactManifest] = {}

    def register_manifest(self, manifest: ComplianceArtifactManifest) -> None:
        self._manifests[manifest.manifest_id] = manifest

    def list_manifests(self) -> List[ComplianceArtifactManifest]:
        return list(self._manifests.values())
