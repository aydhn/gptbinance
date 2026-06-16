from app.waterfall_plane.models import PoolSourceRecord

def register_pool_source(source_id: str, source_type: str) -> PoolSourceRecord:
    return PoolSourceRecord(source_id=source_id, source_type=source_type)
