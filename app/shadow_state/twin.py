from datetime import datetime, timezone
import uuid
from app.shadow_state.models import ShadowTwinSnapshot
from app.shadow_state.venue import venue_truth_adapter
from app.shadow_state.local import local_truth_adapter


class TwinAssembler:
    """Assembles the digital twin snapshot by querying venue and local truth."""

    def assemble_twin(self, profile_id: str, workspace_id: str) -> ShadowTwinSnapshot:
        venue_snap = venue_truth_adapter.fetch_snapshot(profile_id, workspace_id)
        local_snap = local_truth_adapter.fetch_snapshot(profile_id, workspace_id)

        return ShadowTwinSnapshot(
            twin_id=f"twin_{uuid.uuid4().hex[:8]}",
            venue_truth=venue_snap,
            local_derived=local_snap,
            assembled_at=datetime.now(timezone.utc),
        )


twin_assembler = TwinAssembler()
