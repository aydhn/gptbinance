from typing import Dict, List
from app.accountability_plane.models import AccountabilityObject
from app.accountability_plane.trust import AccountabilityTrustEngine
from app.accountability_plane.exceptions import AccountabilityTheaterViolation

class CanonicalAccountabilityRegistry:
    def __init__(self):
        self._store: Dict[str, AccountabilityObject] = {}

    def register(self, acc_obj: AccountabilityObject) -> AccountabilityObject:
        # Evaluate trust before registering
        verdict = AccountabilityTrustEngine.evaluate(acc_obj)
        if verdict.verdict == "blocked":
            raise AccountabilityTheaterViolation(f"Cannot register opaque accountability: {verdict.factors}")

        self._store[acc_obj.accountability_id] = acc_obj
        return acc_obj

    def get(self, accountability_id: str) -> AccountabilityObject:
        return self._store.get(accountability_id)

    def get_all(self) -> List[AccountabilityObject]:
        return list(self._store.values())
