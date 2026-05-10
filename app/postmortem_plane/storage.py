import json
from typing import Dict, Optional
from app.postmortem_plane.models import PostmortemDefinition
from app.postmortem_plane.exceptions import PostmortemStorageError

class PostmortemStorage:
    def __init__(self):
        self._store: Dict[str, str] = {}

    def save(self, postmortem: PostmortemDefinition):
        try:
             # Just store the raw model dump
             self._store[postmortem.postmortem_id] = postmortem.model_dump_json()
        except Exception as e:
             raise PostmortemStorageError(f"Failed to save: {e}")

    def load(self, postmortem_id: str) -> Optional[PostmortemDefinition]:
        if postmortem_id in self._store:
             return PostmortemDefinition.model_validate_json(self._store[postmortem_id])
        return None
