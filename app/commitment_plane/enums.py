from enum import Enum, auto

class CommitmentClass(Enum):
    PROMISE = auto()
    OBLIGATION = auto()
    GUARANTEE = auto()
    TARGET = auto()
    EXPECTATION = auto()
    ASPIRATION = auto()

class PromiseClass(Enum):
    INTERNAL = auto()
    EXTERNAL = auto()
    BOUNDED = auto()
    CONDITIONAL = auto()

class ObligationClass(Enum):
    POLICY_DERIVED = auto()
    CONSTITUTIONAL = auto()
    OPERATIONAL = auto()
    REGULATORY = auto()

class GuaranteeClass(Enum):
    HARD_GUARANTEE = auto()
    BOUNDED_GUARANTEE = auto()
    SERVICE_GUARANTEE = auto()
    RESPONSE_GUARANTEE = auto()

class BindingClass(Enum):
    ADVISORY = auto()
    EXPECTED = auto()
    COMMITTED = auto()
    GUARANTEED = auto()

class OwnerClass(Enum):
    ACCOUNTABLE = auto()
    OPERATIONAL = auto()
    SUPERVISORY = auto()
    FEDERATED = auto()

class BreachClass(Enum):
    MISSED_DEADLINE = auto()
    UNMET_GUARANTEE = auto()
    PARTIAL_FULFILLMENT = auto()
    SILENT_NON_DELIVERY = auto()

class ReliefClass(Enum):
    TEMPORARY_RELIEF = auto()
    CONDITIONAL_RELIEF = auto()
    SCOPE_LIMITED_RELIEF = auto()
    FORCE_MAJEURE_RELIEF = auto()

class DischargeClass(Enum):
    FULFILLED = auto()
    PARTIALLY_DISCHARGED = auto()
    COMPENSATED = auto()
    INVALID_DISCHARGE = auto()

class AsymmetryClass(Enum):
    EXTERNAL_PROMISE_WEAK_INTERNAL = auto()
    OWNER_BENEFICIARY_MISMATCH = auto()
    LOCAL_FEDERATED_ASYMMETRY = auto()

class CommitmentEquivalenceVerdict(Enum):
    EQUIVALENT = auto()
    DIVERGENT = auto()
    UNKNOWN = auto()

class CommitmentTrustVerdict(Enum):
    TRUSTED = auto()
    CAUTION = auto()
    DEGRADED = auto()
    BLOCKED = auto()
    REVIEW_REQUIRED = auto()
