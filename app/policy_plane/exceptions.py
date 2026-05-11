class PolicyPlaneError(Exception):
    pass


class InvalidPolicyDefinition(PolicyPlaneError):
    pass


class InvalidContextMapping(PolicyPlaneError):
    pass


class InvalidVerdict(PolicyPlaneError):
    pass


class PrecedenceViolation(PolicyPlaneError):
    pass


class ConflictResolutionViolation(PolicyPlaneError):
    pass


class ExceptionViolation(PolicyPlaneError):
    pass


class WaiverViolation(PolicyPlaneError):
    pass


class EquivalenceError(PolicyPlaneError):
    pass


class PolicyStorageError(PolicyPlaneError):
    pass
