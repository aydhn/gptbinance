from app.waterfall_plane.models import DeficiencyCarryRecord

def register_deficiency_carry(deficiency_id: str, claim_id: str, carried_amount: float) -> DeficiencyCarryRecord:
    return DeficiencyCarryRecord(deficiency_id=deficiency_id, claim_id=claim_id, carried_amount=carried_amount)
