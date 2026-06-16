from typing import Dict, Any, List

class CollateralEvaluatorBase:
    def evaluate(self, collateral_id: str) -> Dict[str, Any]:
        raise NotImplementedError

class LiquidationEvaluatorBase:
    def evaluate_liquidation(self, liquidation_id: str) -> Dict[str, Any]:
        raise NotImplementedError
