from datetime import datetime, timezone
from app.analytics.regime_attribution import RegimeAttributionAnalyzer
from app.analytics.models import AnalyticsRun, AnalyticsConfig, TradeLifecycleSummary
from app.analytics.enums import AnalyticsScope


def test_regime_attribution():
    run = AnalyticsRun(
        run_id="r1",
        config=AnalyticsConfig(scope=AnalyticsScope.SESSION),
        started_at=datetime.now(timezone.utc),
    )
    t1 = TradeLifecycleSummary(
        trade_id="1",
        symbol="BTC",
        open_time=datetime.now(timezone.utc),
        strategy_family="trend",
        regime="trend",
        pnl=15.0,
    )
    t2 = TradeLifecycleSummary(
        trade_id="2",
        symbol="BTC",
        open_time=datetime.now(timezone.utc),
        strategy_family="trend",
        regime="chop",
        pnl=-10.0,
    )

    analyzer = RegimeAttributionAnalyzer()
    res = analyzer.analyze(run, [t1, t2])

    assert len(res) == 2
    r_trend = [r for r in res if r.regime == "trend"][0]
    r_chop = [r for r in res if r.regime == "chop"][0]

    assert r_trend.pnl == 15.0
    assert r_chop.pnl == -10.0
    assert r_chop.suitability_score < 0
