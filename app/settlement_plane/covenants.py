from app.settlement_plane.models import CovenantRecord

def evaluate_covenant(covenant: CovenantRecord):
    if covenant.is_defective:
        return {"status": "defective", "covenant_id": covenant.id, "warning": "Covenant is marked defective"}
    return {"status": "valid", "covenant_id": covenant.id, "type": covenant.covenant_type}
