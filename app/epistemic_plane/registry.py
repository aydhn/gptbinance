from typing import Dict, List
from app.epistemic_plane.models import BaseEpistemicRecord

class CanonicalEpistemicRegistry:
    def __init__(self):
        self.objects: Dict[str, BaseEpistemicRecord] = {}

    def register(self, obj: BaseEpistemicRecord):
        self.objects[obj.epistemic_id] = obj

    def get(self, epistemic_id: str) -> BaseEpistemicRecord:
        return self.objects.get(epistemic_id)
