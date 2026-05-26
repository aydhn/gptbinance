# liquidation.py
from typing import Dict, List, Optional
from app.insolvency_plane.models import LiquidationRecord

class LiquidationManager:
    def __init__(self):
        self.liquidations: Dict[str, LiquidationRecord] = {}

    def register_liquidation(self, liquidation: LiquidationRecord):
        self.liquidations[liquidation.liquidation_id] = liquidation

    def get_liquidation(self, liquidation_id: str) -> Optional[LiquidationRecord]:
        return self.liquidations.get(liquidation_id)

    def list_liquidations(self) -> List[LiquidationRecord]:
        return list(self.liquidations.values())
