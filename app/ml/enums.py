from enum import Enum


class MlTaskType(Enum):
    CLASSIFICATION = "classification"
    REGRESSION = "regression"


class LabelType(Enum):
    FORWARD_RETURN_SIGN = "forward_return_sign"
    THRESHOLDED_OUTCOME = "thresholded_outcome"
    STRATEGY_INTENT_SUCCESS = "strategy_intent_success"
    QUALITY_BUCKET = "quality_bucket"
    BARRIER = "barrier"


class ModelFamily(Enum):
    LOGISTIC_REGRESSION = "logistic_regression"
    RANDOM_FOREST = "random_forest"
    GRADIENT_BOOSTING = "gradient_boosting"


class SplitType(Enum):
    CONTIGUOUS = "contiguous"
    ANCHORED = "anchored"
    EXPANDING = "expanding"
    WALK_FORWARD = "walk_forward"


class CalibrationType(Enum):
    PLATT = "platt"
    ISOTONIC = "isotonic"
    NONE = "none"


class InferenceVerdict(Enum):
    PASS = "pass"
    CAUTION = "caution"
    REJECT = "reject"
    FALLBACK = "fallback"


class DriftSeverity(Enum):
    NONE = "none"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class RegistryStage(Enum):
    CANDIDATE = "candidate"
    REVIEWED = "reviewed"
    APPROVED_FOR_PAPER = "approved_for_paper"
    APPROVED_FOR_SHADOW = "approved_for_shadow"
    APPROVED_FOR_LIVE = "approved_for_live"
    RETIRED = "retired"


class PromotionVerdict(Enum):
    PASS = "pass"
    CAUTION = "caution"
    FAIL = "fail"


class ModelStatus(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
