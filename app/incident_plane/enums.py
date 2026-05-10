from enum import Enum

class IncidentSeverity(str, Enum):
    SEV0_EMERGENCY = "sev0_emergency"
    SEV1_HIGH = "sev1_high"
    SEV2_MEDIUM = "sev2_medium"
    SEV3_LOW = "sev3_low"
    ADVISORY_ONLY = "advisory_only"

class IncidentUrgency(str, Enum):
    IMMEDIATE = "immediate"
    TIME_BOUNDED = "time_bounded"
    REVIEW_WINDOW = "review_window"
    BACKLOG = "backlog"

class IncidentStatus(str, Enum):
    DETECTED = "detected"
    TRIAGING = "triaging"
    INVESTIGATING = "investigating"
    CONTAINING = "containing"
    STABILIZED = "stabilized"
    RECOVERING = "recovering"
    VERIFYING = "verifying"
    RESOLVED = "resolved"
    CLOSED = "closed"
    REOPENED = "reopened"
    FALSE_POSITIVE = "false_positive"

class VerificationVerdict(str, Enum):
    VERIFIED = "verified"
    FAILED = "failed"
    PENDING_QUIET_PERIOD = "pending_quiet_period"
    INCONCLUSIVE = "inconclusive"

class IncidentTrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
