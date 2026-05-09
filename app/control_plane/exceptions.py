class ControlPlaneError(Exception):
    pass


class InvalidCommandDefinitionError(ControlPlaneError):
    pass


class InvalidActionRequestError(ControlPlaneError):
    pass


class InvalidPreviewStateError(ControlPlaneError):
    pass


class ApprovalViolationError(ControlPlaneError):
    pass


class ExceptionTokenViolationError(ControlPlaneError):
    pass


class RollbackViolationError(ControlPlaneError):
    pass


class ScopeViolationError(ControlPlaneError):
    pass


class ControlStorageError(ControlPlaneError):
    pass


class EquivalenceError(ControlPlaneError):
    pass
