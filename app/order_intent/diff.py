from app.order_intent.models import HighLevelIntent, CompiledOrderPlan, PlanDiff


class DiffCalculator:
    def calculate(self, intent: HighLevelIntent, plan: CompiledOrderPlan) -> PlanDiff:
        # Sum size of trade legs
        compiled_size = sum(
            leg.size for leg in plan.legs if "trade" in leg.leg_type.value
        )

        reasons = []
        if compiled_size != intent.size:
            reasons.append("Size adjusted due to rounding or safety limits.")

        is_multi = len(plan.legs) > 1
        if is_multi:
            reasons.append("Intent compiled into multiple execution legs.")

        return PlanDiff(
            requested_size=intent.size,
            compiled_size=compiled_size,
            is_multi_leg=is_multi,
            diff_reasons=reasons,
        )
