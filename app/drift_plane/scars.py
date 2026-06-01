from app.drift_plane.models import ScarReactivationRecord
from app.drift_plane.enums import ScarClass
from typing import Dict
from datetime import datetime

class ScarManager:
    def __init__(self):
        self.scars: Dict[str, ScarReactivationRecord] = {}

    def add_scar(self, scar_id: str, class_type: ScarClass):
        self.scars[scar_id] = ScarReactivationRecord(
            scar_id=scar_id,
            class_type=class_type,
            reactivated_at=datetime.utcnow()
        )

    def get_scar(self, scar_id: str) -> ScarReactivationRecord:
        return self.scars.get(scar_id)
