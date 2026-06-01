from enum import Enum, auto

class DriftClass(Enum):
    POST_NORMALIZATION_DRIFT = auto()
    POST_RECAPITALIZATION_DRIFT = auto()
    POST_RESOLUTION_RECURRENCE_DRIFT = auto()
    POST_INSOLVENCY_EROSION_DRIFT = auto()
    CUSTOMER_IMPACT_REBOUND_DRIFT = auto()
    COMPLIANCE_EROSION_DRIFT = auto()
    SECURITY_HARDENING_DECAY_DRIFT = auto()
    MIGRATION_REGRESSION_DRIFT = auto()
    RELEASE_REGRESSION_RECURRENCE_DRIFT = auto()
    FEDERATED_ALIGNMENT_DRIFT = auto()
    GUARDRAIL_RETIREMENT_DRIFT = auto()
    CROSS_PLANE_STABILITY_DRIFT = auto()

class BaselineClass(Enum):
    APPROVED = auto()
    PROVISIONAL = auto()
    STALE = auto()
    CONTAMINATED = auto()

class SignalClass(Enum):
    WEAK = auto()
    CORROBORATED = auto()
    CONFLICTING = auto()
    HIDDEN_PATH = auto()

class BreachClass(Enum):
    SOFT = auto()
    MATERIAL = auto()
    CASCADING = auto()
    UNJUSTIFIED_RELAXATION = auto()

class GuardrailClass(Enum):
    WEAKENED = auto()
    BYPASSED = auto()
    RETIRED_WITHOUT_BASIS = auto()
    HIDDEN_DEVIATION = auto()

class RecurrenceClass(Enum):
    PRECURSOR = auto()
    ACTIVE = auto()
    FALSE_COMFORT = auto()
    CHAIN = auto()

class RestrictionClass(Enum):
    STAGED = auto()
    DOMAIN = auto()
    DELAYED = auto()
    UNJUSTIFIED_NON_RETURN = auto()

class ScarClass(Enum):
    VISIBLE = auto()
    BOUNDED = auto()
    HIDDEN = auto()
    ESCALATING = auto()

class RenormalizationClass(Enum):
    REQUIRED_RE_BASELINING = auto()
    REQUIRED_REAUTHORIZATION = auto()
    REQUIRED_REQUALIFICATION = auto()
    FALSE_RENORMALIZATION_CLAIM = auto()

class EquivalenceVerdict(Enum):
    FULLY_EQUIVALENT = auto()
    PARTIALLY_DIVERGENT = auto()
    MATERIALLY_DIVERGENT = auto()
    BLOCKING_DIVERGENCE = auto()

class TrustVerdict(Enum):
    TRUSTED = auto()
    CAUTION = auto()
    DEGRADED = auto()
    BLOCKED = auto()
    REVIEW_REQUIRED = auto()
