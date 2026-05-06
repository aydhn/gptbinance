from app.reliability.trends import HistoricalReliabilityTrendAnalysis
from app.reliability.enums import ReliabilityDomain, TrendClass, ScorecardVerdict
from app.reliability.models import HealthScorecard


def test_trend_history_aggregation():
    # Simulate recent degraded, older healthy
    historical = [
        HealthScorecard(
            scorecard_id="s1",
            domain=ReliabilityDomain.MARKET_TRUTH,
            verdict=ScorecardVerdict.DEGRADED,
        ),
        HealthScorecard(
            scorecard_id="s2",
            domain=ReliabilityDomain.MARKET_TRUTH,
            verdict=ScorecardVerdict.DEGRADED,
        ),
        HealthScorecard(
            scorecard_id="s3",
            domain=ReliabilityDomain.MARKET_TRUTH,
            verdict=ScorecardVerdict.HEALTHY,
        ),
        HealthScorecard(
            scorecard_id="s4",
            domain=ReliabilityDomain.MARKET_TRUTH,
            verdict=ScorecardVerdict.HEALTHY,
        ),
        HealthScorecard(
            scorecard_id="s5",
            domain=ReliabilityDomain.MARKET_TRUTH,
            verdict=ScorecardVerdict.HEALTHY,
        ),
        HealthScorecard(
            scorecard_id="s6",
            domain=ReliabilityDomain.MARKET_TRUTH,
            verdict=ScorecardVerdict.HEALTHY,
        ),
    ]

    trend = HistoricalReliabilityTrendAnalysis.analyze_domain_trend(
        ReliabilityDomain.MARKET_TRUTH, historical
    )
    assert trend.trend_class == TrendClass.DEGRADING
