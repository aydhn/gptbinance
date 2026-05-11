from enum import Enum


class RequirementClass(str, Enum):
    ACCESS_CONTROL = "access_control"
    CHANGE_MANAGEMENT = "change_management"
    INCIDENT_RESPONSE = "incident_response"
    POSTMORTEM_REMEDIATION = "postmortem_remediation"
    RELEASE_APPROVAL = "release_approval"
    WORKFLOW_EVIDENCE = "workflow_evidence"
    MODEL_DATA_INTEGRITY = "model_data_integrity"
    RECONCILIATION = "reconciliation"
    POLICY_EXCEPTION = "policy_exception"
    EVIDENCE_RETENTION = "evidence_retention"
    MIGRATION_SAFETY = "migration_safety"
    AUDIT_LOGGING = "audit_logging"


class ControlClass(str, Enum):
    PREVENTIVE = "preventive"
    DETECTIVE = "detective"
    CORRECTIVE = "corrective"
    COMPENSATING = "compensating"


class EvidenceClass(str, Enum):
    SYSTEM_LOG = "system_log"
    APPROVAL_RECEIPT = "approval_receipt"
    TEST_RESULT = "test_result"
    CONFIGURATION_SNAPSHOT = "configuration_snapshot"
    WORKFLOW_TRACE = "workflow_trace"
    REVIEW_RECORD = "review_record"


class AttestationClass(str, Enum):
    MANAGEMENT = "management"
    OPERATOR = "operator"
    REVIEWER = "reviewer"
    PERIODIC = "periodic"


class CertificationClass(str, Enum):
    INTERNAL = "internal"
    SCOPED = "scoped"
    TIME_BOUNDED = "time_bounded"


class ExceptionClass(str, Enum):
    SCOPE_BOUND = "scope_bound"
    TTL_BOUND = "ttl_bound"
    REASON_BOUND = "reason_bound"


class RetentionClass(str, Enum):
    HOT = "hot"
    ARCHIVE = "archive"
    IMMUTABLE = "immutable"


class AuditReadinessClass(str, Enum):
    READY = "ready"
    NEEDS_REVIEW = "needs_review"
    GAPS_IDENTIFIED = "gaps_identified"
    UNPREPARED = "unprepared"


class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    PARTIAL = "partial"
    DIVERGENT = "divergent"
    UNKNOWN = "unknown"


class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
