from typing import List
from datetime import datetime, timezone
import uuid
from app.readiness_board.models import (
    EvidenceSubmission,
    EvidenceAdmissibilityReport,
    ReadinessBoardConfig,
)
from app.readiness_board.enums import (
    AdmissibilityVerdict,
    PromotionStage,
    EvidenceClass,
)


class AdmissibilityEvaluator:
    def __init__(self, config: ReadinessBoardConfig):
        self.config = config

    def evaluate(
        self, submission: EvidenceSubmission, target_stage: PromotionStage
    ) -> EvidenceAdmissibilityReport:
        reasons = []
        verdict = AdmissibilityVerdict.ADMISSIBLE

        # Check freshness
        age_seconds = (
            datetime.now(timezone.utc) - submission.submitted_at
        ).total_seconds()
        if age_seconds > self.config.stale_evidence_threshold_seconds:
            verdict = AdmissibilityVerdict.INADMISSIBLE
            reasons.append(
                f"Evidence is stale (age: {age_seconds}s > threshold: {self.config.stale_evidence_threshold_seconds}s)"
            )

        # Example validation for stage requirements
        if target_stage == PromotionStage.CANARY_LIVE_CAUTION:
            if submission.evidence_class == EvidenceClass.STRESS_EVIDENCE:
                if not submission.content.get("passed_stress_tests", False):
                    verdict = AdmissibilityVerdict.INADMISSIBLE
                    reasons.append("Stress tests failed, inadmissible for live caution")

        return EvidenceAdmissibilityReport(
            report_id=f"adm_{uuid.uuid4().hex[:8]}",
            submission_id=submission.submission_id,
            verdict=verdict,
            reasons=reasons,
        )

    def check_minimum_evidence_set(
        self, submissions: List[EvidenceSubmission], target_stage: PromotionStage
    ) -> bool:
        classes = {s.evidence_class for s in submissions}
        if target_stage == PromotionStage.PAPER_SHADOW:
            required = {
                EvidenceClass.POLICY_DECISION_PROOFS,
                EvidenceClass.MARKET_TRUTH_EVIDENCE,
                EvidenceClass.EXPERIMENT_EVIDENCE_BUNDLES,
            }
            return required.issubset(classes)
        return True  # Default open for simplicity
