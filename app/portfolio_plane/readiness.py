from typing import Dict, Any

class PortfolioReadinessAggregator:
    def evaluate_readiness(self, portfolio_id: str, context: Dict[str, Any]) -> str:
        # A mock evaluator enforcing the requirement that without clear proof/funding
        # readiness is blocked.
        if "funding_sufficiency" not in context or not context["funding_sufficiency"]:
            return "BLOCKED"
        if "staffing_sufficiency" not in context or not context["staffing_sufficiency"]:
            return "CONDITIONALLY_READY"
        return "READY"
