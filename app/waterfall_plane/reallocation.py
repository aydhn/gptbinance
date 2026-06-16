from app.waterfall_plane.models import ReallocationRecord

def register_reallocation(reallocation_id: str, from_pool: str, to_pool: str, amount: float) -> ReallocationRecord:
    return ReallocationRecord(reallocation_id=reallocation_id, from_pool=from_pool, to_pool=to_pool, amount=amount)
