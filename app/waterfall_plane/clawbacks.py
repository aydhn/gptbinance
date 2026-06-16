from app.waterfall_plane.models import ClawbackRecord
from app.waterfall_plane.enums import ClawbackClass

def register_clawback(clawback_id: str, clawback_class: ClawbackClass, recovered_amount: float) -> ClawbackRecord:
    return ClawbackRecord(clawback_id=clawback_id, clawback_class=clawback_class, recovered_amount=recovered_amount)
