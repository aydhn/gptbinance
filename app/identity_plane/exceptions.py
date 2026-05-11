class IdentityPlaneError(Exception):
    pass

class InvalidPrincipalDefinition(IdentityPlaneError):
    pass

class InvalidRoleAssignment(IdentityPlaneError):
    pass

class InvalidCapabilityGrant(IdentityPlaneError):
    pass

class InvalidSessionState(IdentityPlaneError):
    pass

class DelegationViolation(IdentityPlaneError):
    pass

class ImpersonationViolation(IdentityPlaneError):
    pass

class ElevationViolation(IdentityPlaneError):
    pass

class RevocationViolation(IdentityPlaneError):
    pass
