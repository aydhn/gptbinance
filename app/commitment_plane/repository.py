from app.commitment_plane.models import CommitmentObject
from app.commitment_plane.registry import commitment_registry

class CommitmentRepository:
    @staticmethod
    def write(commitment: CommitmentObject) -> str:
        return commitment_registry.register_commitment(commitment)

    @staticmethod
    def read(commitment_id: str) -> CommitmentObject:
        return commitment_registry.get_commitment(commitment_id)
