from app.release.models import UpgradePlan, UpgradeResult, ReleaseManifest
from app.release.compatibility import CompatibilityChecker
from app.release.migrations import MigrationExecutor
from app.release.enums import UpgradeVerdict, CompatibilityVerdict, MigrationDirection
from datetime import datetime, timezone
import logging

logger = logging.getLogger(__name__)

class UpgradePlanner:
    def __init__(self):
        self.compat_checker = CompatibilityChecker()
        self.mig_executor = MigrationExecutor()

    def create_plan(self, target_release: ReleaseManifest) -> UpgradePlan:
        compat = self.compat_checker.check(target_release)

        mig_plan = None
        if compat.verdict == CompatibilityVerdict.MIGRATION_REQUIRED:
            mig_plan = self.mig_executor.create_plan(
                compat.current_version,
                compat.target_version,
                MigrationDirection.UPGRADE
            )

        verdict = UpgradeVerdict.PASS
        warnings = []

        if compat.verdict == CompatibilityVerdict.INCOMPATIBLE:
            verdict = UpgradeVerdict.FAIL
            warnings.append("Incompatible release.")

        return UpgradePlan(
            target_release=target_release,
            compatibility_report=compat,
            migration_plan=mig_plan,
            verdict=verdict,
            warnings=warnings
        )

    def run_dry_run(self, plan: UpgradePlan) -> UpgradeResult:
        logger.info(f"Running upgrade dry run to {plan.target_release.version.version}")
        return UpgradeResult(
            plan=plan,
            success=True,
            applied_at=datetime.now(timezone.utc)
        )
