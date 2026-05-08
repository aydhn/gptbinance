from enum import Enum


class SleeveClass(str, Enum):
    PRIMARY_ALPHA = "primary_alpha"
    SECONDARY_ALPHA = "secondary_alpha"
    MEAN_REVERSION = "mean_reversion"
    TREND_FOLLOWING = "trend_following"
    EVENT_SENSITIVE = "event_sensitive"
    HEDGE_OVERLAY = "hedge_overlay"
    DEFENSIVE_OVERLAY = "defensive_overlay"
    RECOVERY_MODE = "recovery_mode"
    PAPER_SHADOW_ONLY = "paper_shadow_only"
    CANARY_LIMITED = "canary_limited"


class AllocationClass(str, Enum):
    DIRECTIONAL_LONG = "directional_long"
    DIRECTIONAL_SHORT = "directional_short"
    MARKET_NEUTRAL = "market_neutral"
    HEDGE = "hedge"


class SignalFamily(str, Enum):
    MOMENTUM = "momentum"
    MEAN_REVERSION = "mean_reversion"
    STATARB = "statarb"
    VOLATILITY = "volatility"
    ORDERBOOK_IMBALANCE = "orderbook_imbalance"


class BudgetClass(str, Enum):
    CORE = "core"
    OPPORTUNISTIC = "opportunistic"
    DEFENSIVE = "defensive"


class ConstraintClass(str, Enum):
    MAX_GROSS = "max_gross"
    MAX_NET = "max_net"
    SYMBOL_CONCENTRATION = "symbol_concentration"
    SLEEVE_CONCENTRATION = "sleeve_concentration"
    CORRELATION_CLUSTER = "correlation_cluster"


class TurnoverClass(str, Enum):
    LOW_CHURN = "low_churn"
    NORMAL = "normal"
    HIGH_TURNOVER = "high_turnover"


class CapacityClass(str, Enum):
    HIGH_LIQUIDITY = "high_liquidity"
    MODERATE_LIQUIDITY = "moderate_liquidity"
    THIN_MARKET = "thin_market"


class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    DIVERGED_SAFE = "diverged_safe"
    DIVERGED_CRITICAL = "diverged_critical"
    UNKNOWN = "unknown"


class AllocationVerdict(str, Enum):
    ACCEPTED = "accepted"
    CLIPPED = "clipped"
    DEFERRED = "deferred"
    REJECTED = "rejected"


class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
