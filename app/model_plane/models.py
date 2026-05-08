from typing import List, Dict, Any, Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime
from app.model_plane.enums import (
    ModelDomain,
    ModelClass,
    OutputClass,
    CalibrationClass,
    UncertaintyClass,
    ThresholdClass,
    EnsembleClass,
    EquivalenceVerdict,
    DriftSeverity,
    TrustedSignalVerdict,
)


class ModelPlaneBaseModel(BaseModel):
    model_config = ConfigDict(protected_namespaces=())


class ModelPlaneConfig(ModelPlaneBaseModel):
    storage_path: str = "data/model_plane"
    strict_contracts: bool = True


class ModelRef(ModelPlaneBaseModel):
    model_id: str
    version: str


class OutputSchema(ModelPlaneBaseModel):
    output_class: OutputClass
    description: str
    classes: Optional[List[str]] = None
    expected_range: Optional[List[float]] = None


class ModelSchema(ModelPlaneBaseModel):
    schema_id: str
    input_feature_manifest_id: str
    output_schema: OutputSchema


class ModelSchemaVersion(ModelPlaneBaseModel):
    version_id: str
    schema_id: str
    created_at: datetime


class ModelDefinition(ModelPlaneBaseModel):
    model_id: str
    domain: ModelDomain
    model_class: ModelClass
    schema_id: str
    description: str
    is_experimental: bool = False


class ModelArtifactManifest(ModelPlaneBaseModel):
    artifact_id: str
    checksum: str
    path: str


class ModelCheckpointRecord(ModelPlaneBaseModel):
    checkpoint_id: str
    model_id: str
    created_at: datetime
    source_training_run_id: str
    feature_manifest_id: str
    config_ref: str
    artifact: ModelArtifactManifest
    is_stale: bool = False


class InferenceContract(ModelPlaneBaseModel):
    contract_id: str
    model_id: str
    required_feature_manifest_id: str
    expected_output_schema: OutputSchema
    requires_calibration: bool
    requires_uncertainty: bool
    supports_abstention: bool


class ThresholdPolicy(ModelPlaneBaseModel):
    policy_id: str
    model_id: str
    threshold_class: ThresholdClass
    value: float
    regime_specific: bool = False
    description: str


class EnsemblePolicy(ModelPlaneBaseModel):
    policy_id: str
    ensemble_class: EnsembleClass
    model_refs: List[ModelRef]
    weights: Optional[List[float]] = None
    description: str


class AbstentionPolicy(ModelPlaneBaseModel):
    policy_id: str
    model_id: str
    allow_reject: bool
    min_confidence_required: float
    fallback_strategy: str


class InferenceManifestEntry(ModelPlaneBaseModel):
    model_ref: ModelRef
    checkpoint_id: str
    threshold_policy_id: Optional[str] = None
    abstention_policy_id: Optional[str] = None


class InferenceManifest(ModelPlaneBaseModel):
    manifest_id: str
    entries: List[InferenceManifestEntry]
    ensemble_policy_id: Optional[str] = None
    created_at: datetime


class CalibrationRecord(ModelPlaneBaseModel):
    record_id: str
    checkpoint_id: str
    evaluated_at: datetime
    calibration_class: CalibrationClass
    summary: Dict[str, Any]
    is_stale: bool = False


class UncertaintyRecord(ModelPlaneBaseModel):
    record_id: str
    checkpoint_id: str
    evaluated_at: datetime
    uncertainty_class: UncertaintyClass
    summary: Dict[str, Any]


class InferenceEquivalenceReport(ModelPlaneBaseModel):
    report_id: str
    model_id: str
    evaluated_at: datetime
    verdict: EquivalenceVerdict
    differences: List[str]
    proof_notes: str


class ServingSkewReport(ModelPlaneBaseModel):
    report_id: str
    model_id: str
    evaluated_at: datetime
    skew_detected: bool
    suspected_causes: List[str]


class ModelDriftReport(ModelPlaneBaseModel):
    report_id: str
    model_id: str
    evaluated_at: datetime
    drift_severity: DriftSeverity
    caveats: List[str]


class TrustedSignalVerdictSummary(ModelPlaneBaseModel):
    model_id: str
    verdict: TrustedSignalVerdict
    evaluated_at: datetime
    factors: Dict[str, Any]
    blocker_reasons: List[str]


class ModelAuditRecord(ModelPlaneBaseModel):
    audit_id: str
    model_id: str
    action: str
    timestamp: datetime
    details: Dict[str, Any]
