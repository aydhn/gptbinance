from app.activation.models import ActivationPlan
from app.activation.enums import ActivationStage
from app.activation.exceptions import ActivationControllerError


class StageManager:
    FORBIDDEN_JUMPS = {
        ActivationStage.PREFLIGHT: [ActivationStage.STAGE_4_COMPLETE],
        ActivationStage.STAGE_0_OBSERVE: [ActivationStage.STAGE_4_COMPLETE],
    }

    @staticmethod
    def transition(
        plan: ActivationPlan, target_stage: ActivationStage
    ) -> ActivationPlan:
        current = plan.current_stage

        if target_stage in StageManager.FORBIDDEN_JUMPS.get(current, []):
            raise ActivationControllerError(
                f"Forbidden stage jump: {current.value} -> {target_stage.value}"
            )

        # In a real implementation, we'd verify preconditions and success criteria here.
        plan.current_stage = target_stage
        return plan
