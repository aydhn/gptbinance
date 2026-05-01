from datetime import datetime, timezone
from app.analytics.strategy_attribution import StrategyAttributionAnalyzer
from app.analytics.models import AnalyticsRun, AnalyticsConfig, TradeLifecycleSummary
from app.analytics.enums import AnalyticsScope


def test_strategy_attribution():
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
        regime="chop",
        pnl=10.0,
        fees=1.0,
    )
    t2 = TradeLifecycleSummary(
        trade_id="2",
        symbol="BTC",
        open_time=datetime.now(timezone.utc),
        strategy_family="trend",
        regime="chop",
        pnl=-5.0,
        fees=1.0,
    )
    t3 = TradeLifecycleSummary(
        trade_id="3",
        symbol="BTC",
        open_time=datetime.now(timezone.utc),
        strategy_family="mean_revert",
        regime="chop",
        pnl=20.0,
        fees=1.0,
    )

    analyzer = StrategyAttributionAnalyzer()
    res = analyzer.analyze(run, [t1, t2, t3])

    assert len(res) == 2
    trend = [r for r in res if r.strategy_family == "trend"][0]
    assert trend.trade_count == 2
    assert trend.pnl == 5.0
    assert trend.hit_rate == 0.5
    assert trend.cost_burden == 2.0
