from typing import Dict, Any
from .models import NettingDivergenceReport

class DivergenceManager:
    def __init__(self):
        self.reports: Dict[str, NettingDivergenceReport] = {}

    def evaluate(self, data: Dict[str, Any]) -> NettingDivergenceReport:
        rep = NettingDivergenceReport(**data)
        self.reports[rep.report_id] = rep
        return rep
