from typing import Dict, List, Optional
from .models import TradeoffObject, TradeoffTrustVerdict
from .storage import tradeoff_storage

class TradeoffRepository:
    def get_latest_trusted_tradeoff(self, tradeoff_id: str) -> Optional[TradeoffObject]:
        # Simplification: just return the object from storage
        return tradeoff_storage.get_object(tradeoff_id)

    def get_tradeoff_history(self, tradeoff_id: str) -> List[TradeoffObject]:
        obj = tradeoff_storage.get_object(tradeoff_id)
        return [obj] if obj else []

tradeoff_repository = TradeoffRepository()
