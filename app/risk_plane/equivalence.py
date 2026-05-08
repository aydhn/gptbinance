import uuid

from .models import RiskEquivalenceReport, RiskState
from .enums import EquivalenceVerdict


class EquivalenceChecker:
    def check_equivalence(
        self, replay_state: RiskState, live_state: RiskState
    ) -> RiskEquivalenceReport:
        divergences = []

        if replay_state.completeness_summary != live_state.completeness_summary:
            divergences.append("Completeness mismatch")

        if replay_state.authoritative != live_state.authoritative:
            divergences.append("Authority mismatch")

        if divergences:
            verdict = EquivalenceVerdict.DIVERGENT
        else:
            verdict = EquivalenceVerdict.EQUIVALENT

        return RiskEquivalenceReport(
            report_id=str(uuid.uuid4()),
            verdict=verdict,
            environments_compared=["REPLAY", "LIVE"],
            divergence_sources=divergences,
            proof_notes=[f"Divergences found: {len(divergences)}"],
        )
