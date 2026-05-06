from app.reliability.freeze import ChangeFreezeRecommendationEngine
from app.reliability.enums import ReliabilityDomain, ScorecardVerdict, FreezeClass
from app.reliability.models import HealthScorecard


def test_scope_limited_freeze_recommendation():
    scorecards = [
        HealthScorecard(
            scorecard_id="s1",
            domain=ReliabilityDomain.MARKET_TRUTH,
            verdict=ScorecardVerdict.BLOCKED,
        )
    ]

    recs = ChangeFreezeRecommendationEngine.evaluate(scorecards, [])

    assert len(recs) >= 2
    classes = [r.freeze_class for r in recs]
    assert FreezeClass.NO_EXPANSION_RECOMMENDED in classes
    assert FreezeClass.RELEASE_HOLD_RECOMMENDED in classes
