from enum import Enum


class ReliabilityDomain(str, Enum):
    MARKET_TRUTH = "market_truth"
    SHADOW_TRUTHFULNESS = "shadow_truthfulness"
    LIFECYCLE_HEALTH = "lifecycle_health"
    INCIDENT_OPERATIONS = "incident_operations"
    REMEDIATION_CLOSURE = "remediation_closure"
    MIGRATION_STABILITY = "migration_stability"
    POLICY_INTEGRITY = "policy_integrity"
    ACTIVATION_PROBATION = "activation_probation"
    CAPITAL_OPERABILITY = "capital_operability"
    CROSS_BOOK_STABILITY = "cross_book_stability"
    DECISION_QUALITY_HEALTH = "decision_quality_health"
    RELEASE_READINESS_HEALTH = "release_readiness_health"


class SLOClass(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    ELEVATED = "elevated"
    STANDARD = "standard"


class BudgetClass(str, Enum):
    HARD = "hard"
    SOFT = "soft"


class BurnSeverity(str, Enum):
    FAST_BURN = "fast_burn"
    SLOW_BURN = "slow_burn"
    NORMAL = "normal"
    HEALTHY = "healthy"


class ReadinessDecayClass(str, Enum):
    STALE_EVIDENCE = "stale_evidence"
    UNRESOLVED_DEBT = "unresolved_debt"
    RECURRING_INCIDENT = "recurring_incident"
    WEAK_POSTMORTEM = "weak_postmortem"


class ScorecardVerdict(str, Enum):
    HEALTHY = "healthy"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"


class FreezeClass(str, Enum):
    NO_EXPANSION_RECOMMENDED = "no_expansion_recommended"
    NO_NEW_CANDIDATE_ACTIVATION = "no_new_candidate_activation"
    RELEASE_HOLD_RECOMMENDED = "release_hold_recommended"
    PAPER_ONLY_RECOMMENDED = "paper_only_recommended"
    CANDIDATE_SCOPE_HOLD = "candidate_scope_hold"
    MAJOR_CHANGE_FREEZE = "major_change_freeze"


class OperationalReviewClass(str, Enum):
    ACTIVATION_EXPANSION_HOLD = "activation_expansion_hold"
    CANDIDATE_QUALIFICATION_HOLD = "candidate_qualification_hold"
    BOARD_REVIEW_HOLD = "board_review_hold"
    MIGRATION_APPLY_HOLD = "migration_apply_hold"
    REMEDIATION_ONLY_MODE = "remediation_only_mode"


class TrendClass(str, Enum):
    IMPROVING = "improving"
    STABLE = "stable"
    DEGRADING = "degrading"
    VOLATILE = "volatile"


class ReliabilityVerdict(str, Enum):
    PASS = "pass"
    CAUTION = "caution"
    FAIL = "fail"
