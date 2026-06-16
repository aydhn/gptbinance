from app.waterfall_plane.models import ReserveRecord
from app.waterfall_plane.enums import ReserveClass

def register_reserve(reserve_id: str, reserve_class: ReserveClass, amount: float) -> ReserveRecord:
    return ReserveRecord(reserve_id=reserve_id, reserve_class=reserve_class, amount=amount)
