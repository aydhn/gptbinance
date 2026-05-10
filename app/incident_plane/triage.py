from app.incident_plane.models import IncidentTriageRecord
from datetime import datetime, timezone
from typing import List

class IncidentTriageEngine:
    @staticmethod
    def submit_triage(incident_id: str, facts: List[str], hypotheses: List[str], blockers: List[str], operator: str, proof: str) -> IncidentTriageRecord:
        return IncidentTriageRecord(
            incident_id=incident_id,
            provisional_facts=facts,
            hypotheses=hypotheses,
            missing_information_blockers=blockers,
            proof_notes=proof,
            triaged_at=datetime.now(timezone.utc),
            triaged_by=operator
        )
