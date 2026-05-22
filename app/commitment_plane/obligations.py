from app.commitment_plane.models import ObligationRecord
from app.commitment_plane.enums import ObligationClass

class ObligationManager:
    @staticmethod
    def create_obligation(obligation_class: ObligationClass, description: str, proof_notes: str = None) -> ObligationRecord:
        if not description:
            raise ValueError("Obligation description cannot be empty")
        return ObligationRecord(
            obligation_class=obligation_class,
            description=description,
            proof_notes=proof_notes,
            lineage_refs=[]
        )
