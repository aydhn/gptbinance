from app.ml.models import DriftReport
from app.ml.enums import DriftSeverity
from datetime import datetime, timezone


class DriftChecker:
    def check_drift(self, run_id: str, current_data) -> DriftReport:
        return DriftReport(
            run_id=run_id,
            timestamp=datetime.now(timezone.utc),
            feature_drifts={"f1": 0.05},
            schema_drift_detected=False,
            missingness_drift=0.01,
            severity=DriftSeverity.NONE,
            recommended_action="monitor",
        )
