from app.cost_plane.models import CostObject
from app.cost_plane.enums import CostClass

class CostObjectManager:
    @staticmethod
    def create_direct_cost(cost_id: str, owner: str, scope: str, attribution_semantics: str, measurement_window: str, family: str) -> CostObject:
        return CostObject(
            cost_id=cost_id,
            class_type=CostClass.FIXED,
            owner=owner,
            scope=scope,
            attribution_semantics=attribution_semantics,
            measurement_window=measurement_window,
            metadata={"family": family, "type": "direct"}
        )

    @staticmethod
    def create_shared_cost(cost_id: str, owner: str, scope: str, attribution_semantics: str, measurement_window: str, family: str) -> CostObject:
        return CostObject(
            cost_id=cost_id,
            class_type=CostClass.FIXED,
            owner=owner,
            scope=scope,
            attribution_semantics=attribution_semantics,
            measurement_window=measurement_window,
            metadata={"family": family, "type": "shared"}
        )
