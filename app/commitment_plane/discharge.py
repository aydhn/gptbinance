from app.commitment_plane.models import DischargeRecord
from app.commitment_plane.enums import DischargeClass

class DischargeManager:
    @staticmethod
    def create_discharge(discharge_class: DischargeClass, description: str, proof_notes: str = None) -> DischargeRecord:
        return DischargeRecord(
            discharge_class=discharge_class,
            description=description,
            proof_notes=proof_notes,
            lineage_refs=[]
        )
