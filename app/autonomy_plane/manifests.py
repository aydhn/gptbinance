from app.autonomy_plane.models import AutonomyArtifactManifest
from typing import List

class ManifestBuilder:
    def build(self, manifest_id: str, artifacts: List[str]) -> AutonomyArtifactManifest:
        return AutonomyArtifactManifest(
            manifest_id=manifest_id,
            artifacts=artifacts
        )

manifest_builder = ManifestBuilder()
