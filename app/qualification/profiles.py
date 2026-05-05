from app.policy_kernel.enums import PolicyDomain, PolicyVerdict
from typing import Dict, Any


class QualificationProfiles:
    def check_remediation_debt_blocker(self):
        pass

    def get_policy_domain_outputs(
        self, is_technically_passed: bool, constitution_blocked: bool
    ) -> Dict[str, Any]:
        """Expose Qualification outputs for Policy Kernel Domain format"""
        verdict = PolicyVerdict.ALLOW
        reasons = []

        if constitution_blocked:
            verdict = PolicyVerdict.BLOCK
            reasons.append("Policy constitution blocked despite technical pass")
        elif not is_technically_passed:
            verdict = PolicyVerdict.BLOCK
            reasons.append("Failed technical qualification")

        return {
            "domain": PolicyDomain.QUALIFICATION,
            "reasons": reasons,
            "verdict": verdict,
        }
