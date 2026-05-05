from app.migrations.rollback import RollbackPlanner
from app.migrations.models import MigrationPlan


class ReleaseRollbackManager:
    def __init__(self):
        self.planner = RollbackPlanner()

    def check_rollback(self, plan: MigrationPlan, migrations):
        rollback_plan = self.planner.plan(plan, migrations)
        if not rollback_plan.eligible:
            return "Rollback not supported due to irreversible state migrations."
        return "Rollback eligible"
