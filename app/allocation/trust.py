from app.allocation.models import AllocationIntent
from app.allocation.enums import IntentStatus
from app.performance_plane.models import AttributionNode
from app.performance_plane.enums import AttributionClass
from decimal import Decimal


class AllocationTrustEvaluator:
    @staticmethod
    def evaluate(intent: AllocationIntent) -> float:
        # Dummy evaluation logic
        return 0.95

    @staticmethod
    def export_attribution(
        intent: AllocationIntent, pnl_impact: Decimal, currency: str
    ) -> AttributionNode:
        return AttributionNode(
            attribution_class=AttributionClass.ALLOCATION_SIZING,
            contribution_value=pnl_impact,
            currency=currency,
            proof_notes=[
                "Allocation sizing impact calculated from capacity/budget constraints."
            ],
        )
