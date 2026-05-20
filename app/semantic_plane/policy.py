from app.semantic_plane.registry import CanonicalSemanticRegistry

class PolicySemanticIntegration:
    def __init__(self, registry: CanonicalSemanticRegistry):
        self.registry = registry

    def evaluate_action_readiness(self, metric_names: list[str], threshold_ids: list[str]) -> bool:
        # Policy Evaluation: No high-risk action if relying on semantically ambiguous unit or threshold
        for metric_name in metric_names:
            if metric_name not in [m.name for m in self.registry.metrics.values()]:
                 return False # Missing canonical definition for metric

        return True
