class ControlError(Exception):
    """Base exception for the control module."""

    pass


class InvalidActionRequest(ControlError):
    pass


class ApprovalPolicyViolation(ControlError):
    pass


class AuthorizationDenied(ControlError):
    pass


class StaleApprovalError(ControlError):
    pass


class BreakGlassViolation(ControlError):
    pass


class OperatorIdentityError(ControlError):
    pass


class CommandJournalIntegrityError(ControlError):
    pass


class ApprovalExpiryError(ControlError):
    pass
