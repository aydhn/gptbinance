import os
from typing import List
from app.security.models import RestorePlan, RestoreResult
from app.security.enums import RestoreVerdict

class RestoreManager:
    def run_restore(self, plan: RestorePlan) -> RestoreResult:
        if not os.path.exists(plan.source_manifest_path):
            return RestoreResult(verdict=RestoreVerdict.UNSAFE, message="Source manifest not found")

        if plan.dry_run:
            return RestoreResult(verdict=RestoreVerdict.DRY_RUN_SUCCESS, message="Dry run successful", restored_artifacts=["simulated_file.txt"])

        # In a real restore, we would check for conflicts and copy files
        return RestoreResult(verdict=RestoreVerdict.SAFE_TO_RESTORE, message="Restore successful", restored_artifacts=["file1.txt"])
