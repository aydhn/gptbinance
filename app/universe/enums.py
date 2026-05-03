from enum import Enum

class InstrumentType(str, Enum):
    SPOT = "spot"
    MARGIN = "margin"
    FUTURES = "futures"
    UNKNOWN = "unknown"

class InstrumentStatus(str, Enum):
    TRADING = "trading"
    HALTED = "halted"
    BREAK = "break"
    DELISTED = "delisted"
    MAINTENANCE = "maintenance"
    PRE_TRADING = "pre_trading"
    POST_TRADING = "post_trading"
    UNKNOWN = "unknown"

class LiquiditySeverity(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    VERY_LOW = "very_low"
    UNKNOWN = "unknown"

class SpreadSeverity(str, Enum):
    TIGHT = "tight"
    NORMAL = "normal"
    WIDE = "wide"
    VERY_WIDE = "very_wide"
    UNKNOWN = "unknown"

class EligibilityVerdict(str, Enum):
    ELIGIBLE = "eligible"
    CAUTION = "caution"
    BLOCKED = "blocked"

class LifecycleEventType(str, Enum):
    LISTED = "listed"
    DELISTED = "delisted"
    STATUS_CHANGED = "status_changed"
    FILTERS_CHANGED = "filters_changed"
    MAINTENANCE_STARTED = "maintenance_started"
    MAINTENANCE_ENDED = "maintenance_ended"
    UNKNOWN = "unknown"

class MetadataFreshness(str, Enum):
    FRESH = "fresh"
    STALE = "stale"
    UNKNOWN = "unknown"

class TradabilityClass(str, Enum):
    PREMIUM = "premium"
    STANDARD = "standard"
    SPECULATIVE = "speculative"
    ILLIQUID = "illiquid"
    UNKNOWN = "unknown"
