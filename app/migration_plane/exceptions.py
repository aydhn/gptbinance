class MigrationPlaneError(Exception):
    pass

class InvalidMigrationDefinitionError(MigrationPlaneError):
    pass

class InvalidTransitionContractError(MigrationPlaneError):
    pass

class InvalidVersionPairError(MigrationPlaneError):
    pass

class CompatibilityViolationError(MigrationPlaneError):
    pass

class PrecheckViolationError(MigrationPlaneError):
    pass

class CutoverViolationError(MigrationPlaneError):
    pass

class RollbackViolationError(MigrationPlaneError):
    pass

class EquivalenceError(MigrationPlaneError):
    pass

class MigrationStorageError(MigrationPlaneError):
    pass
