from app.migrations.models import (
    MigrationPlan,
    MigrationRollbackPlan,
    MigrationDefinition,
)
from app.migrations.enums import RollbackStrategy, ReversibilityClass


class RollbackPlanner:
    def plan(
        self, plan: MigrationPlan, migrations: list[MigrationDefinition]
    ) -> MigrationRollbackPlan:
        eligible = True
        strategy = RollbackStrategy.MANUAL_SCRIPT
        risks = []

        for mig in migrations:
            if mig.reversibility == ReversibilityClass.NON_REVERSIBLE:
                eligible = False
                strategy = RollbackStrategy.NOT_SUPPORTED
                risks.append(f"Migration {mig.id} is non-reversible.")

        return MigrationRollbackPlan(
            plan_id=plan.id,
            eligible=eligible,
            strategy=strategy,
            steps=["Restore from before snapshot"] if eligible else [],
            risks=risks,
        )
