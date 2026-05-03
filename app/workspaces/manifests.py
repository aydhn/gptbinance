from datetime import datetime, timezone
from app.workspaces.models import WorkspaceManifest, WorkspaceConfig, WorkspaceProfile
from typing import List

class ManifestGenerator:
    def generate_manifest(self, workspace: WorkspaceConfig, profiles: List[WorkspaceProfile]) -> WorkspaceManifest:
        # In a real system, this would gather more complex refs.
        return WorkspaceManifest(
            workspace_id=workspace.workspace_id,
            profile_ids=[p.profile_id for p in profiles],
            release_refs=[workspace.default_release_line],
            security_posture_refs=["standard_posture"], # placeholder
            data_governance_refs=["v1_governance"], # placeholder
            qualification_refs=[],
            last_active_bundle_refs=[],
            generated_at=datetime.now(timezone.utc)
        )
