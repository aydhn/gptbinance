class SecurityPlaneError(Exception):
    pass

class InvalidSecurityAssetError(SecurityPlaneError):
    pass

class InvalidTrustBoundaryError(SecurityPlaneError):
    pass

class InvalidSecretDefinitionError(SecurityPlaneError):
    pass

class InvalidCredentialLifecycleStateError(SecurityPlaneError):
    pass

class VulnerabilityAssessmentViolationError(SecurityPlaneError):
    pass

class ExposureViolationError(SecurityPlaneError):
    pass

class RotationViolationError(SecurityPlaneError):
    pass

class PatchViolationError(SecurityPlaneError):
    pass

class SecurityStorageError(SecurityPlaneError):
    pass
