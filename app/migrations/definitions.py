from app.migrations.models import (
    MigrationDefinition,
    MigrationScope,
    CompatibilityDeclaration,
    MigrationDependency,
)
from app.migrations.enums import (
    MigrationDomain,
    MigrationType,
    ApplyClass,
    ReversibilityClass,
    MigrationSeverity,
)


class MigrationDSL:
    @staticmethod
    def define(
        id: str,
        name: str,
        domain: MigrationDomain,
        type: MigrationType,
        version_from: str,
        version_to: str,
        scope: MigrationScope,
        compatibility: CompatibilityDeclaration,
        reversibility: ReversibilityClass,
        severity: MigrationSeverity,
        apply_class: ApplyClass,
        dependencies: list[MigrationDependency] = None,
        required_evidence: list[str] = None,
        required_approvals: int = 0,
        rollback_hints: str = "",
        description: str = "",
    ) -> MigrationDefinition:
        return MigrationDefinition(
            id=id,
            name=name,
            domain=domain,
            type=type,
            version_from=version_from,
            version_to=version_to,
            scope=scope,
            dependencies=dependencies or [],
            compatibility=compatibility,
            reversibility=reversibility,
            severity=severity,
            required_evidence=required_evidence or [],
            required_approvals=required_approvals,
            apply_class=apply_class,
            rollback_hints=rollback_hints,
            description=description,
        )
