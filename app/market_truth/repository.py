from app.market_truth.storage import MarketTruthStorage


class MarketTruthRepository:
    def __init__(self, storage: MarketTruthStorage):
        self.storage = storage

    def get_latest_truthfulness(self, symbol: str):
        for rec in reversed(self.storage._records):
            if rec.evidence_bundle.symbol == symbol:
                return rec.evidence_bundle
        return None
