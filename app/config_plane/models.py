from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Any
from datetime import datetime, timezone
from app.config_plane.enums import (
    ConfigDomain,
    MutabilityClass,
    ParameterClass,
    LayerClass,
    ScopeClass,
    DiffSeverity,
    DriftSeverity,
    EquivalenceVerdict,
    ConfigVerdict,
    SecretVisibility,
)


class ConfigParameterRef(BaseModel):
    domain: ConfigDomain
    name: str


class ConfigParameter(BaseModel):
    ref: ConfigParameterRef
    type_name: str
    owner: str
    mutability_class: MutabilityClass
    parameter_class: ParameterClass
    experimentable: bool
    runtime_safe: bool
    release_sensitive: bool
    has_default: bool
    default_value: Optional[Any] = None


class ConfigSchemaVersion(BaseModel):
    version_id: str
    published_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ConfigSchema(BaseModel):
    domain: ConfigDomain
    version: ConfigSchemaVersion
    parameters: Dict[str, ConfigParameter]


class ConfigScope(BaseModel):
    scope_class: ScopeClass
    target_id: Optional[str] = None


class ConfigLayer(BaseModel):
    layer_id: str
    layer_class: LayerClass
    priority: int
    allowed_scopes: List[ScopeClass]


class ConfigSourceRecord(BaseModel):
    source_id: str
    layer_id: str
    scope: ConfigScope
    payload: Dict[str, Any]
    loaded_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ConfigOverride(BaseModel):
    override_id: str
    parameter_ref: ConfigParameterRef
    source_id: str
    layer_id: str
    value: Any
    rationale: str
    applied_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ConfigLineageRecord(BaseModel):
    parameter_ref: ConfigParameterRef
    effective_value: Any
    source_chain: List[str]
    override_chain: List[str]
    is_hidden_default: bool
    secret_redacted: bool


class EffectiveConfigEntry(BaseModel):
    parameter_ref: ConfigParameterRef
    value: Any
    source_id: str
    layer_id: str
    lineage: ConfigLineageRecord


class EffectiveConfigManifest(BaseModel):
    manifest_id: str
    profile: str
    resolved_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    entries: Dict[str, EffectiveConfigEntry]  # key: domain.name
    config_hash: str


class ConfigDiffRecord(BaseModel):
    diff_id: str
    left_manifest_id: str
    right_manifest_id: str
    parameter_ref: ConfigParameterRef
    left_value: Any
    right_value: Any
    severity: DiffSeverity
    mutability_class: MutabilityClass


class ConfigDriftFinding(BaseModel):
    finding_id: str
    parameter_ref: ConfigParameterRef
    expected_value: Any
    actual_value: Any
    severity: DriftSeverity
    description: str
    detected_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ConfigEquivalenceReport(BaseModel):
    report_id: str
    target_manifest_id: str
    baseline_manifest_id: str
    verdict: EquivalenceVerdict
    divergences: List[str]
    evaluated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class RuntimeConfigSnapshot(BaseModel):
    snapshot_id: str
    effective_manifest_id: str
    active_profile: str
    snapshot_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class MutabilityPolicy(BaseModel):
    mutability_class: MutabilityClass
    allowed_layer_classes: List[LayerClass]
    requires_review: bool


class ConfigAuditRecord(BaseModel):
    audit_id: str
    event_type: str
    details: Dict[str, Any]
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ConfigArtifactManifest(BaseModel):
    artifact_id: str
    schemas: List[str]
    effective_manifest_id: str
    diff_ids: List[str]
    drift_ids: List[str]
