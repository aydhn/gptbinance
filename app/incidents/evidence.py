from typing import List, Dict
from .models import IncidentRecord, IncidentSnapshot
from .repository import IncidentRepository

class EvidenceManager:
    def __init__(self, repo: IncidentRepository):
        self.repo = repo

    def get_evidence_bundle(self, incident_id: str) -> Dict[str, List[str]]:
        inc = self.repo.get(incident_id)
        if not inc:
            return {}

        return {
            "snapshots": [s.snapshot_id for s in inc.snapshots],
            "signals": [s.signal_id for s in inc.signals]
        }
