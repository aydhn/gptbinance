from typing import Optional, List, Dict
from typing import Dict, Any, List
# pylint: disable=unused-import
# flake8: noqa, Optional
from .models import MandateRecord
from .enums import MandateClass

class MandatesManager:
    """
    Strictly types mandates and their scope. Prevents title-based shortcuts.
    """
    def __init__(self):
        self.mandates: Dict[str, MandateRecord] = {}

    def _add_mandate(self, id: str, authority_id: str, mclass: MandateClass, caveats: List[str] = None) -> MandateRecord:
        record = MandateRecord(id, authority_id, mclass, caveats or [], [])
        self.mandates[id] = record
        return record

    def add_standing(self, id: str, authority_id: str, caveats: List[str] = None) -> MandateRecord:
        return self._add_mandate(id, authority_id, MandateClass.STANDING, caveats)

    def add_scoped(self, id: str, authority_id: str, caveats: List[str] = None) -> MandateRecord:
        return self._add_mandate(id, authority_id, MandateClass.SCOPED, caveats)

    def add_temporary(self, id: str, authority_id: str, caveats: List[str] = None) -> MandateRecord:
        return self._add_mandate(id, authority_id, MandateClass.TEMPORARY, caveats)

    def add_emergency(self, id: str, authority_id: str, caveats: List[str] = None) -> MandateRecord:
        return self._add_mandate(id, authority_id, MandateClass.EMERGENCY, caveats)

    def get_by_id(self, mandate_id: str) -> Optional[MandateRecord]:
        return self.mandates.get(mandate_id)
