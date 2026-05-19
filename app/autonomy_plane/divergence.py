from app.autonomy_plane.models import AutonomyDivergenceReport

class DivergenceEvaluator:
    def evaluate(self, obj_id: str) -> AutonomyDivergenceReport:
        return AutonomyDivergenceReport(
            divergence_id=f"div_{obj_id}",
            divergence_notes="No divergence detected"
        )
