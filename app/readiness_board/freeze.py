import uuid
from typing import Dict
from app.readiness_board.models import CandidateFreezeSnapshot
from app.readiness_board.storage import ReadinessBoardStorage
from app.readiness_board.exceptions import FreezeError


class FreezeEngine:
    def __init__(self, storage: ReadinessBoardStorage):
        self.storage = storage

    def freeze_candidate(
        self, candidate_id: str, artifacts: Dict[str, str]
    ) -> CandidateFreezeSnapshot:
        candidate = self.storage.get_candidate(candidate_id)
        if not candidate:
            raise FreezeError(f"Candidate {candidate_id} not found")

        snapshot = CandidateFreezeSnapshot(
            snapshot_id=f"snap_{uuid.uuid4().hex[:8]}",
            candidate_id=candidate_id,
            artifacts=artifacts,
            is_valid=True,
        )
        self.storage.save_snapshot(snapshot)
        return snapshot

    def invalidate_snapshot(self, snapshot_id: str) -> None:
        snapshot = self.storage.get_snapshot(snapshot_id)
        if snapshot:
            snapshot.is_valid = False
            self.storage.save_snapshot(snapshot)

    def get_latest_valid_snapshot(self, candidate_id: str) -> CandidateFreezeSnapshot:
        snapshot = self.storage.get_latest_snapshot(candidate_id)
        if not snapshot or not snapshot.is_valid:
            raise FreezeError(
                f"No valid freeze snapshot found for candidate {candidate_id}"
            )
        return snapshot
