from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime, timezone
from app.ml.enums import (
    MlTaskType,
    LabelType,
    ModelFamily,
    SplitType,
    CalibrationType,
    InferenceVerdict,
    DriftSeverity,
    RegistryStage,
    PromotionVerdict,
    ModelStatus,
)


class MlConfig(BaseModel):
    enabled: bool = False
    enforce_strict_time_split: bool = True
    require_calibration: bool = True
    active_model_id: Optional[str] = None
    drift_threshold: float = 0.1


class DatasetSpec(BaseModel):
    feature_set: str
    label_spec_name: str
    split_type: SplitType
    train_start: datetime
    train_end: datetime
    test_start: datetime
    test_end: datetime


class DatasetManifest(BaseModel):
    dataset_id: str
    spec: DatasetSpec
    build_time: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    train_rows: int
    test_rows: int
    null_summary: Dict[str, int]
    temporal_coverage: str


class LabelSpec(BaseModel):
    name: str
    label_type: LabelType
    horizon_periods: int
    success_definition: str
    threshold: Optional[float] = None
    asymmetric_outcome_logic: Optional[str] = None


class LabelDistributionSummary(BaseModel):
    positive_count: int
    negative_count: int
    neutral_count: int
    positive_ratio: float


class TemporalSplitPlan(BaseModel):
    split_type: SplitType
    train_intervals: List[Dict[str, datetime]]
    test_intervals: List[Dict[str, datetime]]


class TrainRun(BaseModel):
    run_id: str
    dataset_id: str
    model_family: ModelFamily
    config_snapshot: Dict[str, Any]
    seed: int
    start_time: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    end_time: Optional[datetime] = None


class ModelArtifact(BaseModel):
    run_id: str
    binary_payload: bytes  # placeholder for the real artifact


class ModelCard(BaseModel):
    run_id: str
    family: ModelFamily
    description: str
    dataset_ref: str
    label_ref: str
    feature_schema: List[str]


class EvaluationReport(BaseModel):
    run_id: str
    precision: float
    recall: float
    f1_score: float
    roc_auc: Optional[float]
    log_loss: float
    brier_score: float


class CalibrationReport(BaseModel):
    run_id: str
    calibrator_type: CalibrationType
    brier_score_before: float
    brier_score_after: float
    raw_vs_calibrated_diff_mean: float


class InferenceRequest(BaseModel):
    run_id: str
    features: Dict[str, float]
    symbol: str
    timestamp: datetime


class InferenceResult(BaseModel):
    request_id: str
    run_id: str
    raw_score: float
    calibrated_score: float
    verdict: InferenceVerdict
    caution_flags: List[str]


class DriftReport(BaseModel):
    run_id: str
    timestamp: datetime
    feature_drifts: Dict[str, float]
    schema_drift_detected: bool
    missingness_drift: float
    severity: DriftSeverity
    recommended_action: str


class PromotionReadinessReport(BaseModel):
    run_id: str
    verdict: PromotionVerdict
    reasons: List[str]
    blockers: List[str]
    next_actions: List[str]


class FeatureImportanceSummary(BaseModel):
    run_id: str
    importance_map: Dict[str, float]
    stable: bool


class ModelRegistryEntry(BaseModel):
    run_id: str
    stage: RegistryStage
    status: ModelStatus
    dataset_id: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class PredictionSnapshot(BaseModel):
    snapshot_id: str
    timestamp: datetime
    run_id: str
    predictions: List[InferenceResult]


class MlAuditRecord(BaseModel):
    event_type: str
    run_id: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    details: Dict[str, Any]
