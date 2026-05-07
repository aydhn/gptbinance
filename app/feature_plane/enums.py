from enum import Enum, auto


class FeatureDomain(Enum):
    MARKET_STRUCTURE = auto()
    VOLATILITY = auto()
    MOMENTUM = auto()
    MEAN_REVERSION = auto()
    MARKET_TRUTH_HEALTH = auto()
    EVENT_RISK = auto()
    RISK_POSTURE = auto()
    CROSS_BOOK = auto()
    SHADOW_TRUTH = auto()
    LIFECYCLE_HEALTH = auto()
    ACTIVATION_RELIABILITY = auto()
    UNKNOWN = auto()


class FeatureTypeClass(Enum):
    SCALAR_FLOAT = auto()
    SCALAR_INT = auto()
    CATEGORICAL = auto()
    BOOLEAN = auto()
    VECTOR_FLOAT = auto()


class FeatureWindowClass(Enum):
    ROLLING_TIME = auto()
    ROLLING_TICK = auto()
    SESSION_BOUND = auto()
    EVENT_CONDITIONED = auto()
    INSTANTANEOUS = auto()


class FeatureSourceClass(Enum):
    MARKET_TRUTH_TICK = auto()
    MARKET_TRUTH_KLINE = auto()
    EVENT_OVERLAY = auto()
    SHADOW_STATE = auto()
    ORDER_LIFECYCLE = auto()
    CAPITAL_POSTURE = auto()
    CROSS_BOOK_POSTURE = auto()
    CONFIG_PLANE = auto()


class LabelClass(Enum):
    TRADE_OUTCOME = auto()
    DIRECTIONAL = auto()
    BARRIER_TOUCH = auto()
    TIMEOUT = auto()


class TargetClass(Enum):
    RETURN = auto()
    VOLATILITY = auto()
    DRAWDOWN = auto()
    DECISION_QUALITY = auto()


class EquivalenceVerdict(Enum):
    EQUIVALENT = auto()
    TOLERABLE_DIVERGENCE = auto()
    STRICT_DIVERGENCE = auto()
    INCOMPARABLE = auto()


class SkewSeverity(Enum):
    NONE = auto()
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()


class DriftSeverity(Enum):
    NONE = auto()
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()


class TrustedFeatureVerdict(Enum):
    TRUSTED = auto()
    CAUTION = auto()
    DEGRADED = auto()
    BLOCKED = auto()
    REVIEW_REQUIRED = auto()


class LeakageSeverity(Enum):
    NONE = auto()
    SUSPICIOUS = auto()
    CONFIRMED_LOW = auto()
    CONFIRMED_HIGH = auto()
    CRITICAL_BLOCKER = auto()
