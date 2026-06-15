from app.indemnity_plane.models import IllusoryIndemnityRecord
def evaluate_illusory(indemnity_id: str, has_illusory_risk: bool) -> IllusoryIndemnityRecord:
    return IllusoryIndemnityRecord(indemnity_id=indemnity_id, has_illusory_risk=has_illusory_risk)
