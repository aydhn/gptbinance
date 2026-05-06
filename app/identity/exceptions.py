class IdentityPlaneError(Exception):
    pass


class InvalidPrincipalError(IdentityPlaneError):
    pass


class InvalidRoleBindingError(IdentityPlaneError):
    pass


class InvalidCapabilityGrantError(IdentityPlaneError):
    pass


class SessionViolationError(IdentityPlaneError):
    pass


class ScopeClaimViolationError(IdentityPlaneError):
    pass


class DelegationViolationError(IdentityPlaneError):
    pass


class ElevationViolationError(IdentityPlaneError):
    pass


class BreakglassViolationError(IdentityPlaneError):
    pass


class AuthorizationStorageError(IdentityPlaneError):
    pass
