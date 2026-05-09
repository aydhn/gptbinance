from app.workflow_plane.models import ResumeRecord
import uuid

class ResumeManager:
    def __init__(self):
        self.records = []

    def resume_run(self, run_id: str, checkpoint_ref: str, reason: str) -> ResumeRecord:
        record = ResumeRecord(
            resume_id=f"res-{uuid.uuid4().hex[:8]}",
            run_id=run_id,
            checkpoint_ref=checkpoint_ref,
            reason=reason
        )
        self.records.append(record)
        return record
