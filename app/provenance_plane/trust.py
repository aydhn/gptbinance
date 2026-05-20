from typing import Dict, Any, List
from .enums import TrustVerdictEnum
from .registry import registry

class ProvenanceTrustEvaluator:
    def evaluate_trust(self, obj_id: str) -> str:
        obj = registry.get(obj_id)
        if not obj: return TrustVerdictEnum.BLOCKED
        if obj.get("custody_gap", False): return TrustVerdictEnum.CAUTION
        if not obj.get("attribution"): return TrustVerdictEnum.REVIEW_REQUIRED
        return TrustVerdictEnum.TRUSTED

trust_evaluator = ProvenanceTrustEvaluator()
