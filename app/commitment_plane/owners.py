from app.commitment_plane.models import OwnerRecord
from app.commitment_plane.enums import OwnerClass

class OwnerManager:
    @staticmethod
    def create_owner(owner_id: str, owner_class: OwnerClass, clarity_notes: str = None) -> OwnerRecord:
        if not owner_id:
            raise ValueError("Owner ID cannot be empty")
        return OwnerRecord(
            owner_id=owner_id,
            owner_class=owner_class,
            clarity_notes=clarity_notes,
            lineage_refs=[]
        )
