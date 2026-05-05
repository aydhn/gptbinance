from app.remediation.models import RemediationPack
from app.remediation.exceptions import ApplyPolicyViolation, StaleFindingError


class PackValidator:
    def validate(self, pack: RemediationPack) -> bool:
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
            # This shouldn't happen based on our recipe registry, but it's a good safety check
            raise ApplyPolicyViolation(
                "Approval required but no request generation mode allowed."
            )

        return True
