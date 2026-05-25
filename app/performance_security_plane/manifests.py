from app.performance_security_plane.models import SecurityArtifactManifest

class ManifestBuilder:
    def build_manifest(self, manifest_id: str, security_refs: list, data_hash: str) -> SecurityArtifactManifest:
        return SecurityArtifactManifest(
            manifest_id=manifest_id,
            security_refs=security_refs,
            hash=data_hash
        )
