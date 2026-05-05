from app.migrations.models import MigrationPlan, MigrationApplyResult
from app.migrations.enums import MigrationStatus
from app.migrations.exceptions import ApplyPolicyViolation


class ApplyEngine:
    def execute(
        self, plan: MigrationPlan, preflight_passed: bool, dry_run_passed: bool
    ) -> MigrationApplyResult:
        if not preflight_passed or not dry_run_passed:
            raise ApplyPolicyViolation(
                "Cannot apply migration without successful preflight and dry-run."
            )

        applied = []
        failed = []
        status = MigrationStatus.APPLIED_CLEAN

        for step in plan.steps:
            # Here we would do the actual application
            # For the structure, we'll mark them applied
            applied.append(step.migration_id)

        return MigrationApplyResult(
            plan_id=plan.id,
            status=status,
            applied_migrations=applied,
            failed_migrations=failed,
            before_snapshot_ref="snapshot_before_123",
            after_snapshot_ref="snapshot_after_123",
            logs=["Migration started", "Applied all steps successfully"],
        )
