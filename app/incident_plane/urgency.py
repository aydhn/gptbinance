from app.incident_plane.enums import IncidentUrgency

class IncidentUrgencyEngine:
    @staticmethod
    def determine_urgency(severity: str, impact_time: int) -> IncidentUrgency:
        return IncidentUrgency.IMMEDIATE
