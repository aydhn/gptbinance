from typing import Dict, Any
from .models import MutualObligationRecord

class ObligationManager:
    def __init__(self):
        self.obligations: Dict[str, MutualObligationRecord] = {}

    def register_obligation(self, data: Dict[str, Any]) -> MutualObligationRecord:
        obl = MutualObligationRecord(**data)
        self.obligations[obl.obligation_id] = obl
        return obl
