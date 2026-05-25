from app.settlement_plane.models import BreachOfSettlementRecord

def evaluate_breach(breach: BreachOfSettlementRecord):
    if breach.breach_type == "material":
        return {"status": "material_breach", "breach_id": breach.id, "warning": "Material breach detected"}
    return {"status": "technical_breach", "breach_id": breach.id}
