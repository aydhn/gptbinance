class OrderLifecycleError(Exception):
    pass


class InvalidLifecycleTransitionError(OrderLifecycleError):
    pass


class DuplicateSubmitError(OrderLifecycleError):
    pass


class IdempotencyViolationError(OrderLifecycleError):
    pass


class VenueEventMappingError(OrderLifecycleError):
    pass


class OrphanOrderError(OrderLifecycleError):
    pass


class TimeoutResolutionError(OrderLifecycleError):
    pass


class ReplaceConflictError(OrderLifecycleError):
    pass


class CancelConflictError(OrderLifecycleError):
    pass


class LifecycleStorageError(OrderLifecycleError):
    pass
