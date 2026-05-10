from typing import Dict, Any, Optional

class ReleasePlaneStorage:
    def __init__(self):
        self.releases: Dict[str, Any] = {}
        self.candidates: Dict[str, Any] = {}
        self.bundles: Dict[str, Any] = {}
        self.pins: Dict[str, Any] = {}
        self.records: Dict[str, Any] = {} # rollouts, compatibility, trust

    def save(self, collection: str, key: str, data: Any):
        getattr(self, collection)[key] = data

    def load(self, collection: str, key: str) -> Optional[Any]:
        return getattr(self, collection).get(key)
