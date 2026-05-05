from enum import Enum


class FunnelStage(Enum):
    SIGNAL_GENERATED = "signal_generated"
    REGIME_CONTEXT_ATTACHED = "regime_context_attached"
    RISK_EVALUATED = "risk_evaluated"
    PORTFOLIO_EVALUATED = "portfolio_evaluated"
    POLICY_EVALUATED = "policy_evaluated"
    INTENT_COMPILED = "intent_compiled"
    LIFECYCLE_SUBMITTED = "lifecycle_submitted"
    ACKNOWLEDGED = "acknowledged"
    PARTIALLY_FILLED = "partially_filled"
    FULLY_FILLED = "fully_filled"
    EXITED = "exited"
    BLOCKED = "blocked"
    SKIPPED = "skipped"
    SUPPRESSED = "suppressed"


class DecisionClass(Enum):
    EXECUTED = "executed"
    BLOCKED = "blocked"
    SKIPPED = "skipped"
    SUPPRESSED = "suppressed"


class BlockReasonClass(Enum):
    MARKET_TRUTH_STALE = "market_truth_stale"
    MARKET_TRUTH_BROKEN_SEQUENCE = "market_truth_broken_sequence"
    EVENT_RISK_BLOCK = "event_risk_block"
    STRESS_BUDGET_BLOCK = "stress_budget_block"
    CAPITAL_NO_NEW_EXPOSURE = "capital_no_new_exposure"
    CAPITAL_FREEZE = "capital_freeze"
    POLICY_HARD_BLOCK = "policy_hard_block"
    POLICY_BLOCK = "policy_block"
    UNIVERSE_INELIGIBLE = "universe_ineligible"
    CROSS_BOOK_CONFLICT = "cross_book_conflict"
    SHADOW_TRUTHFULNESS_POOR = "shadow_truthfulness_poor"
    LIFECYCLE_AMBIGUOUS = "lifecycle_ambiguous"
    ACCOUNT_MODE_MISMATCH = "account_mode_mismatch"
    QUALIFICATION_STALE = "qualification_stale"
    WORKSPACE_BOUNDARY = "workspace_boundary"
    SYMBOL_QUARANTINED = "symbol_quarantined"
    EXECUTION_NOT_SUBMITTED = "execution_not_submitted"
    MANUAL_SKIP_OR_SUPPRESSION = "manual_skip_or_suppression"


class FrictionClass(Enum):
    STRATEGY_ISSUE = "strategy_issue"
    RISK_FILTER = "risk_filter"
    CAPITAL_CONSTRAINT = "capital_constraint"
    EVENT_RISK_RESTRICTION = "event_risk_restriction"
    POLICY_HARD_BLOCK = "policy_hard_block"
    MARKET_TRUTH_DEGRADATION = "market_truth_degradation"
    LIFECYCLE_EXECUTION_ISSUE = "lifecycle_execution_issue"
    CROSS_BOOK_CONFLICT = "cross_book_conflict"
    UNKNOWN_MIXED = "unknown_mixed"


class OutcomeWindow(Enum):
    VERY_SHORT = "very_short"
    SHORT = "short"
    MEDIUM = "medium"
    SESSION_BOUND = "session_bound"
    REGIME_BOUND = "regime_bound"


class OpportunityQuality(Enum):
    EXCELLENT = "excellent"
    GOOD = "good"
    MARGINAL = "marginal"
    POOR = "poor"
    INDETERMINATE = "indeterminate"


class EvidenceConfidence(Enum):
    STRONG = "strong"
    MODERATE = "moderate"
    WEAK = "weak"
    UNSAFE_TO_JUDGE = "unsafe_to_judge"


class HindsightSafetyClass(Enum):
    SAFE = "safe"
    CAVEAT_APPLIED = "caveat_applied"
    UNSAFE = "unsafe"


class ComparisonVerdict(Enum):
    BETTER = "better"
    WORSE = "worse"
    SIMILAR = "similar"
    INCONCLUSIVE = "inconclusive"


class DecisionQualityVerdict(Enum):
    GOOD_BLOCK_CANDIDATE = "good_block_candidate"
    MISSED_ALPHA_CANDIDATE = "missed_alpha_candidate"
    BLOCKED_AND_LIKELY_SAVED_LOSS = "blocked_and_likely_saved_loss"
    INDETERMINATE = "indeterminate"
    UNSAFE_TO_JUDGE = "unsafe_to_judge"
    EXECUTED_WELL = "executed_well"
    EXECUTED_POORLY = "executed_poorly"
