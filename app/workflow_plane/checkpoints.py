from typing import Dict, Any
from datetime import datetime, timezone
import uuid
from app.workflow_plane.models import RunCheckpoint

class CheckpointManager:
    def __init__(self):
        self.checkpoints: Dict[str, RunCheckpoint] = {}

    def create_checkpoint(self, run_id: str, job_id: str, payload_metadata: Dict[str, Any]) -> RunCheckpoint:
        chk = RunCheckpoint(
            checkpoint_id=f"chk-{uuid.uuid4().hex[:8]}",
            run_id=run_id,
            job_id=job_id,
            payload_metadata=payload_metadata,
            freshness=datetime.now(timezone.utc)
        )
        self.checkpoints[chk.checkpoint_id] = chk
        return chk
