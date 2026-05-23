class AuthorityPlaneError(Exception):
    """Base class for Authority Plane errors."""
    pass

class InvalidAuthorityObjectError(AuthorityPlaneError):
    pass

class InvalidMandateError(AuthorityPlaneError):
    pass

class InvalidDelegationError(AuthorityPlaneError):
    pass

class InvalidRatificationError(AuthorityPlaneError):
    pass

class InvalidOverrideError(AuthorityPlaneError):
    pass

class InvalidQuorumError(AuthorityPlaneError):
    pass

class AuthorityOverreachViolation(AuthorityPlaneError):
    pass

class AuthorityStorageError(AuthorityPlaneError):
    pass
