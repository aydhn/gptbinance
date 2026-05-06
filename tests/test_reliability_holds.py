from app.reliability.holds import OperationalHoldRecommendationEngine
from app.reliability.enums import (
    ReliabilityDomain,
    ScorecardVerdict,
    OperationalReviewClass,
)
from app.reliability.models import HealthScorecard


def test_operational_hold_logic():
    scorecards = [
        HealthScorecard(
            scorecard_id="s1",
            domain=ReliabilityDomain.RELEASE_READINESS_HEALTH,
            verdict=ScorecardVerdict.REVIEW_REQUIRED,
        )
    ]
    holds = OperationalHoldRecommendationEngine.evaluate(scorecards)

    assert len(holds) == 1
    assert holds[0].hold_class == OperationalReviewClass.BOARD_REVIEW_HOLD
