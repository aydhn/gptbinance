from app.cost_plane.models import SharedCostPool
import uuid

class SharedCostManager:
    def __init__(self):
        self._pools: list[SharedCostPool] = []

    def create_pool(self, name: str, total_amount: float, currency: str, allocation_policy_id: str, subsidy_warnings: list[str] = None) -> SharedCostPool:
        pool = SharedCostPool(
            pool_id=str(uuid.uuid4()),
            name=name,
            total_amount=total_amount,
            currency=currency,
            allocation_policy_id=allocation_policy_id,
            subsidy_warnings=subsidy_warnings or []
        )
        self._pools.append(pool)
        return pool

    def list_pools(self) -> list[SharedCostPool]:
        return self._pools
