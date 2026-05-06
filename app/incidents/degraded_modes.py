from .models import DegradedModePlan, IncidentRecord
from .enums import DegradedModeType, IncidentSeverity


class DegradedModePlanner:
    @staticmethod
    def propose(incident: IncidentRecord) -> DegradedModePlan:
        mode = DegradedModeType.OBSERVE_ONLY
        if incident.severity in [
            IncidentSeverity.CRITICAL_INCIDENT,
            IncidentSeverity.MAJOR_INCIDENT,
        ]:
            mode = DegradedModeType.PAPER_SHADOW_ONLY
        return DegradedModePlan(
            mode=mode,
            constraints="Automated trading blocked. Review required.",
            affected_scope=incident.scope,
        )
