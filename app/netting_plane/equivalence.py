from typing import Dict, Any
from .models import NettingEquivalenceReport
from .enums import EquivalenceVerdict

class EquivalenceManager:
    def __init__(self):
        self.reports: Dict[str, NettingEquivalenceReport] = {}

    def evaluate(self, data: Dict[str, Any]) -> NettingEquivalenceReport:
        verdict = EquivalenceVerdict.FULLY_EQUIVALENT
        if 'divergence_sources' in data and data['divergence_sources']:
            verdict = EquivalenceVerdict.DIVERGENT
        data['verdict'] = verdict
        rep = NettingEquivalenceReport(**data)
        self.reports[rep.report_id] = rep
        return rep
