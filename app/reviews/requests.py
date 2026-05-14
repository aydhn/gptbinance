from enum import Enum
class IdentityIntegrityReview:
    pass


class ObservabilityIntegrityReview:
    pass


class TelemetrySchemaReview:
    pass


class SamplingReview:
    pass


class RetentionReview:
    pass


class DiagnosticSignalReview:
    pass


class ComplianceIntegrityReview:
    pass


class AttestationReview:
    pass


class CertificationReview:
    pass


class AuditReadinessReview:
    pass

class SecurityIntegrityReviewRequest:
    pass

class SecretRotationReviewRequest:
    pass

class VulnerabilityExploitabilityReviewRequest:
    pass

class TrustBoundaryReviewRequest:
    pass

class PatchVerificationReviewRequest:
    pass

class SecurityExceptionReviewRequest:
    pass

class ReviewClass(str, Enum):
    DECISION_INTEGRITY_REVIEW = 'decision_integrity_review'
    OPTION_SET_REVIEW = 'option_set_review'