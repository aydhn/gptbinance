from decimal import Decimal
import uuid
from typing import List

from app.performance_plane.models import OpportunitySurface
from app.performance_plane.enums import OpportunityClass


class OpportunitySurfaceBuilder:
    @staticmethod
    def build(
        opportunity_class: OpportunityClass,
        estimated_value: Decimal,
        currency: str,
        confidence_score: float,
        caveats: List[str] = None,
    ) -> OpportunitySurface:
        if caveats is None:
            caveats = []

        if confidence_score < 0.8:
            caveats.append("Low confidence opportunity, highly counterfactual.")

        return OpportunitySurface(
            surface_id=str(uuid.uuid4()),
            opportunity_class=opportunity_class,
            estimated_value=estimated_value,
            currency=currency,
            confidence_score=confidence_score,
            caveats=caveats,
        )
