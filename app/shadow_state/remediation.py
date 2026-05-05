import uuid
from typing import List
from app.shadow_state.models import ConvergenceRun, RemediationPlan, RemediationStep
from app.shadow_state.enums import ConvergenceVerdict, RemediationClass, ShadowDomain


class RemediationPlanner:
    def plan(self, run: ConvergenceRun) -> RemediationPlan:
        steps: List[RemediationStep] = []

        if run.global_verdict == ConvergenceVerdict.CLEAN:
            return RemediationPlan(
                plan_id=f"plan_{uuid.uuid4().hex[:8]}",
                run_ref=run.run_id,
                steps=[],
                requires_review=False,
            )

        orders_result = run.domain_results.get(ShadowDomain.ORDERS.value)
        if orders_result and orders_result.verdict in [
            ConvergenceVerdict.SUSPICIOUS_DIVERGENCE,
            ConvergenceVerdict.CRITICAL_DIVERGENCE,
        ]:
            steps.append(
                RemediationStep(
                    step_id=f"step_{uuid.uuid4().hex[:8]}",
                    remediation_class=RemediationClass.LIFECYCLE_REVIEW,
                    description="Review order lifecycle orphans against venue truth",
                )
            )

        modes_result = run.domain_results.get(ShadowDomain.MODES.value)
        if (
            modes_result
            and modes_result.verdict == ConvergenceVerdict.CRITICAL_DIVERGENCE
        ):
            steps.append(
                RemediationStep(
                    step_id=f"step_{uuid.uuid4().hex[:8]}",
                    remediation_class=RemediationClass.MODE_REFRESH,
                    description="Force refresh local mode belief from venue",
                )
            )

        return RemediationPlan(
            plan_id=f"plan_{uuid.uuid4().hex[:8]}",
            run_ref=run.run_id,
            steps=steps,
            requires_review=True,
        )


remediation_planner = RemediationPlanner()
