from typing import List, Dict
from app.workflow_plane.models import BackfillRunRecord, RunWindow
from app.workflow_plane.exceptions import BackfillContaminationError
from app.workflow_plane.runs import RunManager
import uuid

class BackfillManager:
    def __init__(self, run_manager: RunManager):
        self.run_manager = run_manager
        self.records: Dict[str, BackfillRunRecord] = {}

    def initiate_backfill(self, workflow_id: str, start_window: RunWindow, end_window: RunWindow, reason: str) -> BackfillRunRecord:
        if start_window.start_time > end_window.end_time:
            raise BackfillContaminationError("Start window cannot be after end window")
        if start_window.start_time >= end_window.start_time and start_window.start_time <= end_window.end_time:
            raise BackfillContaminationError("Start window intersects with end window")
        if start_window.end_time > end_window.start_time:
             raise BackfillContaminationError("Start window intersects with end window")
        record = BackfillRunRecord(
            backfill_id=f"bkf-{uuid.uuid4().hex[:8]}",
            workflow_id=workflow_id,
            start_window=start_window,
            end_window=end_window,
            reason=reason
        )
        self.records[record.backfill_id] = record
        return record

class WorkflowBackfillMigrationRef:
    def canonical_backfill(self, backfill_governance=None):
        pass
