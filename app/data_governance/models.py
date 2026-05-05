from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
from app.data_governance.enums import (
    DatasetType,
    ContractType,
    SchemaCompatibility,
    QualitySeverity,
    TrustLevel,
    LineageEdgeType,
    CanonicalEntityType,
    ImpactSeverity,
    SchemaChangeType,
    GovernanceVerdict,
)


class DataGovernanceConfig(BaseModel):
    strict_mode: bool = True
    require_provenance: bool = True


class SchemaField(BaseModel):
    name: str
    dtype: str
    nullable: bool = False
    is_unique_key: bool = False
    metadata: Dict[str, str] = Field(default_factory=dict)


class DataSchema(BaseModel):
    schema_id: str
    version: str
    fields: List[SchemaField]
    order_sensitive: bool = False
    created_at: datetime
    metadata: Dict[str, str] = Field(default_factory=dict)


class SchemaVersionRef(BaseModel):
    schema_id: str
    version: str


class DataContract(BaseModel):
    contract_id: str
    contract_type: ContractType
    schema_ref: SchemaVersionRef
    required_fields: List[str]
    optional_fields: List[str]
    unique_keys: List[str]
    description: str


class DatasetRef(BaseModel):
    dataset_id: str
    dataset_type: DatasetType
    version: str


class DataQualityResult(BaseModel):
    rule_name: str
    passed: bool
    severity: QualitySeverity
    affected_rows: int = 0
    affected_fields: List[str] = Field(default_factory=dict)
    evidence: str
    recommended_action: str


class QualityScoreBreakdown(BaseModel):
    total_rules: int
    passed_rules: int
    failed_critical: int
    failed_high: int
    failed_medium: int
    failed_low: int


class DatasetQualityReport(BaseModel):
    dataset_ref: DatasetRef
    run_id: str
    timestamp: datetime
    results: List[DataQualityResult]
    breakdown: QualityScoreBreakdown
    overall_score: float  # 0.0 to 1.0
    status: TrustLevel


class DataQualityRule(BaseModel):
    rule_name: str
    description: str
    severity: QualitySeverity


class LineageNode(BaseModel):
    node_id: str
    dataset_ref: DatasetRef
    producing_module: str


class LineageEdge(BaseModel):
    source_id: str
    target_id: str
    edge_type: LineageEdgeType


class ProvenanceRecord(BaseModel):
    dataset_ref: DatasetRef
    build_time: datetime
    source_refs: List[DatasetRef]
    transform_step_ids: List[str]
    responsible_module: str
    version_refs: Dict[str, str] = Field(default_factory=dict)


class CanonicalId(BaseModel):
    canonical_id: str
    entity_type: CanonicalEntityType
    aliases: List[str]
    is_ambiguous: bool = False


class CanonicalEntityRef(BaseModel):
    canonical_id: str
    entity_type: CanonicalEntityType


class CompatibilityReport(BaseModel):
    from_schema: SchemaVersionRef
    to_schema: SchemaVersionRef
    compatibility: SchemaCompatibility
    breaking_changes: List[str]
    requires_migration: bool


class SchemaDiffReport(BaseModel):
    from_schema: SchemaVersionRef
    to_schema: SchemaVersionRef
    changes: Dict[SchemaChangeType, List[str]]
    is_breaking: bool


class DownstreamImpactReport(BaseModel):
    dataset_ref: DatasetRef
    impacted_components: List[str]
    severity: ImpactSeverity
    recommended_checks: List[str]
    likely_blockers: List[str]


class TrustVerdict(BaseModel):
    dataset_ref: DatasetRef
    verdict: TrustLevel
    score: float
    reasons: List[str]
    evidence_breakdown: Dict[str, str]
    usage_recommendation: str


class GovernanceCatalogEntry(BaseModel):
    dataset_ref: DatasetRef
    contract_id: str
    latest_quality_status: TrustLevel
    latest_trust_verdict: TrustLevel
    last_updated: datetime


class DataGovernanceAuditRecord(BaseModel):
    record_id: str
    timestamp: datetime
    action: str
    details: str


class DataGovernanceArtifactManifest(BaseModel):
    manifest_id: str
    datasets: List[GovernanceCatalogEntry]
    created_at: datetime
