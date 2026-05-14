from app.cost_plane.models import CostArtifactManifest
import uuid

class ManifestBuilder:
    def build_manifest(self, cost_refs: list[str], budget_refs: list[str], allocation_refs: list[str], variance_refs: list[str]) -> CostArtifactManifest:
        return CostArtifactManifest(
            manifest_id=str(uuid.uuid4()),
            cost_refs=cost_refs,
            budget_refs=budget_refs,
            allocation_refs=allocation_refs,
            variance_refs=variance_refs
        )
