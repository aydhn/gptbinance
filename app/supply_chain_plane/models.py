from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime, timezone
from app.supply_chain_plane.enums import (
    ComponentClass,
    OriginClass,
    DependencyClass,
    BuildClass,
    ArtifactClass,
    SbomClass,
    VerificationClass,
    LicenseClass,
    DriftClass,
    ExceptionClass,
    EquivalenceVerdict,
    TrustVerdict,
    ReadinessClass,
)


class SupplyChainPlaneConfig(BaseModel):
    enforce_strict_provenance: bool = True
    require_sboms_for_critical: bool = True
    block_unknown_origins: bool = True


class ComponentRef(BaseModel):
    component_id: str
    digest: Optional[str] = None
    version: Optional[str] = None


class ComponentDefinition(BaseModel):
    component_id: str
    name: str
    component_class: ComponentClass
    owner: str
    criticality: str
    supported_environments: List[str]
    lifecycle_state: str
    producer_metadata: Dict[str, Any] = Field(default_factory=dict)
    lineage_refs: List[ComponentRef] = Field(default_factory=list)


class SourceOriginRecord(BaseModel):
    origin_id: str
    component_ref: ComponentRef
    origin_class: OriginClass
    trust_hints: Dict[str, Any] = Field(default_factory=dict)
    recorded_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class DependencyRecord(BaseModel):
    dependency_id: str
    source_component: ComponentRef
    target_component: ComponentRef
    dependency_class: DependencyClass
    criticality: str
    is_optional: bool = False


class DependencyTree(BaseModel):
    tree_id: str
    root_component: ComponentRef
    dependencies: List[DependencyRecord]
    has_cycles: bool = False
    cycle_warnings: List[str] = Field(default_factory=list)
    missing_node_warnings: List[str] = Field(default_factory=list)


class BuildInputRecord(BaseModel):
    input_id: str
    input_ref: ComponentRef
    input_type: str
    is_pinned: bool


class BuildRecipe(BaseModel):
    recipe_id: str
    component_ref: ComponentRef
    build_class: BuildClass
    toolchain_refs: List[str] = Field(default_factory=list)
    environment_refs: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class BuildProvenanceRecord(BaseModel):
    provenance_id: str
    recipe_ref: str
    inputs: List[BuildInputRecord]
    output_ref: ComponentRef
    recorded_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    is_complete: bool = True
    missing_provenance_warnings: List[str] = Field(default_factory=list)


class GeneratedArtifactRecord(BaseModel):
    artifact_id: str
    provenance_ref: str
    artifact_type: str
    regeneration_suitable: bool


class PackageRecord(BaseModel):
    package_id: str
    component_ref: ComponentRef
    semantic_version: str
    content_digest: str
    repository_source: str
    metadata: Dict[str, Any] = Field(default_factory=dict)


class ContainerArtifactRecord(BaseModel):
    container_id: str
    package_ref: str
    image_digest: str
    tags: List[str]
    base_image_lineage: List[str] = Field(default_factory=list)


class SbomRecord(BaseModel):
    sbom_id: str
    component_ref: ComponentRef
    sbom_class: SbomClass
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    is_transitively_complete: bool = True


class SignatureRecord(BaseModel):
    signature_id: str
    artifact_ref: ComponentRef
    signature_type: str
    signer_identity: str
    signed_at: datetime


class VerificationRecord(BaseModel):
    verification_id: str
    artifact_ref: ComponentRef
    verification_class: VerificationClass
    is_verified: bool
    confidence_notes: str
    verified_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class LicenseRecord(BaseModel):
    license_id: str
    component_ref: ComponentRef
    license_class: LicenseClass
    spdx_id: Optional[str] = None
    burden_notes: str = ""


class OriginTrustRecord(BaseModel):
    trust_id: str
    origin_ref: str
    is_trusted: bool
    suspicion_flags: List[str] = Field(default_factory=list)


class RuntimeLineageRecord(BaseModel):
    runtime_id: str
    environment: str
    running_artifact_ref: ComponentRef
    release_bundle_ref: Optional[ComponentRef] = None
    drift_detected: bool = False
    observed_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class DriftRecord(BaseModel):
    drift_id: str
    drift_class: DriftClass
    component_ref: ComponentRef
    environment: str
    description: str
    severity: str
    detected_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class SupplyChainExceptionRecord(BaseModel):
    exception_id: str
    exception_class: ExceptionClass
    component_ref: ComponentRef
    reason: str
    ttl_expires_at: Optional[datetime] = None
    residual_risk_notes: str = ""


class SupplyChainDebtRecord(BaseModel):
    debt_id: str
    component_ref: ComponentRef
    debt_type: str
    severity: str
    description: str
    recorded_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class SupplyChainEquivalenceReport(BaseModel):
    report_id: str
    component_ref: ComponentRef
    environments_compared: List[str]
    verdict: EquivalenceVerdict
    divergence_sources: List[str] = Field(default_factory=list)


class SupplyChainDivergenceReport(BaseModel):
    report_id: str
    component_ref: ComponentRef
    divergence_type: str
    severity: str
    blast_radius: str


class SupplyChainTrustVerdict(BaseModel):
    verdict_id: str
    component_ref: ComponentRef
    verdict: TrustVerdict
    breakdown: Dict[str, Any] = Field(default_factory=dict)
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class SupplyChainAuditRecord(BaseModel):
    audit_id: str
    action: str
    component_ref: ComponentRef
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    details: Dict[str, Any] = Field(default_factory=dict)


class SupplyChainArtifactManifest(BaseModel):
    manifest_id: str
    component_refs: List[ComponentRef]
    provenance_refs: List[str]
    sbom_refs: List[str]
    signature_refs: List[str]
    runtime_refs: List[str]
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
