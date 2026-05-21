from typing import Dict, Any, List
from .models import TradeoffObject, TradeoffEquivalenceReport
from .enums import EquivalenceVerdict

class TradeoffEquivalenceEvaluator:
    def evaluate(self, envs: List[str], tradeoff_objs: Dict[str, TradeoffObject]) -> TradeoffEquivalenceReport:
        if len(envs) < 2:
            return TradeoffEquivalenceReport(
                report_id="eq-single",
                environments_compared=envs,
                verdict=EquivalenceVerdict.EQUIVALENT,
                divergence_sources=[]
            )

        base_env = envs[0]
        base_obj = tradeoff_objs.get(base_env)

        divergences = []
        verdict = EquivalenceVerdict.EQUIVALENT

        if not base_obj:
            return TradeoffEquivalenceReport(
                report_id="eq-missing-base",
                environments_compared=envs,
                verdict=EquivalenceVerdict.DIVERGENT,
                divergence_sources=["missing_base_object"]
            )

        for env in envs[1:]:
            obj = tradeoff_objs.get(env)
            if not obj:
                divergences.append(f"missing_object_in_{env}")
                verdict = EquivalenceVerdict.DIVERGENT
                continue

            # Compare objectives
            base_obj_ids = {o.objective_id for o in base_obj.objective_set.objectives}
            obj_ids = {o.objective_id for o in obj.objective_set.objectives}

            if base_obj_ids != obj_ids:
                divergences.append(f"objective_divergence_in_{env}")
                verdict = EquivalenceVerdict.DIVERGENT

            # Compare burdens
            base_burden_ids = {b.burden_id for b in base_obj.burden_posture}
            obj_burden_ids = {b.burden_id for b in obj.burden_posture}

            if base_burden_ids != obj_burden_ids:
                 divergences.append(f"burden_divergence_in_{env}")
                 verdict = EquivalenceVerdict.DIVERGENT

        return TradeoffEquivalenceReport(
            report_id=f"eq-{base_env}",
            environments_compared=envs,
            verdict=verdict,
            divergence_sources=divergences
        )

equivalence_evaluator = TradeoffEquivalenceEvaluator()
