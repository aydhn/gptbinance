from app.workflow_plane.models import WorkflowArtifactManifest
import uuid

class ManifestBuilder:
    def build_manifest(self, workflow_id: str, run_id: str, artifacts: list[str]) -> WorkflowArtifactManifest:
        return WorkflowArtifactManifest(
            manifest_id=f"man-{uuid.uuid4().hex[:8]}",
            workflow_id=workflow_id,
            run_id=run_id,
            artifacts=artifacts
        )
