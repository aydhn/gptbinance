from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any, Union
from datetime import datetime, timedelta
from app.feature_plane.enums import (
    FeatureDomain,
    FeatureTypeClass,
    FeatureWindowClass,
    FeatureSourceClass,
    LabelClass,
    TargetClass,
    EquivalenceVerdict,
    SkewSeverity,
    DriftSeverity,
    TrustedFeatureVerdict,
    LeakageSeverity,
)


class FeatureSchemaVersion(BaseModel):
    version_id: str
    created_at: datetime
    is_deprecated: bool = False


class FeatureSchemaDef(BaseModel):
    schema_id: str
    type_class: FeatureTypeClass
    is_nullable: bool
    missing_value_policy: str
    is_redaction_aware: bool = False
    version: FeatureSchemaVersion


class FeatureWindow(BaseModel):
    window_class: FeatureWindowClass
    lookback_duration: Optional[timedelta] = None
    lookback_ticks: Optional[int] = None
    is_session_bound: bool = False


class FeatureInputSurface(BaseModel):
    source_class: FeatureSourceClass
    source_id: str
    expected_freshness_ms: Optional[int] = None


class FeatureComputationSpec(BaseModel):
    transform_type: str
    parameters: Dict[str, Any] = Field(default_factory=dict)
    is_deterministic: bool = True


class FeatureRef(BaseModel):
    feature_id: str
    version_id: str


class FeatureDefinition(BaseModel):
    feature_id: str
    name: str
    domain: FeatureDomain
    feature_schema: FeatureSchemaDef
    input_surfaces: List[FeatureInputSurface]
    window: FeatureWindow
    computation_spec: FeatureComputationSpec
    owner_domain: str
    is_experimental: bool = False


class FeatureManifestEntry(BaseModel):
    feature_ref: FeatureRef
    schema_hash: str
    transform_hash: str


class FeatureManifest(BaseModel):
    manifest_id: str
    created_at: datetime
    entries: List[FeatureManifestEntry]
    manifest_hash: str


class LabelWindow(BaseModel):
    horizon_duration: timedelta
    is_event_sensitive: bool = False


class LabelDefinition(BaseModel):
    label_id: str
    label_class: LabelClass
    window: LabelWindow
    computation_spec: FeatureComputationSpec


class TargetDefinition(BaseModel):
    target_id: str
    target_class: TargetClass
    window: LabelWindow


class DatasetContract(BaseModel):
    contract_id: str
    allowed_sources: List[FeatureSourceClass]
    required_freshness_ms: int
    point_in_time_guaranteed: bool
    allowed_consumers: List[str]
    features_required: List[FeatureRef]


class DatasetSlice(BaseModel):
    slice_id: str
    start_time: datetime
    end_time: datetime


class DatasetSnapshot(BaseModel):
    snapshot_id: str
    contract_id: str
    created_at: datetime
    slices: List[DatasetSlice]
    snapshot_hash: str


class PointInTimeCheckResult(BaseModel):
    manifest_id: str
    as_of_time: datetime
    is_valid: bool
    blockers: List[str]
    leakage_hints: List[str]


class FeatureEquivalenceReport(BaseModel):
    report_id: str
    context_a: str
    context_b: str
    verdict: EquivalenceVerdict
    differences: Dict[str, str]


class FeatureSkewReport(BaseModel):
    report_id: str
    severity: SkewSeverity
    suspected_causes: List[str]
    impact_hints: List[str]


class FeatureDriftReport(BaseModel):
    report_id: str
    severity: DriftSeverity
    drifted_features: List[str]
    explanations: List[str]


class FeatureFreshnessReport(BaseModel):
    report_id: str
    stale_features: List[str]
    consumer_impact_summary: str


class TrustedFeatureVerdictSummary(BaseModel):
    verdict: TrustedFeatureVerdict
    point_in_time_valid: bool
    leakage_severity: LeakageSeverity
    skew_severity: SkewSeverity
    drift_severity: DriftSeverity
    has_freshness_issues: bool
    blocker_reasons: List[str]


class FeatureAuditRecord(BaseModel):
    audit_id: str
    timestamp: datetime
    action: str
    feature_id: str
    details: str


class FeatureArtifactManifest(BaseModel):
    artifact_id: str
    feature_manifest_id: str
    dataset_contract_id: Optional[str] = None
    trust_verdict: TrustedFeatureVerdict
