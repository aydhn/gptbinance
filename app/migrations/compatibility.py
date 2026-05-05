from app.migrations.models import (
    MigrationDefinition,
    CompatibilityCheckResult,
    CompatibilityMatrix,
)
from app.migrations.enums import CompatibilityVerdict


class CompatibilityEvaluator:
    def evaluate(
        self, migration: MigrationDefinition, current_matrix: CompatibilityMatrix
    ) -> CompatibilityCheckResult:
        blockers = []
        warnings = []
        verdict = CompatibilityVerdict.SAFE

        decl = migration.compatibility
        if not decl.backward_compatible:
            warnings.append(
                "Migration is not backward compatible. Rollback might require manual intervention."
            )
            verdict = CompatibilityVerdict.SAFE_WITH_CAUTION

        if not decl.mixed_version_safe:
            blockers.append(
                "Migration is not mixed-version safe. All instances must be upgraded simultaneously."
            )
            verdict = CompatibilityVerdict.INCOMPATIBLE

        # In a real implementation, we'd check against current_matrix for known conflicts
        if migration.id in current_matrix.known_conflicts:
            blockers.append(
                f"Migration {migration.id} has a known conflict in current matrix."
            )
            verdict = CompatibilityVerdict.INCOMPATIBLE

        if blockers:
            verdict = CompatibilityVerdict.INCOMPATIBLE

        return CompatibilityCheckResult(
            verdict=verdict,
            blockers=blockers,
            warnings=warnings,
            safe_window_notes=decl.notes,
        )
