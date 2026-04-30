from enum import Enum


class AllocationMode(str, Enum):
    CONSERVATIVE = "conservative"
    BALANCED = "balanced"
    AGGRESSIVE = "aggressive"


class PortfolioVerdict(str, Enum):
    APPROVE = "approve"
    REDUCE = "reduce"
    DEFER = "defer"
    REJECT = "reject"


class SleeveType(str, Enum):
    STRATEGY = "strategy"
    SYMBOL = "symbol"
    CLUSTER = "cluster"


class OpportunityStatus(str, Enum):
    PENDING = "pending"
    RANKED = "ranked"
    ALLOCATED = "allocated"
    REJECTED = "rejected"
    DEFERRED = "deferred"


class RankingReason(str, Enum):
    HIGH_QUALITY = "high_quality"
    LIQUIDITY_BONUS = "liquidity_bonus"
    FRESHNESS_BONUS = "freshness_bonus"
    REGIME_MATCH = "regime_match"
    OVERLAP_PENALTY = "overlap_penalty"
    CORRELATION_PENALTY = "correlation_penalty"
    CONCENTRATION_PENALTY = "concentration_penalty"
    DEFAULT = "default"


class ConcentrationSeverity(str, Enum):
    NORMAL = "normal"
    CAUTION = "caution"
    BREACH = "breach"


class CorrelationRegime(str, Enum):
    NORMAL = "normal"
    HIGH_CORRELATION = "high_correlation"
    DECOUPLED = "decoupled"


class OverlapType(str, Enum):
    NONE = "none"
    SAME_SYMBOL_SAME_DIR = "same_symbol_same_dir"
    HIGH_CORR_SAME_DIR = "high_corr_same_dir"
    OPPOSING_EXPOSURE = "opposing_exposure"


class BudgetScope(str, Enum):
    TOTAL = "total"
    AVAILABLE = "available"
    RESERVED = "reserved"
    SLEEVE = "sleeve"
