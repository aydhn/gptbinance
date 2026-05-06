from typing import List, Dict
from .models import IncidentRecord
from .repository import IncidentRepository


class IncidentHistoryManager:
    def __init__(self, repo: IncidentRepository):
        self.repo = repo

    def get_repeated_clusters(self) -> Dict[str, int]:
        all_incidents = self.repo.list_all()
        clusters = {}
        for inc in all_incidents:
            key = f"{inc.scope.type.value}:{inc.scope.ref}"
            clusters[key] = clusters.get(key, 0) + 1
        return {k: v for k, v in clusters.items() if v > 1}

    def export_recurring_families(self) -> Dict[str, int]:
        return self.get_repeated_clusters()
