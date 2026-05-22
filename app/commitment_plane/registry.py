from typing import Dict, List, Optional
from app.commitment_plane.models import CommitmentObject
from app.commitment_plane.exceptions import InvalidCommitmentObjectError
from app.commitment_plane.base import CommitmentRegistryBase

class CanonicalCommitmentRegistry(CommitmentRegistryBase):
    def __init__(self):
        self._commitments: Dict[str, CommitmentObject] = {}

    def register_commitment(self, commitment: CommitmentObject) -> str:
        if not commitment.commitment_id:
            raise InvalidCommitmentObjectError("Commitment ID is required")
        if not commitment.owners:
            raise InvalidCommitmentObjectError("Commitment must have at least one owner")

        self._commitments[commitment.commitment_id] = commitment
        return commitment.commitment_id

    def get_commitment(self, commitment_id: str) -> Optional[CommitmentObject]:
        return self._commitments.get(commitment_id)

    def list_commitments(self, family: Optional[str] = None) -> List[CommitmentObject]:
        # Filter by family/scope if needed
        if family:
            return [c for c in self._commitments.values() if family in c.scope]
        return list(self._commitments.values())

# Global registry instance
commitment_registry = CanonicalCommitmentRegistry()
