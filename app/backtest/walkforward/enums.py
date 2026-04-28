from enum import Enum


class WalkForwardMode(str, Enum):
    STANDARD = "standard"
    STRICT = "strict"


class WindowScheme(str, Enum):
    ANCHORED = "anchored"
    ROLLING = "rolling"
    EXPANDING = "expanding"


class SelectionPolicy(str, Enum):
    MAX_EXPECTANCY = "max_expectancy"
    MIN_DRAWDOWN = "min_drawdown"
    BALANCED = "balanced"


class PromotionVerdict(str, Enum):
    PROMOTED = "promoted"
    REJECTED = "rejected"
    SKIPPED = "skipped"


class SegmentStatus(str, Enum):
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED_INSUFFICIENT_DATA = "skipped_insufficient_data"


class AggregateVerdict(str, Enum):
    PASS = "pass"
    CAUTION = "caution"
    FAIL = "fail"


class GateSeverity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"
