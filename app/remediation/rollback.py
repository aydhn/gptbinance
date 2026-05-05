from app.remediation.models import RemediationPack, RollbackPlan
from app.remediation.enums import RemediationClass


class RollbackPlanner:
    def plan_rollback(self, pack: RemediationPack) -> RollbackPlan:
        steps = []
        is_eligible = True
        reason = None

        if pack.recipe.safety_class == RemediationClass.VENUE_AFFECTING:
            is_eligible = False
            reason = "Venue-affecting actions cannot be locally rolled back reliably."
        elif pack.recipe.safety_class == RemediationClass.READ_ONLY:
            # Read only just refreshes state, rolling back is usually just restoring the snapshot
            steps.append({"type": "restore_snapshot", "target": "local_shadow_state"})
        elif pack.recipe.safety_class == RemediationClass.APPROVAL_BOUND_LOCAL:
            steps.append({"type": "revert_metadata", "target": "quarantine_flags"})

        return RollbackPlan(
            is_eligible=is_eligible, steps=steps, reason_if_not_eligible=reason
        )
