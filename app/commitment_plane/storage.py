from app.commitment_plane.models import CommitmentObject

class StorageManager:
    @staticmethod
    def save_commitment(commitment: CommitmentObject) -> bool:
        # Placeholder
        return True

    @staticmethod
    def load_commitment(commitment_id: str) -> CommitmentObject:
        from app.commitment_plane.registry import commitment_registry
        return commitment_registry.get_commitment(commitment_id)
