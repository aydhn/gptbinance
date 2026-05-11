from app.incident_plane.models import IncidentSignal
from datetime import datetime, timezone
from typing import Dict, Any

class IncidentSignalIntake:
    @staticmethod
    def ingest_alert(alert_id: str, payload: Dict[str, Any], confidence: float = 0.8) -> IncidentSignal:
        return IncidentSignal(
            signal_id=f"SIG-ALERT-{alert_id}",
            source_system="observability_alerts",
            raw_payload=payload,
            detected_at=datetime.now(timezone.utc),
            confidence_score=confidence
        )

    @staticmethod
    def ingest_anomaly(anomaly_id: str, payload: Dict[str, Any], confidence: float = 0.6) -> IncidentSignal:
        return IncidentSignal(
            signal_id=f"SIG-ANOMALY-{anomaly_id}",
            source_system="anomaly_detection",
            raw_payload=payload,
            detected_at=datetime.now(timezone.utc),
            confidence_score=confidence
        )

class IncidentSignalMigrationRef:
    def migration_failure(self):
        pass
