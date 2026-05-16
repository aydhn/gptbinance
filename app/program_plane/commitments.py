from app.program_plane.models import CommitmentWindow
from datetime import datetime, timezone

class CommitmentManager:
    def create_commitment(self, program_id: str) -> CommitmentWindow:
        now = datetime.now(timezone.utc)
        return CommitmentWindow(
            window_id=f"cw_{program_id}",
            program_id=program_id,
            target_by=now,
            must_land_by=now,
            is_rebaselined=False
        )
