from app.incident_plane.models import IncidentSignal
from datetime import datetime, timezone
from typing import Dict, Any

class IncidentSignalIntakeLegacy:
    @staticmethod
    def create_signal(signal_type: str, severity_hint: str, blast_radius: str, payload: Dict[str, Any]) -> IncidentSignal:
        return IncidentSignal(
            signal_id=f"LEGACY-{signal_type}",
            source_system="legacy_intake",
            raw_payload={"severity_hint": severity_hint, "blast_radius": blast_radius, **payload},
            detected_at=datetime.now(timezone.utc),
            confidence_score=0.5
        )

