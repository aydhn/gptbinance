from app.workflow_plane.checkpoints import CheckpointManager
from datetime import datetime

def test_checkpoint_creation():
    mgr = CheckpointManager()
    chk = mgr.create_checkpoint("run-1", "job-1", {"status": "ok"})
    assert chk.run_id == "run-1"
    assert chk.payload_metadata["status"] == "ok"
    assert chk.downstream_compatible is True
