from app.order_intent.models import HighLevelIntent, IntentContext
from app.order_intent.exceptions import CompilePolicyViolation


class PolicyEngine:
    def check_intent(self, intent: HighLevelIntent, context: IntentContext) -> None:
        if not context.authorized:
            raise CompilePolicyViolation("Intent lacks required authorization.")

        if context.event_risk_active and intent.intent_type.value.startswith("open"):
            raise CompilePolicyViolation(
                "Cannot open new positions during active event risk."
            )

        if not context.capital_tier_allows_new and intent.intent_type.value.startswith(
            "open"
        ):
            raise CompilePolicyViolation(
                "Capital tier restricts opening new positions."
            )

        if context.cross_book_conflict:
            raise CompilePolicyViolation(
                "Cross-book conflict detected for this symbol."
            )
