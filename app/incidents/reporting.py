from typing import List
from .models import IncidentRecord


class IncidentReporter:
    @staticmethod
    def format_incident_summary(inc: IncidentRecord) -> str:
        return f"[{inc.incident_id}] {inc.severity.value} - {inc.state.value} - Scope: {inc.scope.type.value}:{inc.scope.ref}"

    @staticmethod
    def format_timeline(inc: IncidentRecord) -> str:
        lines = [f"Timeline for {inc.incident_id}:"]
        for ev in inc.timeline:
            lines.append(f"- {ev.timestamp}: [{ev.event_type}] {ev.description}")
        return "\n".join(lines)

    @staticmethod
    def generate_digest(active_incidents: List[IncidentRecord]) -> str:
        if not active_incidents:
            return "Active Incidents: 0"
        lines = [f"Active Incidents: {len(active_incidents)}"]
        for inc in active_incidents:
            lines.append(IncidentReporter.format_incident_summary(inc))
        return "\n".join(lines)
