# Stub for equivalence logic
from app.semantic_plane.models import SemanticEquivalenceReport
from app.semantic_plane.enums import EquivalenceVerdict
from app.semantic_plane.base import EquivalenceEvaluatorBase

class DefaultEquivalenceEvaluator(EquivalenceEvaluatorBase):
    def evaluate(self, semantic_id: str) -> SemanticEquivalenceReport:
        # Dummy evaluator
        return SemanticEquivalenceReport(
            equivalence_id=f"eq_{semantic_id}",
            semantic_id=semantic_id,
            verdict=EquivalenceVerdict.EQUIVALENT,
            blockers=[]
        )
