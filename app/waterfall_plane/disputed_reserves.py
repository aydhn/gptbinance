from app.waterfall_plane.models import DisputedClaimReserveRecord

def register_disputed_reserve(reserve_id: str, claim_id: str, amount: float) -> DisputedClaimReserveRecord:
    return DisputedClaimReserveRecord(reserve_id=reserve_id, claim_id=claim_id, amount=amount)
