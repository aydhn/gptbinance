from app.reliability.scorecards import DomainHealthScorecardBuilder
from app.reliability.enums import (
    ReliabilityDomain,
    BurnSeverity,
    ScorecardVerdict,
    ReadinessDecayClass,
)
from app.reliability.models import BurnRateReport, ReadinessDecayRecord


def test_domain_scorecard_generation():
    burn_reports = [
        BurnRateReport(
            report_id="r1",
            budget_id="b1",
            short_window_burn_rate=0.2,
            long_window_burn_rate=0.2,
            severity=BurnSeverity.FAST_BURN,
        )
    ]

    scorecard = DomainHealthScorecardBuilder.build(
        ReliabilityDomain.MARKET_TRUTH, burn_reports, []
    )
    assert scorecard.verdict == ScorecardVerdict.BLOCKED
    assert len(scorecard.blockers) > 0

    decay_records = [
        ReadinessDecayRecord(
            record_id="d1",
            domain=ReliabilityDomain.MARKET_TRUTH,
            decay_class=ReadinessDecayClass.STALE_EVIDENCE,
            severity_score=0.9,
            evidence_ref="e",
            description="d",
        )
    ]

    scorecard_decay = DomainHealthScorecardBuilder.build(
        ReliabilityDomain.MARKET_TRUTH, [], decay_records
    )
    assert scorecard_decay.verdict == ScorecardVerdict.DEGRADED
