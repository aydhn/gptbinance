from enum import Enum


class FeatureCategory(str, Enum):
    PRICE = "price"
    VOLUME = "volume"
    TREND = "trend"
    VOLATILITY = "volatility"
    OSCILLATOR = "oscillator"
    STRUCTURE = "structure"
    DIVERGENCE = "divergence"
    MTF = "mtf"
    CUSTOM = "custom"


class InputDataType(str, Enum):
    KLINE = "kline"
    TICK = "tick"
    DERIVED = "derived"


class WindowMode(str, Enum):
    ROLLING = "rolling"
    EXPANDING = "expanding"
    FIXED = "fixed"


class AlignmentMode(str, Enum):
    STRICT_CLOSED = "strict_closed"
    FORWARD_FILL = "forward_fill"


class NormalizationMode(str, Enum):
    ZSCORE = "zscore"
    MINMAX = "minmax"
    PERCENTILE = "percentile"
    NONE = "none"


class DivergenceType(str, Enum):
    REGULAR_BULLISH = "regular_bullish"
    REGULAR_BEARISH = "regular_bearish"
    HIDDEN_BULLISH = "hidden_bullish"
    HIDDEN_BEARISH = "hidden_bearish"
    NONE = "none"


class PivotType(str, Enum):
    HIGH = "high"
    LOW = "low"
    NONE = "none"


class FeatureQualityStatus(str, Enum):
    GOOD = "good"
    WARNING = "warning"
    BAD = "bad"
