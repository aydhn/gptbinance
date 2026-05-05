class MigrationFabricError(Exception):
    pass


class InvalidMigrationDefinitionError(MigrationFabricError):
    pass


class DependencyResolutionError(MigrationFabricError):
    pass


class CompatibilityError(MigrationFabricError):
    pass


class IrreversibleMigrationError(MigrationFabricError):
    pass


class DryRunFailure(MigrationFabricError):
    pass


class ApplyPolicyViolation(MigrationFabricError):
    pass


class RollbackPlanningError(MigrationFabricError):
    pass


class VerificationFailure(MigrationFabricError):
    pass


class MigrationStorageError(MigrationFabricError):
    pass
