from typing import Dict, List
from app.liability_plane.models import LiabilityObject
from app.liability_plane.exceptions import InvalidLiabilityObjectError

class CanonicalLiabilityRegistry:
    def __init__(self):
        self._liabilities: Dict[str, LiabilityObject] = {}

    def register_liability(self, obj: LiabilityObject) -> None:
        if not obj.liability_id:
            raise InvalidLiabilityObjectError("Liability ID cannot be empty.")
        if obj.liability_id in self._liabilities:
            raise InvalidLiabilityObjectError(f"Liability {obj.liability_id} already exists.")
        self._liabilities[obj.liability_id] = obj

    def get_liability(self, liability_id: str) -> LiabilityObject:
        if liability_id not in self._liabilities:
            raise InvalidLiabilityObjectError(f"Liability {liability_id} not found.")
        return self._liabilities[liability_id]

    def list_liabilities(self) -> List[LiabilityObject]:
        return list(self._liabilities.values())
