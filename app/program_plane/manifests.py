from app.program_plane.models import ProgramArtifactManifest

class ProgramManifestBuilder:
    def build(self, program_id: str) -> ProgramArtifactManifest:
        return ProgramArtifactManifest(
            manifest_id=f"man_{program_id}",
            program_id=program_id,
            artifact_hash="hash123"
        )
