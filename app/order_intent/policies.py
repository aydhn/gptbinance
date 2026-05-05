from app.order_intent.models import HighLevelIntent, IntentContext
from app.order_intent.exceptions import CompilePolicyViolation
from app.policy_kernel.enums import PolicyDomain, PolicyVerdict
from typing import Dict, Any


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

    def get_policy_domain_outputs(
        self, intent: HighLevelIntent, context: IntentContext
    ) -> Dict[str, Any]:
        """Expose Order Intent outputs for Policy Kernel Domain format"""
        verdict = PolicyVerdict.ALLOW
        reasons = []

        if not context.authorized:
            verdict = PolicyVerdict.HARD_BLOCK
            reasons.append("Intent lacks required authorization.")
        elif context.event_risk_active and intent.intent_type.value.startswith("open"):
            verdict = PolicyVerdict.BLOCK
            reasons.append("Cannot open new positions during active event risk.")
        elif (
            not context.capital_tier_allows_new
            and intent.intent_type.value.startswith("open")
        ):
            verdict = PolicyVerdict.BLOCK
            reasons.append("Capital tier restricts opening new positions.")
        elif context.cross_book_conflict:
            verdict = PolicyVerdict.BLOCK
            reasons.append("Cross-book conflict detected for this symbol.")

        return {
            "domain": PolicyDomain.ORDER_INTENT,
            "reasons": reasons,
            "verdict": verdict,
        }
