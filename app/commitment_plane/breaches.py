from app.commitment_plane.models import BreachRecord
from app.commitment_plane.enums import BreachClass

class BreachManager:
    @staticmethod
    def create_breach(breach_class: BreachClass, description: str, proof_notes: str = None) -> BreachRecord:
        return BreachRecord(
            breach_class=breach_class,
            description=description,
            proof_notes=proof_notes,
            lineage_refs=[]
        )
