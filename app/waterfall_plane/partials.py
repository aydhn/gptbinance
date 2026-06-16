from app.waterfall_plane.models import PartialSatisfactionRecord

def register_partial_satisfaction(satisfaction_id: str, claim_id: str, amount_satisfied: float, deficiency: float) -> PartialSatisfactionRecord:
    return PartialSatisfactionRecord(satisfaction_id=satisfaction_id, claim_id=claim_id, amount_satisfied=amount_satisfied, deficiency=deficiency)
