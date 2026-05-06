from app.postmortems.models import RecurrenceRiskReport
from typing import Any


class RecurrenceScorer:
    def score(self, root_causes: Any, actions: Any) -> RecurrenceRiskReport:
        base_score = 0.5
        factors = []

        if not actions or not actions.get("corrective"):
            base_score += 0.3
            factors.append("No corrective actions")

        if root_causes and len(root_causes) > 0:
            base_score += 0.1
            factors.append("Identified root causes pending validation")

        score = min(1.0, max(0.0, base_score))
        return RecurrenceRiskReport(score=score, factors=factors)

    def export_recurrence_risk(self, root_causes: Any, actions: Any) -> float:
        report = self.score(root_causes, actions)
        return report.score
