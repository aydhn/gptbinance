from typing import Dict, List, Optional
from app.federation_plane.models import PortabilityRecord
from app.federation_plane.exceptions import InvalidPortabilityClaim


class PortabilityManager:
    def __init__(self):
        self._portabilities: Dict[str, PortabilityRecord] = {}

    def register(self, record: PortabilityRecord):
        if not record.portability_id or not record.proof_notes:
            raise InvalidPortabilityClaim("No portable-by-default fiction allowed.")
        self._portabilities[record.portability_id] = record

    def get_portability(self, portability_id: str) -> Optional[PortabilityRecord]:
        return self._portabilities.get(portability_id)

    def list_portabilities(self) -> List[PortabilityRecord]:
        return list(self._portabilities.values())
