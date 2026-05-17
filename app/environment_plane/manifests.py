from app.environment_plane.models import EnvironmentArtifactManifest

def build_manifest(artifact_hash: str, lineage_refs: str) -> EnvironmentArtifactManifest:
    return EnvironmentArtifactManifest(artifact_hash=artifact_hash, lineage_refs=lineage_refs)
