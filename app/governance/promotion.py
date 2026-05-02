from app.governance.models import PromotionCandidateReport, CandidateBundle
from app.governance.enums import PromotionReadiness, BundleStage


class PromotionEvaluator:
    def evaluate(self, bundle: CandidateBundle) -> PromotionCandidateReport:
        # Check validation summaries, ML readiness, Rollback readiness, etc.
        blockers = []
        warnings: list[str] = []
        readiness = PromotionReadiness.READY

        if not bundle.rollback_ref:
            blockers.append("Missing rollback reference")
            readiness = PromotionReadiness.BLOCKED

        stage_rec = (
            BundleStage.APPROVED_FOR_PAPER
            if readiness == PromotionReadiness.READY
            else BundleStage.CANDIDATE
        )

        return PromotionCandidateReport(
            bundle_id=bundle.bundle_id,
            readiness=readiness,
            stage_recommendation=stage_rec,
            blockers=blockers,
            warnings=warnings,
            next_actions=["Review rollback ref" if blockers else "Proceed to Paper"],
        )
