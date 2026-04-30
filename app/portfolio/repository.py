from typing import Optional
from app.portfolio.storage import PortfolioStorage
from app.portfolio.models import PortfolioDecisionBatch, PortfolioSummary


class PortfolioRepository:
    def __init__(self, storage: PortfolioStorage = None):
        self.storage = storage or PortfolioStorage()

    def store_decision_batch(self, batch: PortfolioDecisionBatch):
        self.storage.save_batch(batch)

    def get_decision_batch(self, run_id: str) -> Optional[PortfolioDecisionBatch]:
        return self.storage.load_batch(run_id)

    def store_summary(self, summary: PortfolioSummary):
        self.storage.save_summary(summary)

    def get_summary(self, run_id: str) -> Optional[PortfolioSummary]:
        return self.storage.load_summary(run_id)
