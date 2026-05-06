from .models import ContainmentPlan, IncidentRecord
from .enums import IncidentSeverity, ContainmentIntentType

class ContainmentPlanner:
    @staticmethod
    def recommend(incident: IncidentRecord) -> ContainmentPlan:
        intent = ContainmentIntentType.NO_NEW_EXPOSURE
        if incident.severity == IncidentSeverity.CRITICAL_INCIDENT:
            if incident.scope.type == "GLOBAL":
                intent = ContainmentIntentType.GLOBAL_HALT_ADVISORY
            else:
                intent = ContainmentIntentType.PROFILE_HOLD
        return ContainmentPlan(
            intent=intent,
            rationale=f"Recommended due to severity {incident.severity.value}",
            affected_scope=incident.scope
        )
