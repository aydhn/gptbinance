from app.research_plane.models import ResearchItem, ResearchMaturationReport
from app.research_plane.enums import ConfidenceClass


class MaturationAnalytics:
    def analyze(self, item: ResearchItem) -> ResearchMaturationReport:
        evidence_count = sum(len(b.entries) for b in item.evidence_bundles)
        resolved_contradictions = sum(
            1 for c in item.contradictions if not c.unresolved_burden
        )
        unresolved_contradictions = sum(
            1 for c in item.contradictions if c.unresolved_burden
        )

        # Simple stagnation detection
        stagnant = evidence_count == 0 and unresolved_contradictions > 0

        candidate = False
        if (
            item.confidence
            and item.confidence.current_class == ConfidenceClass.STRATEGY_CANDIDATE
        ):
            candidate = True

        dead_end = False
        if (
            item.confidence
            and item.confidence.current_class == ConfidenceClass.INVALIDATED
        ):
            dead_end = True

        return ResearchMaturationReport(
            hypothesis_ref=(
                item.hypotheses[0].hypothesis_id if item.hypotheses else "unknown"
            ),
            evidence_growth=evidence_count,
            contradiction_resolution_trend=resolved_contradictions,
            stagnation_detected=stagnant,
            maturation_to_candidate=candidate,
            dead_end=dead_end,
        )
