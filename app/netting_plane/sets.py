from typing import Dict, Any
from .models import NettingSetRecord

class NettingSetManager:
    def __init__(self):
        self.sets: Dict[str, NettingSetRecord] = {}

    def register_set(self, data: Dict[str, Any]) -> NettingSetRecord:
        nset = NettingSetRecord(**data)
        self.sets[nset.set_id] = nset
        return nset
