from enum import Enum

class AutonomyClass(str, Enum):
    ADVISORY = "advisory"
    BOUNDED_SELF_HEALING = "bounded_self_healing"
    DRIFT_RESPONSE = "drift_response"
    ADAPTATION_SUPPORT = "adaptation_support"
    ASSURANCE_MONITORING = "assurance_monitoring"
    RELEASE_SAFETY = "release_safety"
    MIGRATION_GUARDED = "migration_guarded"
    BENEFICIARY_PROTECTION = "beneficiary_protection"
    FEDERATED_DELEGATION = "federated_delegation"
    POLICY_ENFORCED = "policy_enforced"
    OVERRIDE_SENSITIVE = "override_sensitive"
    CROSS_PLANE_BOUNDED_EXECUTION = "cross_plane_bounded_execution"

class MandateClass(str, Enum):
    NARROW = "narrow"
    BROAD = "broad"
    AMBIGUOUS = "ambiguous"
    STALE = "stale"

class GrantClass(str, Enum):
    VALID = "valid"
    CONDITIONAL = "conditional"
    EXPIRING = "expiring"
    UNSAFE = "unsafe"

class ScopeClass(str, Enum):
    BOUNDED = "bounded"
    FEDERATED = "federated"
    DISPUTED = "disputed"
    OVERCLAIMED = "overclaimed"

class ReviewClass(str, Enum):
    REQUIRED = "required"
    WAIVED = "waived"
    BYPASSED = "bypassed"
    COSMETIC = "cosmetic"

class OverrideClass(str, Enum):
    VALID = "valid"
    EMERGENCY = "emergency"
    FAILED = "failed"
    INVISIBLE = "invisible"

class ConfidenceClass(str, Enum):
    VALID = "valid"
    OVERCONFIDENT = "overconfident"
    UNDERCONFIDENT = "underconfident"
    MISMATCHED = "mismatched"

class EscalationClass(str, Enum):
    TIMELY = "timely"
    LATE = "late"
    MISSING = "missing"
    EXCESSIVE = "excessive"

class RevocationClass(str, Enum):
    IMMEDIATE = "immediate"
    CONDITIONAL = "conditional"
    DELAYED = "delayed"
    MISSING_TRIGGER = "missing_trigger"

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
