from app.waterfall_plane.models import PoolAvailabilityRecord

def register_pool_availability(availability_id: str, status: str) -> PoolAvailabilityRecord:
    return PoolAvailabilityRecord(availability_id=availability_id, status=status)
