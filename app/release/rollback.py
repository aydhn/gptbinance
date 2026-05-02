from app.release.models import RollbackPlan, RollbackResult, ReleaseManifest
from app.release.compatibility import CompatibilityChecker
from app.release.migrations import MigrationExecutor
from app.release.enums import RollbackVerdict, CompatibilityVerdict, MigrationDirection
from app.control.models import AuthorizationResult
from datetime import datetime, timezone
import logging

logger = logging.getLogger(__name__)


class RollbackPlanner:
    def __init__(self):
        self.compat_checker = CompatibilityChecker()
        self.mig_executor = MigrationExecutor()

    def create_plan(self, target_release: ReleaseManifest) -> RollbackPlan:
        compat = self.compat_checker.check(target_release)

        mig_plan = None
        if compat.verdict == CompatibilityVerdict.MIGRATION_REQUIRED:
            mig_plan = self.mig_executor.create_plan(
                compat.current_version,
                compat.target_version,
                MigrationDirection.DOWNGRADE,
            )

        verdict = RollbackVerdict.PASS
        warnings = []

        if compat.verdict == CompatibilityVerdict.INCOMPATIBLE:
            verdict = RollbackVerdict.FAIL
            warnings.append("Incompatible release for rollback.")

        return RollbackPlan(
            target_release=target_release,
            compatibility_report=compat,
            migration_plan=mig_plan,
            verdict=verdict,
            warnings=warnings,
        )

    def run_dry_run(self, plan: RollbackPlan) -> RollbackResult:
        logger.info(
            f"Running rollback dry run to {plan.target_release.version.version}"
        )
        return RollbackResult(
            plan=plan, success=True, applied_at=datetime.now(timezone.utc)
        )

    def apply_rollback(
        self, plan: RollbackPlan, auth_bundle: AuthorizationResult
    ) -> RollbackResult:
        if not auth_bundle or auth_bundle.verdict.value != "approved":
            logger.error(
                "Rollback apply blocked: Missing or denied authorization bundle."
            )
            return RollbackResult(
                plan=plan, success=False, applied_at=datetime.now(timezone.utc)
            )

        logger.info(f"Applying rollback to {plan.target_release.version.version}")
        return RollbackResult(
            plan=plan, success=True, applied_at=datetime.now(timezone.utc)
        )
