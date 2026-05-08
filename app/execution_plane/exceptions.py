class ExecutionPlaneError(Exception):
    """Base exception for all execution plane errors."""

    pass


class InvalidVenueDefinitionError(ExecutionPlaneError):
    pass


class InvalidOrderSpecError(ExecutionPlaneError):
    pass


class VenueConstraintViolationError(ExecutionPlaneError):
    pass


class RoutingError(ExecutionPlaneError):
    pass


class IdempotencyViolationError(ExecutionPlaneError):
    pass


class CancelReplaceViolationError(ExecutionPlaneError):
    pass


class FillQualityError(ExecutionPlaneError):
    pass


class EquivalenceError(ExecutionPlaneError):
    pass


class ExecutionStorageError(ExecutionPlaneError):
    pass
