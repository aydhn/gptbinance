# Stub for trust logic
from app.semantic_plane.models import SemanticTrustVerdict
from app.semantic_plane.enums import TrustVerdict
from app.semantic_plane.base import TrustEvaluatorBase

class DefaultTrustEvaluator(TrustEvaluatorBase):
    def __init__(self, registry):
        self.registry = registry

    def evaluate(self, semantic_id: str) -> SemanticTrustVerdict:
        if semantic_id in self.registry.conflicts:
            return SemanticTrustVerdict(
                verdict_id=f"tv_{semantic_id}",
                semantic_id=semantic_id,
                verdict=TrustVerdict.BLOCKED,
                blockers=["Unresolved semantic conflict detected."],
                caveats="Resolve conflict for canonical trust."
            )
        return SemanticTrustVerdict(
            verdict_id=f"tv_{semantic_id}",
            semantic_id=semantic_id,
            verdict=TrustVerdict.TRUSTED,
            blockers=[],
            caveats=""
        )
