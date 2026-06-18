from app.waterfall_plane.models import ProceedsPoolRecord
from app.waterfall_plane.enums import PoolClass

def register_pool(pool_id: str, pool_class: PoolClass, total_amount: float) -> ProceedsPoolRecord:
    return ProceedsPoolRecord(pool_id=pool_id, pool_class=pool_class, total_amount=total_amount)

# Added for Phase 163 Clearing Plane Integration
from app.clearing_plane.integration import integrate_with_clearing_plane

def evaluate_clearing_integration_hook():
    integration = integrate_with_clearing_plane("app/waterfall_plane/pools.py")
    return integration.evaluate_posture()
