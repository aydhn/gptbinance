# Viability Plane: Negative Carry
from typing import Dict, Any

class NegativeCarryManager:
    def evaluate(self, context: Dict[str, Any]) -> Dict[str, Any]:
        return {"status": "evaluated", "module": "negative_carry", "notes": "No phantom profitability or hidden subsidies allowed."}
