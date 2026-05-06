import json
import os
from typing import List, Optional
from datetime import datetime
from .models import IncidentRecord

class IncidentStorage:
    def __init__(self, storage_dir: str = ".incidents_data"):
        self.storage_dir = storage_dir
        os.makedirs(self.storage_dir, exist_ok=True)

    def _get_path(self, incident_id: str) -> str:
        return os.path.join(self.storage_dir, f"{incident_id}.json")

    def save(self, incident: IncidentRecord):
        path = self._get_path(incident.incident_id)
        with open(path, "w") as f:
            f.write(incident.model_dump_json(indent=2))

    def load(self, incident_id: str) -> Optional[IncidentRecord]:
        path = self._get_path(incident_id)
        if not os.path.exists(path):
            return None
        with open(path, "r") as f:
            data = json.load(f)
            return IncidentRecord.model_validate(data)

    def list_all(self) -> List[IncidentRecord]:
        incidents = []
        for filename in os.listdir(self.storage_dir):
            if filename.endswith(".json"):
                with open(os.path.join(self.storage_dir, filename), "r") as f:
                    data = json.load(f)
                    incidents.append(IncidentRecord.model_validate(data))
        return incidents
