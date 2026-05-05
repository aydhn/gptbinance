from app.market_truth.models import MarketTruthAuditRecord


class MarketTruthStorage:
    def __init__(self):
        self._records = []

    def save_audit_record(self, record: MarketTruthAuditRecord):
        self._records.append(record)
