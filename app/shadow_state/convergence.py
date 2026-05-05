from app.policy_kernel.enums import PolicyDomain, PolicyVerdict
from typing import Dict, Any


class ConvergenceTracker:
    def add_remediation_debt_field(self):
        pass  # Placeholder for convergence metadata updates

    def get_policy_domain_outputs(self, has_critical_drift: bool) -> Dict[str, Any]:
        """Expose Shadow State Truthfulness outputs for Policy Kernel Domain format"""
        verdict = (
            PolicyVerdict.HARD_BLOCK if has_critical_drift else PolicyVerdict.ALLOW
        )

        return {
            "domain": PolicyDomain.SHADOW,
            "reasons": ["Critical unresolved drift detected"]
            if has_critical_drift
            else [],
            "verdict": verdict,
        }
