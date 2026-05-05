from app.policy_kernel.enums import PolicyDomain, PolicyVerdict
from typing import Dict, Any


class LifecyclePolicyHook:
    def check_orphan_risk(self) -> bool:
        return False

    def get_policy_domain_outputs(self) -> Dict[str, Any]:
        """Expose Lifecycle outputs for Policy Kernel Domain format"""
        has_risk = self.check_orphan_risk()
        verdict = PolicyVerdict.HARD_BLOCK if has_risk else PolicyVerdict.ALLOW

        return {
            "domain": PolicyDomain.LIFECYCLE,
            "reasons": ["Unresolved orphan risk detected"] if has_risk else [],
            "verdict": verdict,
        }
