class PerformanceSecurityPlaneError(Exception):
    pass

class InvalidSecurityObjectError(PerformanceSecurityPlaneError):
    pass

class InvalidSecuredObligationError(PerformanceSecurityPlaneError):
    pass

class InvalidDrawError(PerformanceSecurityPlaneError):
    pass

class InvalidReleaseError(PerformanceSecurityPlaneError):
    pass

class InvalidSubstituteCollateralError(PerformanceSecurityPlaneError):
    pass

class InvalidValuationError(PerformanceSecurityPlaneError):
    pass

class PhantomCollateralViolationError(PerformanceSecurityPlaneError):
    pass

class SecurityStorageError(PerformanceSecurityPlaneError):
    pass
