from app.waterfall_plane.models import ContingentClaimReserveRecord

def register_contingent_reserve(reserve_id: str, claim_id: str, amount: float) -> ContingentClaimReserveRecord:
    return ContingentClaimReserveRecord(reserve_id=reserve_id, claim_id=claim_id, amount=amount)
