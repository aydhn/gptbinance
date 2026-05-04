from app.order_intent.models import HighLevelIntent, CompiledOrderPlan, PlanExplanation


class Explainer:
    def explain(
        self, intent: HighLevelIntent, plan: CompiledOrderPlan
    ) -> PlanExplanation:
        reason = f"Compiled {intent.intent_type.value} into a {plan.plan_type.value} plan with {len(plan.legs)} legs."
        changes = {"original_size": intent.size, "legs_count": len(plan.legs)}
        return PlanExplanation(reason=reason, field_changes=changes)
