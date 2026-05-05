from enum import Enum, auto


class ActivationClass(Enum):
    PAPER_SHADOW = "paper_shadow"
    CANDIDATE_QUALIFICATION = "candidate_qualification"
    CANARY_LIMITED = "canary_limited"
    SYMBOL_SUBSET = "symbol_subset"
    NO_NEW_EXPOSURE = "no_new_exposure"
    DEGRADED_RECOVERY = "degraded_recovery"
    ROLLBACK_PRIOR = "rollback_prior"


class ActivationStage(Enum):
    PREFLIGHT = "preflight"
    STAGE_0_OBSERVE = "stage_0_observe_only"
    STAGE_1_LIMITED_SYMBOLS = "stage_1_limited_symbols"
    STAGE_2_LIMITED_SESSIONS = "stage_2_limited_sessions"
    STAGE_3_LIMITED_CAPITAL = "stage_3_limited_capital_tier"
    STAGE_4_COMPLETE = "stage_4_candidate_scope_complete"
    HOLD = "stage_hold"
    HALT = "stage_halt"
    REVERTED = "stage_reverted"


class ProbationVerdict(Enum):
    PASS = "pass"
    CAUTION = "caution"
    FAIL = "fail"
    INCONCLUSIVE = "inconclusive"
    PENDING = "pending"


class ExpansionVerdict(Enum):
    ELIGIBLE = "eligible"
    BLOCKED = "blocked"
    REQUIRES_APPROVAL = "requires_approval"


class HaltSeverity(Enum):
    ADVISORY = "advisory"
    CAUTION = "caution"
    CRITICAL_IMMEDIATE = "critical_immediate"


class RevertClass(Enum):
    FULL_REVERT = "full_revert"
    PARTIAL_SCOPE_REVERT = "partial_scope_revert"
    NO_REVERT_AVAILABLE = "no_revert_available"


class ActiveSetStatus(Enum):
    ACTIVE = "active"
    SUPERSEDED = "superseded"
    REVERTED = "reverted"
    HALTED = "halted"
