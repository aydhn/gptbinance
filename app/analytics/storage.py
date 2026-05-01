import json
import os
from typing import List, Optional
from app.analytics.models import SessionAnalyticsSummary, TradeJournalEntry


class AnalyticsStorage:
    def __init__(self, base_path: str = "data/analytics"):
        self.base_path = base_path
        os.makedirs(self.base_path, exist_ok=True)

    def _get_run_path(self, run_id: str) -> str:
        path = os.path.join(self.base_path, run_id)
        os.makedirs(path, exist_ok=True)
        return path

    def save_journal(self, run_id: str, entries: List[TradeJournalEntry]):
        path = os.path.join(self._get_run_path(run_id), "journal.json")
        with open(path, "w") as f:
            json.dump([e.model_dump(mode="json") for e in entries], f, indent=2)

    def load_journal(self, run_id: str) -> List[TradeJournalEntry]:
        path = os.path.join(self._get_run_path(run_id), "journal.json")
        if not os.path.exists(path):
            return []
        with open(path, "r") as f:
            data = json.load(f)
        return [TradeJournalEntry(**d) for d in data]

    def save_session_summary(self, summary: SessionAnalyticsSummary):
        path = os.path.join(self._get_run_path(summary.run_id), "session_summary.json")
        with open(path, "w") as f:
            json.dump(summary.model_dump(mode="json"), f, indent=2)

    def load_session_summary(self, run_id: str) -> Optional[SessionAnalyticsSummary]:
        path = os.path.join(self._get_run_path(run_id), "session_summary.json")
        if not os.path.exists(path):
            return None
        with open(path, "r") as f:
            data = json.load(f)
        return SessionAnalyticsSummary(**data)
