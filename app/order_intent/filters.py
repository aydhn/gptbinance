from app.order_intent.models import CompiledOrderLeg


class InstrumentFilters:
    def apply_filters(self, leg: CompiledOrderLeg) -> CompiledOrderLeg:
        # Mock logic: In reality, this would fetch stepSize, tickSize from an exchange info store.
        # Ensure sizes are positive and roughly aligned.
        # We don't mutate sizes silently without explaining, so we might just validate here
        # or round and record the change in PlanDiff later.

        # E.g. Rounding size to 3 decimal places (mock stepSize)
        leg.size = round(leg.size, 3)
        return leg
