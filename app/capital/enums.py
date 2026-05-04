from enum import Enum


class CapitalTierClass(str, Enum):
    PAPER = "paper"
    TESTNET = "testnet"
    CANARY = "canary"
    LIVE_CAUTION = "live_caution"
    LIVE_CORE = "live_core"


class CapitalPostureState(str, Enum):
    NORMAL = "normal"
    FROZEN = "frozen"
    REDUCED = "reduced"
    CAUTION = "caution"


class EscalationVerdict(str, Enum):
    PASS = "pass"
    CAUTION = "caution"
    BLOCKED = "blocked"


class ReductionVerdict(str, Enum):
    HOLD = "hold"
    REDUCE = "reduce"
    FREEZE = "freeze"


class FreezeStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    THAW_PENDING = "thaw_pending"


class BudgetSeverity(str, Enum):
    SOFT = "soft"
    HARD = "hard"


class EvidenceFreshness(str, Enum):
    FRESH = "fresh"
    STALE = "stale"
    MISSING = "missing"


class LossWindow(str, Enum):
    INTRADAY = "intraday"
    ROLLING_24H = "rolling_24h"
    WEEKLY = "weekly"


class CapitalDecisionClass(str, Enum):
    ESCALATION = "escalation"
    REDUCTION = "reduction"
    FREEZE = "freeze"
    TRANCHE_ACTIVATION = "tranche_activation"


class ScopeType(str, Enum):
    WORKSPACE = "workspace"
    PROFILE = "profile"
