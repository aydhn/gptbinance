from typing import List, Dict
from app.migrations.models import CompatibilityMatrix
from app.migrations.enums import MigrationDomain


class CompatibilityMatrixBuilder:
    def build(
        self,
        current_versions: Dict[MigrationDomain, str],
        known_conflicts: List[str] = None,
    ) -> CompatibilityMatrix:
        return CompatibilityMatrix(
            domain_versions=current_versions,
            mixed_version_safety=False if known_conflicts else True,
            known_conflicts=known_conflicts or [],
        )
