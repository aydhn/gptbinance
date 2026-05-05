from enum import Enum, auto


class PolicyDomain(Enum):
    RISK = auto()
    CAPITAL = auto()
    EVENT_RISK = auto()
    STRESS_RISK = auto()
    CROSS_BOOK = auto()
    WORKSPACE = auto()
    CONTROL = auto()
    LIFECYCLE = auto()
    SHADOW = auto()
    QUALIFICATION = auto()
    REMEDIATION = auto()
    ORDER_INTENT = auto()
    GENERAL = auto()


class RuleClass(Enum):
    STANDARD = auto()
    INVARIANT = auto()


class PolicyVerdict(Enum):
    ALLOW = auto()
    ADVISORY = auto()
    CAUTION = auto()
    BLOCK = auto()
    HARD_BLOCK = auto()


class EvidenceFreshness(Enum):
    FRESH = auto()
    STALE = auto()
    MISSING = auto()


class ConflictClass(Enum):
    ALLOW_VS_BLOCK = auto()
    WAIVABLE_VS_NON_WAIVABLE = auto()
    REDUCE_ONLY_VS_NO_NEW_EXPOSURE = auto()


class PrecedenceClass(Enum):
    INVARIANT_OVER_RULE = auto()
    HARD_BLOCK_OVER_BLOCK = auto()
    BLOCK_OVER_CAUTION = auto()
    SPECIFIC_OVER_GENERIC = auto()
    STALE_EVIDENCE_DENIAL = auto()


class WaiverClass(Enum):
    RULE_SPECIFIC = auto()
    SCOPE_SPECIFIC = auto()


class DriftSeverity(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()


class GapSeverity(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()
