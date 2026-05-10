from datetime import timezone
from typing import Dict, List, Optional
from datetime import datetime
from app.release_plane.models import ReleaseCandidate, ReleaseCandidateRef
from app.release_plane.exceptions import ReleasePlaneError

class ReleaseCandidateRegistry:
    def __init__(self):
        self._candidates: Dict[str, ReleaseCandidate] = {}
        self._pending_approvals: Dict[str, List[str]] = {}

    def register(self, candidate: ReleaseCandidate) -> None:
        if candidate.candidate_id in self._candidates:
            raise ReleasePlaneError(f"Candidate {candidate.candidate_id} already exists.")

        self._candidates[candidate.candidate_id] = candidate
        self._pending_approvals[candidate.candidate_id] = []

    def get(self, candidate_id: str) -> Optional[ReleaseCandidate]:
        candidate = self._candidates.get(candidate_id)
        if candidate and candidate.expiry and candidate.expiry < datetime.now(timezone.utc):
            # Handle expiry explicitly
            pass
        return candidate

    def get_all(self) -> List[ReleaseCandidate]:
        return list(self._candidates.values())

    def add_approval(self, candidate_id: str, approver: str) -> None:
        if candidate_id not in self._candidates:
            raise ReleasePlaneError("Candidate not found")
        self._pending_approvals[candidate_id].append(approver)

    def is_approved(self, candidate_id: str, required_approvers: int = 1) -> bool:
        if candidate_id not in self._pending_approvals:
            return False
        return len(self._pending_approvals[candidate_id]) >= required_approvers

candidate_registry = ReleaseCandidateRegistry()
