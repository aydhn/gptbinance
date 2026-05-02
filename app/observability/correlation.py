from typing import Dict, List, Optional
from datetime import datetime, timezone
import uuid
from app.observability.models import AlertEvent, AlertCorrelationGroup
from app.observability.enums import CorrelationVerdict


class AlertCorrelator:
    def __init__(self):
        self._groups: List[AlertCorrelationGroup] = []

    def correlate(self, active_alerts: List[AlertEvent]) -> List[AlertCorrelationGroup]:
        """Simple correlation engine based on time window and component overlap"""
        # Reset groups for this run for simplicity, in reality this would be stateful
        new_groups: List[AlertCorrelationGroup] = []

        if not active_alerts:
            return new_groups

        # Group by component
        comp_groups: Dict[str, List[AlertEvent]] = {}
        for alert in active_alerts:
            comp_groups.setdefault(alert.component.value, []).append(alert)

        for comp, alerts in comp_groups.items():
            if len(alerts) > 1:
                # Correlate alerts on the same component
                # Define a weight for severity:
                severity_weight = {"info": 0, "warning": 1, "error": 2, "critical": 3}
                primary = max(
                    alerts,
                    key=lambda a: (
                        severity_weight.get(a.severity.value, 0),
                        a.occurrence_count,
                    ),
                )
                related = [a.alert_id for a in alerts if a.alert_id != primary.alert_id]

                group = AlertCorrelationGroup(
                    group_id=f"grp_{uuid.uuid4().hex[:8]}",
                    verdict=CorrelationVerdict.RELATED,
                    primary_alert_id=primary.alert_id,
                    related_alert_ids=related,
                    likely_parent_issue=f"Multiple issues on {comp}",
                )
                new_groups.append(group)

        # Example Cross component correlation
        # If execution reject storm AND stream stale -> network/connectivity issue
        # This is where specific domain logic goes.

        self._groups.extend(new_groups)
        return new_groups

    def get_groups(self) -> List[AlertCorrelationGroup]:
        return self._groups.copy()


correlator = AlertCorrelator()
