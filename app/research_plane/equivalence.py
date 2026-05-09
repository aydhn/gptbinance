from app.research_plane.models import ResearchItem, ResearchEquivalenceReport
from app.research_plane.enums import EquivalenceVerdict


class EquivalenceAnalyzer:
    def analyze(
        self, replay_item: ResearchItem, runtime_item: ResearchItem
    ) -> ResearchEquivalenceReport:
        # Simplistic equivalence check based on question
        divergence = []
        verdict = EquivalenceVerdict.EQUIVALENT

        if not replay_item.question or not runtime_item.question:
            verdict = EquivalenceVerdict.INCOMPARABLE
            divergence.append("Missing questions for comparison.")
        elif replay_item.question.text != runtime_item.question.text:
            verdict = EquivalenceVerdict.DIVERGENT
            divergence.append("Questions do not match.")

        # Compare contradictions
        if len(replay_item.contradictions) != len(runtime_item.contradictions):
            verdict = (
                EquivalenceVerdict.PARTIAL_EQUIVALENCE
                if verdict == EquivalenceVerdict.EQUIVALENT
                else verdict
            )
            divergence.append("Contradiction counts differ.")

        return ResearchEquivalenceReport(
            report_id=f"eq_{replay_item.research_id}_{runtime_item.research_id}",
            hypothesis_ref=(
                replay_item.hypotheses[0].hypothesis_id
                if replay_item.hypotheses
                else "unknown"
            ),
            verdict=verdict,
            divergence_sources=divergence,
        )
