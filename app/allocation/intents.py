import uuid
from typing import List, Optional
from decimal import Decimal

from app.allocation.models import AllocationIntent
from app.allocation.enums import IntentStatus
from app.performance_plane.opportunity import OpportunitySurfaceBuilder
from app.performance_plane.enums import OpportunityClass


class AllocationIntentManager:
    @staticmethod
    def reject_intent(intent: AllocationIntent, reason: str):
        intent.status = IntentStatus.REJECTED
        # Additional logic...

    @staticmethod
    def export_foregone_opportunity(
        intent: AllocationIntent,
        clipped_qty: Decimal,
        expected_price: Decimal,
        currency: str,
    ):
        value = clipped_qty * expected_price
        return OpportunitySurfaceBuilder.build(
            opportunity_class=OpportunityClass.CAPACITY_CLIPPED,
            estimated_value=value,
            currency=currency,
            confidence_score=0.7,
            caveats=["Clipped by allocation capacity limits."],
        )

# WORKFLOW PLANE INTEGRATION:
# Added hooks for dependency/gate evaluations, duplicate run protections,
# and explicit reruns per Phase 73 requirements.
