from enum import Enum


class EventSourceType(str, Enum):
    MACRO = "macro"
    EXCHANGE = "exchange"
    SYSTEM = "system"
    MANUAL = "manual"


class EventCategory(str, Enum):
    MACRO_POLICY = "macro_policy"
    INFLATION = "inflation"
    LABOR = "labor"
    GDP = "gdp"
    EXCHANGE_MAINTENANCE = "exchange_maintenance"
    EXCHANGE_RESTRICTION = "exchange_restriction"
    FUNDING_SETTLEMENT = "funding_settlement"
    SYSTEM_MAINTENANCE = "system_maintenance"
    RELEASE = "release"
    QUALIFICATION = "qualification"
    MANUAL_BLACKOUT = "manual_blackout"
    OTHER = "other"


class EventSeverity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"
    UNKNOWN = "unknown"


class EventConfidence(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CONFIRMED = "confirmed"


class EventGateVerdict(str, Enum):
    ALLOW = "allow"
    CAUTION = "caution"
    REDUCE = "reduce"
    DEFER = "defer"
    BLOCK = "block"
    EXIT_ONLY = "exit_only"
    REDUCE_ONLY = "reduce_only"
    SHADOW_ONLY = "shadow_only"
    HALT = "halt"


class CooldownMode(str, Enum):
    NONE = "none"
    REDUCE_ONLY = "reduce_only"
    EXIT_ONLY = "exit_only"
    SHADOW_ONLY = "shadow_only"
    NO_NEW_POSITIONS = "no_new_positions"
    FULL_HALT = "full_halt"


class BlackoutType(str, Enum):
    MANUAL = "manual"
    EXCHANGE_MAINTENANCE = "exchange_maintenance"
    SYSTEM_MAINTENANCE = "system_maintenance"
    MACRO_RISK = "macro_risk"


class ImpactClass(str, Enum):
    NEGLIGIBLE = "negligible"
    MINOR = "minor"
    MODERATE = "moderate"
    SEVERE = "severe"


class EventFreshness(str, Enum):
    FRESH = "fresh"
    STALE = "stale"
    UNKNOWN = "unknown"


class EventVerdict(str, Enum):
    SAFE = "safe"
    CAUTION = "caution"
    UNSAFE = "unsafe"
