# confirmation.py
from typing import Dict, List, Optional
from app.insolvency_plane.models import ConfirmationRecord

class ConfirmationManager:
    def __init__(self):
        self.confirmations: Dict[str, ConfirmationRecord] = {}

    def confirm_plan(self, confirmation: ConfirmationRecord):
        self.confirmations[confirmation.confirmation_id] = confirmation

    def get_confirmation(self, confirmation_id: str) -> Optional[ConfirmationRecord]:
        return self.confirmations.get(confirmation_id)

    def list_confirmations(self) -> List[ConfirmationRecord]:
        return list(self.confirmations.values())
