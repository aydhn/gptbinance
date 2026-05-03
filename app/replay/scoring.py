import logging

from app.replay.models import ReplayabilityScore, ReplayVerdict

logger = logging.getLogger(__name__)


class DummyScorer:
    def score(self) -> ReplayabilityScore:
        return ReplayabilityScore(
            source_completeness=1.0,
            lineage_completeness=1.0,
            snapshot_fidelity=1.0,
            schema_compatibility=1.0,
            decision_path_coverage=1.0,
            diff_magnitude=0.0,
            deterministic_reproducibility=1.0,
            forensic_evidence_completeness=1.0,
            overall_score=1.0,
            verdict=ReplayVerdict.TRUSTED,
            blockers=[],
            next_actions=[],
        )
