from typing import List, Dict, Any
from app.activation.base import RolloutPlannerBase
from app.activation.models import (
    ActivationIntent,
    ActivationPlan,
    ActivationPlanStep,
    ProbationWindow,
)
from app.activation.enums import ActivationStage, ActivationClass
from datetime import datetime, timezone, timedelta


class RolloutPlanner(RolloutPlannerBase):
    def build_plan(self, intent: ActivationIntent) -> ActivationPlan:
        steps = []

        # PREFLIGHT is always first
        steps.append(
            ActivationPlanStep(
                stage=ActivationStage.PREFLIGHT,
                preconditions=["Board decision verified", "Shadow tests clean"],
                success_criteria=["Preflight checks passed"],
                halt_triggers=["Preflight verification failed"],
            )
        )

        # Build stages based on activation class
        now = datetime.now(timezone.utc)
        probation_duration = intent.probation_requirements.get("duration_minutes", 60)

        if intent.activation_class == ActivationClass.CANARY_LIMITED:
            steps.append(
                ActivationPlanStep(
                    stage=ActivationStage.STAGE_0_OBSERVE,
                    preconditions=["Preflight complete"],
                    success_criteria=["Observe window clean"],
                    probation_window=ProbationWindow(
                        start_time=now,
                        end_time=now + timedelta(minutes=probation_duration),
                        required_metrics=["market_truth_health", "shadow_cleanliness"],
                    ),
                    halt_triggers=["Shadow drift detected"],
                )
            )
            steps.append(
                ActivationPlanStep(
                    stage=ActivationStage.STAGE_1_LIMITED_SYMBOLS,
                    preconditions=["Stage 0 complete and clean"],
                    success_criteria=["Limited symbol window clean"],
                    probation_window=ProbationWindow(
                        start_time=now + timedelta(minutes=probation_duration),
                        end_time=now + timedelta(minutes=probation_duration * 2),
                        required_metrics=["lifecycle_health", "execution_friction"],
                    ),
                    halt_triggers=["Execution friction spike"],
                )
            )
        elif intent.activation_class == ActivationClass.PAPER_SHADOW:
            steps.append(
                ActivationPlanStep(
                    stage=ActivationStage.STAGE_0_OBSERVE,
                    preconditions=["Preflight complete"],
                    success_criteria=["Shadow execution clean"],
                    probation_window=ProbationWindow(
                        start_time=now,
                        end_time=now + timedelta(minutes=probation_duration),
                        required_metrics=["shadow_cleanliness", "market_truth_health"],
                    ),
                    halt_triggers=["Critical shadow drift"],
                )
            )
        else:
            steps.append(
                ActivationPlanStep(
                    stage=ActivationStage.STAGE_4_COMPLETE,
                    preconditions=["Preflight complete"],
                    success_criteria=["Direct activation completed safely"],
                    probation_window=ProbationWindow(
                        start_time=now,
                        end_time=now + timedelta(minutes=probation_duration),
                        required_metrics=["lifecycle_health", "capital_posture"],
                    ),
                    halt_triggers=["Capital posture breach"],
                )
            )

        return ActivationPlan(
            intent_id=intent.intent_id,
            steps=steps,
            current_stage=ActivationStage.PREFLIGHT,
        )
