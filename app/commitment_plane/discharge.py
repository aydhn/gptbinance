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

# OBLIGATION PLANE INTEGRATION
def check_commitment_discharge(commitment_discharged: bool, mandatory_duty_unresolved: bool) -> str:
    # commitment discharged while mandatory duty unresolved explicit caution
    if commitment_discharged and mandatory_duty_unresolved:
        return "CAUTION: Commitment discharged while mandatory underlying duty remains unresolved."
    return "Commitment discharge validated."
