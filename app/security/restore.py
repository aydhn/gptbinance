import os
import logging
from typing import Optional
from app.security.models import RestorePlan, RestoreResult
from app.security.enums import RestoreVerdict
from app.control.models import AuthorizationResult

logger = logging.getLogger(__name__)


class RestoreManager:
    def run_restore(
        self, plan: RestorePlan, auth_bundle: Optional[AuthorizationResult] = None
    ) -> RestoreResult:
        if not os.path.exists(plan.source_manifest_path):
            return RestoreResult(
                verdict=RestoreVerdict.UNSAFE, message="Source manifest not found"
            )

        if plan.dry_run:
            return RestoreResult(
                verdict=RestoreVerdict.DRY_RUN_SUCCESS,
                message="Dry run successful",
                restored_artifacts=["simulated_file.txt"],
            )

        if not auth_bundle or auth_bundle.verdict.value != "approved":
            logger.error(
                "Restore apply blocked: Missing or denied authorization bundle."
            )
            return RestoreResult(
                verdict=RestoreVerdict.UNSAFE, message="Authorization denied or missing"
            )

        # In a real restore, we would check for conflicts and copy files
        return RestoreResult(
            verdict=RestoreVerdict.SAFE_TO_RESTORE,
            message="Restore successful",
            restored_artifacts=["file1.txt"],
        )
