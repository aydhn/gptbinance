from enum import Enum

class TradeoffClass(str, Enum):
    AUTHORITATIVE = "authoritative"
    DECISION_CRITICAL = "decision_critical"
    LOCAL = "local"
    FEDERATED = "federated"

class ObjectiveClass(str, Enum):
    SPEED = "speed"
    SAFETY = "safety"
    RELIABILITY = "reliability"
    COMPLIANCE = "compliance"
    VALUE = "value"
    SECURITY = "security"
    CONTINUITY = "continuity"

class PriorityClass(str, Enum):
    HARD = "hard"
    SOFT = "soft"
    BOUNDED = "bounded"
    EMERGENCY = "emergency"

class UtilityClass(str, Enum):
    LOCAL = "local"
    GLOBAL = "global"
    BOUNDED = "bounded"
    UNCERTAIN = "uncertain"

class BurdenClass(str, Enum):
    DIRECT = "direct"
    DELAYED = "delayed"
    HIDDEN = "hidden"
    TRANSFERRED = "transferred"
    HUMAN = "human"

class SacrificeClass(str, Enum):
    BOUNDED = "bounded"
    TEMPORARY = "temporary"
    IRREVERSIBLE = "irreversible"
    UNACCEPTABLE = "unacceptable"

class ExternalityClass(str, Enum):
    DOWNSTREAM = "downstream"
    CROSS_TEAM = "cross_team"
    CROSS_TENANT = "cross_tenant"
    FUTURE = "future"

class DominanceClass(str, Enum):
    DOMINATED = "dominated"
    WEAKLY_DOMINATED = "weakly_dominated"
    NON_DOMINATED = "non_dominated"
    INCOMPARABLE = "incomparable"

class FrontierClass(str, Enum):
    LOCAL = "local"
    GLOBAL = "global"
    CONSTRAINED = "constrained"
    EMERGENCY = "emergency"

class FeasibilityClass(str, Enum):
    TECHNICAL = "technical"
    ORGANIZATIONAL = "organizational"
    TEMPORARAL = "temporal"
    CONSTITUTIONAL = "constitutional"

class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    PARTIAL = "partial"
    DIVERGENT = "divergent"

class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
