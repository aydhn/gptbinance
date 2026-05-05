from datetime import datetime, timezone, timedelta
from app.readiness_board.models import ReadinessBoardConfig, EvidenceSubmission
from app.readiness_board.admissibility import AdmissibilityEvaluator
from app.readiness_board.enums import (
    PromotionStage,
    AdmissibilityVerdict,
    EvidenceClass,
)


def test_admissibility_stale():
    config = ReadinessBoardConfig(stale_evidence_threshold_seconds=10)
    evaluator = AdmissibilityEvaluator(config)

    sub = EvidenceSubmission(
        submission_id="sub_1",
        candidate_id="cand_1",
        evidence_class=EvidenceClass.MARKET_TRUTH_EVIDENCE,
        content={},
        source_ref="src",
        submitted_at=datetime.now(timezone.utc) - timedelta(seconds=20),
    )

    rep = evaluator.evaluate(sub, PromotionStage.PAPER_SHADOW)
    assert rep.verdict == AdmissibilityVerdict.INADMISSIBLE


def test_admissibility_live_caution():
    config = ReadinessBoardConfig()
    evaluator = AdmissibilityEvaluator(config)

    sub = EvidenceSubmission(
        submission_id="sub_1",
        candidate_id="cand_1",
        evidence_class=EvidenceClass.STRESS_EVIDENCE,
        content={"passed_stress_tests": False},
        source_ref="src",
    )

    rep = evaluator.evaluate(sub, PromotionStage.CANARY_LIVE_CAUTION)
    assert rep.verdict == AdmissibilityVerdict.INADMISSIBLE
