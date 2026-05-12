from typing import Dict, Any, List
from app.release_plane.models import CanaryRecord, ReleaseCandidateRef
from app.release_plane.enums import CanaryClass
from app.release_plane.exceptions import RolloutViolation
import uuid

class CanaryManager:
    def create_canary(self, candidate_id: str, scope: str, caps: Dict[str, Any], observation_seconds: int) -> CanaryRecord:
        # Enforce canary scope and caps
        if not caps:
            raise RolloutViolation("Canary must have defined caps.")

        return CanaryRecord(
            canary_id=f"canary-{uuid.uuid4().hex[:8]}",
            candidate_ref=ReleaseCandidateRef(candidate_id=candidate_id),
            canary_class=CanaryClass.TRAFFIC_SPLIT,
            scope=scope,
            caps=caps,
            observation_window_seconds=observation_seconds,
            promotion_readiness=False,
            stop_criteria=["error_rate_spike", "latency_degradation"],
            lineage_refs=[]
        )

    def evaluate_promotion(self, record: CanaryRecord, evidence_passed: bool) -> CanaryRecord:
        if not evidence_passed:
            raise RolloutViolation("Cannot promote canary with weak evidence.")
        if not getattr(record, "telemetry_support", True):
            raise RolloutViolation("Cannot promote canary lacking telemetry support.")
        record.promotion_readiness = True
        return record
