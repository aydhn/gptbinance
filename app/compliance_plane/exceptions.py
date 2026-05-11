class CompliancePlaneError(Exception):
    """Base exception for compliance plane errors."""

    pass


class InvalidRequirementDefinition(CompliancePlaneError):
    pass


class InvalidControlMapping(CompliancePlaneError):
    pass


class InvalidEvidenceRequirement(CompliancePlaneError):
    pass


class InvalidAttestationState(CompliancePlaneError):
    pass


class InvalidCertificationState(CompliancePlaneError):
    pass


class ExceptionAcceptanceViolation(CompliancePlaneError):
    pass


class RetentionViolation(CompliancePlaneError):
    pass


class EquivalenceError(CompliancePlaneError):
    pass


class ComplianceStorageError(CompliancePlaneError):
    pass
