from typing import Dict, Any
from .models import CounterpartyPairRecord

class CounterpartyManager:
    def __init__(self):
        self.pairs: Dict[str, CounterpartyPairRecord] = {}

    def register_pair(self, data: Dict[str, Any]) -> CounterpartyPairRecord:
        pair = CounterpartyPairRecord(**data)
        self.pairs[pair.pair_id] = pair
        return pair
