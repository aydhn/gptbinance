import uuid
from typing import List
from datetime import datetime, timezone
from app.model_plane.models import ModelDriftReport
from app.model_plane.enums import DriftSeverity


class ModelDriftEvaluator:
    def evaluate_drift(
        self, model_id: str, score_drift_metric: float, abstention_drift_metric: float
    ) -> ModelDriftReport:
        severity = DriftSeverity.NONE
        caveats = []

        if score_drift_metric > 0.5:
            severity = DriftSeverity.CRITICAL
            caveats.append("Score distribution drifted significantly")
        elif score_drift_metric > 0.2:
            severity = DriftSeverity.MODERATE
            caveats.append("Moderate score drift detected")

        if abstention_drift_metric > 0.3:
            if severity in [DriftSeverity.NONE, DriftSeverity.LOW]:
                severity = DriftSeverity.MODERATE
            caveats.append("Abstention rate shifted unexpectedly")

        return ModelDriftReport(
            report_id=str(uuid.uuid4()),
            model_id=model_id,
            evaluated_at=datetime.now(timezone.utc),
            drift_severity=severity,
            caveats=caveats,
        )
