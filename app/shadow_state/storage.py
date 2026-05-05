from app.shadow_state.models import ShadowTwinSnapshot, ConvergenceRun, RemediationPlan


class ShadowStorage:
    def __init__(self):
        self._twins = {}
        self._runs = {}
        self._plans = {}

    def save_twin(self, twin: ShadowTwinSnapshot):
        self._twins[twin.twin_id] = twin

    def save_run(self, run: ConvergenceRun):
        self._runs[run.run_id] = run

    def save_plan(self, plan: RemediationPlan):
        self._plans[plan.plan_id] = plan


shadow_storage = ShadowStorage()
