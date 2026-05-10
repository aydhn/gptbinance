from app.release_plane.models import ReleaseDivergenceReport, ReleaseCandidateRef
from typing import List, Dict, Any
import uuid

class ReleaseDivergenceAnalyzer:
    def analyze(self, candidate_id: str, drift_data: Dict[str, Any]) -> ReleaseDivergenceReport:
        env_drift = drift_data.get("environment_drift", [])
        pin_drift = drift_data.get("pin_drift", [])

        severity = "low"
        if env_drift or pin_drift:
            severity = "high"

        # Also check for rollout mismatch, activation mismatch, partial hotfix drift
        if drift_data.get("partial_hotfix_drift"):
             severity = "critical"

        return ReleaseDivergenceReport(
            report_id=f"div-{uuid.uuid4().hex[:8]}",
            candidate_ref=ReleaseCandidateRef(candidate_id=candidate_id),
            environment_drift=env_drift,
            pin_drift=pin_drift,
            severity=severity
        )
