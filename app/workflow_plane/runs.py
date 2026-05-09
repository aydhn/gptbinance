from typing import Dict, List, Optional
from datetime import datetime, timezone
import uuid
from app.workflow_plane.models import WorkflowRun, RunWindow
from app.workflow_plane.enums import RunState, TriggerClass
from app.workflow_plane.exceptions import DuplicateRunError

class RunManager:
    def __init__(self):
        self._runs: Dict[str, WorkflowRun] = {}
        self._window_index: Dict[str, Dict[str, str]] = {}

    def initiate_run(self, workflow_id: str, window: RunWindow, trigger: TriggerClass, is_rerun: bool = False) -> WorkflowRun:
        if workflow_id not in self._window_index:
            self._window_index[workflow_id] = {}

        existing_run_id = self._window_index[workflow_id].get(window.window_id)
        if existing_run_id and not is_rerun:
            existing_run = self._runs[existing_run_id]
            if existing_run.state not in [RunState.FAILED, RunState.CANCELLED, RunState.RERUN_SUPERSEDED]:
                raise DuplicateRunError(f"Duplicate run attempted for {workflow_id} in window {window.window_id}. Use explicit rerun.")

        run_id = f"run-{uuid.uuid4().hex[:8]}"
        run = WorkflowRun(
            run_id=run_id,
            workflow_id=workflow_id,
            window=window,
            trigger_class=trigger,
            state=RunState.QUEUED,
            started_at=datetime.now(timezone.utc)
        )
        self._runs[run_id] = run
        self._window_index[workflow_id][window.window_id] = run_id
        return run

    def get_run(self, run_id: str) -> Optional[WorkflowRun]:
        return self._runs.get(run_id)

    def get_all_runs(self) -> List[WorkflowRun]:
        return list(self._runs.values())
