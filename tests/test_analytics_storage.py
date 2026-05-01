import os
import shutil
from datetime import datetime, timezone
from app.analytics.storage import AnalyticsStorage
from app.analytics.models import TradeJournalEntry, SessionAnalyticsSummary
from app.analytics.enums import JournalEventType


def test_analytics_storage():
    test_path = "data/test_analytics"
    if os.path.exists(test_path):
        shutil.rmtree(test_path)

    storage = AnalyticsStorage(test_path)

    e1 = TradeJournalEntry(
        entry_id="1",
        run_id="test_run",
        timestamp=datetime.now(timezone.utc),
        event_type=JournalEventType.ORDER_FILLED,
        symbol="BTC",
    )
    storage.save_journal("test_run", [e1])

    loaded = storage.load_journal("test_run")
    assert len(loaded) == 1
    assert loaded[0].entry_id == "1"

    summ = SessionAnalyticsSummary(run_id="test_run", total_pnl=100.0)
    storage.save_session_summary(summ)

    loaded_summ = storage.load_session_summary("test_run")
    assert loaded_summ is not None
    assert loaded_summ.total_pnl == 100.0

    shutil.rmtree(test_path)
