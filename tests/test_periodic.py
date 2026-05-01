from datetime import datetime, timezone
from app.analytics.periodic import PeriodicSummaryGenerator

from app.analytics.enums import PeriodGranularity


def test_periodic():
    generator = PeriodicSummaryGenerator()
    s1 = generator.generate_session_summary("r1", 10.0, [], [], None, None, [], [], [])
    s2 = generator.generate_session_summary("r2", -5.0, [], [], None, None, [], [], [])

    res = generator.aggregate_periods(
        PeriodGranularity.DAY,
        datetime.now(timezone.utc),
        datetime.now(timezone.utc),
        [s1, s2],
    )

    assert res.granularity == PeriodGranularity.DAY
    assert res.total_pnl == 5.0
    assert len(res.session_summaries) == 2
