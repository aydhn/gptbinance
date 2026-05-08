from app.research_plane.models import ResearchItem, ResearchReadinessRecord
from app.research_plane.enums import ReadinessClass, ConfidenceClass


class ReadinessEvaluator:
    def evaluate(self, item: ResearchItem) -> ResearchReadinessRecord:
        blockers = []

        if not item.hypotheses:
            blockers.append("No hypotheses defined.")

        unresolved_contradictions = [
            c for c in item.contradictions if c.unresolved_burden
        ]
        if unresolved_contradictions:
            blockers.append(
                f"Has {len(unresolved_contradictions)} unresolved contradictions."
            )

        if not item.evidence_bundles or not any(
            e.entries for e in item.evidence_bundles
        ):
            blockers.append("Missing required evidence coverage.")

        if item.confidence and item.confidence.current_class not in [
            ConfidenceClass.EXPERIMENT_READY,
            ConfidenceClass.STRATEGY_CANDIDATE,
        ]:
            blockers.append(
                f"Confidence class {item.confidence.current_class.name} is insufficient."
            )

        readiness_class = (
            ReadinessClass.NOT_READY if blockers else ReadinessClass.EXPERIMENT_READY
        )

        return ResearchReadinessRecord(
            hypothesis_ref=(
                item.hypotheses[0].hypothesis_id if item.hypotheses else "unknown"
            ),
            readiness_class=readiness_class,
            blockers=blockers,
            proof_notes="Evaluated by ReadinessEvaluator",
        )
