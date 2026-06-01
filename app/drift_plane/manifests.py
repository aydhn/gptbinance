from app.drift_plane.models import DriftArtifactManifest

class ManifestBuilder:
    def build_manifest(self, manifest_id: str) -> DriftArtifactManifest:
        return DriftArtifactManifest(
            manifest_id=manifest_id
        )
