from typing import Dict, Any

class AdjudicationRegistryBase:
    def register(self, item: Any) -> str: pass
    def get(self, id: str) -> Any: pass

class DeterminationEvaluatorBase:
    def evaluate(self, determination: Any) -> Dict[str, Any]: pass

class DispositionEvaluatorBase:
    def evaluate(self, disposition: Any) -> Dict[str, Any]: pass

class TrustEvaluatorBase:
    def evaluate_trust(self, adjudication_id: str) -> str: pass
