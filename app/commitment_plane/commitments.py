from app.commitment_plane.models import CommitmentRecord, CommitmentObject
from typing import List

class CommitmentManager:
    @staticmethod
    def create_record(commitment: CommitmentObject, status: str = "active", notes: str = None) -> CommitmentRecord:
        if not commitment.commitment_id:
            raise ValueError("Commitment must have an ID")
        return CommitmentRecord(
            commitment=commitment,
            status=status,
            proof_notes=notes,
            lineage_refs=[]
        )
