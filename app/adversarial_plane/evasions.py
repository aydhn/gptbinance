from typing import List, Optional
from app.adversarial_plane.models import EvasionRecord
from app.adversarial_plane.enums import EvasionClass

def create_evasion(evasion_id: str, evasion_class: EvasionClass, caveats: str, lineage_refs: Optional[List[str]] = None) -> EvasionRecord:
    return EvasionRecord(
        evasion_id=evasion_id,
        evasion_class=evasion_class,
        caveats=caveats,
        lineage_refs=lineage_refs or []
    )

class EvasionManager:
    def __init__(self):
        self._evasions = {}

    def add_evasion(self, ev: EvasionRecord):
        self._evasions[ev.evasion_id] = ev

    def get_evasion(self, evasion_id: str) -> Optional[EvasionRecord]:
        return self._evasions.get(evasion_id)

    def list_evasions(self) -> List[EvasionRecord]:
        return list(self._evasions.values())
