from typing import List
from app.postmortem_plane.models import PostmortemDivergenceReport

class PostmortemDivergenceEvaluator:
    @staticmethod
    def evaluate(report_id: str, environments: List[str], cause_disagreement: bool, action_mismatch: bool) -> PostmortemDivergenceReport:
        severity = "HIGH" if cause_disagreement else ("MEDIUM" if action_mismatch else "LOW")
        return PostmortemDivergenceReport(
            report_id=report_id,
            environments_compared=environments,
            cause_disagreement=cause_disagreement,
            action_mismatch=action_mismatch,
            verification_mismatch=False,
            debt_classification_drift=False,
            divergence_severity=severity
        )
