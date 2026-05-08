from decimal import Decimal
import uuid
from typing import List

from app.performance_plane.models import DragComponent
from app.performance_plane.enums import DragClass


class ComponentRegistry:
    @staticmethod
    def register_drag(
        drag_class: DragClass,
        impact_value: Decimal,
        currency: str,
        lineage_refs: List[str] = None,
    ) -> DragComponent:
        return DragComponent(
            component_id=str(uuid.uuid4()),
            drag_class=drag_class,
            impact_value=impact_value,
            currency=currency,
            lineage_refs=lineage_refs or [],
        )
