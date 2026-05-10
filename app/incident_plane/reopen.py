from app.incident_plane.enums import IncidentStatus

class IncidentReopenEngine:
    @staticmethod
    def reopen(incident_id: str, reason: str) -> IncidentStatus:
        if not reason:
            raise ValueError("Silent reopen not allowed")
        return IncidentStatus.REOPENED
