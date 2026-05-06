from app.reliability.repository import ReliabilityRepository
from app.reliability.enums import ReliabilityDomain, ScorecardVerdict
from app.reliability.models import HealthScorecard


def test_scorecards_read_write():
    repo = ReliabilityRepository()
    sc = HealthScorecard(
        scorecard_id="test_sc",
        domain=ReliabilityDomain.MARKET_TRUTH,
        verdict=ScorecardVerdict.HEALTHY,
    )

    repo.save_scorecard(sc)

    latest = repo.get_latest_scorecards()
    assert len(latest) >= 1
    ids = [s.scorecard_id for s in latest]
    assert "test_sc" in ids
