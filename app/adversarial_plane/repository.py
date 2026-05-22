from typing import Dict, Any, List
from app.adversarial_plane.storage import StorageManager

class AdversarialRepository:
    def __init__(self, storage: StorageManager):
        self.storage = storage

    def get_latest_trusted_query(self) -> Dict[str, Any]:
        return self.storage.load("latest_trusted_query") or {}

    def save_latest_trusted_query(self, query: Dict[str, Any]):
        self.storage.save("latest_trusted_query", query)

    def get_exploit_history(self) -> List[Dict[str, Any]]:
        return self.storage.load("exploit_history") or []

    def append_exploit_history(self, event: Dict[str, Any]):
        history = self.get_exploit_history()
        history.append(event)
        self.storage.save("exploit_history", history)
