from app.migrations.models import MigrationPlan, MigrationRollforwardPlan


class RollforwardPlanner:
    def plan(self, plan: MigrationPlan) -> MigrationRollforwardPlan:
        return MigrationRollforwardPlan(
            plan_id=plan.id,
            follow_up_migrations=["fix_script_v2"],
            quarantine_mode=True,
            degraded_compatibility_mode=True,
            recovery_path_suggestions=[
                "Review logs and apply missing patches manually"
            ],
            staged_stabilization_steps=[
                "Pause trading",
                "Verify schema",
                "Resume degraded",
            ],
        )
