from pydantic import BaseModel
from typing import Optional
from app.migrations.models import (
    MigrationPreflightReport,
    MigrationDryRunResult,
    MigrationApplyResult,
    MigrationVerificationResult,
    CompatibilityCheckResult,
)


class MigrationEvidenceBundle(BaseModel):
    plan_id: str
    compatibility_report: Optional[CompatibilityCheckResult] = None
    preflight_report: Optional[MigrationPreflightReport] = None
    dry_run_result: Optional[MigrationDryRunResult] = None
    apply_result: Optional[MigrationApplyResult] = None
    verification_result: Optional[MigrationVerificationResult] = None

    def is_complete(self) -> bool:
        return all(
            [
                self.compatibility_report,
                self.preflight_report,
                self.dry_run_result,
                self.apply_result,
                self.verification_result,
            ]
        )
