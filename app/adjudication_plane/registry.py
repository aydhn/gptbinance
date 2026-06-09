from .models import AdjudicationObject
from .exceptions import InvalidAdjudicationObject
from typing import Dict

class CanonicalAdjudicationRegistry:
    def __init__(self):
        self._records: Dict[str, AdjudicationObject] = {}

    def register(self, obj: AdjudicationObject) -> str:
        if not obj.adjudication_id:
            raise InvalidAdjudicationObject("Adjudication ID is required")
        self._records[obj.adjudication_id] = obj
        return obj.adjudication_id

    def get(self, adjudication_id: str) -> AdjudicationObject:
        return self._records.get(adjudication_id)
