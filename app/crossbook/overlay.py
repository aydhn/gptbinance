from app.policy_kernel.enums import PolicyDomain, PolicyVerdict
from typing import Dict, Any


class CrossbookOverlay:
    def provide_remediation_suggestions(self):
        pass  # Placeholder

    def get_policy_domain_outputs(self, mock_verdict_str: str) -> Dict[str, Any]:
        """Expose Crossbook Overlay outputs for Policy Kernel Domain format"""
        verdict = PolicyVerdict.ALLOW
        if mock_verdict_str == "BLOCK":
            verdict = PolicyVerdict.BLOCK
        elif mock_verdict_str == "CAUTION":
            verdict = PolicyVerdict.CAUTION

        return {
            "domain": PolicyDomain.CROSS_BOOK,
            "reasons": ["Crossbook overlay assessment"],
            "verdict": verdict,
        }
