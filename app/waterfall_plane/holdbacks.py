from app.waterfall_plane.models import HoldbackRecord

def register_holdback(holdback_id: str, amount: float) -> HoldbackRecord:
    return HoldbackRecord(holdback_id=holdback_id, amount=amount)
