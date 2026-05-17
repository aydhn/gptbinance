from enum import Enum

class ChangeClass(str, Enum):
    STANDARD = "standard"
    NORMAL = "normal"
    EMERGENCY = "emergency"
    FREEZE_EXCEPTION = "freeze_exception"
    NO_OP = "no_op"
    CONFIGURATION_ONLY = "configuration_only"

class RequestClass(str, Enum):
    INFRASTRUCTURE = "infrastructure"
    RUNTIME = "runtime"
    GOVERNANCE = "governance"
    DOCUMENTATION = "documentation"
    RECOVERY = "recovery"
    PLANNED = "planned"
    PROTECTIVE = "protective"

class ApprovalClass(str, Enum):
    PRE_APPROVED = "pre_approved"
    NORMAL_APPROVAL = "normal_approval"
    EMERGENCY_APPROVAL = "emergency_approval"
    EXCEPTION_APPROVAL = "exception_approval"

class WindowClass(str, Enum):
    NORMAL = "normal"
    RELEASE = "release"
    MAINTENANCE = "maintenance"
    EMERGENCY = "emergency"

class BlastRadiusClass(str, Enum):
    LOCAL = "local"
    CROSS_PLANE = "cross_plane"
    RELEASE_STAGE = "release_stage"
    UNKNOWN = "unknown"

class ExecutionClass(str, Enum):
    PLANNED = "planned"
    EMERGENCY = "emergency"
    MANUAL = "manual"
    AUTOMATED = "automated"

class RollbackClass(str, Enum):
    TESTED_READY = "tested_ready"
    PLAN_ONLY = "plan_only"
    PARTIAL = "partial"
    NOT_FEASIBLE = "not_feasible"

class VerificationClass(str, Enum):
    PRE_CHANGE = "pre_change"
    POST_CHANGE = "post_change"
    DOWNSTREAM = "downstream"
    NEGATIVE = "negative"
    UNVERIFIED = "unverified"

class FreezeClass(str, Enum):
    RELEASE_FREEZE = "release_freeze"
    INCIDENT_FREEZE = "incident_freeze"
    COMPLIANCE_FREEZE = "compliance_freeze"
    CALENDAR_FREEZE = "calendar_freeze"

class ExceptionClass(str, Enum):
    EMERGENCY = "emergency"
    FREEZE = "freeze"
    VERIFICATION = "verification"
    ROLLBACK_GAP = "rollback_gap"

class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    PARTIAL = "partial"
    DIVERGENT = "divergent"

class ChangeTrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
