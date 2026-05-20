from app.semantic_plane.registry import CanonicalSemanticRegistry
from app.semantic_plane.trust import DefaultTrustEvaluator

class ReadinessBoardSemanticIntegration:
    def __init__(self, registry: CanonicalSemanticRegistry):
        self.registry = registry
        self.trust_evaluator = DefaultTrustEvaluator(registry)

    def generate_semantic_integrity_bundle(self, semantic_ids: list[str]) -> dict:
        bundle = {
            "domain": "semantic_integrity",
            "verdicts": []
        }
        for sid in semantic_ids:
            verdict = self.trust_evaluator.evaluate(sid)
            bundle["verdicts"].append({
                "semantic_id": sid,
                "verdict": verdict.verdict.value,
                "blockers": verdict.blockers
            })

        return bundle
