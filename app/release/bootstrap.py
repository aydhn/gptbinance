from app.release.models import BootstrapResult, InstallPlan
from app.release.enums import InstallVerdict
from datetime import datetime, timezone
import os
import logging

logger = logging.getLogger(__name__)


class Bootstrapper:
    def bootstrap(self, plan: InstallPlan) -> BootstrapResult:
        logger.info("Bootstrapping environment...")

        required_dirs = ["data", "config", "logs", "data/backups", "data/release"]
        for d in required_dirs:
            os.makedirs(d, exist_ok=True)

        success = True
        error_msg = None

        if plan.verdict == InstallVerdict.FAIL:
            success = False
            error_msg = "Install plan verdict is FAIL, aborting bootstrap."

        return BootstrapResult(
            plan=plan,
            success=success,
            applied_at=datetime.now(timezone.utc),
            error_message=error_msg,
        )
