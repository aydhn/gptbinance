from datetime import datetime, timezone
from app.analytics.portfolio_attribution import PortfolioAttributionAnalyzer
from app.analytics.models import AnalyticsRun, AnalyticsConfig
from app.analytics.enums import AnalyticsScope


def test_portfolio_attribution():
    run = AnalyticsRun(
        run_id="r1",
        config=AnalyticsConfig(scope=AnalyticsScope.SESSION),
        started_at=datetime.now(timezone.utc),
    )

    mock_data = {
        "total_approved": 10,
        "total_reduced": 2,
        "total_deferred": 1,
        "total_rejected": 5,
    }

    analyzer = PortfolioAttributionAnalyzer()
    res = analyzer.analyze(run, mock_data)

    assert res.total_approved == 10
    assert res.total_rejected == 5
