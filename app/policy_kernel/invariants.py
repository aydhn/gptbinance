from typing import Dict, Any, List

class Invariants:
    @staticmethod
    def check(context: Dict[str, Any]) -> List[str]:
        violations = []
        if context.get("high_risk_action") and context.get("unresolved_low_cost_exploit_path"):
            violations.append("no trusted high-risk action under unresolved low-cost exploit path")
        if context.get("approval_claim") and context.get("gameable_completion_evidence"):
            violations.append("no approval claim may rely on adversarially gameable completion evidence")
        return violations
