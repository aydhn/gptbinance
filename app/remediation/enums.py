from enum import Enum


class RemediationClass(str, Enum):
    READ_ONLY = "read_only"
    LOCAL_RECOMPUTE = "local_recompute"
    REVIEW_ONLY = "review_only"
    APPROVAL_BOUND_LOCAL = "approval_bound_local"
    VENUE_AFFECTING = "venue_affecting"  # NO DIRECT APPLY


class ApplyMode(str, Enum):
    DIRECT_SAFE = "direct_safe"
    REQUEST_GENERATION = "request_generation"
    MANUAL_INSTRUCTION = "manual_instruction"


class BlastRadiusSeverity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class VerificationVerdict(str, Enum):
    FIXED = "fixed"
    IMPROVED = "improved"
    UNCHANGED = "unchanged"
    REGRESSED = "regressed"
    NEEDS_REVIEW = "needs_review"


class DebtSeverity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"
    BLOCKER = "blocker"
