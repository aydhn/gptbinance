from typing import Dict
from .models import EscrowObject

class CanonicalEscrowRegistry:
    def __init__(self):
        self.escrows: Dict[str, EscrowObject] = {}

    def register_escrow(self, escrow: EscrowObject):
        self.escrows[escrow.escrow_id] = escrow

    def get_escrow(self, escrow_id: str) -> EscrowObject:
        return self.escrows.get(escrow_id)
