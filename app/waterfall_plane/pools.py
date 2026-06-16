from app.waterfall_plane.models import ProceedsPoolRecord
from app.waterfall_plane.enums import PoolClass

def register_pool(pool_id: str, pool_class: PoolClass, total_amount: float) -> ProceedsPoolRecord:
    return ProceedsPoolRecord(pool_id=pool_id, pool_class=pool_class, total_amount=total_amount)
