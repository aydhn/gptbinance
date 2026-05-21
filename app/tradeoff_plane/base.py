from typing import Dict, Any, List

class TradeoffRegistryBase:
    def register(self, tradeoff_obj: Any) -> None:
        raise NotImplementedError

    def get(self, tradeoff_id: str) -> Any:
        raise NotImplementedError

    def list_all(self) -> List[Any]:
        raise NotImplementedError

class DominanceEvaluatorBase:
    def evaluate(self, options: List[Any]) -> Any:
        raise NotImplementedError

class FrontierEvaluatorBase:
    def evaluate(self, tradeoffs: List[Any]) -> Any:
        raise NotImplementedError

class TrustEvaluatorBase:
    def evaluate(self, tradeoff_obj: Any) -> Any:
        raise NotImplementedError
