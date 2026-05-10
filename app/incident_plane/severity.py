from app.incident_plane.enums import IncidentSeverity
from app.incident_plane.exceptions import InvalidSeverityEscalation

class IncidentSeverityEngine:
    @staticmethod
    def escalate(current: IncidentSeverity, target: IncidentSeverity, rationale: str) -> IncidentSeverity:
        # Simplified example
        if not rationale:
            raise InvalidSeverityEscalation("Rationale required for severity change.")
        return target
