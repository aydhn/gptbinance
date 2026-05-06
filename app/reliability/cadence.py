import uuid
from typing import List, Dict
from app.reliability.base import CadenceArtifactBuilderBase
from app.reliability.models import (
    OperationalCadenceArtifact,
    DomainHealthSummary,
    BurnRateReport,
    ReadinessDecayRecord,
    FreezeRecommendation,
    HoldRecommendation,
    HealthScorecard,
)
from app.reliability.enums import ScorecardVerdict


class OperationalCadenceArtifactBuilder(CadenceArtifactBuilderBase):
    def build_artifact(
        self,
        artifact_type: str,
        scorecards: List[HealthScorecard] = None,
        burn_reports: List[BurnRateReport] = None,
        decay_records: List[ReadinessDecayRecord] = None,
        freeze_recs: List[FreezeRecommendation] = None,
        hold_recs: List[HoldRecommendation] = None,
    ) -> OperationalCadenceArtifact:
        scorecards = scorecards or []
        burn_reports = burn_reports or []
        decay_records = decay_records or []
        freeze_recs = freeze_recs or []
        hold_recs = hold_recs or []

        sc_dict = {s.domain.value: s for s in scorecards}

        overall_verdict = ScorecardVerdict.HEALTHY
        if any(s.verdict == ScorecardVerdict.BLOCKED for s in scorecards):
            overall_verdict = ScorecardVerdict.BLOCKED
        elif any(s.verdict == ScorecardVerdict.REVIEW_REQUIRED for s in scorecards):
            overall_verdict = ScorecardVerdict.REVIEW_REQUIRED
        elif any(s.verdict == ScorecardVerdict.DEGRADED for s in scorecards):
            overall_verdict = ScorecardVerdict.DEGRADED
        elif any(s.verdict == ScorecardVerdict.CAUTION for s in scorecards):
            overall_verdict = ScorecardVerdict.CAUTION

        summary = DomainHealthSummary(
            scorecards=sc_dict, overall_verdict=overall_verdict
        )

        return OperationalCadenceArtifact(
            artifact_id=f"cadence_{uuid.uuid4().hex[:8]}",
            artifact_type=artifact_type,
            domain_summary=summary,
            burn_reports=burn_reports,
            decay_records=decay_records,
            freeze_recommendations=freeze_recs,
            hold_recommendations=hold_recs,
        )
