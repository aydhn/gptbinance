from app.renewal_plane.models import RenewalObject
from typing import Dict, List, Optional
from app.renewal_plane.enums import RenewalClass, ContinuationClass

class CanonicalRenewalRegistry:
    def __init__(self):
        self._registry: Dict[str, RenewalObject] = {}

    def register(self, obj: RenewalObject):
        self._registry[obj.renewal_id] = obj

    def get(self, renewal_id: str) -> Optional[RenewalObject]:
        return self._registry.get(renewal_id)

    def list_all(self) -> List[RenewalObject]:
        return list(self._registry.values())

    def get_by_class(self, r_class: RenewalClass) -> List[RenewalObject]:
        return [o for o in self._registry.values() if o.renewal_class == r_class]

    def has_stale_continuations(self) -> bool:
        for o in self._registry.values():
            if o.continuation_posture in [ContinuationClass.EXTENSION, ContinuationClass.PROVISIONAL]:
                return True
        return False
