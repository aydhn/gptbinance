from app.order_intent.models import CompiledOrderPlan, PlanValidationResult


class PlanValidator:
    def validate(self, plan: CompiledOrderPlan) -> PlanValidationResult:
        errors = []
        warnings = []

        for leg in plan.legs:
            if leg.size <= 0 and not leg.close_position:
                errors.append(f"Leg {leg.leg_id} has invalid size <= 0")

            if leg.reduce_only and leg.close_position:
                errors.append(
                    f"Leg {leg.leg_id} cannot be both reduceOnly and closePosition"
                )

        return PlanValidationResult(
            is_valid=len(errors) == 0, errors=errors, warnings=warnings
        )
