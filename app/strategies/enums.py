from enum import Enum


class StrategyType(Enum):
    TREND_FOLLOW = "trend_follow"
    MEAN_REVERSION = "mean_reversion"
    BREAKOUT = "breakout"
    STRUCTURE = "structure"
    UNKNOWN = "unknown"


class SignalDirection(Enum):
    LONG = "long"
    SHORT = "short"
    NEUTRAL = "neutral"


class SignalStrength(Enum):
    STRONG = "strong"
    MODERATE = "moderate"
    WEAK = "weak"


class SignalStatus(Enum):
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    FILTERED = "filtered"


class IntentType(Enum):
    ENTRY = "entry"
    EXIT = "exit"


class ConflictType(Enum):
    OPPOSING_DIRECTION = "opposing_direction"
    MULTIPLE_SAME_DIRECTION = "multiple_same_direction"


class ResolutionType(Enum):
    HIGHEST_SCORE = "highest_score"
    FRESHEST = "freshest"
    NO_CLEAR_INTENT = "no_clear_intent"
    MERGED = "merged"


class CooldownScope(Enum):
    SYMBOL = "symbol"
    STRATEGY = "strategy"
    DIRECTION = "direction"


class RationaleCategory(Enum):
    RULE_PASS = "rule_pass"
    RULE_FAIL = "rule_fail"
    FILTER_PASS = "filter_pass"
    FILTER_FAIL = "filter_fail"
    CONFIRMATION = "confirmation"
    SCORE_PENALTY = "score_penalty"
    SCORE_BONUS = "score_bonus"
    COOLDOWN = "cooldown"
