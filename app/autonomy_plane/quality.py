from app.autonomy_plane.models import AutonomyObject
from typing import List

class QualityEvaluator:
    def evaluate(self, obj: AutonomyObject) -> List[str]:
        warnings = []
        if not obj.delegation_id:
            warnings.append("Stale delegation warning")
        if obj.authorization_posture == "unverified":
            warnings.append("Self-approval warning")
        return warnings

quality_evaluator = QualityEvaluator()
