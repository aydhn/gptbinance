from app.release_plane.models import SupersessionRecord, ReleaseRef
from app.release_plane.exceptions import RolloutViolation
import uuid

class SupersessionManager:
    def __init__(self):
        self._records = {}

    def record_supersession(self, old_release_id: str, new_release_id: str, rollback_window_sec: int) -> SupersessionRecord:
        # Enforce no silent replacement
        if not old_release_id or not new_release_id:
             raise RolloutViolation("Supersession requires both old and new release IDs.")

        record = SupersessionRecord(
            supersession_id=f"sup-{uuid.uuid4().hex[:8]}",
            superseded_release=ReleaseRef(release_id=old_release_id),
            superseded_by=ReleaseRef(release_id=new_release_id),
            retained_rollback_window_seconds=rollback_window_sec,
            lineage_refs=[]
        )
        self._records[record.supersession_id] = record
        return record
