from typing import List, Optional
from .models import IncidentRecord
from .storage import IncidentStorage

class IncidentRepository:
    def __init__(self, storage: IncidentStorage):
        self.storage = storage

    def save(self, incident: IncidentRecord):
        self.storage.save(incident)

    def get(self, incident_id: str) -> Optional[IncidentRecord]:
        return self.storage.load(incident_id)

    def list_active(self) -> List[IncidentRecord]:
        all_incidents = self.storage.list_all()
        return [i for i in all_incidents if i.state.value not in ["CLOSED"]]

    def list_all(self) -> List[IncidentRecord]:
        return self.storage.list_all()
