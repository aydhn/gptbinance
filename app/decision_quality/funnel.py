from typing import List, Optional
from datetime import datetime, timezone
from .models import DecisionFunnelRecord, FunnelStageRecord, OpportunityCandidate
from .enums import FunnelStage, DecisionClass


class SignalToActionFunnel:
    """
    Manages the signal-to-action funnel for an opportunity.
    """

    def __init__(self):
        # In a real application, this would persist state.
        self._active_funnels = {}

    def start_funnel(self, candidate: OpportunityCandidate) -> DecisionFunnelRecord:
        record = DecisionFunnelRecord(
            opportunity_id=candidate.id,
            stages=[],
            final_class=DecisionClass.SUPPRESSED,  # Default until completed
            created_at=datetime.now(timezone.utc),
        )
        self._active_funnels[candidate.id] = record
        return record

    def record_stage(
        self,
        opportunity_id: str,
        stage: FunnelStage,
        passed: bool,
        entered_at: datetime,
        exited_at: Optional[datetime] = None,
        reason_refs: Optional[List[str]] = None,
    ) -> FunnelStageRecord:
        if opportunity_id not in self._active_funnels:
            raise ValueError(f"No active funnel for opportunity {opportunity_id}")

        latency_ms = None
        if exited_at:
            latency_ms = (exited_at - entered_at).total_seconds() * 1000.0

        stage_record = FunnelStageRecord(
            id=f"{opportunity_id}_{stage.value}",
            opportunity_id=opportunity_id,
            stage=stage,
            entered_at=entered_at,
            exited_at=exited_at,
            passed=passed,
            latency_ms=latency_ms,
            reason_refs=reason_refs or [],
        )

        self._active_funnels[opportunity_id].stages.append(stage_record)
        return stage_record

    def finalize_funnel(
        self, opportunity_id: str, final_class: DecisionClass
    ) -> DecisionFunnelRecord:
        if opportunity_id not in self._active_funnels:
            raise ValueError(f"No active funnel for opportunity {opportunity_id}")

        record = self._active_funnels[opportunity_id]
        record.final_class = final_class
        return record

    def get_funnel(self, opportunity_id: str) -> Optional[DecisionFunnelRecord]:
        return self._active_funnels.get(opportunity_id)
