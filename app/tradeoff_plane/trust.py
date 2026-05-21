from datetime import datetime
from typing import Dict, List, Any
from .models import TradeoffObject, TradeoffTrustVerdict
from .enums import TrustVerdict
from .base import TrustEvaluatorBase

class TradeoffTrustEvaluator(TrustEvaluatorBase):
    def evaluate(self, tradeoff_obj: TradeoffObject) -> TradeoffTrustVerdict:
        factors = {}
        verdict = TrustVerdict.TRUSTED

        # Objective Clarity
        if not tradeoff_obj.objective_set or not tradeoff_obj.objective_set.objectives:
            factors["objective_clarity"] = "missing_objectives"
            verdict = TrustVerdict.BLOCKED
        else:
            factors["objective_clarity"] = "clear"

        # Burden Visibility
        if not tradeoff_obj.burden_posture:
             factors["burden_visibility"] = "no_burdens_declared"
             if verdict == TrustVerdict.TRUSTED:
                 verdict = TrustVerdict.CAUTION
        else:
            has_hidden = any(b.is_hidden for b in tradeoff_obj.burden_posture)
            if has_hidden:
                factors["burden_visibility"] = "hidden_burdens_detected"
                verdict = TrustVerdict.DEGRADED
            else:
                factors["burden_visibility"] = "visible"

        # Sacrifice Explicitness
        if not tradeoff_obj.sacrifices:
             factors["sacrifice_explicitness"] = "no_sacrifices_declared"
        else:
             factors["sacrifice_explicitness"] = "explicit"

        return TradeoffTrustVerdict(
            verdict_id=f"tr-trust-{tradeoff_obj.tradeoff_id}-{int(datetime.utcnow().timestamp())}",
            tradeoff_id=tradeoff_obj.tradeoff_id,
            verdict=verdict,
            factors=factors
        )

trust_evaluator = TradeoffTrustEvaluator()
