from app.security_plane.models import SecurityArtifactManifest

class ManifestBuilder:
    def build(self, manifest_id: str) -> SecurityArtifactManifest:
        return SecurityArtifactManifest(manifest_id=manifest_id)
