class QualificationError(Exception):
    """Base exception for qualification errors."""

    pass


class InvalidQualificationProfileError(QualificationError):
    """Raised when an unknown or invalid profile is requested."""

    pass


class MissingEvidenceError(QualificationError):
    """Raised when mandatory evidence is missing."""

    pass


class TraceabilityError(QualificationError):
    """Raised when requirements are untraced or incorrectly mapped."""

    pass


class ContractVerificationError(QualificationError):
    """Raised when component contracts are violated."""

    pass


class ForbiddenActionVerificationError(QualificationError):
    """Raised when a forbidden action is allowed (which is a failure of the safety mechanism)."""

    pass


class WaiverPolicyViolationError(QualificationError):
    """Raised when waiver policy is violated (e.g., waiving a critical live safety finding)."""

    pass


class CertificationEvaluationError(QualificationError):
    """Raised when there is an error evaluating the final certification verdict."""

    pass


class EvidencePackError(QualificationError):
    """Raised when assembling the evidence pack fails."""

    pass
