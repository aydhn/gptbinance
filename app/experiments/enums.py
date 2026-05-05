from enum import Enum


class HypothesisClass(str, Enum):
    RISK_FILTER_TOO_RESTRICTIVE = "risk_filter_too_restrictive"
    POLICY_FRICTION_EXCESSIVE_IN_REGIME = "policy_friction_excessive_in_regime"
    MARKET_TRUTH_THRESHOLDS_TOO_SENSITIVE = "market_truth_thresholds_too_sensitive"
    EVENT_COOLDOWN_TOO_WIDE = "event_cooldown_too_wide"
    CROSS_BOOK_POLICY_OVERBLOCKING = "cross_book_policy_overblocking"
    CAPITAL_TIER_GATES_TOO_CONSERVATIVE = "capital_tier_gates_too_conservative"
    STRATEGY_SIGNAL_NOISE_HIGH = "strategy_signal_noise_high"
    EXECUTION_PLAN_COMPLEXITY_DRAG = "execution_plan_complexity_drag"
    UNIVERSE_ELIGIBILITY_TOO_NARROW = "universe_eligibility_too_narrow"
    STRESS_OVERLAY_DISPROPORTIONATE = "stress_overlay_disproportionate"
    OTHER = "other"


class ExperimentType(str, Enum):
    BASELINE_COMPARISON = "baseline_comparison"
    ABLATION = "ablation"
    SENSITIVITY = "sensitivity"
    REGIME_SPLIT = "regime_split"
    TIME_SPLIT = "time_split"


class ArmType(str, Enum):
    BASELINE = "baseline"
    CANDIDATE = "candidate"
    COUNTERFACTUAL = "counterfactual"
    ABLATION = "ablation"


class EvaluationSurface(str, Enum):
    OFFLINE_BACKTEST = "offline_backtest"
    REPLAY_COUNTERFACTUAL = "replay_counterfactual"
    PAPER_HISTORY_DIAGNOSTIC = "paper_history_diagnostic"


class ComparisonVerdict(str, Enum):
    IMPROVEMENT = "improvement"
    DEGRADATION = "degradation"
    MIXED = "mixed"
    INCONCLUSIVE = "inconclusive"


class FragilityClass(str, Enum):
    ROBUST = "robust"
    OVERFIT_SUSPICION = "overfit_suspicion"
    NARROW_REGIME = "narrow_regime"
    LOW_SAMPLE = "low_sample"
    UNSTABLE_OPTIMUM = "unstable_optimum"
    STALE_TRUTH_CONTAMINATION = "stale_truth_contamination"


class EvidenceConfidence(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class PromotionClass(str, Enum):
    REJECT = "reject"
    KEEP_RESEARCHING = "keep_researching"
    QUALIFIES_FOR_PAPER_SHADOW = "qualifies_for_paper_shadow"
    QUALIFIES_FOR_CANDIDATE_QUALIFICATION = "qualifies_for_candidate_qualification"
    NEEDS_POLICY_REVIEW = "needs_policy_review"


class ExperimentVerdict(str, Enum):
    SUCCESS = "success"
    FAILURE = "failure"
    ABORTED = "aborted"


class ScopeType(str, Enum):
    WORKSPACE = "workspace"
    PROFILE = "profile"
    SYMBOL = "symbol"
    REGIME = "regime"
    TIME_WINDOW = "time_window"
    DOMAIN = "domain"
