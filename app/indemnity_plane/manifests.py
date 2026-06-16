from app.indemnity_plane.models import IndemnityArtifactManifest
def build_manifest(manifest_id: str) -> IndemnityArtifactManifest:
    return IndemnityArtifactManifest(manifest_id=manifest_id)
