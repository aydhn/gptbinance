from app.commitment_plane.models import ReliefRecord
from app.commitment_plane.enums import ReliefClass

class ReliefManager:
    @staticmethod
    def create_relief(relief_class: ReliefClass, description: str, abuse_notes: str = None) -> ReliefRecord:
        return ReliefRecord(
            relief_class=relief_class,
            description=description,
            abuse_notes=abuse_notes,
            lineage_refs=[]
        )
