from .models import IncidentSignal, IncidentRecord


class IncidentClustering:
    @staticmethod
    def is_related(signal: IncidentSignal, incident: IncidentRecord) -> bool:
        if (
            signal.scope_type == incident.scope.type
            and signal.scope_ref == incident.scope.ref
        ):
            return True
        if incident.scope.type == "GLOBAL":
            return True
        return False
