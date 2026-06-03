# Viability Plane: Burn
from typing import Dict, Any

class BurnManager:
    def evaluate(self, context: Dict[str, Any]) -> Dict[str, Any]:
        return {"status": "evaluated", "module": "burn", "notes": "No phantom profitability or hidden subsidies allowed."}
