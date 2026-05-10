from typing import List
from app.postmortem_plane.models import PostmortemEquivalenceReport, PostmortemDefinition
from app.postmortem_plane.enums import EquivalenceVerdict

class PostmortemEquivalenceEvaluator:
    @staticmethod
    def evaluate(report_id: str, environments: List[str], p1: PostmortemDefinition, p2: PostmortemDefinition) -> PostmortemEquivalenceReport:

        # In a real impl, deeply compare causal chains and actions
        action_match = len(p1.corrective_actions) == len(p2.corrective_actions)
        cause_match = len(p1.root_causes) == len(p2.root_causes)

        verdict = EquivalenceVerdict.DIVERGENT
        if action_match and cause_match:
             verdict = EquivalenceVerdict.EQUIVALENT
        elif cause_match:
             verdict = EquivalenceVerdict.PARTIAL_EQUIVALENT

        return PostmortemEquivalenceReport(
            report_id=report_id,
            environments_compared=environments,
            verdict=verdict,
            action_path_equivalence=action_match,
            verification_equivalence=False,
            proof_notes=f"Causes: {cause_match}, Actions: {action_match}"
        )
