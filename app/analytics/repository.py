from typing import List, Optional
from app.analytics.storage import AnalyticsStorage
from app.analytics.models import SessionAnalyticsSummary, TradeJournalEntry


class AnalyticsRepository:
    def __init__(self, storage: AnalyticsStorage = None):
        self.storage = storage or AnalyticsStorage()

    def save_journal(self, run_id: str, entries: List[TradeJournalEntry]):
        self.storage.save_journal(run_id, entries)

    def get_journal(self, run_id: str) -> List[TradeJournalEntry]:
        return self.storage.load_journal(run_id)

    def save_session_summary(self, summary: SessionAnalyticsSummary):
        self.storage.save_session_summary(summary)

    def get_session_summary(self, run_id: str) -> Optional[SessionAnalyticsSummary]:
        return self.storage.load_session_summary(run_id)
