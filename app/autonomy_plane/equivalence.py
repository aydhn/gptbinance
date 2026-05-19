from app.autonomy_plane.models import AutonomyEquivalenceReport
from app.autonomy_plane.enums import EquivalenceVerdict

class EquivalenceEvaluator:
    def evaluate(self, obj_id: str) -> AutonomyEquivalenceReport:
        return AutonomyEquivalenceReport(
            equivalence_id=f"eq_{obj_id}",
            verdict=EquivalenceVerdict.EQUIVALENT
        )
