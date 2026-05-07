from datetime import datetime
from typing import Any, Dict, List

from pydantic import BaseModel

from app.config_plane.enums import (
    ConfigDomain,
    DiffSeverity,
    DriftSeverity,
    EquivalenceVerdict,
    LayerClass,
    MutabilityClass,
    ParameterClass,
    ScopeClass,
)


class ConfigParameter(BaseModel):
    name: str
    domain: ConfigDomain
    param_type: ParameterClass
    default_policy: Any
    owner: str
    mutability_class: MutabilityClass
    experimentability_class: str
    is_secret_adjacent: bool
    is_runtime_safe: bool
    is_release_sensitive: bool


class ConfigParameterRef(BaseModel):
    name: str
    version: str


class ConfigSchemaVersion(BaseModel):
    version_id: str
    created_at: datetime


class ConfigSchema(BaseModel):
    domain: ConfigDomain
    version: ConfigSchemaVersion
    parameters: Dict[str, ConfigParameter]


class ConfigScope(BaseModel):
    scope_class: ScopeClass
    target: str


class ConfigLayer(BaseModel):
    layer_id: str
    layer_class: LayerClass
    allowed_scopes: List[ScopeClass]
    precedence_order: int


class ConfigSourceRecord(BaseModel):
    source_id: str
    layer_id: str
    freshness: datetime
    immutable_handle: str


class ConfigOverride(BaseModel):
    override_id: str
    parameter_name: str
    source_id: str
    layer_class: LayerClass
    value: Any
    reason: str


class EffectiveConfigEntry(BaseModel):
    parameter_name: str
    resolved_value: Any
    source_layer: LayerClass
    source_id: str
    is_hidden_default: bool
    lineage_refs: List[str]


class EffectiveConfigManifest(BaseModel):
    manifest_id: str
    created_at: datetime
    scope: ConfigScope
    entries: Dict[str, EffectiveConfigEntry]
    config_hash: str
    unresolved_blockers: List[str]


class ConfigDiffRecord(BaseModel):
    parameter_name: str
    left_value: Any
    right_value: Any
    semantic_class: str
    severity: DiffSeverity


class ConfigDriftFinding(BaseModel):
    finding_id: str
    parameter_name: str
    expected_value: Any
    actual_value: Any
    drift_type: str
    severity: DriftSeverity
    blast_radius: str


class ConfigLineageRecord(BaseModel):
    parameter_name: str
    value: Any
    source_chain: List[str]
    override_chain: List[str]
    review_refs: List[str]


class MutabilityPolicy(BaseModel):
    mutability_class: MutabilityClass
    allowed_patch_classes: List[LayerClass]


class ConfigEquivalenceReport(BaseModel):
    report_id: str
    base_manifest_hash: str
    compare_manifest_hash: str
    verdict: EquivalenceVerdict
    divergences: List[ConfigDiffRecord]


class RuntimeConfigSnapshot(BaseModel):
    snapshot_id: str
    captured_at: datetime
    active_manifest_ref: str
    active_hash: str


class ConfigAuditRecord(BaseModel):
    audit_id: str
    action: str
    timestamp: datetime
    actor: str


class ConfigArtifactManifest(BaseModel):
    artifact_id: str
    manifest_refs: List[str]


class ConfigPlaneConfig(BaseModel):
    enabled: bool = True
