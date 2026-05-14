from app.cost_plane.models import CostObject
from app.cost_plane.base import CostRegistryBase
from app.cost_plane.exceptions import InvalidCostObjectError

class CanonicalCostRegistry(CostRegistryBase):
    def __init__(self):
        self._costs: dict[str, CostObject] = {}
        self._families = [
            "compute_spend", "gpu_spend", "storage_spend", "network_egress_spend",
            "vendor_api_spend", "exchange_fee_spend", "observability_spend",
            "continuity_standby_spend", "security_compliance_overhead",
            "model_inference_spend", "workflow_batch_spend", "release_activation_overhead"
        ]

    def register_cost(self, cost_object: CostObject) -> None:
        if not cost_object.cost_id:
            raise InvalidCostObjectError("Cost object must have an explicit cost_id.")
        if cost_object.metadata.get("family") not in self._families:
            raise InvalidCostObjectError(f"Cost object family must be one of {self._families}")

        self._costs[cost_object.cost_id] = cost_object

    def get_cost(self, cost_id: str) -> CostObject:
        if cost_id not in self._costs:
            raise InvalidCostObjectError(f"Cost object {cost_id} not found in registry. No undocumented cost ids allowed.")
        return self._costs[cost_id]

    def list_costs(self) -> list[CostObject]:
        return list(self._costs.values())
