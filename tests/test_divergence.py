from datetime import datetime, timezone
from app.analytics.divergence import DivergenceAnalyzer
from app.analytics.models import AnalyticsRun, AnalyticsConfig
from app.analytics.enums import AnalyticsScope, DivergenceType, ComparisonVerdict


def test_divergence():
    run = AnalyticsRun(
        run_id="r1",
        config=AnalyticsConfig(scope=AnalyticsScope.SESSION),
        started_at=datetime.now(timezone.utc),
    )
    analyzer = DivergenceAnalyzer()
    res = analyzer.analyze(run, [])

    assert len(res) > 0
    assert res[0].type == DivergenceType.PAPER_VS_LIVE
    assert res[0].live_vs_paper.verdict == ComparisonVerdict.MINOR_DIVERGENCE
