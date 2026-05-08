from enum import Enum


class SimulationClass(str, Enum):
    PRODUCTION = "production"
    EXPLORATORY = "exploratory"


class SimulationMode(str, Enum):
    REPLAY_EVENT_TRUTH = "replay_event_truth"
    BAR_APPROXIMATION = "bar_approximation"
    PAPER_PROJECTION = "paper_projection"
    HYBRID_EXECUTION_APPROXIMATION = "hybrid_execution_approximation"
    FROZEN_FEATURE_MODEL_TRIAL = "frozen_feature_model_trial"


class PartitionClass(str, Enum):
    TRAIN = "train"
    VALIDATION = "validation"
    TEST = "test"
    OUT_OF_SAMPLE = "out_of_sample"
    ROLLING_OOS = "rolling_oos"
    WALK_FORWARD_FOLD = "walk_forward_fold"
    REGIME_SEGMENTED = "regime_segmented"


class AssumptionClass(str, Enum):
    FILL = "fill"
    SLIPPAGE = "slippage"
    LATENCY = "latency"
    FEE_FUNDING = "fee_funding"
    ORDER_LEGALITY = "order_legality"
    MISSING_DATA = "missing_data"


class SensitivityClass(str, Enum):
    SLIPPAGE_SENSITIVITY = "slippage_sensitivity"
    LATENCY_SENSITIVITY = "latency_sensitivity"
    FEE_FUNDING_SENSITIVITY = "fee_funding_sensitivity"
    MISSING_DATA_SENSITIVITY = "missing_data_sensitivity"
    EXECUTION_APPROXIMATION = "execution_approximation"


class OOSClass(str, Enum):
    STRICT_OOS = "strict_oos"
    CONTAMINATED = "contaminated"
    LEAKAGE_SUSPECTED = "leakage_suspected"


class WalkForwardClass(str, Enum):
    PROMOTION_GRADE = "promotion_grade"
    INSUFFICIENT_FOLDS = "insufficient_folds"
    EMBARGO_VIOLATION = "embargo_violation"


class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    PARTIAL_EQUIVALENCE = "partial_equivalence"
    DIVERGENT = "divergent"


class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"


class CounterfactualConfidence(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    SPECULATIVE = "speculative"
