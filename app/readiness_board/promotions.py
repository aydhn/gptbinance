import uuid
from app.readiness_board.models import StagedPromotionPlan
from app.readiness_board.enums import PromotionStage


class PromotionManager:
    def evaluate_path(
        self, candidate_id: str, current_stage: PromotionStage
    ) -> StagedPromotionPlan:
        # Define allowed paths
        allowed_paths = {
            PromotionStage.CANDIDATE_REGISTRY: PromotionStage.PAPER_SHADOW,
            PromotionStage.PAPER_SHADOW: PromotionStage.CANDIDATE_QUALIFICATION,
            PromotionStage.CANDIDATE_QUALIFICATION: PromotionStage.CANARY_LIVE_CAUTION,
            PromotionStage.CANARY_LIVE_CAUTION: PromotionStage.LIVE,
        }

        target = allowed_paths.get(current_stage)
        if target:
            return StagedPromotionPlan(
                plan_id=f"plan_{uuid.uuid4().hex[:8]}",
                candidate_id=candidate_id,
                current_stage=current_stage,
                target_stage=target,
                allowed=True,
                reasons=[f"Valid path from {current_stage.value} to {target.value}"],
            )
        else:
            return StagedPromotionPlan(
                plan_id=f"plan_{uuid.uuid4().hex[:8]}",
                candidate_id=candidate_id,
                current_stage=current_stage,
                target_stage=PromotionStage.LIVE,  # Dummy target when invalid
                allowed=False,
                reasons=[f"No valid promotion path from {current_stage.value}"],
            )
