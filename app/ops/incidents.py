from app.ops.base import IncidentHandlerBase
from app.ops.models import IncidentRecord, IncidentType, IncidentSeverity
from app.ops.repository import OpsRepository
import uuid
from typing import List


class IncidentHandler(IncidentHandlerBase):
    def __init__(self, repository: OpsRepository):
        self.repository = repository

    def report_incident(
        self, run_id: str, type: IncidentType, severity: IncidentSeverity, details: str
    ) -> str:
        incident_id = str(uuid.uuid4())
        record = IncidentRecord(
            incident_id=incident_id,
            run_id=run_id,
            type=type,
            severity=severity,
            details=details,
        )
        self.repository.append_incident(record)
        self._escalate(record)
        return incident_id

    def get_active_incidents(self, run_id: str) -> List[IncidentRecord]:
        incidents = self.repository.get_incidents(run_id)
        return [inc for inc in incidents if not inc.resolved]

    def _escalate(self, incident: IncidentRecord) -> None:
        pass
