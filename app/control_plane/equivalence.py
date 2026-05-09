from app.control_plane.models import ControlEquivalenceReport, ActionRequest
from app.control_plane.enums import EquivalenceVerdict


class EquivalenceEngine:
    def evaluate_equivalence(
        self, live_action: ActionRequest, paper_action: ActionRequest
    ) -> ControlEquivalenceReport:
        verdict = EquivalenceVerdict.EQUIVALENT
        reasons = []

        if live_action.command_id != paper_action.command_id:
            verdict = EquivalenceVerdict.DIVERGENT
            reasons.append("Command mismatch between environments")

        return ControlEquivalenceReport(
            action_id=live_action.action_id, verdict=verdict, divergence_reasons=reasons
        )
