from typing import List
from app.release_plane.models import RolloutPlan, RolloutStage, ReleaseCandidate, ReleaseCandidateRef
from app.release_plane.enums import RolloutClass
from app.release_plane.base import RolloutEvaluatorBase
from app.release_plane.exceptions import RolloutViolation
import uuid

class GovernanceRolloutEvaluator(RolloutEvaluatorBase):
    def evaluate(self, candidate: ReleaseCandidate) -> RolloutPlan:
        # Enforce no instant unreviewed full rollout
        stages = [
            RolloutStage(stage_id="candidate_prepared", stage_name="Candidate Prepared", description="Initial stage"),
            RolloutStage(stage_id="canary_active", stage_name="Canary Active", description="Running in canary scope"),
            RolloutStage(stage_id="probationary_active", stage_name="Probationary Active", description="Running with strict caps"),
            RolloutStage(stage_id="live_full_active", stage_name="Live Full Active", description="Full production rollout")
        ]

        return RolloutPlan(
            plan_id=f"rp-{uuid.uuid4().hex[:8]}",
            candidate_ref=ReleaseCandidateRef(candidate_id=candidate.candidate_id),
            rollout_class=RolloutClass.STAGED,
            stages=stages,
            current_stage="candidate_prepared"
        )

    def advance_stage(self, plan: RolloutPlan, next_stage_id: str, evidence_approved: bool) -> RolloutPlan:
        if not evidence_approved:
            raise RolloutViolation("Cannot advance rollout without approved evidence.")

        stage_ids = [s.stage_id for s in plan.stages]
        if next_stage_id not in stage_ids:
            raise RolloutViolation(f"Invalid stage ID: {next_stage_id}")

        current_idx = stage_ids.index(plan.current_stage)
        next_idx = stage_ids.index(next_stage_id)

        # Enforce no hidden state jumps
        if next_idx != current_idx + 1 and next_stage_id != "rollback_pending":
             raise RolloutViolation("Rollout stages must be advanced sequentially.")

        # Create a new instance because models are frozen
        new_plan = plan.model_copy(update={"current_stage": next_stage_id})
        return new_plan
