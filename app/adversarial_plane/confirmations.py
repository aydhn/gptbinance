from typing import List, Optional
from app.adversarial_plane.models import ConfirmationRecord
from app.adversarial_plane.enums import ConfirmationClass

def create_confirmation(confirmation_id: str, confirmation_class: ConfirmationClass, scope: str, stale_warning: Optional[str] = None, lineage_refs: Optional[List[str]] = None) -> ConfirmationRecord:
    return ConfirmationRecord(
        confirmation_id=confirmation_id,
        confirmation_class=confirmation_class,
        scope=scope,
        stale_warning=stale_warning,
        lineage_refs=lineage_refs or []
    )

class ConfirmationManager:
    def __init__(self):
        self._confirmations = {}

    def add_confirmation(self, conf: ConfirmationRecord):
        self._confirmations[conf.confirmation_id] = conf

    def get_confirmation(self, confirmation_id: str) -> Optional[ConfirmationRecord]:
        return self._confirmations.get(confirmation_id)

    def list_confirmations(self) -> List[ConfirmationRecord]:
        return list(self._confirmations.values())
