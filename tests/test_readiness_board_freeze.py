import pytest
from app.readiness_board.storage import ReadinessBoardStorage
from app.readiness_board.candidates import CandidateRegistry
from app.readiness_board.freeze import FreezeEngine
from app.readiness_board.models import CandidateScope
from app.readiness_board.enums import CandidateClass
from app.readiness_board.exceptions import FreezeError


def test_freeze_candidate():
    storage = ReadinessBoardStorage()
    registry = CandidateRegistry(storage)
    freeze = FreezeEngine(storage)

    cand = registry.register_candidate(CandidateClass.PAPER_SHADOW, CandidateScope())
    snap = freeze.freeze_candidate(cand.candidate_id, artifacts={"policy": "v1"})

    assert snap.snapshot_id.startswith("snap_")
    assert snap.is_valid is True

    freeze.invalidate_snapshot(snap.snapshot_id)
    assert storage.get_snapshot(snap.snapshot_id).is_valid is False

    with pytest.raises(FreezeError):
        freeze.get_latest_valid_snapshot(cand.candidate_id)
