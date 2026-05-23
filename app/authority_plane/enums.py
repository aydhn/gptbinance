from enum import Enum, auto

class AuthorityClass(Enum):
    BINDING = auto()
    ADVISORY = auto()
    TEMPORARY = auto()
    EMERGENCY = auto()
    FEDERATED = auto()
    SHADOW = auto()

class MandateClass(Enum):
    STANDING = auto()
    SCOPED = auto()
    TEMPORARY = auto()
    EMERGENCY = auto()

class DecisionRightClass(Enum):
    APPROVE = auto()
    DENY = auto()
    CONDITIONALLY_APPROVE = auto()
    RECOMMEND_ONLY = auto()

class DelegationClass(Enum):
    SCOPED = auto()
    TEMPORARY = auto()
    EMERGENCY = auto()
    TASK_SPECIFIC = auto()
    SILENT = auto() # Indicates an anomaly

class OverrideClass(Enum):
    EMERGENCY = auto()
    SCOPED = auto()
    TEMPORARY = auto()

class VetoClass(Enum):
    HARD = auto()
    SCOPED = auto()
    SUSPENSIVE = auto()
    ADVISORY_SIGNAL = auto()

class RatificationClass(Enum):
    VALID = auto()
    INSUFFICIENT = auto()
    POST_HOC = auto()

class EscalationClass(Enum):
    AUTHORITY_TRANSFER = auto()
    DEADLOCK_BREAK = auto()
    EMERGENCY_ESCALATION = auto()
    UNRESOLVED = auto()

class QuorumClass(Enum):
    SATISFIED = auto()
    PARTIAL = auto()
    INVALID = auto()
    PROXY = auto()

class LegitimacyClass(Enum):
    LEGITIMATE = auto()
    LEGITIMACY_GAP = auto()

class EquivalenceVerdict(Enum):
    EQUIVALENT = auto()
    DIVERGENT = auto()

class TrustVerdict(Enum):
    TRUSTED = auto()
    CAUTION = auto()
    DEGRADED = auto()
    BLOCKED = auto()
    REVIEW_REQUIRED = auto()
