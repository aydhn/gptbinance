from typing import Dict, List, Optional
from app.security_plane.models import KeyDefinition

class KeyManager:
    def __init__(self):
        self._keys: Dict[str, KeyDefinition] = {}

    def register_key(self, key: KeyDefinition) -> None:
        self._keys[key.key_id] = key

    def list_keys(self) -> List[KeyDefinition]:
        return list(self._keys.values())
