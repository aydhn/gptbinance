from enum import Enum, auto


class RegimeFamily(Enum):
    TREND = auto()
    VOLATILITY = auto()
    MEAN_REVERSION = auto()
    STRUCTURE = auto()


class RegimeStrength(Enum):
    WEAK = auto()
    MODERATE = auto()
    STRONG = auto()
    EXTREME = auto()


class TransitionType(Enum):
    NONE = auto()
    SUDDEN = auto()
    GRADUAL = auto()
    WHIPSAW = auto()


class SuitabilityVerdict(Enum):
    AVOID = auto()
    CAUTION = auto()
    ALLOW = auto()
    OPTIMAL = auto()


class ContextQuality(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()


class VolatilityRegime(Enum):
    LOW_ENERGY = auto()
    NORMAL = auto()
    EXPANSION = auto()
    NOISY_HIGH_VOL = auto()


class TrendRegime(Enum):
    STRONG_UPTREND = auto()
    WEAK_UPTREND = auto()
    NO_TREND = auto()
    WEAK_DOWNTREND = auto()
    STRONG_DOWNTREND = auto()


class StructureRegime(Enum):
    BREAKOUT_PRESSURE = auto()
    CONTINUATION = auto()
    DETERIORATION = auto()
    SWING_COMPRESSION = auto()
    SWING_EXPANSION = auto()


class LiquidityRegime(Enum):
    LOW = auto()
    NORMAL = auto()
    HIGH = auto()
