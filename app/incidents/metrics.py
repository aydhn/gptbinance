from typing import List, Dict
from .models import IncidentRecord
from .repository import IncidentRepository


class IncidentMetrics:
    def __init__(self, repo: IncidentRepository):
        self.repo = repo

    def compute_summary(self) -> Dict[str, str]:
        # Placeholder for simulated metric calculations
        return {
            "mttd": "Under simulation",
            "mttr": "Under simulation",
            "unresolved_age": "N/A",
        }

    def export_reliability_metrics(self) -> Dict[str, str]:
        return {
            "mttd": "Under simulation",
            "time_to_containment": "Under simulation",
            "unresolved_age": "N/A",
        }
