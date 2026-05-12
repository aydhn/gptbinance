class ReliabilityPlaneError(Exception):
    pass


class InvalidReliabilityDefinition(ReliabilityPlaneError):
    pass


class InvalidServiceProfile(ReliabilityPlaneError):
    pass


class InvalidSliDefinition(ReliabilityPlaneError):
    pass


class InvalidSloDefinition(ReliabilityPlaneError):
    pass


class InvalidBudgetPolicy(ReliabilityPlaneError):
    pass


class MaintenanceViolation(ReliabilityPlaneError):
    pass


class DegradedModeViolation(ReliabilityPlaneError):
    pass


class EquivalenceError(ReliabilityPlaneError):
    pass


class ReliabilityStorageError(ReliabilityPlaneError):
    pass
