from app.remediation.models import RemediationPack
from app.remediation.exceptions import ApplyPolicyViolation, StaleFindingError
from app.policy_kernel.evaluation import evaluate_policy
from app.policy_kernel.context import assemble_policy_context
from app.policy_kernel.evidence import assemble_evidence_bundle
from app.policy_kernel.enums import PolicyVerdict


class PackValidator:
    def validate(
        self, pack: RemediationPack, workspace_id: str, profile_id: str, mode: str
    ) -> bool:
        if pack.finding_ref.is_stale:
            raise StaleFindingError(f"Pack {pack.pack_id} uses a stale finding.")

        if not pack.recipe:
            raise ApplyPolicyViolation("Pack is missing a valid recipe.")

        if (
            pack.recipe.requires_approval
            and "request_generation"
            not in [m.value for m in pack.recipe.allowed_apply_modes]
            and "manual_instruction"
            not in [m.value for m in pack.recipe.allowed_apply_modes]
        ):
            raise ApplyPolicyViolation(
                "Approval required but no request generation mode allowed."
            )

        # Policy Kernel Check before Apply
        ctx = assemble_policy_context(
            "remediation_apply", workspace_id, profile_id, mode
        )
        ev = assemble_evidence_bundle()  # Assume mock evidence
        decision = evaluate_policy("remediation_apply", ctx, ev)

        if decision.final_verdict == PolicyVerdict.HARD_BLOCK:
            raise ApplyPolicyViolation(
                f"Policy Kernel DENIED remediation apply. Reason: {decision.reasoning}"
            )

        return True
