from typing import List
from .models import IncidentRecord
from .enums import IncidentSeverity

class IncidentPolicyChecker:
    @staticmethod
    def block_recovery(incident: IncidentRecord) -> List[str]:
        # Evaluate hard blockers based on incident state
        blockers = []
        if incident.severity == IncidentSeverity.CRITICAL_INCIDENT and incident.state != "CONTAINED":
            blockers.append("Critical incident must be fully contained before recovery can be planned.")
        return blockers
