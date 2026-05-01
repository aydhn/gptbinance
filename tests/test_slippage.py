from datetime import datetime, timezone
from app.analytics.slippage import SlippageAnalyzer
from app.analytics.models import AnalyticsRun, AnalyticsConfig
from app.analytics.enums import AnalyticsScope


def test_slippage():
    run = AnalyticsRun(
        run_id="r1",
        config=AnalyticsConfig(scope=AnalyticsScope.SESSION),
        started_at=datetime.now(timezone.utc),
    )
    analyzer = SlippageAnalyzer()
    res = analyzer.analyze(run, [])

    assert res.avg_entry_slippage_bps > 0
    assert "BTCUSDT" in res.symbol_slippage
