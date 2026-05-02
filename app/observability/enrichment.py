from typing import Dict, List, Optional
from app.observability.models import AlertEvent, EnrichedIncidentHint, RunbookRef
from app.observability.runbooks import registry as runbook_registry
from app.observability.enums import ComponentType


class IncidentEnricher:
    def enrich_alert(self, alert: AlertEvent) -> EnrichedIncidentHint:
        suggested_runbook = None
        if alert.runbook_ref:
            suggested_runbook = runbook_registry.get_runbook(alert.runbook_ref)

        # Simple heuristic mapping if explicit ref is missing
        if not suggested_runbook:
            if alert.component == ComponentType.DATA_STREAM:
                suggested_runbook = runbook_registry.get_runbook("RB-STREAM-001")
            elif alert.component == ComponentType.EXECUTION:
                suggested_runbook = runbook_registry.get_runbook("RB-EXEC-001")

        context = f"Alert generated on {alert.component.value}. Severity: {alert.severity.value}."
        if alert.evidence:
            context += f" Evidence: {alert.evidence}"

        return EnrichedIncidentHint(
            alert_id=alert.alert_id,
            impacted_components=[alert.component],
            suggested_runbook=suggested_runbook,
            context=context,
        )


enricher = IncidentEnricher()
