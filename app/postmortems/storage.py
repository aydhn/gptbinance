from typing import Dict, Any


class PostmortemStorage:
    def save(self, postmortem_id: str, data: Dict[str, Any]):
        pass

    def load(self, postmortem_id: str) -> Dict[str, Any]:
        return {}
