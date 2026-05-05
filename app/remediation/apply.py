import uuid
from app.remediation.models import RemediationPack, ApplyResult
from app.remediation.enums import RemediationClass, ApplyMode
from app.remediation.exceptions import ApplyPolicyViolation


class ApplyExecutor:
    def execute(self, pack: RemediationPack) -> ApplyResult:
        # STRICT RULE: Venue-affecting remediations MUST NOT be directly applied.
        if pack.recipe.safety_class == RemediationClass.VENUE_AFFECTING:
            return ApplyResult(
                success=True,
                mode_used=ApplyMode.REQUEST_GENERATION,
                generated_request_id=f"REQ-{uuid.uuid4().hex[:6].upper()}",
                error_message="VENUE_AFFECTING class cannot be auto-applied. Generated approval request instead.",
            )

        if (
            pack.recipe.requires_approval
            and ApplyMode.DIRECT_SAFE in pack.recipe.allowed_apply_modes
        ):
            raise ApplyPolicyViolation("Approval required but DIRECT_SAFE attempted.")

        # For Read-only and safe local updates
        return ApplyResult(
            success=True,
            mode_used=ApplyMode.DIRECT_SAFE,
            before_snapshot_ref="snap_before_123",
            after_snapshot_ref="snap_after_123",
        )
