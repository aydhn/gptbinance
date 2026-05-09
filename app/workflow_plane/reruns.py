from typing import Optional
import uuid
from app.workflow_plane.models import RerunRecord, WorkflowRun
from app.workflow_plane.enums import RunState, RerunClass
from app.workflow_plane.exceptions import InvalidRerunError
from app.workflow_plane.runs import RunManager

class RerunManager:
    def __init__(self, run_manager: RunManager):
        self.run_manager = run_manager
        self.records = []

    def execute_rerun(self, original_run_id: str, reason: str, approver: str) -> WorkflowRun:
        original = self.run_manager.get_run(original_run_id)
        if not original:
            raise InvalidRerunError("Original run not found")

        original.state = RunState.RERUN_SUPERSEDED

        new_run = self.run_manager.initiate_run(
            workflow_id=original.workflow_id,
            window=original.window,
            trigger=original.trigger_class,
            is_rerun=True
        )
        original.superseded_by = new_run.run_id

        record = RerunRecord(
            rerun_id=f"rrn-{uuid.uuid4().hex[:8]}",
            original_run_id=original.run_id,
            new_run_id=new_run.run_id,
            reason=reason,
            rerun_class=RerunClass.SAME_WINDOW_RERUN,
            same_window=True,
            approved_by=approver
        )
        self.records.append(record)
        return new_run
