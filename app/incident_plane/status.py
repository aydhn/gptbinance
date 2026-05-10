from typing import List
from datetime import datetime, timezone
from app.incident_plane.enums import IncidentStatus
from app.incident_plane.exceptions import InvalidStatusTransition
from app.incident_plane.models import IncidentStatusEvent

class IncidentStatusMachine:
    VALID_TRANSITIONS = {
        IncidentStatus.DETECTED: [IncidentStatus.TRIAGING, IncidentStatus.FALSE_POSITIVE],
        IncidentStatus.TRIAGING: [IncidentStatus.INVESTIGATING, IncidentStatus.FALSE_POSITIVE],
        IncidentStatus.INVESTIGATING: [IncidentStatus.CONTAINING, IncidentStatus.RECOVERING],
        IncidentStatus.CONTAINING: [IncidentStatus.STABILIZED, IncidentStatus.RECOVERING],
        IncidentStatus.STABILIZED: [IncidentStatus.RECOVERING],
        IncidentStatus.RECOVERING: [IncidentStatus.VERIFYING],
        IncidentStatus.VERIFYING: [IncidentStatus.RESOLVED, IncidentStatus.REOPENED],
        IncidentStatus.RESOLVED: [IncidentStatus.CLOSED, IncidentStatus.REOPENED],
        IncidentStatus.CLOSED: [IncidentStatus.REOPENED],
        IncidentStatus.REOPENED: [IncidentStatus.TRIAGING, IncidentStatus.INVESTIGATING],
        IncidentStatus.FALSE_POSITIVE: []
    }

    @staticmethod
    def transition(current: IncidentStatus, target: IncidentStatus, reason: str, operator: str, incident_id: str = "TBD") -> IncidentStatusEvent:
        if target not in IncidentStatusMachine.VALID_TRANSITIONS.get(current, []):
            raise InvalidStatusTransition(f"Cannot transition from {current} to {target}. Rule violation.")

        return IncidentStatusEvent(
            incident_id=incident_id,
            previous_status=current,
            new_status=target,
            reason=reason,
            transitioned_by=operator
        )
