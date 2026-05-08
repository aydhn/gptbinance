from enum import Enum, auto


class StrategyClass(Enum):
    ALPHA_SEEKING = auto()
    HEDGE = auto()
    MARKET_MAKING = auto()
    EXECUTION = auto()
    ARBITRAGE = auto()
    CASH_MANAGEMENT = auto()


class StrategyFamily(Enum):
    TREND_FOLLOWING = auto()
    MEAN_REVERSION = auto()
    BREAKOUT = auto()
    MOMENTUM_ROTATION = auto()
    EVENT_SENSITIVE = auto()
    CARRY_LIKE = auto()
    EXECUTION_OVERLAY = auto()
    HEDGE_OVERLAY = auto()
    REGIME_SWITCHING = auto()
    DEFENSIVE_FILTER = auto()


class LifecycleState(Enum):
    HYPOTHESIS_ONLY = auto()
    RESEARCH_CANDIDATE = auto()
    REPLAY_QUALIFIED = auto()
    PAPER_CANDIDATE = auto()
    PAPER_ACTIVE = auto()
    PROBATIONARY_LIVE = auto()
    ACTIVE_LIMITED = auto()
    ACTIVE_FULL = auto()
    DEGRADED = auto()
    FROZEN = auto()
    RETIRED = auto()
    ARCHIVED = auto()


class PromotionClass(Enum):
    REPLAY_TO_PAPER = auto()
    PAPER_TO_PROBATION = auto()
    PROBATION_TO_ACTIVE_LIMITED = auto()
    ACTIVE_LIMITED_TO_FULL = auto()


class FreezeClass(Enum):
    PERFORMANCE = auto()
    RISK = auto()
    DATA_INTEGRITY = auto()
    MODEL_INTEGRITY = auto()
    FEATURE_INTEGRITY = auto()
    EXECUTION_INTEGRITY = auto()
    INCIDENT_RELATED = auto()


class RetirementClass(Enum):
    THESIS_INVALIDATED = auto()
    PERSISTENT_UNDERPERFORMANCE = auto()
    OVERLAP_CANNIBALIZATION = auto()
    OBSOLETE_DEPENDENCIES = auto()
    PERMANENT_FREEZE = auto()


class FitClass(Enum):
    STRONG_FIT = auto()
    MARGINAL_FIT = auto()
    MISMATCH = auto()
    UNKNOWN = auto()


class DecaySeverity(Enum):
    NONE = auto()
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()


class EquivalenceVerdict(Enum):
    EQUIVALENT = auto()
    PARTIALLY_EQUIVALENT = auto()
    DIVERGENT = auto()
    UNKNOWN = auto()


class TrustVerdict(Enum):
    TRUSTED = auto()
    CAUTION = auto()
    DEGRADED = auto()
    BLOCKED = auto()
    REVIEW_REQUIRED = auto()
