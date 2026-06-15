from enum import Enum

class WarrantyClass(Enum):
    ATTESTED_STATE = "attested_state"
    REMEDY_DELIVERY = "remedy_delivery"
    COMPLIANCE_BACKING = "compliance_backing"
    SUCCESSOR_CLEANUP = "successor_cleanup"
    SUNSET_DISABLEMENT = "sunset_disablement"
    CONTROL_STATE = "control_state"
    ROLLBACK_CLEAN_STATE = "rollback_clean_state"
    FEDERATED_BACKING = "federated_backing"
    CROSS_PLANE_CLAIM_BACKING = "cross_plane_claim_backing"
    UNKNOWN = "unknown"

class ClaimClass(Enum):
    BOUNDED_CLEAN_STATE = "bounded_clean_state"
    CONDITIONAL = "conditional"
    OVERBROAD = "overbroad"
    UNSUPPORTED = "unsupported"
    LAUNDERED = "laundered"

class WarrantorClass(Enum):
    DIRECT = "direct"
    DELEGATED = "delegated"
    EXTERNAL = "external"
    SHADOW = "shadow"

class CoverageClass(Enum):
    BOUNDED = "bounded"
    PARTIAL = "partial"
    BROAD = "broad"
    HIDDEN_GAP = "hidden_gap"

class ExclusionClass(Enum):
    CLEAR = "clear"
    NARROW = "narrow"
    OVERBROAD = "overbroad"
    HIDDEN = "hidden"
    WARRANTY_SWALLOWING = "warranty_swallowing"

class BreachClass(Enum):
    FULL = "full"
    PARTIAL = "partial"
    DISPUTED = "disputed"
    HIDDEN = "hidden"

class CureClass(Enum):
    VALID = "valid"
    PARTIAL = "partial"
    COSMETIC = "cosmetic"
    UNCURED = "uncured"

class ValidityClass(Enum):
    BOUNDED = "bounded"
    NARROW = "narrow"
    OVERLONG = "overlong"
    MISSING = "missing"

class DebtClass(Enum):
    STALE_COVERAGE = "stale_coverage"
    HIDDEN_DISCLAIMER = "hidden_disclaimer"
    CURE_FAILURE = "cure_failure"
    CONTRADICTION = "contradiction"
    ILLUSORY_BACKING = "illusory_backing"

class WarrantyEquivalenceVerdictEnum(Enum):
    EQUIVALENT = "equivalent"
    PARTIAL_DIVERGENCE = "partial_divergence"
    FULL_DIVERGENCE = "full_divergence"
    UNKNOWN = "unknown"

class WarrantyTrustVerdictEnum(Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
