from typing import List
from .models import DecisionFunnelRecord, DecisionFrictionRecord
from .enums import FunnelStage, FrictionClass


class FrictionAnalyzer:
    """
    Analyzes funnel drop-offs to attribute friction to specific sources.
    """

    STAGE_FRICTION_MAPPING = {
        FunnelStage.RISK_EVALUATED: FrictionClass.RISK_FILTER,
        FunnelStage.PORTFOLIO_EVALUATED: FrictionClass.CAPITAL_CONSTRAINT,
        FunnelStage.POLICY_EVALUATED: FrictionClass.POLICY_HARD_BLOCK,
        FunnelStage.INTENT_COMPILED: FrictionClass.LIFECYCLE_EXECUTION_ISSUE,
        FunnelStage.LIFECYCLE_SUBMITTED: FrictionClass.LIFECYCLE_EXECUTION_ISSUE,
    }

    def analyze_friction(
        self, funnel_record: DecisionFunnelRecord
    ) -> List[DecisionFrictionRecord]:
        """
        Analyzes a funnel record to generate friction records based on failed stages.
        """
        frictions = []
        for stage in funnel_record.stages:
            if not stage.passed:
                friction_class = self._map_stage_to_friction(stage.stage)

                frictions.append(
                    DecisionFrictionRecord(
                        opportunity_id=funnel_record.opportunity_id,
                        friction_class=friction_class,
                        severity=1.0,  # Base severity
                        description=f"Friction encountered at stage: {stage.stage.value}",
                    )
                )
        return frictions

    def _map_stage_to_friction(self, stage: FunnelStage) -> FrictionClass:
        """
        Maps a funnel stage to a friction class.
        """
        return self.STAGE_FRICTION_MAPPING.get(stage, FrictionClass.UNKNOWN_MIXED)
