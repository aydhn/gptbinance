from app.policy_kernel.evaluation import evaluate_policy
from app.policy_kernel.context import assemble_policy_context
from app.policy_kernel.evidence import assemble_evidence_bundle
from app.policy_kernel.enums import PolicyVerdict


class PromotionGovernance:
    def check_outstanding_remediation_debt(self):
        pass

    def check_promotion_readiness(
        self, workspace_id: str, profile_id: str, mode: str
    ) -> bool:
        ctx = assemble_policy_context("promotion", workspace_id, profile_id, mode)
        ev = assemble_evidence_bundle()
        decision = evaluate_policy("promotion", ctx, ev)

        if decision.final_verdict in [PolicyVerdict.BLOCK, PolicyVerdict.HARD_BLOCK]:
            print(f"Promotion DENIED by Policy Constitution: {decision.reasoning}")
            return False

        print(f"Promotion TECHNICAL READINESS vs POLICY ALLOW checks out.")
        return True
