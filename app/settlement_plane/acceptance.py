from app.settlement_plane.models import AcceptanceRecord

def evaluate_acceptance(acceptance: AcceptanceRecord):
    if acceptance.defects:
        return {"status": "defective", "acceptance_id": acceptance.id, "defects": acceptance.defects}
    return {"status": "valid", "acceptance_id": acceptance.id}
