from app.migrations.models import MigrationPlan, MigrationPreflightReport
from app.migrations.enums import PreflightVerdict


class PreflightEngine:
    def run_preflight(self, plan: MigrationPlan) -> MigrationPreflightReport:
        # Mock checks for the preflight report
        blockers = []
        warnings = []

        # Example validation logic
        active_runtime_collision = False
        unresolved_remediation_debt = False
        policy_hard_blocks = []

        verdict = PreflightVerdict.PASS
        if (
            blockers
            or active_runtime_collision
            or unresolved_remediation_debt
            or policy_hard_blocks
        ):
            verdict = PreflightVerdict.BLOCK

        return MigrationPreflightReport(
            plan_id=plan.id,
            verdict=verdict,
            active_runtime_collision=active_runtime_collision,
            unresolved_remediation_debt=unresolved_remediation_debt,
            stale_qualification=False,
            policy_hard_blocks=policy_hard_blocks,
            backup_readiness=True,
            workspace_cleanliness=True,
            evidence_completeness=True,
            blockers=blockers,
            warnings=warnings,
        )
