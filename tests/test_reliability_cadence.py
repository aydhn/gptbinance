from app.reliability.cadence import OperationalCadenceArtifactBuilder
from app.reliability.enums import ReliabilityDomain, ScorecardVerdict
from app.reliability.models import HealthScorecard


def test_daily_weekly_artifact_generation():
    builder = OperationalCadenceArtifactBuilder()
    scorecards = [
        HealthScorecard(
            scorecard_id="s1",
            domain=ReliabilityDomain.MARKET_TRUTH,
            verdict=ScorecardVerdict.HEALTHY,
        )
    ]

    artifact = builder.build_artifact("daily_digest", scorecards=scorecards)
    assert artifact.artifact_type == "daily_digest"
    assert artifact.domain_summary.overall_verdict == ScorecardVerdict.HEALTHY
