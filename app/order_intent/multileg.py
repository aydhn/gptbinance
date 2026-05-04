import uuid
from datetime import datetime, timezone
from typing import List
from app.order_intent.models import (
    HighLevelIntent,
    IntentContext,
    CompiledOrderPlan,
    CompiledOrderLeg,
)
from app.order_intent.enums import PlanType
from app.order_intent.spot import SpotCompiler
from app.order_intent.margin import MarginCompiler
from app.order_intent.futures import FuturesCompiler
from app.order_intent.enums import VenueProduct


class IntentCompiler:
    def __init__(self):
        self.spot = SpotCompiler()
        self.margin = MarginCompiler()
        self.futures = FuturesCompiler()

    def compile_intent(
        self, intent: HighLevelIntent, context: IntentContext
    ) -> CompiledOrderPlan:
        legs: List[CompiledOrderLeg] = []

        if intent.product == VenueProduct.SPOT:
            legs.append(self.spot.compile(intent, context))
        elif intent.product in [
            VenueProduct.MARGIN_CROSS,
            VenueProduct.MARGIN_ISOLATED,
        ]:
            legs.extend(self.margin.compile(intent, context))
        elif intent.product in [VenueProduct.FUTURES_USDM, VenueProduct.FUTURES_COINM]:
            legs.append(self.futures.compile(intent, context))

        # Basic application of flags (could inject ReduceOnlyCompiler etc here)
        if intent.intent_type.value in ["reduce_position", "futures_reduce_only_close"]:
            for leg in legs:
                if "trade" in leg.leg_type.value:
                    leg.reduce_only = True

        if intent.intent_type.value in [
            "close_position",
            "futures_close_position_all",
            "flatten_symbol",
        ]:
            for leg in legs:
                if "trade" in leg.leg_type.value:
                    leg.close_position = True

        plan_type = PlanType.SINGLE_LEG if len(legs) == 1 else PlanType.MULTI_LEG

        return CompiledOrderPlan(
            plan_id=f"plan_{uuid.uuid4().hex[:8]}",
            intent_id=intent.intent_id,
            plan_type=plan_type,
            legs=legs,
            created_at=datetime.now(timezone.utc),
            compiled_at=datetime.now(timezone.utc),
        )
